# FILE: src/fieldsight/retrieval.py
#
# PURPOSE
# THE ONLY module that talks to the Knowledge Base.
#
# REQUIREMENT REFS: §3 constraints, §7 Query pipeline
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - retrieve(query, filters: doc_type/section_path, k) → list[RetrievedChunk] with
#     scores.
#   - Refusal gate: if best score < threshold → BelowThreshold carrying what was searched.
#   - Multi-hop: when a CPL-172 or LOI chunk construes a Part 1904 section, run a second
#     filtered retrieval on CFR-1904 at that section_path.
#   - get_chunk(chunk_id) for `fieldsight sources --ref`.
#   - Records every retrieval (query, filters, chunk ids, scores, latency) in the run
#     record.
#
# MUST / MUST NOT
#   - Retrieval unavailable → RetrievalUnavailable; workers refuse, never answer from
#     memory.
#   - Target < 800 ms.
