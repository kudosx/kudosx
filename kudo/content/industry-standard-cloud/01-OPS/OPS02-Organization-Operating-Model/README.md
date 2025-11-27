# OPS02: How do you structure your organization to support your business outcomes?

## References

- [AWS OPS02](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops-02.html)
- [Team Topologies](https://teamtopologies.com/)
- [Platform Engineering](https://platformengineering.org/)

## Date

2025-11-27

## Focus Area

Organization

## Tổng quan

OPS02 tập trung vào cách cấu trúc tổ chức để hỗ trợ business outcomes. Bao gồm operating model, team structure, và clear ownership.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [OPS02-BP01](OPS02-BP01-Resources-Have-Identified-Owners.md) | Resources have identified owners | Mỗi resource cần có owner |
| [OPS02-BP02](OPS02-BP02-Processes-Have-Identified-Owners.md) | Processes have identified owners | Mỗi process cần có người chịu trách nhiệm |
| [OPS02-BP03](OPS02-BP03-Operations-Have-Identified-Owners.md) | Operations have identified owners | Các hoạt động vận hành cần được phân công |
| [OPS02-BP04](OPS02-BP04-Team-Members-Know-Responsibilities.md) | Team members know responsibilities | Mọi người hiểu rõ trách nhiệm |
| [OPS02-BP05](OPS02-BP05-Mechanisms-To-Identify-Ownership.md) | Mechanisms to identify ownership | Có cơ chế xác định trách nhiệm |
| [OPS02-BP06](OPS02-BP06-Mechanisms-For-Requests.md) | Mechanisms for requests | Có process để request thay đổi |

## Team Topologies

| Team Type | Responsibility |
|-----------|---------------|
| **Stream-aligned** | End-to-end delivery cho business domain |
| **Platform** | Internal services, reduce cognitive load |
| **Enabling** | Coach và support teams |
| **Complicated-subsystem** | Deep specialist expertise |

## Checklist

- [ ] Clear ownership defined for all workloads
- [ ] RACI matrix documented
- [ ] Team interfaces defined
- [ ] Escalation paths documented
- [ ] Platform team established (if applicable)
