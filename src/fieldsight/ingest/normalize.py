# FILE: src/fieldsight/ingest/normalize.py
#
# PURPOSE
# The single structured-output call that builds NormalizedRecord.
#
# REQUIREMENT REFS: §7 Normalize
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Input: redacted Textract key/values + supporting text.
#   - Maps free-text treatments to TreatmentCode members (keeping raw text).
#   - Leaves admission_basis as stated in evidence; does not decide reportability.
#   - Attaches source artifact + confidence to each field (Textract confidence, not model
#     confidence).
#
# MUST / MUST NOT
#   - One retry with schema reminder, then typed failure.
