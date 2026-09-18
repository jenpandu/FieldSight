# FILE: src/fieldsight/db/connection.py
#
# PURPOSE
# Connection pool creation.
#
# REQUIREMENT REFS: §8 (IAM DB auth where supported; local credential for compose)
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - build_pool(settings): local DSN from typed config in local env; IAM auth token (via
#     aws/clients.py rds client) when deployed.
#   - Registers pgvector type adapters.
#
# MUST / MUST NOT
#   - No queries here — only the pool.
