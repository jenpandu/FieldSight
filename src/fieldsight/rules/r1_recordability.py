# FILE: src/fieldsight/rules/r1_recordability.py
#
# PURPOSE
# R1 — is the case recordable.
#
# REQUIREMENT REFS: §6 R1; CFR-1904 §§1904.4, 1904.5, 1904.7(b)(1)
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Inputs: work_related, new_case, death, days_away>0, restricted/transfer>0, medical
#     treatment beyond first aid (from R3), loss_of_consciousness, significant diagnosed
#     injury.
#   - Outcome: recordable / not_recordable / insufficient_data(field).
#
# TESTED BY
#   tests/unit/test_r1_recordability.py
#
# DONE WHEN
#   Each general recording criterion has a positive and a negative test.
