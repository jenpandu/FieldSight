# FILE: src/fieldsight/ingest/packet.py
#
# PURPOSE
# Orchestrates `submit`: the 7 ingestion steps, inline and synchronous.
#
# REQUIREMENT REFS: §7 Artifact ingestion
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - 1 Store: hash each artifact, put to S3 by hash, idempotent.
#   - 2 Crack: Textract async for PDFs (wait out the job), per-field confidence kept.
#   - 3 Images: multimodal corroboration against the supervisor note (images.py).
#   - 4 Redact: deterministic by field name before anything reaches a model, log or index.
#   - 5 Prompt Attacks filter on every cracked string.
#   - 6 Normalize: one structured-output call (normalize.py).
#   - 7 Skip and log malformed artifacts; produce IngestionReport.
#
# MUST / MUST NOT
#   - Extraction is a deterministic pipeline + one structured-output call — NOT an agent.
#   - A failure on one artifact never kills the submit (P4's malformed file).
#
# DONE WHEN
#   submit on each packet yields an INC id, a stored record, and an ingestion report; P4
#   lists its malformed artifact under failures.
