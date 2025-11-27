# OPS05: How do you reduce defects, ease remediation, and improve flow into production?

## References

- [AWS OPS05](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops-05.html)
- [The Twelve-Factor App](https://12factor.net/)
- [Terraform](https://www.terraform.io/)
- [Open Policy Agent](https://www.openpolicyagent.org/)

## Date

2025-11-27

## Focus Area

Prepare

## Tổng quan

OPS05 tập trung vào giảm defects, dễ dàng remediation, và cải thiện flow vào production thông qua IaC, testing, và CI/CD.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [OPS05-BP01](OPS05-BP01-Use-Version-Control.md) | Use version control | Sử dụng version control cho code |
| [OPS05-BP02](OPS05-BP02-Test-And-Validate.md) | Test and validate changes | Implement testing strategies |
| [OPS05-BP03](OPS05-BP03-Configuration-Management.md) | Configuration management | Quản lý configuration |
| [OPS05-BP04](OPS05-BP04-Build-Deployment-Management.md) | Build and deployment management | CI/CD pipelines |
| [OPS05-BP05](OPS05-BP05-Patch-Management.md) | Patch management | Regular patching |
| [OPS05-BP06](OPS05-BP06-Share-Design-Standards.md) | Share design standards | Chia sẻ design standards |
| [OPS05-BP07](OPS05-BP07-Code-Quality.md) | Code quality practices | Code reviews, linting |

## Infrastructure as Code

| Tool | Language | License |
|------|----------|---------|
| Terraform | HCL | BSL |
| OpenTofu | HCL | MPL 2.0 |
| Pulumi | Python/TS/Go | Apache 2.0 |

## Twelve-Factor App

1. Codebase - One codebase, many deploys
2. Dependencies - Explicitly declare dependencies
3. Config - Store config in environment
4. Backing services - Treat as attached resources
5. Build, release, run - Separate stages
6. Processes - Stateless processes
7. Port binding - Export services via port
8. Concurrency - Scale via process model
9. Disposability - Fast startup, graceful shutdown
10. Dev/prod parity - Keep environments similar
11. Logs - Treat as event streams
12. Admin processes - Run as one-off processes

## Checklist

- [ ] Version control for all code
- [ ] CI/CD pipelines configured
- [ ] Infrastructure as Code implemented
- [ ] Policy as Code implemented
- [ ] Testing strategy defined
- [ ] Code review process established
