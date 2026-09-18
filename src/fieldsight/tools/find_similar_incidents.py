# FILE: src/fieldsight/tools/find_similar_incidents.py
#
# PURPOSE
# Read tool routed via Gateway → ECS API (pgvector).
#
# REQUIREMENT REFS: §9
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Returns candidates: incident id, closed outcome, deciding rule, similarity score,
#     matching narrative span.
#   - Never a conclusion.
#
# MUST / MUST NOT
#   - A worker adopting the nearest neighbour's outcome as its own is a failure — reviewer
#     checks for it.
