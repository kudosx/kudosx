# REL05-BP01: Implement graceful degradation

## Description

Implement fallbacks khi dependencies fail.

## Implementation Guidance

- Define degraded modes for each dependency
- Implement fallback responses (cached, default)
- Prioritize core functionality
- Communicate degraded state to users
- Test degraded modes regularly

## Risk Level

High - Without degradation, partial failures become total failures.

## Related Best Practices

- [REL05-BP04](REL05-BP04-Fail-Fast-Limit-Queues.md)
- [REL04-BP02](../REL04-Workload-Distributed-Systems/REL04-BP02-Loosely-Coupled-Dependencies.md)
