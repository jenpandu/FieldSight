# FILE: src/fieldsight/models/dossier.py
#
# PURPOSE
# The rendered output of analyze.
#
# REQUIREMENT REFS: §1, §12
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 2
#
# WHAT GOES HERE
#   - Dossier: incident_id, workers_ran (+why), proposals, rule outcomes with provenance,
#     claims + sources, photo verdicts, ingestion gaps, escalation status + triggers,
#     disclosure text, synthetic-data notice.
#   - ReviewRecord: original_payload, edited_payload (narrative only), approver, decision,
#     timestamp.
#
# MUST / MUST NOT
#   - Edit-then-approve may change wording, notes, or repoint a citation within the same
#     source — never a rule outcome, computed date or cited document. Validate this in
#     code.
