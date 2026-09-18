# FILE: src/fieldsight/tools/idempotency.py
#
# PURPOSE
# Idempotency key derivation.
#
# REQUIREMENT REFS: §9
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - key = sha256(session_id | tool_name | canonical_json(arguments)).
#   - canonical_json: sorted keys at every depth, fixed separators, normalized
#     numbers/dates.
#
# TESTED BY
#   tests/unit/test_idempotency.py — order-independent, nested dicts, lists preserved in
#   order.
