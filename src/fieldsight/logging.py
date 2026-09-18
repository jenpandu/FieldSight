# FILE: src/fieldsight/logging.py
#
# PURPOSE
# Structured logging with the correlation id carried in a contextvar.
#
# REQUIREMENT REFS: §10 events have a sink, §13
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - correlation_id ContextVar + helpers to set/get per turn.
#   - structlog (or stdlib JSON) config that injects correlation_id, command, incident_id,
#     participant on every line.
#   - A processor that passes every event through the single redactor (ingest/redact.py)
#     before emission.
#
# MUST / MUST NOT
#   - No PII in any log line — redaction is enforced here, not by convention.
