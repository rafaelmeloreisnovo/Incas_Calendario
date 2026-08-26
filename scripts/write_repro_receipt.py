#!/usr/bin/env python3
"""Emit a machine-readable receipt for the reproducible core gate.

Stdlib-only by design. The receipt binds the GitHub execution identity,
immutable container/action references declared by the workflow, gate outcomes,
and SHA-256 hashes of the project inputs exercised by the gate.
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "artifacts" / "reproducibility" / "receipt.json"

CRITICAL_INPUTS = (
    ".github/workflows/reproducible-core.yml",
    "scripts/write_repro_receipt.py",
    "scripts/validate_calendar_matrix.py",
    "scripts/cycle_phase_features.py",
    "data/calendar_cycles_matrix.json",
    "data/calendar_round_lunar_extension_20260825.v1.json",
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    return value if value else "TOKEN_VAZIO"


def read_os_release() -> dict[str, str]:
    result: dict[str, str] = {}
    path = Path("/etc/os-release")
    if not path.is_file():
        return result
    for raw in path.read_text(encoding="utf-8").splitlines():
        if "=" not in raw:
            continue
        key, value = raw.split("=", 1)
        result[key] = value.strip().strip('"')
    return result


def main() -> int:
    out = Path(os.environ.get("REPRO_RECEIPT_PATH", str(DEFAULT_OUT)))
    if not out.is_absolute():
        out = ROOT / out

    inputs: dict[str, dict[str, object]] = {}
    missing: list[str] = []
    for rel in CRITICAL_INPUTS:
        path = ROOT / rel
        if path.is_file():
            inputs[rel] = {
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            }
        else:
            inputs[rel] = {"state": "TOKEN_VAZIO"}
            missing.append(rel)

    gate_outcomes = {
        "calendar_matrix": env("GATE_MATRIX_OUTCOME"),
        "cycle_phase": env("GATE_PHASE_OUTCOME"),
        "required_root_files": env("GATE_ROOT_OUTCOME"),
        "docs_directory": env("GATE_DOCS_OUTCOME"),
    }

    os_release = read_os_release()
    payload = {
        "schema": "rafaelia.reproducible-core-receipt/v1",
        "repository": env("GITHUB_REPOSITORY"),
        "head_sha": env("GITHUB_SHA"),
        "ref": env("GITHUB_REF"),
        "event": env("GITHUB_EVENT_NAME"),
        "run_id": env("GITHUB_RUN_ID"),
        "run_attempt": env("GITHUB_RUN_ATTEMPT"),
        "workflow_ref": env("GITHUB_WORKFLOW_REF"),
        "execution_scope": "calendar-matrix + cycle-phase + repository structural gates",
        "container": {
            "image": env("REPRO_CONTAINER_IMAGE"),
            "immutable_digest_required": True,
        },
        "actions": {
            "checkout_commit": env("REPRO_CHECKOUT_SHA"),
            "upload_artifact_commit": env("REPRO_UPLOAD_ARTIFACT_SHA"),
        },
        "runtime": {
            "python": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "python_executable": sys.executable,
            "platform": platform.platform(),
            "machine": platform.machine(),
            "os_release": {
                "ID": os_release.get("ID", "TOKEN_VAZIO"),
                "VERSION_ID": os_release.get("VERSION_ID", "TOKEN_VAZIO"),
            },
        },
        "gate_outcomes": gate_outcomes,
        "inputs": inputs,
        "missing_inputs": missing,
        "all_project_gates_passed": all(v == "success" for v in gate_outcomes.values()),
        "claim_allowed": False,
        "scientific_empirical_claims_validated": False,
        "boundary": "This receipt proves only the declared software/data validation scope; it does not validate archaeological, astronomical causal, historical, or physical claims.",
    }

    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    payload["canonical_payload_sha256"] = hashlib.sha256(canonical).hexdigest()

    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(out.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, out)

    print(f"receipt={out}")
    print(f"payload_sha256={payload['canonical_payload_sha256']}")
    print(f"all_project_gates_passed={str(payload['all_project_gates_passed']).lower()}")
    if missing:
        print("missing_inputs=" + ",".join(missing))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
