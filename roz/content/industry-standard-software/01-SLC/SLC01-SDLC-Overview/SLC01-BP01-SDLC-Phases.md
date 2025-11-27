# SLC01-BP01: SDLC Phases

Các giai đoạn trong Software Development Life Cycle.

## SDLC Flow

```
┌──────────────────┐
│   Requirements   │
│    Gathering     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  System Design   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│     Coding       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│     Testing      │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   Deployment     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   Maintenance    │
└──────────────────┘
```

## 6 Giai đoạn chính

### 1. Requirements Gathering & Analysis

| Hoạt động | Output |
|-----------|--------|
| Thu thập yêu cầu từ stakeholders | Interview notes, surveys |
| Phân tích tính khả thi | Feasibility report |
| Tạo tài liệu đặc tả | SRS document |

### 2. System Design

| Hoạt động | Output |
|-----------|--------|
| Thiết kế kiến trúc hệ thống | Architecture diagram |
| Thiết kế database | ERD, schema |
| Thiết kế UI/UX | Wireframes, mockups |

### 3. Coding/Implementation

| Hoạt động | Output |
|-----------|--------|
| Viết code theo thiết kế | Source code |
| Code review | Review comments |
| Unit testing | Test results |

### 4. Testing

| Loại test | Mục đích |
|-----------|----------|
| Integration testing | Test component interactions |
| System testing | Test toàn bộ hệ thống |
| UAT | User Acceptance Testing |

### 5. Deployment

| Hoạt động | Output |
|-----------|--------|
| Deploy lên production | Running application |
| Monitoring setup | Dashboards, alerts |
| User training | Training materials |

### 6. Maintenance & Support

| Hoạt động | Mục đích |
|-----------|----------|
| Bug fixes | Sửa lỗi phát sinh |
| Feature enhancements | Thêm tính năng mới |
| Performance optimization | Cải thiện hiệu năng |

## Mapping với Pillars

| SDLC Phase | Pillar |
|------------|--------|
| Requirements | REQ |
| Design | DES |
| Implementation | IMP |
| Testing | TES |
| Deployment | DEP |
| Maintenance | All |

## Checklist

- [ ] Mỗi phase có deliverables rõ ràng
- [ ] Gate reviews giữa các phases
- [ ] Documentation cho mỗi phase
- [ ] Stakeholder sign-off
