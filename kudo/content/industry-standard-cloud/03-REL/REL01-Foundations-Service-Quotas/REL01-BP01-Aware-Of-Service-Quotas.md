# REL01-BP01: Aware of service quotas and constraints

## Description

Biết và hiểu các limits của services đang sử dụng để tránh unexpected failures.

## Implementation Guidance

- Document all service quotas for services being used
- Understand default vs maximum quotas
- Identify which quotas can be increased vs fixed
- Create a quota inventory for your workload
- Review quotas when adding new services

## Risk Level

High - Hitting quotas unexpectedly can cause service outages.

## Related Best Practices

- [REL01-BP02](REL01-BP02-Manage-Service-Quotas.md)
- [REL06-BP01](../REL06-Change-Resource-Monitoring/REL06-BP01-Monitor-All-Components.md)
