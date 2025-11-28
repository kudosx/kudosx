# REL05-BP02: Throttle requests

## Description

Implement rate limiting để protect services.

## Implementation Guidance

- Define rate limits per client/API
- Use token bucket or leaky bucket algorithms
- Return 429 with Retry-After header
- Implement different limits per tier
- Monitor and adjust limits based on capacity

## Risk Level

High - Without throttling, services can be overwhelmed.

## Related Best Practices

- [REL05-BP03](REL05-BP03-Control-Retry-Calls.md)
- [REL07-BP02](../REL07-Change-Demand-Handling/REL07-BP02-Use-Throttling.md)
