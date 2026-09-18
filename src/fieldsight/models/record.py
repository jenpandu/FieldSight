# FILE: src/fieldsight/models/record.py
#
# PURPOSE
# The normalized incident record produced by extraction.
#
# REQUIREMENT REFS: §7 Normalize, §8 seeds share this field set
# OWNER LANE: A - data (repository, seeds, ingestion, retrieval)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - ExtractedField[T]: value, confidence, source_artifact_hash, source_page,
#     textract_block_id.
#   - NormalizedRecord (extra='forbid'): case_number, establishment_id, date_of_injury,
#     time_of_event, time_began_work, date_of_treatment, return_to_work_date (optional),
#     activity_before, what_happened, injury_description, body_part, treatments
#     (list[TreatmentCode] with raw text), treated_in_er, inpatient_checkbox,
#     admission_basis, admitted_at, date_of_death, amputation, loss_of_eye,
#     days_restricted, equipment_energized, narrative_redacted.
#   - IngestionReport: artifacts_processed, fields_extracted, fields_below_floor, failures
#     (artifact, reason).
#   - PhotoCorroboration: artifact_hash, verdict, rationale.
#
# MUST / MUST NOT
#   - Every field carries its source artifact and confidence.
#   - Employee name/address/DOB never appear — they are redacted before this model is
#     built.
