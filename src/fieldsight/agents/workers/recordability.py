# FILE: src/fieldsight/agents/workers/recordability.py
#
# PURPOSE
# Recordability Worker.
#
# REQUIREMENT REFS: §5 table; R1, R3, R4
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Goal: 'Is this recordable, and which 300-Log column?'
#   - Corpus scope: CFR-1904 §§1904.4/.5/.7/.29, CPL-172, FORM-301 (use
#     doc_type/section_path filters).
#   - Multi-hop: 1904.7(b)(3) day counting → FORM-301 column definitions; CPL-172 IX.E.10
#     → 1904.7(b)(5)(ii).
#   - Ends by calling propose_classification.
