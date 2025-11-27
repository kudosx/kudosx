# REQ03-BP02: Change Management

Quy trình quản lý thay đổi yêu cầu một cách có kiểm soát.

## Change Control Process

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Request   │ →  │   Analyze   │ →  │   Approve   │ →  │  Implement  │
│   Change    │    │   Impact    │    │   /Reject   │    │   Change    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

## Change Request Template

```markdown
## Change Request: CR-001

**Requested by**: [Name]
**Date**: [Date]
**Priority**: Critical | High | Medium | Low

### Current State
[Mô tả yêu cầu hiện tại]

### Proposed Change
[Mô tả thay đổi mong muốn]

### Reason for Change
[Lý do cần thay đổi]

### Impact Analysis
- **Scope**: [Affected requirements]
- **Schedule**: [Timeline impact]
- **Cost**: [Budget impact]
- **Quality**: [Risk assessment]

### Affected Items
- Requirements: REQ-001, REQ-002
- Design: DES-003
- Code: auth.ts, login.tsx
- Tests: TC-001, TC-002

### Decision
- [ ] Approved
- [ ] Rejected
- [ ] Deferred

**Approved by**: [Name]
**Date**: [Date]
**Notes**: [Decision rationale]
```

## Impact Analysis Checklist

| Area | Questions |
|------|-----------|
| **Scope** | Những requirements nào bị ảnh hưởng? |
| **Design** | Cần thay đổi architecture không? |
| **Code** | Bao nhiêu files cần modify? |
| **Testing** | Test cases nào cần update? |
| **Documentation** | Docs nào cần cập nhật? |
| **Schedule** | Delay bao lâu? |
| **Cost** | Tốn thêm bao nhiêu effort? |
| **Risk** | Có risk mới không? |

## Change Control Board (CCB)

### Thành phần
- Product Owner
- Tech Lead
- QA Lead
- Project Manager

### Trách nhiệm
- Review change requests
- Evaluate impact
- Approve/Reject changes
- Prioritize approved changes

## Best Practices

### DO
- Document mọi change request
- Analyze impact trước khi approve
- Communicate changes cho team
- Update traceability matrix
- Version control requirements

### DON'T
- Approve changes không qua review
- Skip impact analysis
- Implement changes không approved
- Forget to update docs

## Metrics

| Metric | Mục đích |
|--------|----------|
| Change request count | Đo lường stability |
| Approval rate | Đo lường process efficiency |
| Cycle time | Thời gian từ request → implement |
| Rework rate | Changes gây ra defects |

## Checklist

- [ ] Change request được document
- [ ] Impact analysis hoàn thành
- [ ] CCB đã review
- [ ] Decision được record
- [ ] Stakeholders được notify
- [ ] Traceability matrix updated
