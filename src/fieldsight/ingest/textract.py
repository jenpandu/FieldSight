# FILE: src/fieldsight/ingest/textract.py
#
# PURPOSE
# Textract async flow and response parsing.
#
# REQUIREMENT REFS: §7 Crack, §15 preflight
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - start_analysis(s3 object, features=[FORMS, TABLES]) → job id.
#   - wait_for_job with bounded polling + backoff; pages through NextToken.
#   - parse_forms → key/value pairs with confidence; parse_tables → rows/cells preserving
#     columns.
#   - Single-page images may use the sync AnalyzeDocument; PDFs always use async.
#
# TESTED BY
#   tests/unit/test_textract_parse.py with recorded JSON responses.
