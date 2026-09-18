# ECS Fargate + ALB (§15)

Cluster, task definition referencing ECR image BY DIGEST, service with min 2 tasks, ALB + target group health check on /readyz, auto-scaling on CPU or request count.
