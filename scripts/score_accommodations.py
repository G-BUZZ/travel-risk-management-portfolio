#!/usr/bin/env python3
"""Score synthetic accommodation options for a travel risk management portfolio project."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "sample_accommodation_matrix.csv"
OUTPUT = ROOT / "outputs" / "accommodation_ranking.csv"

SCORE_COLUMNS = [
    "access_control",
    "neighbourhood_suitability",
    "transport_reliability",
    "emergency_access",
    "operational_practicality",
    "source_confidence",
]


def category(score: float) -> str:
    if score >= 4.2:
        return "Preferred option"
    if score >= 3.4:
        return "Acceptable with notes"
    if score >= 2.6:
        return "Requires review"
    return "Avoid unless justified"


def main() -> None:
    with INPUT.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        scores = [float(row[col]) for col in SCORE_COLUMNS]
        avg = sum(scores) / len(scores)
        row["average_score"] = f"{avg:.2f}"
        row["category"] = category(avg)

    rows.sort(key=lambda r: float(r["average_score"]), reverse=True)

    OUTPUT.parent.mkdir(exist_ok=True)
    fieldnames = list(rows[0].keys())
    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
