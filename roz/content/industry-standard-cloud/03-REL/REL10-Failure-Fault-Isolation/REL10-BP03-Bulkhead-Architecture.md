# REL10-BP03: Employ bulkhead architectures

## Description

Use bulkheads để isolate failure domains.

## Implementation Guidance

- Separate resources per tenant/workload
- Implement cell-based architecture
- Use separate databases per service
- Isolate critical from non-critical paths
- Test isolation effectiveness

## Risk Level

Medium - Shared resources allow failures to spread.

## Related Best Practices

- [REL10-BP01](REL10-BP01-Deploy-Multiple-Locations.md)
- [REL04-BP02](../REL04-Workload-Distributed-Systems/REL04-BP02-Loosely-Coupled-Dependencies.md)
