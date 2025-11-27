# DES01-BP01: Architecture Patterns

Chọn và áp dụng architecture patterns phù hợp với yêu cầu hệ thống.

## Common Patterns

### 1. Layered Architecture

```
┌─────────────────────────────────────┐
│         Presentation Layer          │  ← UI, API Controllers
├─────────────────────────────────────┤
│          Business Layer             │  ← Business Logic, Services
├─────────────────────────────────────┤
│         Persistence Layer           │  ← Repositories, DAOs
├─────────────────────────────────────┤
│          Database Layer             │  ← Database
└─────────────────────────────────────┘
```

**Ưu điểm**: Đơn giản, dễ hiểu, separation of concerns
**Nhược điểm**: Tight coupling, khó scale độc lập

### 2. Microservices Architecture

```
┌──────────┐  ┌──────────┐  ┌──────────┐
│  User    │  │  Order   │  │ Payment  │
│ Service  │  │ Service  │  │ Service  │
└────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │             │
     └─────────────┼─────────────┘
                   │
            ┌──────┴──────┐
            │ API Gateway │
            └─────────────┘
```

**Ưu điểm**: Scale độc lập, team autonomy, fault isolation
**Nhược điểm**: Complexity, distributed system challenges

### 3. Event-Driven Architecture

```
┌─────────┐     ┌─────────────┐     ┌─────────┐
│Producer │ ──► │ Event Bus   │ ──► │Consumer │
└─────────┘     │ (Kafka/SQS) │     └─────────┘
                └─────────────┘
```

**Ưu điểm**: Loose coupling, scalability, real-time
**Nhược điểm**: Eventual consistency, debugging khó

## Pattern Selection Guide

| Yêu cầu | Pattern đề xuất |
|---------|-----------------|
| Startup nhỏ, team < 5 | Monolith/Layered |
| Scale high traffic | Microservices |
| Real-time processing | Event-Driven |
| Complex business logic | Domain-Driven Design |
| Read-heavy workload | CQRS |

## Quality Attributes

| Attribute | Đo lường |
|-----------|----------|
| **Scalability** | Requests/second, concurrent users |
| **Availability** | Uptime %, MTTR |
| **Performance** | Response time, throughput |
| **Security** | Vulnerabilities, compliance |
| **Maintainability** | Code complexity, change frequency |

## Checklist

- [ ] Xác định quality attributes chính
- [ ] Evaluate các pattern options
- [ ] Document trade-offs
- [ ] Tạo Architecture Decision Record
- [ ] Review với team
