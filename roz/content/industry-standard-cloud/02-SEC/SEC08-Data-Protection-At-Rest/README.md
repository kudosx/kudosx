# SEC08: How do you protect your data at rest?

## References

- [AWS SEC08](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-08.html)

## Date

2025-11-27

## Focus Area

Data Protection

## Tổng quan

SEC08 tập trung vào bảo vệ data at rest thông qua encryption.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [SEC08-BP01](SEC08-BP01-Implement-Secure-Key-Management.md) | Secure key management | KMS, key rotation |
| [SEC08-BP02](SEC08-BP02-Enforce-Encryption-At-Rest.md) | Enforce encryption at rest | Encrypt all storage |
| [SEC08-BP03](SEC08-BP03-Automate-Protection.md) | Automate protection | Automated encryption |
| [SEC08-BP04](SEC08-BP04-Enforce-Access-Control.md) | Enforce access control | Key policies |

## Checklist

- [ ] KMS configured
- [ ] All storage encrypted
- [ ] Key rotation enabled
- [ ] Access controls on keys
