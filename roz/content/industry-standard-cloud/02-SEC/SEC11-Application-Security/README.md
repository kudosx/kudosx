# SEC11: How do you incorporate and validate the security properties of applications?

## References

- [AWS SEC11](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-11.html)
- [OWASP Top 10:2025](https://owasp.org/Top10/)

## Date

2025-11-27

## Focus Area

Application Security

## Tổng quan

SEC11 tập trung vào application security trong development lifecycle.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [SEC11-BP01](SEC11-BP01-Train-For-Security.md) | Train for security | Security training |
| [SEC11-BP02](SEC11-BP02-Automate-Security-Testing.md) | Automate security testing | SAST/DAST |
| [SEC11-BP03](SEC11-BP03-Security-Reviews.md) | Security reviews | Code and design reviews |
| [SEC11-BP04](SEC11-BP04-Centralize-Security-Services.md) | Centralize security services | Shared security services |
| [SEC11-BP05](SEC11-BP05-Deploy-Securely.md) | Deploy securely | Secure deployment |

## OWASP Top 10

1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Auth Failures
8. Software Integrity Failures
9. Security Logging Failures
10. Server-Side Request Forgery

## Checklist

- [ ] Security training completed
- [ ] SAST in CI/CD
- [ ] DAST for APIs
- [ ] Dependency scanning
- [ ] Security reviews conducted
