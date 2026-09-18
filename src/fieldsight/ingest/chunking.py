# FILE: src/fieldsight/ingest/chunking.py
#
# PURPOSE
# Structure-aware chunking with stable ids.
#
# REQUIREMENT REFS: §7 Corpus ingestion
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Heading detectors per document: CFR '§ 1904.x' + bare (b)/(10) markers; CFR-269
#     paragraph (l) sub-paragraphs and tables; CPL-172 section designations (IX.E, IX.P
#     ...); FR-2014 page anchors; LOI-PACK split by letter date; FORM-301 by page/column
#     definitions.
#   - Fallback size-based split; record chunk size and overlap as config.
#   - chunk_id = deterministic hash of (doc_id, section_path, ordinal).
#   - section_path in citation form, e.g. 1904.39(b)(10).
#
# TESTED BY
#   tests/unit/test_chunking.py — ids stable across runs; tables kept whole; (b)(10) gets
#   its own section_path.
