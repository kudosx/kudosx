# REL05-BP05: Set client timeouts

## Description

Configure appropriate timeouts ở client side.

## Implementation Guidance

- Set connection timeouts (short, e.g., 1-5s)
- Set read/write timeouts based on SLA
- Configure retry policies with timeouts
- Monitor timeout rates
- Adjust timeouts based on p99 latencies

## Risk Level

Medium - Missing timeouts cause resource exhaustion.

## Related Best Practices

- [REL05-BP04](REL05-BP04-Fail-Fast-Limit-Queues.md)
- [REL05-BP03](REL05-BP03-Control-Retry-Calls.md)
