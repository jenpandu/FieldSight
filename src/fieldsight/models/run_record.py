# FILE: src/fieldsight/models/run_record.py
#
# PURPOSE
# The per-turn run record — the thing `trace` renders and §13 measures.
#
# REQUIREMENT REFS: §5 run record, §8 run record, §10 events, §11 corrections
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - RunRecord: correlation_id, session_id, incident_id, analyst_id, command,
#     started/ended, workers_dispatched (+why), redispatches (+trigger), retrievals
#     (query, filters, chunk ids, scores), tool_invocations (name, args hash, idempotency
#     key, outcome), rule_invocations (rule id, inputs, result, path=harness|tool),
#     reviewer verdict per iteration, model_calls (model id, tokens in/out, duration,
#     cost), escalation triggers evaluated + fired, guard events (remedy, triggering
#     claim), totals per agent.
#   - supersedes_id for corrections — a correction is a new record, never an edit.
#
# MUST / MUST NOT
#   - Everything in here passes through the redactor before persistence.
