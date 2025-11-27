# DES01-BP02: Architecture Decision Records

Document các quyết định kiến trúc quan trọng và lý do đằng sau chúng.

## ADR Template

```markdown
# ADR-001: [Title]

## Status
Proposed | Accepted | Deprecated | Superseded by ADR-XXX

## Context
[Bối cảnh và vấn đề cần giải quyết]

## Decision
[Quyết định được đưa ra]

## Consequences

### Positive
- [Lợi ích 1]
- [Lợi ích 2]

### Negative
- [Rủi ro/trade-off 1]
- [Rủi ro/trade-off 2]

## Alternatives Considered

### Option 1: [Name]
- Pros: ...
- Cons: ...

### Option 2: [Name]
- Pros: ...
- Cons: ...

## References
- [Link to relevant docs]
```

## Ví dụ ADR

```markdown
# ADR-003: Use PostgreSQL as Primary Database

## Status
Accepted

## Context
Chúng ta cần chọn database cho hệ thống.
Requirements:
- ACID compliance cho financial transactions
- Support complex queries
- Scalability cho 1M+ users

## Decision
Sử dụng PostgreSQL làm primary database.

## Consequences

### Positive
- ACID compliance đầy đủ
- Rich SQL features, JSON support
- Strong community, well-documented
- Horizontal scaling với Citus

### Negative
- Cần DBA expertise để optimize
- Vertical scaling có giới hạn

## Alternatives Considered

### Option 1: MySQL
- Pros: Popular, nhiều developers biết
- Cons: Weaker JSON support, replication phức tạp

### Option 2: MongoDB
- Pros: Flexible schema, easy scaling
- Cons: No ACID for multi-document, eventual consistency
```

## ADR Structure trong repo

```
docs/
└── architecture/
    └── decisions/
        ├── README.md          # Index của tất cả ADRs
        ├── ADR-001-api-style.md
        ├── ADR-002-auth-method.md
        └── ADR-003-database.md
```

## When to Write ADR

- Chọn technology/framework mới
- Thay đổi architecture pattern
- Quyết định về security approach
- Trade-offs quan trọng

## Checklist

- [ ] ADR có title rõ ràng
- [ ] Context đầy đủ
- [ ] Decision được state rõ ràng
- [ ] Consequences (cả positive và negative)
- [ ] Alternatives được document
- [ ] Được review và approve
