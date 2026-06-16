#!/usr/bin/env python3
"""Summarise synthetic traveller feedback by theme and severity."""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "sample_traveller_feedback.csv"
OUTPUT = ROOT / "outputs" / "feedback_summary.md"


def main() -> None:
    with INPUT.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    by_theme = Counter(row["theme"] for row in rows)
    by_severity = Counter(row["severity"] for row in rows)
    actions = defaultdict(list)

    for row in rows:
        actions[row["theme"]].append(row["recommended_action"])

    lines = [
        "# Generated Traveller Feedback Summary",
        "",
        "This output is generated from synthetic feedback data.",
        "",
        "## Feedback by theme",
        "",
    ]

    for theme, count in by_theme.most_common():
        lines.append(f"- **{theme}**: {count} item(s)")

    lines.extend(["", "## Feedback by severity", ""])
    for severity in ["high", "medium", "low"]:
        lines.append(f"- **{severity}**: {by_severity.get(severity, 0)} item(s)")

    lines.extend(["", "## Recommended actions by theme", ""])
    for theme, recs in actions.items():
        lines.append(f"### {theme}")
        for rec in recs:
            lines.append(f"- {rec}")
        lines.append("")

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
