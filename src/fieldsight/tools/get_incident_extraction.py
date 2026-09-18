# FILE: src/fieldsight/tools/get_incident_extraction.py
#
# PURPOSE
# Read tool routed via AgentCore Gateway → ECS API.
#
# REQUIREMENT REFS: §9
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - No model-supplied incident id — subject injected.
#   - Returns the normalized record fields with confidence, or a structured entitlement
#     denial.
#   - Gateway unreachable → ToolUnavailable; capability disabled, rest continues.
