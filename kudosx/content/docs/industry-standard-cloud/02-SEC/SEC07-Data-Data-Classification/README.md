# SEC07: How do you classify your data?

## References

- [AWS SEC07](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-07.html)

## Date

2025-11-27

## Focus Area

Data Protection

## Tổng quan

SEC07 tập trung vào data classification để áp dụng controls phù hợp.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [SEC07-BP01](SEC07-BP01-Identify-Data.md) | Identify data | Inventory all data |
| [SEC07-BP02](SEC07-BP02-Define-Controls.md) | Define controls | Controls theo classification |
| [SEC07-BP03](SEC07-BP03-Automate-Classification.md) | Automate classification | Automated classification |
| [SEC07-BP04](SEC07-BP04-Data-Lifecycle.md) | Data lifecycle | Retention, archival, deletion |

## Data Classification Levels

| Level | Description | Example |
|-------|-------------|---------|
| Public | No restrictions | Marketing content |
| Internal | Internal use only | Internal docs |
| Confidential | Limited access | Customer data |
| Restricted | Highly sensitive | PII, financial |

## Checklist

- [ ] Data inventory created
- [ ] Classification levels defined
- [ ] Controls mapped to levels
- [ ] Data lifecycle defined
