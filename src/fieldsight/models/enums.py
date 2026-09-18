# FILE: src/fieldsight/models/enums.py
#
# PURPOSE
# Every closed vocabulary in the system, defined in code.
#
# REQUIREMENT REFS: §5 (control type enum), §6, §10 readiness labels
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - ReadinessLabel: policy_question, classify, action, out_of_scope.
#   - WorkerName: recordability, reportability, hazard_control.
#   - AdmissionBasis: none, care_or_treatment (1904.39(b)(9)),
#     observation_or_diagnostic_only (1904.39(b)(10)).
#   - AmputationKind: none, amputation, plus every (b)(11) exclusion: avulsion,
#     enucleation, degloving, scalping, severed_ear, broken_tooth, chipped_tooth.
#   - TreatmentCode: the 14 first-aid items (A)-(N) of 1904.7(b)(5)(ii), known non-first-
#     aid codes (sutures, staples, rx_medication, rigid_splint, surgery, physical_therapy,
#     other_immunization ...), and other_unlisted.
#   - LogColumn: G, H, I, J.
#   - ControlType: the hazard-control types CFR-269 paragraph (l) can ground (e.g. minimum
#     approach distance, insulating PPE, insulated tools, de-energize/ground, qualified-
#     person requirement ...) — derive the list by reading (l).
#   - CorroborationVerdict: corroborates, contradicts, inconclusive.
#   - ReviewVerdictKind: approved, rejected.
#   - TriggerName: one member per §10 escalation trigger.
#   - RefusalReason: below_threshold, out_of_corpus, determination_request,
#     action_request, readiness_blocked, budget_exceeded, capability_unavailable,
#     prompt_attack.
#   - ReviewDecision: approve, edit_then_approve, reject.
