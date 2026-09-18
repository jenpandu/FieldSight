# FILE: src/fieldsight/harness/readiness.py
#
# PURPOSE
# Stage 3 — readiness gate.
#
# REQUIREMENT REFS: §10 stage 3
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Fast-tier classification into ReadinessLabel.
#   - policy_question → answer from retrieval, no worker. classify → run workflow. action
#     → refuse outright (nothing writes without two-person approval). out_of_scope →
#     refuse, name escalation path.
#   - Deterministic check regardless of label: normalized record exists, required fields
#     present, R5 floor passes.
#   - The check can stop a classify turn, never start one.
#
# DONE WHEN
#   P3 is stopped here with the illegible field named; no worker is dispatched.
