# FILE: src/fieldsight/agents/workers/base.py
#
# PURPOSE
# Builds a worker subgraph: model node ↔ tool node loop.
#
# REQUIREMENT REFS: §5 (workers loop on their own tools)
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Model bound to the worker's tools via Converse toolConfig (through aws/bedrock.py or
#     langchain-aws with the client injected).
#   - Loop continues while stop_reason == tool_use; stops when the model stops requesting
#     tools OR the tool-call cap is hit.
#   - Termination is a structured event (stop reason / cap), never phrasing.
#   - Output: exactly one typed proposal or InsufficientData.
#
# MUST / MUST NOT
#   - A fixed one-retrieval-one-rule shape fails the requirement.
#   - Retrieval down → worker returns a refusal, never an ungrounded answer.
