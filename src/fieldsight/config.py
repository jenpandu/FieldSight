# FILE: src/fieldsight/config.py
#
# PURPOSE
# All configuration, typed with pydantic-settings. Invalid config fails at startup.
#
# REQUIREMENT REFS: §3 constraints, §10 Bounds, §10 near-boundary margins, §8 run record cost
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Settings (root) with nested groups: AwsSettings, ModelSettings,
#     KnowledgeBaseSettings, GuardrailSettings, DatabaseSettings, GatewaySettings,
#     BoundsSettings, MarginSettings, PricingSettings, RetrievalSettings.
#   - ModelSettings: model id per tier (reasoning, fast, embedding, multimodal, judge) and
#     which tier each agent uses.
#   - BoundsSettings: max tokens per call per agent, max tool invocations per turn, max
#     graph recursion depth, max reviewer iterations, max retrieved chunks and tokens,
#     per-turn wall clock, per-call HTTP timeout, per-session cost ceiling in USD.
#   - MarginSettings: near-boundary margin per rule IN THE BOUNDARY'S OWN UNIT (hours
#     around 24h, days around 30 days, days around 180 days, absolute confidence around
#     0.60). Never a percentage.
#   - PricingSettings: $ per 1k input/output tokens per model id — used to derive cost in
#     run records.
#   - RetrievalSettings: similarity refusal threshold (chosen from the golden set,
#     documented in the eval report), top_k.
#   - CONFIDENCE_FLOOR = 0.60 as a named setting consumed by R5.
#   - get_settings() cached accessor.
#
# MUST / MUST NOT
#   - Defaults live in code; environment overrides them.
#   - Validators reject nonsense (negative caps, margin >= boundary, threshold outside
#     0-1).
#   - No secrets as defaults.
#
# TESTED BY
#   tests/unit/test_config.py — invalid values fail at startup; overrides work.
#
# DONE WHEN
#   Every bound and margin in docs/architecture.md decisions table maps 1:1 to a field
#   here.
