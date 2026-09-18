# FILE: src/fieldsight/tools/gateway_client.py
#
# PURPOSE
# Client the CLI/runtime uses to call the AgentCore Gateway MCP server.
#
# REQUIREMENT REFS: §9 AgentCore Gateway
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 3
#
# WHAT GOES HERE
#   - Obtains the caller's OAuth token (AgentCore Identity / Cognito) — identity comes
#     from the token, never from an argument.
#   - Health probe so the harness can report which capabilities are down.
