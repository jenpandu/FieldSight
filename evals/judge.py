# FILE: evals/judge.py
#
# PURPOSE
# Groundedness / citation accuracy evaluator.
#
# REQUIREMENT REFS: §14 custom evaluators
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Separate Bedrock Converse call on the JUDGE deployment (not the reasoning tier).
#   - Input: claim + cited chunk text. Output: Pydantic verdict supported / not_supported
#     / partially_supported + rationale.
