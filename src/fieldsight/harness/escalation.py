# FILE: src/fieldsight/harness/escalation.py
#
# PURPOSE
# Deterministic eligibility: run record → list of fired triggers.
#
# REQUIREMENT REFS: §10 Escalation
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Triggers (OR-ed, each recorded by name): field below 0.60; insufficient_data; value
#     within near-boundary margin; reviewer not approved or >1 iteration; citation failed
#     to resolve/support; retrieval below threshold anywhere; prompt attack fired;
#     fatality or any 1904.39-reportable outcome; photo contradicts narrative.
#   - Any trigger → enqueue in review queue with trigger names.
#
# MUST / MUST NOT
#   - A model's self-reported confidence is never an input.
#
# TESTED BY
#   tests/unit/test_escalation.py — each trigger fires on one input and not on a near-
#   identical one.
