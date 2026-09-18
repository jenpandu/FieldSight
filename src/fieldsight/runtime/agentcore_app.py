# FILE: src/fieldsight/runtime/agentcore_app.py
#
# PURPOSE
# AgentCore Runtime entrypoint (Bring Your Own Framework).
#
# REQUIREMENT REFS: §3, §15
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 3
#
# WHAT GOES HERE
#   - Wraps build_graph() + harness with the bedrock-agentcore SDK app/entrypoint (verify
#     names against the pin).
#   - Payload: command, incident id, analyst identity (verified), question.
#   - Uses the Runtime execution role.
