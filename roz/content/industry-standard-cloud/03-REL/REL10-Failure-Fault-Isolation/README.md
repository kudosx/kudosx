# REL10: How do you use fault isolation to protect your workload?

## References

- [AWS REL10](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-10.html)

## Date

2025-11-27

## Focus Area

Failure Management

## Tổng quan

REL10 tập trung vào fault isolation strategies.

## Best Practices

### REL10-BP01: Deploy workload to multiple locations
Multi-AZ, multi-region.

### REL10-BP02: Automate recovery for single-location failures
Auto failover.

### REL10-BP03: Employ bulkhead architectures
Separate failure domains.

## Bulkhead Pattern

Isolate failures to prevent cascade effects.

## Checklist

- [ ] Multi-AZ deployment
- [ ] Failover automated
- [ ] Failure domains isolated
