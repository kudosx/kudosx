# REL11-BP04: Use static stability

## Description

Pre-provision capacity để handle failures without scaling.

## Implementation Guidance

- Provision enough capacity for N+1/N+2
- Avoid relying on scaling during failures
- Pre-allocate resources in all zones
- Test with reduced capacity
- Consider cold start times

## Risk Level

Medium - Dependent on scaling may fail during incidents.

## Related Best Practices

- [REL11-BP03](REL11-BP03-Automate-Healing.md)
- [REL07-BP01](../REL07-Change-Demand-Handling/REL07-BP01-Use-Automation-To-Manage-Changes.md)
