# FILE: src/fieldsight/harness/bounds.py
#
# PURPOSE
# Budgets and caps, check-and-stop.
#
# REQUIREMENT REFS: §10 Bounds
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - SessionBudget loaded from Postgres; accumulates tokens and $ after each call;
#     persists across ask turns.
#   - Refuses to start the next leg once spent → partial response naming the ceiling.
#   - Per-turn wall-clock deadline; per-call timeouts; tool-call counter.
#
# TESTED BY
#   tests/unit/test_bounds.py
