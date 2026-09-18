# FILE: src/fieldsight/harness/write_layer.py
#
# PURPOSE
# The only write path — harness-only, after recorded approval.
#
# REQUIREMENT REFS: §9 (execution row), §12 review, §13 write fails after approval
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 3
#
# WHAT GOES HERE
#   - Executes the approved outcome write with the harness-derived idempotency key.
#   - Retry with the same key; on exhaustion a clear failure.
#   - Unreachable from any agent tool.
