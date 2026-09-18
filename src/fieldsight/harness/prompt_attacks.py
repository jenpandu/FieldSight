# FILE: src/fieldsight/harness/prompt_attacks.py
#
# PURPOSE
# Stage 2 — Bedrock Guardrails Prompt Attacks filter.
#
# REQUIREMENT REFS: §10 stage 2, §11 indirect injection
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Runs on analyst input and on every string cracked out of an artifact (the latter
#     also at submit).
#   - Fires → event + escalation trigger 'prompt attack filter fired'.
