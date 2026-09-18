# FILE: src/fieldsight/rules/r5_confidence.py
#
# PURPOSE
# R5 — confidence floor (pipeline parameter, not regulatory).
#
# REQUIREMENT REFS: §6 R5
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Input: mapping of field → confidence for required fields.
#   - Any field strictly below 0.60 → human_determination, naming every such field.
#   - Exactly 0.60 passes.
#
# TESTED BY
#   tests/unit/test_r5_confidence.py — 0.59 / 0.60 / 0.61.
