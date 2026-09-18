# FILE: src/fieldsight/harness/events.py
#
# PURPOSE
# Event sink.
#
# REQUIREMENT REFS: §10 (an event has a sink)
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - emit(event): writes a row on the turn's run record AND a structured log line with
#     correlation id, remedy, triggering field/claim.
