# OPS10: How do you manage workload and operations events?

## References

- [AWS OPS10](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops-10.html)
- [Google SRE - Incident Management](https://sre.google/sre-book/managing-incidents/)

## Date

2025-11-27

## Focus Area

Operate

## Tổng quan

OPS10 tập trung vào quản lý events bao gồm planned events và unplanned events (incidents).

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [OPS10-BP01](OPS10-BP01-Event-Incident-Problem-Management.md) | Event, incident, problem management | Process rõ ràng |
| [OPS10-BP02](OPS10-BP02-Process-Per-Alert.md) | Process per alert | Mỗi alert có response |
| [OPS10-BP03](OPS10-BP03-Prioritize-Events.md) | Prioritize events | Prioritize theo business impact |
| [OPS10-BP04](OPS10-BP04-Escalation-Paths.md) | Escalation paths | Escalation paths rõ ràng |
| [OPS10-BP05](OPS10-BP05-Customer-Communication.md) | Customer communication | Communication plan |
| [OPS10-BP06](OPS10-BP06-Status-Dashboards.md) | Status dashboards | Status page cho stakeholders |
| [OPS10-BP07](OPS10-BP07-Automate-Responses.md) | Automate responses | Tự động hóa responses |

## Incident Severity Levels

| Level | Impact | Response Time |
|-------|--------|---------------|
| **SEV1** | Critical - total outage | Immediate |
| **SEV2** | Major - degraded service | < 1 hour |
| **SEV3** | Minor - limited impact | < 4 hours |
| **SEV4** | Low - minimal impact | Next business day |

## Checklist

- [ ] Incident management process defined
- [ ] On-call rotation established
- [ ] Escalation paths documented
- [ ] Communication templates ready
- [ ] Status page configured
- [ ] Automated responses implemented
