# REL13: How do you plan for disaster recovery (DR)?

## References

- [AWS REL13](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-13.html)

## Date

2025-11-27

## Focus Area

Failure Management

## Tổng quan

REL13 tập trung vào disaster recovery planning.

## Best Practices

### REL13-BP01: Define recovery objectives
RTO và RPO.

### REL13-BP02: Use defined recovery strategies
DR strategy.

### REL13-BP03: Test disaster recovery implementation
Regular DR tests.

### REL13-BP04: Manage configuration drift
Consistent configurations.

### REL13-BP05: Automate recovery
Automated DR.

## DR Strategies

| Strategy | RTO | Cost |
|----------|-----|------|
| Backup & Restore | Hours | $ |
| Pilot Light | 10s min | $$ |
| Warm Standby | Minutes | $$$ |
| Multi-site Active | Real-time | $$$$ |

## Checklist

- [ ] RTO/RPO defined
- [ ] DR strategy selected
- [ ] DR documented
- [ ] DR tested regularly
- [ ] Recovery automated
