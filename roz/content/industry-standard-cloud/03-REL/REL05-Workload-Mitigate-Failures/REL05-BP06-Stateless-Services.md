# REL05-BP06: Make services stateless where possible

## Description

Design stateless services để improve reliability và scalability.

## Implementation Guidance

- Store state externally (database, cache)
- Avoid server-side sessions
- Use JWT or stateless tokens
- Design for horizontal scaling
- Handle any-instance routing

## Risk Level

Medium - Stateful services complicate scaling and recovery.

## Related Best Practices

- [REL05-BP01](REL05-BP01-Graceful-Degradation.md)
- [REL07-BP01](../REL07-Change-Demand-Handling/REL07-BP01-Use-Automation-To-Manage-Changes.md)
