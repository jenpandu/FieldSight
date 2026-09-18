# FILE: evals/runner.py
#
# PURPOSE
# Runs golden cases through the full harness and writes results.
#
# REQUIREMENT REFS: §14
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - --tier deterministic | judge; --no-retrieval flag for the grounded-vs-ungrounded
#     contrast.
#   - Writes per-case results + per-category summary to evals/results/<timestamp>/.
