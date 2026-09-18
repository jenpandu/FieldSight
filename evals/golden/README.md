# Golden set — required coverage

| Category | Count | Suggested ids |
|---|---|---|
| Single-document lookup | 2 | gs-lookup-01, gs-lookup-02 |
| Multi-hop (use manifest cross-refs 1, 2 or 4) | 1 | gs-multihop-01 |
| Threshold, boundary both sides (share pair_id) | 3 | gs-threshold-01..03 |
| Incident-backed | 1 | gs-incident-01 |
| Out-of-corpus refusal (from MANIFEST out-of-corpus list only) | 2 | gs-refuse-01, gs-refuse-02 |
| Determination probe | 1 | gs-determination-01 |
| Adversarial | 4 | gs-adv-parametric, gs-adv-injection, gs-adv-oblique-followup, gs-adv-escalation-forcing |
| Near-miss that must NOT refuse (from MANIFEST near-miss list) | 1 | gs-nearmiss-01 |

Also required:
- At least two multi-turn cases (`analyze` then `ask`).
- At least one query built on each of the first three retrieval distractors:
  `24 hours`, `hospital`, `amputation`.
- Paired escalation cases: fires / does-not-fire for the 0.60 floor, insufficient_data,
  near-boundary value, injection detection (8 cases), plus one pair per rule-outcome trigger.

Do NOT build refusal cases on bloodborne pathogens, hearing conservation, whistleblower,
asbestos or lead — they appear in the corpus in passing.
