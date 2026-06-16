# 08. Traveller Feedback Analysis

## Purpose

Traveller feedback is useful because it captures practical friction that may not appear in official sources: unsafe routes, confusing airport procedures, unreliable transport, poor hotel access, or repeated communication problems.

## Workflow

1. Collect feedback after each trip.
2. Remove personal data not needed for the analysis.
3. Tag each entry by theme.
4. Rate severity and recurrence.
5. Compare feedback with existing source notes.
6. Update accommodation, route, or briefing recommendations.
7. Escalate repeated or serious issues.

## Feedback categories

| Category | Example |
|---|---|
| Transport | Airport taxi refused card payment; late-night route felt unsafe. |
| Accommodation | Reception unattended after midnight. |
| Area safety | Aggressive approaches near station. |
| Administration | Unexpected document check. |
| Health | Difficulty finding English-speaking clinic. |
| Communication | Emergency number not clear in briefing. |

## Severity model

| Severity | Meaning |
|---|---|
| Low | Minor inconvenience; no safety impact. |
| Medium | Practical disruption or discomfort; possible mitigation needed. |
| High | Direct safety concern, repeated issue, or escalation needed. |

## Generated output

The script `scripts/feedback_summary.py` reads `data/sample_traveller_feedback.csv` and writes a summary to `outputs/feedback_summary.md`.
