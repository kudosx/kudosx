# REL10-BP01: Deploy workload to multiple locations

## Description

Deploy across multiple AZs/regions để isolate failures.

## Implementation Guidance

- Deploy to at least 2 availability zones
- Distribute load evenly across zones
- Replicate data across zones
- Consider multi-region for DR
- Test zone failure scenarios

## Risk Level

High - Single location failures affect all users.

## Related Best Practices

- [REL10-BP02](REL10-BP02-Automate-Recovery.md)
- [REL02-BP01](../REL02-Foundations-Network-Topology/REL02-BP01-HA-Network-Connectivity.md)
