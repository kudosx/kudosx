# REL07-BP02: Obtain resources upon detection of impairment

## Description

Scale resources khi detect failures hoặc degradation.

## Implementation Guidance

- Monitor for service degradation
- Trigger scaling on error rate increase
- Replace unhealthy instances automatically
- Use health checks effectively
- Configure appropriate cooldown periods

## Risk Level

Medium - Slow recovery from failures impacts users.

## Related Best Practices

- [REL07-BP01](REL07-BP01-Use-Automation-To-Manage-Changes.md)
- [REL05-BP04](../REL05-Workload-Mitigate-Failures/REL05-BP04-Fail-Fast-Limit-Queues.md)
