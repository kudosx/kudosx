# REL01: How do you manage service quotas and constraints?

## References

- [AWS REL01](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-01.html)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)

## Date

2025-11-27

## Focus Area

Foundations

## Tổng quan

REL01 tập trung vào quản lý service quotas và constraints.

## Best Practices

### REL01-BP01: Aware of service quotas and constraints
Biết limits của services đang sử dụng.

### REL01-BP02: Manage service quotas across accounts and regions
Quản lý quotas across accounts.

### REL01-BP03: Accommodate fixed service quotas and constraints through architecture
Design để work within limits.

### REL01-BP04: Monitor and manage quotas
Monitor usage vs quotas.

### REL01-BP05: Automate quota management
Tự động hóa quota requests.

### REL01-BP06: Ensure a sufficient gap between current quotas and max usage
Buffer giữa usage và limits.

## Checklist

- [ ] Service quotas documented
- [ ] Quota monitoring in place
- [ ] Quota alerts configured
- [ ] Architecture respects limits
