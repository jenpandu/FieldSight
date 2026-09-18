# FILE: src/fieldsight/tools/propose.py
#
# PURPOSE
# propose_classification, propose_reporting_determination, propose_hazard_control.
#
# REQUIREMENT REFS: §5, §9
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Each takes a typed proposal, returns it validated or rejected, writes nothing.
#   - propose_hazard_control citation gate (schema-level): regulatory_citation.chunk_id
#     must resolve to a CFR-269 paragraph (l) chunk or an approach-distance table row;
#     otherwise rejected.
#   - No resolving control → worker returns InsufficientData.
#
# TESTED BY
#   tests/unit/test_propose_citation_gate.py (separate from the output-guard support
#   check).
