# REL05: How do you design interactions in a distributed system to mitigate or withstand failures?

## References

- [AWS REL05](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-05.html)
- [Resilience4j](https://resilience4j.readme.io/)

## Date

2025-11-27

## Focus Area

Workload Architecture

## Tổng quan

REL05 tập trung vào mitigating failures trong distributed systems.

## Best Practices

### REL05-BP01: Implement graceful degradation
Fallbacks khi dependencies fail.

### REL05-BP02: Throttle requests
Rate limiting.

### REL05-BP03: Control and limit retry calls
Exponential backoff.

### REL05-BP04: Fail fast and limit queues
Timeouts, circuit breakers.

### REL05-BP05: Set client timeouts
Client-side timeouts.

### REL05-BP06: Make services stateless where possible
Stateless services.

### REL05-BP07: Implement emergency levers
Kill switches.

## Circuit Breaker Pattern

States: CLOSED → OPEN → HALF_OPEN

## Checklist

- [ ] Graceful degradation implemented
- [ ] Rate limiting configured
- [ ] Retry with backoff
- [ ] Circuit breakers implemented
- [ ] Timeouts configured
