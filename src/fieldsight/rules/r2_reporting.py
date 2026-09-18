# FILE: src/fieldsight/rules/r2_reporting.py
#
# PURPOSE
# R2 — reporting clock.
#
# REQUIREMENT REFS: §6 R2; CFR-1904 §1904.39(a), (b)(6), (b)(9), (b)(10), (b)(11); LOI 2021-01-08
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Inputs: incident_at, death_at, admission_basis, admitted_at, amputation kind,
#     loss_of_eye.
#   - Fatality within thirty (30) days of the incident → 8h.
#   - In-patient hospitalization FOR CARE OR TREATMENT within twenty-four (24) hours →
#     24h. Observation or diagnostic testing only → not reportable ((b)(10)).
#   - Amputation or loss of an eye within 24h → 24h. Amputation excludes avulsions,
#     enucleations, deglovings, scalpings, severed ears, broken or chipped teeth ((b)(11))
#     — encode verbatim as enum members.
#   - Otherwise none.
#   - Decide and document: whether a previously reported hospitalization followed by death
#     needs a second report (LOI 2021-01-08 says no) — if encoded, add input + source.
#
# MUST / MUST NOT
#   - Takes admission_basis, NOT the Form 301 checkbox. The checkbox is the P4 trap.
#   - Boundaries inclusive or exclusive: decide, record in docs/architecture.md, test both
#     sides.
#
# TESTED BY
#   tests/unit/test_r2_reporting.py — exactly 24h vs 24h+1min, exactly 30 days vs 30
#   days+1s, observation-only, chipped tooth, each missing field.
