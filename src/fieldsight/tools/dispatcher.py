# FILE: src/fieldsight/tools/dispatcher.py
#
# PURPOSE
# Executes tool calls for agents; injects the session subject.
#
# REQUIREMENT REFS: §9 tool rules
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Injects incident_id / analyst_id from the session — never from model arguments.
#   - Computes the idempotency key, enforces the per-turn tool-call cap, records every
#     invocation.
#   - Converts exceptions into structured tool errors.
#
# MUST / MUST NOT
#   - No tool schema exposed to a model contains an incident id.
