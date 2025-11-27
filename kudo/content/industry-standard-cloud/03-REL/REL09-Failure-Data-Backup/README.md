# REL09: How do you back up data?

## References

- [AWS REL09](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-09.html)

## Date

2025-11-27

## Focus Area

Failure Management

## Tổng quan

REL09 tập trung vào data backup strategy.

## Best Practices

### REL09-BP01: Identify all data that needs to be backed up
Data inventory.

### REL09-BP02: Establish recovery point objectives (RPO)
RPO cho mỗi data type.

### REL09-BP03: Establish recovery time objectives (RTO)
RTO cho mỗi workload.

### REL09-BP04: Implement appropriate backup strategies
Backup strategy.

### REL09-BP05: Test backup and recovery procedures
Regular tests.

### REL09-BP06: Automate backup strategies
Automated backups.

## RPO vs RTO

- **RPO**: Max acceptable data loss (time)
- **RTO**: Max acceptable downtime

## Checklist

- [ ] Data inventory complete
- [ ] RPO defined
- [ ] RTO defined
- [ ] Backups automated
- [ ] Recovery tested
