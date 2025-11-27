# REL04: How do you design interactions in a distributed system to prevent failures?

## References

- [AWS REL04](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-04.html)

## Date

2025-11-27

## Focus Area

Workload Architecture

## Tổng quan

REL04 tập trung vào designing interactions để prevent failures.

## Best Practices

### REL04-BP01: Identify which kind of distributed system is required
Understand consistency needs.

### REL04-BP02: Implement loosely coupled dependencies
Async communication, queues.

### REL04-BP03: Do constant work
Avoid thundering herd.

### REL04-BP04: Make all responses idempotent
Idempotency keys.

## Checklist

- [ ] Dependencies loosely coupled
- [ ] Async patterns used
- [ ] Idempotency implemented
