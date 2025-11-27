# REL05-BP04: Fail fast and limit queues

## Description

Implement timeouts và circuit breakers để fail fast.

## Implementation Guidance

- Set aggressive timeouts on all calls
- Implement circuit breaker pattern
- Limit queue depths to prevent buildup
- Shed load when overwhelmed
- Return errors quickly rather than hang

## Risk Level

High - Slow failures consume resources and cascade.

## Related Best Practices

- [REL05-BP01](REL05-BP01-Graceful-Degradation.md)
- [REL05-BP05](REL05-BP05-Client-Timeouts.md)
