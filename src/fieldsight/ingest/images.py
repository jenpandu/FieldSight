# FILE: src/fieldsight/ingest/images.py
#
# PURPOSE
# Multimodal photo corroboration.
#
# REQUIREMENT REFS: §7 Images, §10 trigger 'photo contradicts narrative'
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - For each image: Bedrock multimodal call with the redacted narrative →
#     PhotoCorroboration (structured output).
#   - Malformed images (zero-byte, truncated JPEG) raise MalformedArtifact → skipped and
#     logged.
#
# DONE WHEN
#   P4's photo returns 'contradicts'; P2's corroborates.
