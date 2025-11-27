# SLC02-BP02: DevOps Culture

Văn hóa và principles của DevOps.

## DevOps Infinity Loop

```
┌─────────────────────────────────────────────────────────────┐
│                   DevOps Infinity Loop                       │
│                                                              │
│    ┌──────┐   ┌──────┐   ┌──────┐   ┌───────┐   ┌───────┐  │
│    │ Plan │ → │ Code │ → │Build │ → │ Test  │ → │Release│  │
│    └──────┘   └──────┘   └──────┘   └───────┘   └───┬───┘  │
│        ▲                                             │      │
│        │                                             ▼      │
│    ┌──────┐   ┌──────┐   ┌──────┐              ┌───────┐   │
│    │Learn │ ← │Monitor│ ← │Operate│ ←─────────│Deploy │    │
│    └──────┘   └──────┘   └──────┘              └───────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Core Principles

| Principle | Mô tả |
|-----------|-------|
| **Collaboration** | Dev và Ops làm việc cùng nhau |
| **Automation** | Tự động hóa mọi thứ có thể |
| **Continuous Improvement** | Cải tiến liên tục |
| **Customer Focus** | Tập trung vào giá trị cho khách hàng |
| **Shared Responsibility** | Chia sẻ trách nhiệm |

## DORA Metrics

| Metric | Elite | High | Medium | Low |
|--------|-------|------|--------|-----|
| **Deployment Frequency** | On-demand | Daily-Weekly | Weekly-Monthly | Monthly+ |
| **Lead Time** | < 1 hour | 1 day - 1 week | 1 week - 1 month | > 1 month |
| **Change Failure Rate** | 0-15% | 16-30% | 31-45% | > 45% |
| **Time to Restore** | < 1 hour | < 1 day | 1 day - 1 week | > 1 week |

## Three Ways of DevOps

### 1. Flow (Left to Right)
- Fast flow from Dev to Ops to Customer
- Small batch sizes
- Reduce work in progress

### 2. Feedback (Right to Left)
- Fast feedback at all stages
- Amplify feedback loops
- Fix problems early

### 3. Continuous Learning
- Culture of experimentation
- Learn from failures
- Share knowledge

## DevSecOps

```
Security integrated at every stage:

Code    → SAST, Secret scanning
Build   → SCA, License check
Test    → DAST, Penetration test
Deploy  → Config audit
Monitor → SIEM, IDS
```

## Thống kê ngành

- **71%** tổ chức đã áp dụng Agile
- **83%** đã áp dụng DevOps
- Elite performers deploy **208x** more frequently

## Checklist

- [ ] Dev và Ops collaborate daily
- [ ] CI/CD pipeline automated
- [ ] Monitoring và alerting in place
- [ ] Blameless post-mortems
- [ ] Continuous improvement culture
