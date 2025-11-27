# SEC01: How do you securely operate your workload?

## References

- [AWS SEC01](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-01.html)
- [NIST SP 800-207 Zero Trust](https://csrc.nist.gov/publications/detail/sp/800-207/final)

## Date

2025-11-27

## Focus Area

Security

## Tổng quan

SEC01 tập trung vào secure operations của workload, bao gồm separation of duties, least privilege, và security practices trong operations.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [SEC01-BP01](SEC01-BP01-Separate-Workloads-Using-Accounts.md) | Separate workloads using accounts | Tách workloads vào separate accounts |
| [SEC01-BP02](SEC01-BP02-Secure-Account.md) | Secure account | Bảo mật root account và IAM |
| [SEC01-BP03](SEC01-BP03-Identify-Control-Objectives.md) | Identify control objectives | Xác định security control objectives |
| [SEC01-BP04](SEC01-BP04-Stay-Up-To-Date-With-Security.md) | Stay up to date with security | Theo dõi security threats |
| [SEC01-BP05](SEC01-BP05-Reduce-Security-Management-Scope.md) | Reduce security management scope | Giảm scope cần manage |
| [SEC01-BP06](SEC01-BP06-Automate-Configuration-Management.md) | Automate configuration management | Tự động hóa security config |
| [SEC01-BP07](SEC01-BP07-Threat-Model.md) | Threat model | Threat modeling cho workload |
| [SEC01-BP08](SEC01-BP08-Evaluate-Security-Services.md) | Evaluate security services | Đánh giá security services mới |

## Zero Trust Principles

1. Never trust, always verify
2. Assume breach
3. Verify explicitly
4. Use least privilege access

## Checklist

- [ ] Workloads separated by accounts
- [ ] Root account secured
- [ ] MFA enabled
- [ ] Security threats monitored
- [ ] Threat model documented
- [ ] Security automation implemented
