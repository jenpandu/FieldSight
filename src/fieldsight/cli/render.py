# FILE: src/fieldsight/cli/render.py
#
# PURPOSE
# Terminal rendering (rich).
#
# REQUIREMENT REFS: §12 operator surface
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Dossier with numbered sources and visible rule provenance (rule, inputs).
#   - Trace: plan, dispatches + why, tool loops, retrievals with scores, rule calls,
#     reviewer verdicts, tokens/cost per agent.
#   - Queue listing with named triggers; decision card for approve / edit-then-approve /
#     reject.
#   - Refusals rendered as answers: reason, what was searched, escalation path.
#   - Persistent AI-generated + synthetic-data disclosure on every dossier.
