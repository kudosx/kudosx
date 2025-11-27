# REL13-BP02: Use defined recovery strategies

## Description

Select DR strategy phù hợp với RTO/RPO requirements.

## Implementation Guidance

- Backup & Restore: Hours RTO, lowest cost
- Pilot Light: 10s minutes RTO
- Warm Standby: Minutes RTO
- Multi-site Active: Real-time, highest cost
- Match strategy to business needs

## Risk Level

High - Wrong strategy won't meet objectives.

## Related Best Practices

- [REL13-BP01](REL13-BP01-Define-Recovery-Objectives.md)
- [REL13-BP05](REL13-BP05-Automate-Recovery.md)
