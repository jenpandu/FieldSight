# FILE: src/fieldsight/tools/__init__.py
#
# PURPOSE
# Tool registry: which tools each participant holds.
#
# REQUIREMENT REFS: §9 tool table
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Coordinator: none. Recordability: search_knowledge_base, get_incident_extraction,
#     evaluate_rule, propose_classification. Reportability: search_knowledge_base,
#     get_incident_extraction, evaluate_rule, propose_reporting_determination. Hazard
#     Control: search_knowledge_base, find_similar_incidents, propose_hazard_control.
#     Reviewer: search_knowledge_base.
