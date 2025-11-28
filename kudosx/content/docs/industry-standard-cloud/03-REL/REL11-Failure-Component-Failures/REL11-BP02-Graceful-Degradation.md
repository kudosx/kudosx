# REL11-BP02: Graceful degradation

## Description

Implement fallback behavior khi components fail.

## Implementation Guidance

- Define degraded modes per component
- Implement cached responses
- Provide default/fallback data
- Communicate degraded state to users
- Prioritize core functionality

## Risk Level

High - Without degradation, partial failures become total.

## Related Best Practices

- [REL11-BP03](REL11-BP03-Automate-Healing.md)
- [REL05-BP01](../REL05-Workload-Mitigate-Failures/REL05-BP01-Graceful-Degradation.md)
