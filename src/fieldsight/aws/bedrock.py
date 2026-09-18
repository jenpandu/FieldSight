# FILE: src/fieldsight/aws/bedrock.py
#
# PURPOSE
# Thin Converse API wrapper every agent, extractor, gate and judge goes through.
#
# REQUIREMENT REFS: §3 (all models via Converse), §4 service 4 (Guardrails on every call), §8 run record token/cost
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - converse(model_tier, messages, system, tools=None, tool_choice=None) → typed
#     ConverseResult (text/tool uses, stop_reason, usage, latency).
#   - Always attaches guardrailConfig (content filters) to every call.
#   - structured_output(model_tier, prompt, schema: type[BaseModel]) — forces a tool call
#     whose inputSchema is schema.model_json_schema(); validates; one retry with the
#     validation error as a schema reminder; then StructuredOutputInvalid.
#   - apply_guardrail(text, source='INPUT') for the Prompt Attacks filter on analyst input
#     and cracked strings.
#   - Usage accounting: tokens, model id, duration, cost from PricingSettings → pushed to
#     the turn's budget and run record.
#
# MUST / MUST NOT
#   - Never parse model prose with regex to recover structure.
#   - Budget checked before each call (check-and-stop).
