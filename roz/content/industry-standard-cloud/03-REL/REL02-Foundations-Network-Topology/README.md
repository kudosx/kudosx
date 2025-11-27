# REL02: How do you plan your network topology?

## References

- [AWS REL02](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-02.html)

## Date

2025-11-27

## Focus Area

Foundations

## Tổng quan

REL02 tập trung vào network topology design cho reliability.

## Best Practices

### REL02-BP01: Use highly available network connectivity for workload public endpoints
Multiple AZs, regions.

### REL02-BP02: Provision redundant connectivity between private networks
Redundant connections.

### REL02-BP03: Ensure IP subnet allocation accounts for expansion and availability
IP planning.

### REL02-BP04: Prefer hub-and-spoke topologies over many-to-many mesh
Simplified topology.

### REL02-BP05: Enforce non-overlapping private IP address ranges
Avoid IP conflicts.

## Checklist

- [ ] Multi-AZ deployment
- [ ] Redundant network paths
- [ ] IP ranges planned
- [ ] Network topology documented
