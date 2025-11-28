# PERF04-BP04: Use load balancing to distribute traffic

## Description

Implement load balancing cho traffic distribution.

## Implementation Guidance

- Choose appropriate LB type (L4/L7)
- Configure health checks
- Distribute across availability zones
- Implement sticky sessions if needed
- Monitor LB performance

## Risk Level

High - Single point of entry without LB reduces availability.

## Related Best Practices

- [PERF04-BP02](PERF04-BP02-Networking-Features.md)
- [REL02-BP01](../../03-REL/REL02-Foundations-Network-Topology/REL02-BP01-HA-Network-Connectivity.md)
