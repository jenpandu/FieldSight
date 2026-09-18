# FILE: src/fieldsight/rules/registry.py
#
# PURPOSE
# Single entry point for invoking a rule, from either path.
#
# REQUIREMENT REFS: §6 (two invocation paths, both recorded)
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - evaluate(rule_id, inputs, path='harness'|'tool') → RuleResult.
#   - Records every invocation into the current turn's run record (rule id, inputs,
#     result, path, duration).
#   - Harness path is authoritative; tool path (evaluate_rule) is secondary.
#
# MUST / MUST NOT
#   - The only way a threshold outcome can enter a dossier.
#   - Performance target < 10 ms per evaluation — assert in a test.
