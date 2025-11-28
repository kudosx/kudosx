# SEC09: How do you protect your data in transit?

## References

- [AWS SEC09](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-09.html)

## Date

2025-11-27

## Focus Area

Data Protection

## Tổng quan

SEC09 tập trung vào bảo vệ data in transit thông qua TLS.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [SEC09-BP01](SEC09-BP01-Implement-Secure-Protocols.md) | Secure protocols | TLS 1.2+ |
| [SEC09-BP02](SEC09-BP02-Enforce-Encryption-In-Transit.md) | Enforce encryption | HTTPS everywhere |
| [SEC09-BP03](SEC09-BP03-Authenticate-Network-Communications.md) | Authenticate communications | mTLS |

## Checklist

- [ ] TLS 1.2+ enforced
- [ ] HTTP redirected to HTTPS
- [ ] Certificate management automated
- [ ] Internal traffic encrypted
