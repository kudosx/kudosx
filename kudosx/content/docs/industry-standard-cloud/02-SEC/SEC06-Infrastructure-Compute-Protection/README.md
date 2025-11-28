# SEC06: How do you protect your compute resources?

## References

- [AWS SEC06](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-06.html)
- [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes)

## Date

2025-11-27

## Focus Area

Infrastructure Protection

## Tổng quan

SEC06 tập trung vào bảo vệ compute resources (EC2, containers, serverless).

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [SEC06-BP01](SEC06-BP01-Vulnerability-Management.md) | Vulnerability management | Regular vulnerability scanning |
| [SEC06-BP02](SEC06-BP02-Reduce-Attack-Surface.md) | Reduce attack surface | Minimize installed packages |
| [SEC06-BP03](SEC06-BP03-Managed-Services.md) | Managed services | Use managed services |
| [SEC06-BP04](SEC06-BP04-Automate-Protection.md) | Automate protection | Automated patching |
| [SEC06-BP05](SEC06-BP05-Actions-At-Distance.md) | Actions at distance | Avoid direct SSH |
| [SEC06-BP06](SEC06-BP06-Software-Integrity.md) | Software integrity | Code signing, image scanning |

## Container Security

- Use minimal base images
- Scan images for vulnerabilities
- Run as non-root
- Use read-only file systems
- Apply Pod Security Standards

## Checklist

- [ ] Vulnerability scanning enabled
- [ ] Minimal base images used
- [ ] Containers run as non-root
- [ ] Image signing implemented
- [ ] Pod Security Standards applied
