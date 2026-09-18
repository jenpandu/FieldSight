# FILE: src/fieldsight/agents/graph.py
#
# PURPOSE
# build_graph() — the LangGraph StateGraph. Imported by both the CLI and the AgentCore
# Runtime entrypoint.
#
# REQUIREMENT REFS: §5 graph shape + requirements table
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Nodes: coordinator, recordability, reportability, hazard_control (each worker a
#     compiled subgraph), reviewer, eligibility.
#   - START → coordinator.
#   - Conditional edges coordinator → list of workers from the typed DispatchPlan (plain
#     Python routing function). Returning several names runs them concurrently.
#   - Each worker → reviewer. Reviewer runs once, after all dispatched workers finish in
#     the same step.
#   - Conditional edge reviewer → coordinator (rejected, under cap) or → eligibility
#     (approved OR cap reached).
#   - eligibility → END.
#   - Compile with the Postgres checkpointer; invoke with recursion_limit from
#     BoundsSettings.
#
# MUST / MUST NOT
#   - LangGraph carries the topology — no hand-rolled asyncio loop, no other agent
#     framework.
#   - Two independent caps: recursion_limit AND review_iterations in state.
#
# TESTED BY
#   tests/integration/test_graph_shapes.py — P1 one worker, P2 three with concurrency, P3
#   none, P4 rejection + re-dispatch.
