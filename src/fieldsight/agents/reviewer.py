# FILE: src/fieldsight/agents/reviewer.py
#
# PURPOSE
# Dossier Reviewer — a harness stage with its own compiled graph and thread.
#
# REQUIREMENT REFS: §5 Reviewer, §5 P4 requirement
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Receives ONLY list[Proposal] — never worker transcripts or tool histories.
#   - Own checkpointer thread: analyst:incident:reviewer.
#   - Checks per claim: grounded (cited chunk supports it — may use
#     search_knowledge_base), cited (index resolves), attributed (threshold outcome has a
#     rule invocation id), determination-shaped language.
#   - Deterministic check: a claim that something IS an in-patient hospitalization must
#     cite 1904.39(b)(9) or (b)(10), not only the (a)(2) clock → otherwise reject as
#     'definition not established'.
#   - Returns ReviewVerdict with narrowed goals for rejected legs.
#   - Increments review_iterations.
