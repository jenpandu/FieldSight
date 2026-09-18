# FILE: src/fieldsight/agents/workers/reportability.py
#
# PURPOSE
# Reportability Worker.
#
# REQUIREMENT REFS: §5 table; R2
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Goal: 'Is this reportable, on what clock, and does an exclusion apply?'
#   - Corpus scope: CFR-1904 §1904.39, FR-2014, LOI-PACK.
#   - Must establish admission_basis from evidence and ground it in (b)(9)/(b)(10) before
#     evaluate_rule.
#   - Multi-hop: §1904.39 → LOI carving out the exception; CPL-172 IX.P.1 → LOI
#     2021-01-08.
#   - Ends by calling propose_reporting_determination.
