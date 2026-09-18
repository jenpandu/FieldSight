# FILE: src/fieldsight/ingest/corpus.py
#
# PURPOSE
# Offline corpus ingestion into the Bedrock Knowledge Base.
#
# REQUIREMENT REFS: §7 Corpus ingestion, §17 CFR-269 tables
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Crack corpus/pdf/*.pdf via Textract async.
#   - Chunk via chunking.py.
#   - Write each chunk to S3 as its own object with a .metadata.json sidecar (doc_id,
#     title, doc_type, section_path, page, chunk_id).
#   - KB data source configured with chunking strategy NONE so your chunk ids survive.
#   - Start ingestion job and wait.
#   - Explicit check that every CFR-269 approach-distance table survives with columns
#     intact.
