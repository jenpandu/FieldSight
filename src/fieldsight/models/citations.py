# FILE: src/fieldsight/models/citations.py
#
# PURPOSE
# Machine-checkable citations.
#
# REQUIREMENT REFS: §7 query pipeline, §12 citations that resolve
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Source: index, doc_id, title, section_path, chunk_id, score.
#   - Claim: text, source_indices (list[int]), kind (fact|threshold|precedent).
#   - RetrievedChunk: chunk_id, doc_id, title, doc_type, section_path, page, text, score.
#
# MUST / MUST NOT
#   - Prose refers to sources by index only; every index must resolve.
