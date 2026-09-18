# FILE: src/fieldsight/tools/search_knowledge_base.py
#
# PURPOSE
# Native read tool over retrieval.py.
#
# REQUIREMENT REFS: §9
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Pydantic input: query, optional doc_type, optional section_path. Output: chunks with
#     source indices or a structured refusal.
#   - Precise docstring with per-parameter descriptions (it becomes the tool description).
