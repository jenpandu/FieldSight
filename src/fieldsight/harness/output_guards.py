# FILE: src/fieldsight/harness/output_guards.py
#
# PURPOSE
# Stage 4 — deterministic output checks over the turn's own run record.
#
# REQUIREMENT REFS: §10 stage 4
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Uncited claims.
#   - Assertions without provenance.
#   - Threshold outcomes with no rules-engine invocation THIS TURN → blocked.
#   - Determination-shaped language (phrase list + fast-tier check).
#   - Missing disclosure.
#   - PII in output.
#   - Citation support check (judge-style) — separate from propose_hazard_control's schema
#     gate.
