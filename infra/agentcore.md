# AgentCore (§9, §15)

- Runtime: BYO framework container, execution role, how to update to a new digest.
- Gateway: MCP server exposing the read tools; OpenAPI target → ALB for find_similar_incidents and get_incident_extraction; inbound auth.
- Identity: how callers are verified (e.g. Cognito/JWT); what an unverified request gets.
- External client demo: MCP Inspector or Claude Code config used to list and call tools.
