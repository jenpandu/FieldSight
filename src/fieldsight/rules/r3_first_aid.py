# FILE: src/fieldsight/rules/r3_first_aid.py
#
# PURPOSE
# R3 — medical treatment beyond first aid (closed list).
#
# REQUIREMENT REFS: §6 R3; CFR-1904 §1904.7(b)(5)(ii)-(iii); CPL-172 IX.E.10
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - FIRST_AID frozenset of the 14 TreatmentCode members (A)-(N).
#   - Outcome: beyond_first_aid if ANY treatment code is not in the set; first_aid_only
#     otherwise; insufficient_data if treatments missing.
#   - Sources include both CFR-1904 (b)(5)(ii) and CPL-172 IX.E.10 (cross-reference #1).
#
# MUST / MUST NOT
#   - Pure set membership. The free-text → code mapping happens in normalization, not
#     here.
#   - (b)(5)(iii): the list is complete — unlisted means medical treatment.
#
# TESTED BY
#   tests/unit/test_r3_first_aid.py — sutures vs Steri-Strips, tetanus vs other
#   immunization, rigid vs non-rigid support, empty list.
