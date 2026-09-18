# FILE: src/fieldsight/models/proposals.py
#
# PURPOSE
# Typed proposal objects the workers produce. Proposals never write.
#
# REQUIREMENT REFS: §5, §9 propose_* tools
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - ClassificationProposal: recordable outcome, log column, rule invocation ids, claims,
#     sources.
#   - ReportingProposal: clock (8h|24h|none), exclusion applied (if any), rule invocation
#     ids, claims, sources.
#   - HazardControlProposal: control_type (ControlType enum), mandatory
#     regulatory_citation (CFR-269 (l) paragraph or approach-distance table row, by
#     chunk_id), optional precedents from find_similar_incidents, claims.
#   - InsufficientData: worker, missing_field_or_evidence, what_was_searched.
#   - DispatchPlan (Coordinator output): workers + reason per worker, goal per worker,
#     ask_mode for ask turns
#     (answer_from_dossier|fresh_retrieval|rerun_rule|dispatch_worker), terminate flag.
#   - ReviewVerdict: verdict, per-claim findings (grounded? cited? attributed?
#     determination-shaped?), narrowed goals for re-dispatch.
