# FILE: src/fieldsight/agents/state.py
#
# PURPOSE
# Typed graph state and reducers.
#
# REQUIREMENT REFS: §5 graph shape
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - FlowState TypedDict: incident context (redacted), plan, goals per worker, proposals,
#     rule_invocations, retrieval log, review verdict, review_iterations, triggers_seen.
#   - Reducers for keys written by parallel workers: merge_by_worker (a re-dispatched
#     worker REPLACES its previous proposal), operator.add for append-only logs.
#
# MUST / MUST NOT
#   - Without reducers, two parallel workers writing the same key raises at runtime.
