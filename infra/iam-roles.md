# IAM roles (§11)

One section per role with its trust policy and least-privilege permissions:
- Local developer assumed role
- AgentCore Runtime execution role
- AgentCore Gateway role
- ECS task role and task execution role
- GitHub Actions OIDC deploy role
- Knowledge Base service role
- Textract access (S3 read on artifact/corpus buckets)

No long-lived access keys anywhere.
