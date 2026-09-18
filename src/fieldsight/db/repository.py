# FILE: src/fieldsight/db/repository.py
#
# PURPOSE
# THE ONLY module that runs SQL. Pydantic in, Pydantic out.
#
# REQUIREMENT REFS: §3 constraints, §8, §11
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - Incidents: create/get normalized record, store extraction fields with confidence,
#     store artifacts by hash (idempotent).
#   - Entitlements: analyst_can_read(analyst_id, incident_id) via grants over
#     establishment partition.
#   - Similar incidents: find_similar(embedding, k, entitled_establishments) using
#     pgvector; returns incident id, closed outcome, deciding rule, score, matching
#     narrative span.
#   - Run records: append-only insert; insert_correction(supersedes_id, ...);
#     get_for_incident.
#   - Review queue: enqueue(triggers), list_queue(), record_decision(original_payload,
#     edited_payload, approver, decision, ts).
#   - Sessions: get_or_create(analyst_id, incident_id); accumulate cost; load for ask.
#   - Write layer target: the post-approval execution write, keyed by idempotency key.
#
# MUST / MUST NOT
#   - Parameterized queries only — no f-string SQL.
#   - extra='forbid' on anything parsed from outside the process.
#   - No model-authored SQL exists anywhere.
#
# TESTED BY
#   tests/integration/test_repository.py against compose Postgres.
