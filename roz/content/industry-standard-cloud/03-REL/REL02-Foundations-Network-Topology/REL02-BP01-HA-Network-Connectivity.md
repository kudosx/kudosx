# REL02-BP01: Use highly available network connectivity for public endpoints

## Description

Đảm bảo network connectivity có high availability cho public endpoints.

## Implementation Guidance

- Deploy across multiple Availability Zones
- Use load balancers for traffic distribution
- Implement DNS failover strategies
- Configure health checks for endpoints
- Consider multi-region deployment for critical apps

## Risk Level

High - Single point of failure in networking causes complete outage.

## Related Best Practices

- [REL02-BP02](REL02-BP02-Redundant-Connectivity.md)
- [REL10-BP01](../REL10-Failure-Fault-Isolation/REL10-BP01-Deploy-Multiple-Locations.md)
