#!/usr/bin/env python3
"""Generate deterministic cyclic phase features for RAFAELIA calendar/astronomy studies.

Standard-library only.  This module deliberately does not choose a Maya calendar
correlation epoch.  The caller MUST provide an explicit epoch, preserving the
invariant that a cycle phase is not a causal claim and that historical epoch
choice is auditable.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXTENSION = ROOT / "data" / "calendar_round_lunar_extension_20260825.v1.json"
TROPICAL_YEAR_DAYS = 365.2422


@dataclass(frozen=True)
class Cycle:
    cycle_id: str
    period_days: float
    domain: str


BUILTIN_CYCLES = (
    Cycle("tzolkin_260", 260.0, "maya_calendar"),
    Cycle("haab_365", 365.0, "maya_calendar"),
    Cycle("calendar_round_18980", 18_980.0, "maya_calendar"),
    Cycle("lunar_synodic", 29.53059, "lunar"),
    Cycle("spring_neap", 14.765295, "lunar_tide"),
    Cycle("lunar_nodal", 18.61 * TROPICAL_YEAR_DAYS, "lunar_tide"),
    Cycle("solar_rotation_27d", 27.0, "heliophysics"),
    Cycle("solar_half_rotation_13_5d", 13.5, "heliophysics"),
    Cycle("semiannual_equinox", TROPICAL_YEAR_DAYS / 2.0, "geomagnetic_geometry"),
    Cycle("tropical_year", TROPICAL_YEAR_DAYS, "sun_earth_geometry"),
)


def parse_time(value: str) -> dt.datetime:
    text = value.strip().replace("Z", "+00:00")
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError:
        try:
            parsed = dt.datetime.combine(dt.date.fromisoformat(text), dt.time())
        except ValueError as exc:
            raise argparse.ArgumentTypeError(f"invalid ISO date/time: {value!r}") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def days_between(epoch: dt.datetime, when: dt.datetime) -> float:
    return (when - epoch).total_seconds() / 86_400.0


def phase_feature(elapsed_days: float, period_days: float) -> Dict[str, float]:
    if not math.isfinite(elapsed_days):
        raise ValueError("elapsed_days must be finite")
    if not math.isfinite(period_days) or period_days <= 0.0:
        raise ValueError("period_days must be finite and positive")
    position_days = elapsed_days % period_days
    fraction = position_days / period_days
    angle = math.tau * fraction
    return {
        "position_days": position_days,
        "fraction": fraction,
        "angle_rad": angle,
        "sin": math.sin(angle),
        "cos": math.cos(angle),
    }


def features(epoch: dt.datetime, when: dt.datetime, cycles: Iterable[Cycle] = BUILTIN_CYCLES) -> Dict[str, object]:
    elapsed = days_between(epoch, when)
    result: Dict[str, object] = {
        "schema": "rafaelia.cycle-phase-features.v1",
        "claim_allowed": False,
        "epoch_utc": epoch.isoformat(),
        "time_utc": when.isoformat(),
        "elapsed_days": elapsed,
        "invariant": "PHASE_ALIGNMENT != CAUSALITY",
        "cycles": {},
    }
    cycle_map: Dict[str, object] = {}
    for cycle in cycles:
        cycle_map[cycle.cycle_id] = {
            "period_days": cycle.period_days,
            "domain": cycle.domain,
            **phase_feature(elapsed, cycle.period_days),
        }
    result["cycles"] = cycle_map
    return result


def validate_extension(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("claim_allowed") is not False:
        raise RuntimeError("extension must preserve claim_allowed=false")
    periods = {record.get("id"): record for record in data.get("records", [])}
    cr = periods.get("CAL-MAYA-CALENDAR-ROUND-18980")
    if not isinstance(cr, dict) or float(cr.get("period_days", 0.0)) != 18_980.0:
        raise RuntimeError("Calendar Round 18,980-day invariant missing")
    if int(cr.get("period_haab", 0)) != 52 or int(cr.get("period_tzolkin", 0)) != 73:
        raise RuntimeError("Calendar Round 52 Haab / 73 Tzolkin invariant failed")


def self_test() -> None:
    assert math.lcm(260, 365) == 18_980
    assert 18_980 // 260 == 73
    assert 18_980 // 365 == 52
    tropical_years = 18_980 / TROPICAL_YEAR_DAYS
    assert abs(tropical_years - 51.96551767566836) < 1e-12
    for cycle in BUILTIN_CYCLES:
        f = phase_feature(cycle.period_days, cycle.period_days)
        assert abs(f["fraction"]) < 1e-12
        assert abs(f["sin"]) < 1e-12
        assert abs(f["cos"] - 1.0) < 1e-12
    f = phase_feature(10.0, 29.53059)
    assert abs((f["sin"] ** 2 + f["cos"] ** 2) - 1.0) < 1e-12


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epoch", type=parse_time, help="explicit auditable cycle epoch (ISO-8601)")
    parser.add_argument("--time", dest="when", type=parse_time, help="observation time (ISO-8601)")
    parser.add_argument("--extension", type=Path, default=DEFAULT_EXTENSION)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    validate_extension(args.extension)
    if args.self_test:
        self_test()
        print("PASS cycle_phase_features")
        return 0

    if args.epoch is None or args.when is None:
        parser.error("--epoch and --time are required unless --self-test is used")

    print(json.dumps(features(args.epoch, args.when), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
