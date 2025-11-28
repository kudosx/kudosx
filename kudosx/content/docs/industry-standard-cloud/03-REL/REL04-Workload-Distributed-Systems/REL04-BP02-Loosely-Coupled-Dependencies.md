# REL04-BP02: Implement loosely coupled dependencies

## Description

Sử dụng loose coupling để isolate failures.

## Implementation Guidance

- Use message queues for async communication
- Implement event-driven architecture
- Avoid synchronous chains of calls
- Design for eventual consistency
- Use bulkheads to isolate components

## Risk Level

High - Tight coupling causes cascading failures.

## Related Best Practices

- [REL04-BP01](REL04-BP01-Identify-Distributed-System-Required.md)
- [REL05-BP01](../REL05-Workload-Mitigate-Failures/REL05-BP01-Graceful-Degradation.md)
