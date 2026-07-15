#!/usr/bin/env python3
"""Validate and summarize the relational calendar matrix.

Standard-library only; suitable for Termux and CI.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence, Set, Tuple

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "calendar_cycles_matrix.json"
DEFAULT_OUTPUT = ROOT / "artifacts" / "calendar_matrix_summary.md"

RECORD_REQUIRED = {
    "id",
    "place",
    "culture",
    "cycle_name",
    "calendar_type",
    "period",
    "observable",
    "method",
    "geometry",
    "uncertainty",
    "evidence_state",
    "attention_state",
    "source_refs",
    "notes",
}
RELATION_REQUIRED = {"source", "relation", "target", "evidence_state", "method"}


class MatrixError(RuntimeError):
    pass


def load(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise MatrixError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise MatrixError(
            f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    if not isinstance(value, dict):
        raise MatrixError("top-level JSON value must be an object")
    return value


def missing_fields(item: Mapping[str, Any], required: Set[str]) -> List[str]:
    return sorted(required.difference(item))


def is_token_vazio_record(record: Mapping[str, Any]) -> bool:
    return record.get("evidence_state") == "TOKEN_VAZIO"


def validate_period(record: Mapping[str, Any], context: str, errors: List[str]) -> None:
    period = record.get("period")
    if period is None:
        if not is_token_vazio_record(record):
            errors.append(f"{context}: period may be null only for TOKEN_VAZIO records")
        return
    if not isinstance(period, dict):
        errors.append(f"{context}: period must be an object or null")
        return
    for field in ("value", "unit", "kind"):
        if field not in period:
            errors.append(f"{context}: period missing {field!r}")
    value = period.get("value")
    if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
        errors.append(f"{context}: period.value must be a positive number")
    if not isinstance(period.get("unit"), str) or not period.get("unit"):
        errors.append(f"{context}: period.unit must be a non-empty string")
    if not isinstance(period.get("kind"), str) or not period.get("kind"):
        errors.append(f"{context}: period.kind must be a non-empty string")


def validate_matrix(
    matrix: Mapping[str, Any]
) -> Tuple[Dict[str, Dict[str, Any]], List[Dict[str, Any]]]:
    errors: List[str] = []
    records_raw = matrix.get("records")
    relations_raw = matrix.get("relations")
    evidence_states = set(matrix.get("evidence_states", []))
    attention_states = set(matrix.get("attention_states", []))
    relation_types = set(matrix.get("relation_types", []))

    if not isinstance(records_raw, list):
        errors.append("records must be a list")
        records_raw = []
    if not isinstance(relations_raw, list):
        errors.append("relations must be a list")
        relations_raw = []
    if not evidence_states:
        errors.append("evidence_states must not be empty")
    if not attention_states:
        errors.append("attention_states must not be empty")
    if not relation_types:
        errors.append("relation_types must not be empty")

    records: Dict[str, Dict[str, Any]] = {}
    for index, raw in enumerate(records_raw):
        context = f"records[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{context}: must be an object")
            continue
        for field in missing_fields(raw, RECORD_REQUIRED):
            errors.append(f"{context}: missing field {field!r}")
        record_id = raw.get("id")
        if not isinstance(record_id, str) or not record_id:
            errors.append(f"{context}: id must be a non-empty string")
            continue
        if record_id in records:
            errors.append(f"{context}: duplicate id {record_id!r}")
            continue
        records[record_id] = dict(raw)

        if raw.get("evidence_state") not in evidence_states:
            errors.append(f"{context}: invalid evidence_state {raw.get('evidence_state')!r}")
        if raw.get("attention_state") not in attention_states:
            errors.append(f"{context}: invalid attention_state {raw.get('attention_state')!r}")

        for field in ("place", "culture", "cycle_name", "calendar_type", "method", "notes"):
            if not isinstance(raw.get(field), str) or not raw.get(field):
                errors.append(f"{context}: {field} must be a non-empty string")

        for field in ("observable", "geometry", "source_refs"):
            if not isinstance(raw.get(field), list) or not raw.get(field):
                errors.append(f"{context}: {field} must be a non-empty list")

        uncertainty = raw.get("uncertainty")
        if not isinstance(uncertainty, dict):
            errors.append(f"{context}: uncertainty must be an object")
        else:
            if not isinstance(uncertainty.get("status"), str) or not uncertainty.get("status"):
                errors.append(f"{context}: uncertainty.status must be a non-empty string")
            if not isinstance(uncertainty.get("note"), str) or not uncertainty.get("note"):
                errors.append(f"{context}: uncertainty.note must be a non-empty string")

        validate_period(raw, context, errors)

        refs = raw.get("source_refs") if isinstance(raw.get("source_refs"), list) else []
        has_real_ref = any(ref != "TOKEN_VAZIO" for ref in refs)
        if raw.get("evidence_state") in {"VERIFIED", "PARTIAL", "HYPOTHESIS"} and not has_real_ref:
            errors.append(f"{context}: scientific record requires a non-TOKEN_VAZIO source")
        if raw.get("evidence_state") == "TOKEN_VAZIO" and has_real_ref:
            errors.append(
                f"{context}: TOKEN_VAZIO record has a source; review whether it should be promoted"
            )

        if raw.get("calendar_type") == "candidate-multicycle" and raw.get("evidence_state") != "TOKEN_VAZIO":
            errors.append(
                f"{context}: candidate-multicycle must remain TOKEN_VAZIO until method and source are registered"
            )

    relations: List[Dict[str, Any]] = []
    seen: Set[Tuple[str, str, str]] = set()
    for index, raw in enumerate(relations_raw):
        context = f"relations[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{context}: must be an object")
            continue
        for field in missing_fields(raw, RELATION_REQUIRED):
            errors.append(f"{context}: missing field {field!r}")
        source = raw.get("source")
        target = raw.get("target")
        relation = raw.get("relation")
        if source not in records:
            errors.append(f"{context}: unknown source {source!r}")
        if target not in records:
            errors.append(f"{context}: unknown target {target!r}")
        if relation not in relation_types:
            errors.append(f"{context}: invalid relation {relation!r}")
        if raw.get("evidence_state") not in evidence_states:
            errors.append(f"{context}: invalid evidence_state {raw.get('evidence_state')!r}")
        if not isinstance(raw.get("method"), str) or not raw.get("method"):
            errors.append(f"{context}: method must be a non-empty string")
        key = (str(source), str(relation), str(target))
        if key in seen:
            errors.append(f"{context}: duplicate relation {key}")
        seen.add(key)
        relations.append(dict(raw))

    if errors:
        raise MatrixError("calendar matrix failed:\n" + "\n".join(f"- {e}" for e in errors))
    return records, relations


def render_summary(
    matrix: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    relations: Sequence[Mapping[str, Any]],
) -> str:
    evidence = Counter(str(item["evidence_state"]) for item in records.values())
    attention = Counter(str(item["attention_state"]) for item in records.values())
    places = Counter(str(item["place"]) for item in records.values())

    lines = [
        "# Calendar Matrix Summary",
        "",
        "> Generated deterministically from `data/calendar_cycles_matrix.json`.",
        "",
        f"- Schema: `{matrix.get('schema_version', 'TOKEN_VAZIO')}`",
        f"- Matrix date: `{matrix.get('generated_on', 'TOKEN_VAZIO')}`",
        f"- Calendar records: **{len(records)}**",
        f"- Relations: **{len(relations)}**",
        f"- Places or place classes: **{len(places)}**",
        "",
        "## Evidence states",
        "",
        "| State | Count |",
        "|---|---:|",
    ]
    for state in matrix.get("evidence_states", []):
        lines.append(f"| `{state}` | {evidence.get(str(state), 0)} |")

    lines.extend(
        [
            "",
            "## Attention states",
            "",
            "| State | Count |",
            "|---|---:|",
        ]
    )
    for state in matrix.get("attention_states", []):
        lines.append(f"| `{state}` | {attention.get(str(state), 0)} |")

    lines.extend(
        [
            "",
            "## Records",
            "",
            "| ID | Place | Culture | Cycle | Period | Evidence | Attention |",
            "|---|---|---|---|---|---|---|",
        ]
    )
    for record_id in sorted(records):
        item = records[record_id]
        period = item.get("period")
        if isinstance(period, dict):
            period_text = f"{period.get('value')} {period.get('unit')} ({period.get('kind')})"
        else:
            period_text = "TOKEN_VAZIO"
        values = [
            record_id,
            str(item["place"]),
            str(item["culture"]),
            str(item["cycle_name"]),
            period_text,
            str(item["evidence_state"]),
            str(item["attention_state"]),
        ]
        values = [value.replace("|", "\\|") for value in values]
        lines.append(
            f"| `{values[0]}` | {values[1]} | {values[2]} | {values[3]} | "
            f"{values[4]} | `{values[5]}` | `{values[6]}` |"
        )

    lines.extend(
        [
            "",
            "## Scientific boundary",
            "",
            "- Candidate regions are research scope, not established calendar claims.",
            "- Shared periods or angles do not establish contact, causality or a universal mechanism.",
            "- Records without source remain `TOKEN_VAZIO`.",
            "- Records without complete uncertainty remain `PARTIAL` or `UNDERSERVED`.",
            "",
        ]
    )
    return "\n".join(lines)


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(content, encoding="utf-8")
    temp.replace(path)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="validate without writing summary")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    try:
        matrix = load(args.input)
        records, relations = validate_matrix(matrix)
    except MatrixError as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 2

    print(f"[OK] matrix valid: records={len(records)} relations={len(relations)}")
    if args.check:
        return 0
    atomic_write(args.output, render_summary(matrix, records, relations))
    print(f"[OK] wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
