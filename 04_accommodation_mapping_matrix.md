# 04. Accommodation Mapping Matrix

## Purpose

Accommodation mapping supports safer and more practical travel decisions. It should not be based only on price or distance.

For travel risk management, the assessment should consider access, transport, neighbourhood context, emergency support, operational practicality, and source confidence.

## Criteria

| Criterion | Description | Score range |
|---|---|---:|
| Access control | Reception, entry management, guest access procedures. | 1-5 |
| Neighbourhood suitability | Security context around the property. | 1-5 |
| Transport reliability | Availability of safe airport / venue transfers. | 1-5 |
| Emergency access | Nearby medical, police, embassy/consular, or assistance access. | 1-5 |
| Operational practicality | Distance to meeting venue, cancellation terms, check-in timing. | 1-5 |
| Source confidence | Quality of information available about the property. | 1-5 |

## Scoring interpretation

| Average score | Suggested category |
|---:|---|
| 4.2 - 5.0 | Preferred option |
| 3.4 - 4.1 | Acceptable with notes |
| 2.6 - 3.3 | Requires review |
| 1.0 - 2.5 | Avoid unless justified |

## Red flags

- Location next to known protest route or high-crime transport hub without mitigation.
- Poor access control or unclear reception coverage.
- Lack of reliable transport options after dark.
- Repeated traveller feedback about unsafe arrival/departure conditions.
- Contradictory or outdated source information.
- No clear cancellation or contingency option.

## Output

The sample accommodation matrix is in:

- `data/sample_accommodation_matrix.csv`

The scoring script is in:

- `scripts/score_accommodations.py`

Generated output is in:

- `outputs/accommodation_ranking.csv`
