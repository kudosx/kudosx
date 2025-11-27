# REL04-BP04: Make all responses idempotent

## Description

Implement idempotency để handle retries safely.

## Implementation Guidance

- Use idempotency keys for mutations
- Store request/response for deduplication
- Design APIs to be naturally idempotent
- Handle duplicate messages gracefully
- Set appropriate TTL for idempotency records

## Risk Level

High - Non-idempotent operations cause data corruption on retry.

## Related Best Practices

- [REL04-BP02](REL04-BP02-Loosely-Coupled-Dependencies.md)
- [REL05-BP03](../REL05-Workload-Mitigate-Failures/REL05-BP03-Control-Retry-Calls.md)
