# REL01-BP03: Accommodate fixed service quotas through architecture

## Description

Design architecture để work within limits không thể thay đổi.

## Implementation Guidance

- Identify hard limits that cannot be increased
- Design workload to work within constraints
- Implement sharding or partitioning patterns
- Use multiple accounts/regions if needed
- Consider alternative services with higher limits

## Risk Level

Medium - Architecture must respect immutable constraints.

## Related Best Practices

- [REL01-BP01](REL01-BP01-Aware-Of-Service-Quotas.md)
- [REL03-BP01](../REL03-Workload-Service-Architecture/REL03-BP01-Segment-Workload.md)
