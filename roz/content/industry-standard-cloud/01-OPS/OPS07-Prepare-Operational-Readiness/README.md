# OPS07: How do you know that you are ready to support a workload?

## References

- [AWS OPS07](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops-07.html)
- [Google SRE - Runbooks](https://sre.google/sre-book/effective-troubleshooting/)

## Date

2025-11-27

## Focus Area

Prepare

## Tổng quan

OPS07 đảm bảo team sẵn sàng support workload thông qua runbooks, playbooks, và operational readiness reviews.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [OPS07-BP01](OPS07-BP01-Personnel-Capability.md) | Personnel capability | Team có đủ skills |
| [OPS07-BP02](OPS07-BP02-Operational-Readiness-Review.md) | Operational readiness review | Regular ORR |
| [OPS07-BP03](OPS07-BP03-Use-Runbooks.md) | Use runbooks | Documented runbooks |
| [OPS07-BP04](OPS07-BP04-Use-Playbooks.md) | Use playbooks | Playbooks cho troubleshooting |
| [OPS07-BP05](OPS07-BP05-Informed-Decisions.md) | Informed decisions | Đủ thông tin trước deploy |

## Runbooks vs Playbooks

| Type | Purpose | When |
|------|---------|------|
| **Runbook** | Step-by-step routine procedures | Scheduled tasks |
| **Playbook** | Troubleshooting guides | Incidents |

## Runbook Template

```markdown
# Runbook: [Name]

## Purpose
[What this runbook accomplishes]

## Prerequisites
- [ ] Required access
- [ ] Required tools

## Steps
1. Step one
2. Step two
3. Step three

## Verification
How to verify success

## Rollback
Steps to rollback if needed
```

## Checklist

- [ ] Team trained on workload
- [ ] ORR process established
- [ ] Runbooks documented
- [ ] Playbooks for common issues
- [ ] On-call rotation defined
- [ ] Escalation paths documented
