# FILE: src/fieldsight/harness/remedies.py
#
# PURPOSE
# Maps each guard failure to its remedy.
#
# REQUIREMENT REFS: §10 remedies table
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Uncited claim → regenerate with objection.
#   - Determination language → regenerate once, then refuse + log gate miss.
#   - Missing disclosure → append deterministically.
#   - Unattributed threshold → run the rule, inject result, regenerate.
#   - PII in output → redact, raise event, never regenerate.
#
# MUST / MUST NOT
#   - Every remedy emits an event (events.py). Nothing is silently repaired.
