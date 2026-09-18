# FILE: src/fieldsight/cli/main.py
#
# PURPOSE
# Console entry point with the 8 commands.
#
# REQUIREMENT REFS: §12
# OWNER LANE: B - core (rules engine, harness, escalation, CLI)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - submit <dir> → INC id (cracks inline, waits for Textract).
#   - analyze <id>, dossier <id>, ask <id> '<q>', sources <id> --ref N, trace <id>, queue,
#     review <id>.
#   - Each command: load config → build boto3 session → build graph → run harness →
#     render. ~10 lines each; logic lives in the package.
#
# MUST / MUST NOT
#   - Needs --analyst identity (or from config/token) for entitlements.
