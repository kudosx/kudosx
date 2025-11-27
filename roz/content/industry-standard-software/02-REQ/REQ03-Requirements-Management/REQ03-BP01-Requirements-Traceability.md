# REQ03-BP01: Requirements Traceability

Theo dõi yêu cầu từ business objectives đến code và tests.

## Traceability Matrix

```
Business Goal → Feature → Requirement → Design → Code → Test
     │            │           │           │        │       │
     └────────────┴───────────┴───────────┴────────┴───────┘
                    Bidirectional Traceability
```

## Traceability Matrix Template

| Req ID | Description | Source | Design | Code | Test | Status |
|--------|-------------|--------|--------|------|------|--------|
| REQ-001 | User login | PRD-2.1 | DES-003 | auth.ts:45 | TC-001 | Implemented |
| REQ-002 | Password reset | PRD-2.2 | DES-004 | reset.ts:12 | TC-002 | In Progress |
| REQ-003 | 2FA support | PRD-2.3 | - | - | - | Not Started |

## Types of Traceability

### 1. Forward Traceability
```
Requirements → Design → Implementation → Testing
```
- Đảm bảo mọi requirement được implement
- Verify coverage

### 2. Backward Traceability
```
Testing → Implementation → Design → Requirements
```
- Xác định source của mỗi component
- Impact analysis khi thay đổi

### 3. Bi-directional Traceability
- Kết hợp cả hai
- Cho phép truy vết cả hai chiều

## Tools hỗ trợ

| Tool | Mô tả |
|------|-------|
| Jira + Xray | Link stories → test cases |
| Azure DevOps | Built-in traceability |
| Doors | Enterprise requirements management |
| GitHub Issues | Link issues → PRs → code |

## Traceability trong Git

```bash
# Commit message linking to requirement
git commit -m "feat(auth): implement login flow

Implements REQ-001
Closes #123"
```

## Benefits

1. **Impact Analysis**: Biết được thay đổi ảnh hưởng gì
2. **Coverage**: Đảm bảo không bỏ sót requirement
3. **Audit**: Truy vết được nguồn gốc mọi thứ
4. **Change Control**: Kiểm soát thay đổi tốt hơn

## Checklist

- [ ] Mọi requirement có ID unique
- [ ] Link requirement → design document
- [ ] Link design → code (file:line)
- [ ] Link requirement → test cases
- [ ] Traceability matrix được cập nhật
