# FILE: src/fieldsight/models/refusals.py
#
# PURPOSE
# Refusals as first-class typed outputs, rendered as answers not errors.
#
# REQUIREMENT REFS: §10, §12 operator surface
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Refusal: reason_code (RefusalReason), what_was_searched, escalation_path text,
#     missing_field (optional), partial_result (optional, for budget ceilings).
#   - DegradedResponse: unavailable_capabilities, what still ran.
