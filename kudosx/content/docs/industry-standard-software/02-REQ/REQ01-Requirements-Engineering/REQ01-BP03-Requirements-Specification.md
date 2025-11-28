# REQ01-BP03: Requirements Specification

Đặc tả yêu cầu một cách rõ ràng, đầy đủ và có thể verify.

## Tiêu chuẩn SMART cho yêu cầu

| Tiêu chí | Mô tả | Ví dụ tốt |
|----------|-------|-----------|
| **S**pecific | Cụ thể, không mơ hồ | "Hệ thống phải load trang trong 2 giây" |
| **M**easurable | Đo lường được | "99.9% uptime" thay vì "luôn available" |
| **A**chievable | Khả thi | Dựa trên đánh giá technical |
| **R**elevant | Liên quan business | Gắn với business objective |
| **T**ime-bound | Có thời hạn | "Release trong Q1 2025" |

## Template đặc tả yêu cầu

```markdown
## REQ-001: [Tên yêu cầu]

**Priority**: High | Medium | Low
**Type**: Functional | Non-functional
**Status**: Draft | Review | Approved

### Mô tả
[Mô tả chi tiết yêu cầu]

### Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

### Dependencies
- REQ-002, REQ-003

### Notes
[Ghi chú bổ sung]
```

## Cấu trúc SRS (Software Requirements Specification)

```
1. Introduction
   1.1 Purpose
   1.2 Scope
   1.3 Definitions & Acronyms

2. Overall Description
   2.1 Product Perspective
   2.2 User Classes
   2.3 Constraints

3. Specific Requirements
   3.1 Functional Requirements
   3.2 Non-functional Requirements
   3.3 Interface Requirements

4. Appendices
```

## Anti-patterns cần tránh

| Anti-pattern | Vấn đề | Cách sửa |
|--------------|--------|----------|
| "Hệ thống phải nhanh" | Không đo lường được | "Response time < 200ms" |
| "User-friendly interface" | Quá chung chung | Định nghĩa cụ thể UX criteria |
| "Xử lý tất cả trường hợp" | Không thể test | Liệt kê các cases cụ thể |

## Checklist

- [ ] Mỗi requirement có ID unique
- [ ] Đáp ứng tiêu chuẩn SMART
- [ ] Có acceptance criteria
- [ ] Được review và approve
- [ ] Traceability đến business objectives
