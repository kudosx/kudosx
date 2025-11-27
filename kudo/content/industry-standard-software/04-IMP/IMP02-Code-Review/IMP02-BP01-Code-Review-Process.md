# IMP02-BP01: Code Review Process

Quy trình và guidelines để review code hiệu quả.

## Why Code Review?

- Phát hiện bugs sớm
- Knowledge sharing
- Đảm bảo code quality
- Mentoring junior developers

## Review Checklist

### Functionality
- [ ] Code thực hiện đúng requirements
- [ ] Edge cases được handle
- [ ] Error handling phù hợp

### Design
- [ ] Code tuân thủ architecture
- [ ] Không duplicate code (DRY)
- [ ] SOLID principles được áp dụng

### Readability
- [ ] Naming conventions nhất quán
- [ ] Functions/classes không quá dài
- [ ] Comments giải thích "why", không phải "what"

### Testing
- [ ] Unit tests cover các cases chính
- [ ] Edge cases được test
- [ ] Tests dễ đọc và maintain

### Security
- [ ] Input validation
- [ ] No sensitive data in logs
- [ ] Authentication/Authorization đúng

### Performance
- [ ] Không có N+1 queries
- [ ] Không có memory leaks
- [ ] Efficient algorithms

## PR Description Template

```markdown
## What
[Brief description of changes]

## Why
[Reason for the change]

## How
[How you implemented it]

## Testing
- [ ] Unit tests added/updated
- [ ] Manual testing done

## Screenshots (if UI changes)
[Add screenshots]

## Checklist
- [ ] Code follows style guide
- [ ] Tests pass
- [ ] Documentation updated
```

## Giving Feedback

### DO
```
✅ "Consider using a Map instead of Object for better performance with frequent lookups"

✅ "This could be simplified using optional chaining: user?.profile?.name"

✅ "Nice solution! Nit: variable name could be more descriptive"
```

### DON'T
```
❌ "This is wrong"
❌ "Why did you do it this way?"
❌ "This code is bad"
```

## Comment Prefixes

| Prefix | Meaning |
|--------|---------|
| `[MUST]` | Bắt buộc phải fix |
| `[SHOULD]` | Nên fix |
| `[NIT]` | Nhỏ, optional |
| `[QUESTION]` | Hỏi để hiểu |
| `[SUGGESTION]` | Đề xuất cải thiện |

## Response Time

| PR Size | Expected Review Time |
|---------|---------------------|
| S (< 100 lines) | Same day |
| M (100-500 lines) | 1-2 days |
| L (> 500 lines) | 2-3 days |

## Checklist

- [ ] PR có description đầy đủ
- [ ] Code được self-review trước
- [ ] Tests pass
- [ ] Review feedback constructive
- [ ] Approved bởi ít nhất 1 reviewer
