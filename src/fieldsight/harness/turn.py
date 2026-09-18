# FILE: src/fieldsight/harness/turn.py
#
# PURPOSE
# run_turn(command, session, request) — the one pipeline for every turn.
#
# REQUIREMENT REFS: §10 (four ordered stages), §10 sessions
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Sets correlation id; loads session + budget from Postgres.
#   - Stage 1 input_validation → Stage 2 prompt_attacks → Stage 3 readiness → graph (only
#     for classify, or ask planning) → Stage 4 output_guards → remedies → escalation →
#     persist run record.
#   - Harness invokes the authoritative rules deterministically on the normalized record.
#   - Returns Dossier | Answer | Refusal | DegradedResponse.
#
# MUST / MUST NOT
#   - ask goes through the full harness — same guards, bounds, output checks, run record.
#   - Every command starts cold and reads state from Postgres.
