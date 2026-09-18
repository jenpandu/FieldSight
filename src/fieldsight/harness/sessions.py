# FILE: src/fieldsight/harness/sessions.py
#
# PURPOSE
# Session management across commands.
#
# REQUIREMENT REFS: §10 Sessions
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Session keyed by (analyst_id, incident_id); participant thread ids from
#     db/checkpointer.py.
#   - Loads prior dossier + rule invocations for ask.
