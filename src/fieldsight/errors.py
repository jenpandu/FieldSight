# FILE: src/fieldsight/errors.py
#
# PURPOSE
# Custom exception hierarchy so failures are distinguishable by type.
#
# REQUIREMENT REFS: §13 code quality, §13 failure behaviour
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - FieldSightError (base) → ExtractionError, TextractJobFailed, MalformedArtifact;
#     RetrievalError, RetrievalUnavailable, BelowThreshold; RuleError; GateError,
#     ReadinessBlocked, PromptAttackDetected; OutputGuardViolation; BudgetExceeded,
#     TokenCeilingExceeded; ToolUnavailable (Gateway/ECS down); EntitlementDenied;
#     StructuredOutputInvalid; WriteFailedAfterApproval.
#   - Each carries a machine-readable reason_code used by typed refusals and run-record
#     events.
#
# MUST / MUST NOT
#   - Tools and harness convert these to structured results/refusals; they never leak as
#     tracebacks to the analyst.
