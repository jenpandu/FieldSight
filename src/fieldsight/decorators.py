# FILE: src/fieldsight/decorators.py
#
# PURPOSE
# Cross-cutting concerns as decorators that preserve functools.wraps.
#
# REQUIREMENT REFS: §13 code quality, §10 bounds and retries
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - @timed — records wall-clock duration into the current run record.
#   - @with_retry — bounded, backed-off, jittered retries; honours throttling responses;
#     raises typed error on exhaustion.
#   - @record_tool_invocation — writes tool name, args hash, idempotency key, outcome to
#     the run record.
#   - @record_rule_invocation — writes rule id, inputs, result to the run record.
#   - @check_budget — refuses to start a call when the session budget is spent.
#   - Async-aware variants for async paths.
#
# TESTED BY
#   tests/unit/test_decorators.py — wraps preserved, async variants tested as async.
