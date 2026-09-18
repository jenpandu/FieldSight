# FILE: src/fieldsight/rules/base.py
#
# PURPOSE
# RuleResult and Source types shared by all rules.
#
# REQUIREMENT REFS: §6 requirements
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Source(doc_id, section_path).
#   - RuleResult(rule_id, outcome, sources: list[Source], inputs, missing_field) — frozen,
#     extra='forbid'.
#   - INSUFFICIENT_DATA constant and a helper that builds an insufficient_data result
#     naming the field.
#
# MUST / MUST NOT
#   - Never a bare boolean.
#   - Pure: no I/O, no clock reads, no randomness.
