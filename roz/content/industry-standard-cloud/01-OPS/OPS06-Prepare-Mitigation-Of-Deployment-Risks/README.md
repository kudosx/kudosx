# OPS06: How do you mitigate deployment risks?

## References

- [AWS OPS06](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops-06.html)
- [GitOps Principles](https://opengitops.dev/)
- [Argo CD](https://argo-cd.readthedocs.io/)

## Date

2025-11-27

## Focus Area

Prepare

## Tổng quan

OPS06 tập trung vào giảm thiểu risks khi deployment thông qua strategies như blue-green, canary, và GitOps.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [OPS06-BP01](OPS06-BP01-Plan-For-Unsuccessful-Changes.md) | Plan for unsuccessful changes | Có rollback plan |
| [OPS06-BP02](OPS06-BP02-Test-Deployments.md) | Test deployments | Test trong staging trước |
| [OPS06-BP03](OPS06-BP03-Safe-Deployment-Strategies.md) | Safe deployment strategies | Blue-green, canary |
| [OPS06-BP04](OPS06-BP04-Automate-Testing-Rollback.md) | Automate testing and rollback | Tự động hóa |

## Deployment Strategies

| Strategy | Description | Risk |
|----------|-------------|------|
| **Rolling** | Gradually replace instances | Medium |
| **Blue-Green** | Two identical environments | Low |
| **Canary** | Small % traffic to new version | Low |
| **Feature Flags** | Toggle features in runtime | Low |

## GitOps Principles

1. **Declarative** - Entire system described declaratively
2. **Versioned** - Canonical desired state versioned in Git
3. **Automated** - Approved changes auto-applied
4. **Self-healing** - Software agents ensure correctness

## Tools

| Tool | Type | Source |
|------|------|--------|
| Argo CD | GitOps | CNCF |
| Flux CD | GitOps | CNCF |
| Spinnaker | CD | Netflix/OSS |

## Checklist

- [ ] Rollback plan documented
- [ ] Staging environment exists
- [ ] Safe deployment strategy chosen
- [ ] Automated rollback configured
- [ ] Feature flags implemented
- [ ] GitOps workflow established
