# FILE: src/fieldsight/agents/coordinator.py
#
# PURPOSE
# The Coordinator node: plans, dispatches, judges completeness, re-dispatches.
#
# REQUIREMENT REFS: §5 Coordinator, §10 ask is a planning case
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - One Bedrock call (reasoning or fast tier — decide) returning DispatchPlan via
#     structured output.
#   - Hazard Control only when equipment_energized (CFR-269 can ground a control) —
#     enforce in the routing function too, not just the prompt.
#   - Re-dispatch on insufficient_data, low-confidence findings, or rejected citations,
#     with a NARROWED goal taken from the ReviewVerdict.
#   - First-pass reportability goal is narrow ('determine the applicable reporting clock')
#     — this is what makes P4's rejection reproducible.
#   - For ask turns, sets ask_mode: answer_from_dossier / fresh_retrieval / rerun_rule /
#     dispatch_worker.
#   - Records which workers ran and why.
#
# MUST / MUST NOT
#   - No tools.
#   - Dispatching every worker on every incident is a failure.
