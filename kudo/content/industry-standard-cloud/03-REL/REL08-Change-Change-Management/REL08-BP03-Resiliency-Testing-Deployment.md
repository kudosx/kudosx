# REL08-BP03: Integrate resiliency testing in deployment

## Description

Include chaos/resiliency tests trong deployment pipeline.

## Implementation Guidance

- Add chaos experiments to staging
- Test failure scenarios pre-production
- Verify circuit breakers work
- Validate timeout configurations
- Test rollback procedures

## Risk Level

Medium - Untested resilience fails in production.

## Related Best Practices

- [REL08-BP02](REL08-BP02-Functional-Testing-Deployment.md)
- [REL12-BP05](../REL12-Failure-Reliability-Testing/REL12-BP05-Chaos-Engineering.md)
