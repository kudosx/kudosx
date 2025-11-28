# SEC02: How do you manage identities for people and machines?

## References

- [AWS SEC02](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-02.html)
- [OAuth 2.1](https://oauth.net/2.1/)
- [OIDC](https://openid.net/connect/)

## Date

2025-11-27

## Focus Area

Identity and Access Management

## Tổng quan

SEC02 tập trung vào quản lý identities cho cả people và machines (service accounts).

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [SEC02-BP01](SEC02-BP01-Strong-Sign-In.md) | Strong sign-in mechanisms | MFA, strong passwords |
| [SEC02-BP02](SEC02-BP02-Temporary-Credentials.md) | Temporary credentials | Avoid long-lived credentials |
| [SEC02-BP03](SEC02-BP03-Secrets-Management.md) | Secrets management | Secure secret storage |
| [SEC02-BP04](SEC02-BP04-Centralized-IdP.md) | Centralized identity provider | SSO, centralized IdP |
| [SEC02-BP05](SEC02-BP05-Audit-Rotate-Credentials.md) | Audit and rotate credentials | Regular rotation |
| [SEC02-BP06](SEC02-BP06-User-Groups-Attributes.md) | User groups and attributes | Group-based access |

## Authentication Standards

| Standard | Use Case |
|----------|----------|
| OAuth 2.1 | Authorization |
| OIDC | Authentication |
| SAML 2.0 | Enterprise SSO |
| FIDO2/WebAuthn | Passwordless |

## Checklist

- [ ] MFA enabled for all users
- [ ] Temporary credentials used
- [ ] Secrets stored securely
- [ ] Centralized IdP configured
- [ ] Credential rotation automated
- [ ] Audit logging enabled
