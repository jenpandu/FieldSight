# FILE: src/fieldsight/ingest/redact.py
#
# PURPOSE
# THE ONE redactor used everywhere (ingest, logs, run records, eval store).
#
# REQUIREMENT REFS: §7 Redact, §11
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Redact by field name: employee full name, street, city/state/zip, date of birth (and
#     any other Form 301 personal fields you decide).
#   - Returns (redacted_text, removed_spans).
#   - A second pass for output: detects PII in generated text for the 'PII in output'
#     remedy.
#
# MUST / MUST NOT
#   - Deterministic. No model involvement.
#
# TESTED BY
#   tests/unit/test_redact.py
