# FILE: src/fieldsight/db/checkpointer.py
#
# PURPOSE
# LangGraph Postgres checkpointer on the same instance.
#
# REQUIREMENT REFS: §8 (checkpointer keyed by thread id), §10 sessions
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - build_checkpointer(pool) using langgraph-checkpoint-postgres (verify class name
#     against the pin).
#   - thread_id(analyst_id, incident_id, participant) → 'analyst:incident:participant'.
#     One per participant, created once and reused.
#
# MUST / MUST NOT
#   - The Reviewer's thread id never equals a worker's.
