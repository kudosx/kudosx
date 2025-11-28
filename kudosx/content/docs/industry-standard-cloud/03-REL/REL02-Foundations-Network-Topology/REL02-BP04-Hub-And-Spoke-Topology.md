# REL02-BP04: Prefer hub-and-spoke topologies over mesh

## Description

Sử dụng hub-and-spoke topology thay vì mesh phức tạp.

## Implementation Guidance

- Centralize network transit in hub
- Connect spokes through hub only
- Simplify routing tables
- Reduce number of connections to manage
- Implement consistent security policies at hub

## Risk Level

Low - Simpler topology is easier to manage and troubleshoot.

## Related Best Practices

- [REL02-BP02](REL02-BP02-Redundant-Connectivity.md)
- [REL03-BP01](../REL03-Workload-Service-Architecture/REL03-BP01-Segment-Workload.md)
