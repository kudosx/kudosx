# REL04-BP03: Do constant work

## Description

Design để avoid thundering herd và load spikes.

## Implementation Guidance

- Spread work evenly over time
- Use jitter in scheduled tasks
- Implement request coalescing
- Pre-warm caches gradually
- Avoid synchronized batch operations

## Risk Level

Medium - Thundering herd can overwhelm systems.

## Related Best Practices

- [REL04-BP02](REL04-BP02-Loosely-Coupled-Dependencies.md)
- [REL07-BP02](../REL07-Change-Demand-Handling/REL07-BP02-Use-Throttling.md)
