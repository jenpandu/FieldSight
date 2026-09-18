# FILE: src/fieldsight/aws/clients.py
#
# PURPOSE
# THE ONLY module that builds boto3 sessions and clients.
#
# REQUIREMENT REFS: §3 constraints (one module builds Bedrock clients), §11 (IAM roles only)
# OWNER LANE: C - agents & infra (graph, workers, API, AgentCore, CI/CD)
# TARGET SPRINT: 1
#
# WHAT GOES HERE
#   - build_session(settings): assumed role locally, default credential chain (execution
#     role) when deployed.
#   - Factory functions: bedrock_runtime, bedrock_agent_runtime (KB retrieve),
#     bedrock_agent (KB ingestion jobs), textract, s3, rds (IAM auth token),
#     bedrock_agentcore (runtime invoke), guardrail client.
#   - Shared botocore Config: adaptive retries, max attempts, connect/read timeouts from
#     BoundsSettings.
#
# MUST / MUST NOT
#   - No other module imports boto3 (enforced by ruff banned-api).
#   - Never reads access keys from config.
