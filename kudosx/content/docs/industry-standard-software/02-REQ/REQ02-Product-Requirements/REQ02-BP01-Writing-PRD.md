# REQ02-BP01: Writing PRD

Viết Product Requirements Document (PRD) rõ ràng và actionable.

## Document Hierarchy

PRD nên được tổ chức theo cấu trúc phân cấp 3 tầng:

```
PRD.md                           # Product-level overview
├── EPIC-01-[Name]/
│   ├── EPIC.md                  # Epic overview & business context
│   ├── US-001-[Name].md         # User Story with acceptance criteria
│   └── US-002-[Name].md
└── EPIC-02-[Name]/
    ├── EPIC.md
    └── US-003-[Name].md
```

### Level 1: PRD (Product Level)

Tổng quan toàn bộ sản phẩm, không đi vào chi tiết implementation.

### Level 2: EPIC (Feature Group Level)

Nhóm các tính năng liên quan, có business value rõ ràng.

### Level 3: User Story (Implementation Level)

Chi tiết từng chức năng với acceptance criteria cụ thể.

---

## PRD Template

```markdown
# [Product Name] - Requirements Documentation

**Version**: 1.0
**Last Updated**: YYYY-MM-DD
**Product**: [Product Name]

---

## Overview

Mô tả ngắn gọn về sản phẩm và giá trị mang lại cho người dùng.

---

## Document Structure

```
spec/products/[product]/
├── PRD.md
├── EPIC-01-[Name]/
│   ├── EPIC.md
│   └── US-001-[Name].md
└── ...
```

---

## Quick Links

### Epics
- [EPIC-01: Name](EPIC-01-Name/EPIC.md) - Description
- [EPIC-02: Name](EPIC-02-Name/EPIC.md) - Description

---

## Summary

### Epics

| Epic | Name | Stories | Points | Priority |
|------|------|---------|--------|----------|
| EPIC-01 | [Name] | X | Y | P0 |
| **Total** | | **X** | **Y** | |

### By Priority

| Priority | Stories | Points |
|----------|---------|--------|
| P0 | X | Y |
| P1 | X | Y |

---

## Key Metrics

| Metric | Target |
|--------|--------|
| [KPI 1] | > X% |
| [KPI 2] | < Yms |

---

## Timeline

| Phase | Scope | Epics |
|-------|-------|-------|
| **MVP** | Core flow | EPIC-01 → EPIC-03 (P0) |
| **v1.1** | Enhancement | EPIC-04 (P1) |

---

## Related

- [Industry Standard - REQ](../../../docs/industry-standard-software/02-REQ/)
```

---

## EPIC Template

```markdown
# EPIC-XX: [Name]

**Epic ID**: EPIC-XX
**Name**: [Name]
**Priority**: P0 | P1 | P2
**Status**: Draft | Ready | In Progress | Done

---

## Description

Mô tả epic này giải quyết vấn đề gì, cho ai.

---

## Business Value

- Value 1 (measurable)
- Value 2 (measurable)

---

## User Stories

| Story ID | Title | Priority | Points |
|----------|-------|----------|--------|
| [US-001](./US-001-Name.md) | Title | P0 | 3 |

**Total Points**: X

---

## User Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Step 1    │───▶│   Step 2    │───▶│   Step 3    │
│  (US-001)   │    │  (US-002)   │    │             │
└─────────────┘    └─────────────┘    └─────────────┘
```

---

## Requirements

### Functional
- Requirement 1
- Requirement 2

### Non-Functional
- Performance: < X seconds
- Availability: > 99.9%

---

## Dependencies

- Service A
- External API B

---

## Acceptance Criteria (Epic Level)

- [ ] User có thể complete flow A
- [ ] Metric X > target
```

---

## Real-World Example: Moni Loan

### PRD Structure

```
spec/products/loan/
├── PRD.md
├── EPIC-01-Onboarding/
│   ├── EPIC.md
│   ├── US-001-User-Registration.md
│   ├── US-002-eKYC-ID-Card.md
│   ├── US-003-eKYC-Face-Verification.md
│   └── US-004-Link-Bank-Account.md
├── EPIC-02-Loan-Application/
│   ├── EPIC.md
│   ├── US-005-View-Loan-Packages.md
│   ├── US-006-Submit-Application.md
│   └── US-007-Alternative-Data.md
├── EPIC-03-Approval-Disbursement/
├── EPIC-04-Loan-Management/
├── EPIC-05-Repayment/
└── EPIC-06-Loan-Lifecycle/
```

### Key Metrics Example

| Metric | Target |
|--------|--------|
| Conversion Rate | > 15% |
| Approval Rate | > 60% |
| Time to Disbursement | < 24h |
| On-time Repayment | > 95% |
| NPS Score | > 50 |

### Epic Summary Example

| Epic | Name | Stories | Points | Priority |
|------|------|---------|--------|----------|
| EPIC-01 | Onboarding | 4 | 26 | P0 |
| EPIC-02 | Loan Application | 3 | 16 | P0 |
| EPIC-03 | Approval & Disbursement | 3 | 13 | P0 |
| EPIC-04 | Loan Management | 2 | 8 | P0 |
| EPIC-05 | Repayment | 5 | 23 | P0 |
| EPIC-06 | Loan Lifecycle | 2 | 5 | P1 |
| **Total** | | **19** | **91** | |

---

## Best Practices

### DO

- Tổ chức theo hierarchy: PRD → EPIC → User Story
- Sử dụng naming convention nhất quán (EPIC-XX, US-XXX)
- Link các documents với nhau
- Include user flow diagrams (ASCII art)
- Tập trung vào "What" và "Why", không phải "How"
- Sử dụng metrics đo lường được
- Include mockups/wireframes references
- Review với stakeholders trước khi finalize

### DON'T

- Viết quá chi tiết về implementation
- Bỏ qua edge cases
- Không có acceptance criteria
- Copy-paste từ PRD khác
- Trộn lẫn các levels (PRD chứa chi tiết của User Story)

---

## Checklist

### PRD Level
- [ ] Overview rõ ràng
- [ ] Document structure được định nghĩa
- [ ] Summary tables đầy đủ
- [ ] Key metrics có target
- [ ] Timeline/phases được plan

### EPIC Level
- [ ] Business value được xác định
- [ ] User stories được list với priority và points
- [ ] User flow diagram có
- [ ] Requirements (functional & non-functional)
- [ ] Dependencies được identify
- [ ] Epic-level acceptance criteria

### User Story Level
- [ ] Story format chuẩn (As a... I want... So that...)
- [ ] Acceptance criteria dạng Gherkin (Given-When-Then)
- [ ] Technical notes
- [ ] Dependencies
- [ ] UI/UX notes
