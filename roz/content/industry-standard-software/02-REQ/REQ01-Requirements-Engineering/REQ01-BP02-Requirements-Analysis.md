# REQ01-BP02: Requirements Analysis

Phân tích, làm rõ và validate yêu cầu đã thu thập.

## Mục tiêu

- Đảm bảo yêu cầu đầy đủ (complete)
- Đảm bảo yêu cầu nhất quán (consistent)
- Đảm bảo yêu cầu khả thi (feasible)
- Đảm bảo yêu cầu có thể kiểm tra (testable)

## Quy trình phân tích

### 1. Classification

Phân loại yêu cầu theo:
- **Functional**: Chức năng hệ thống phải làm
- **Non-functional**: Performance, security, usability
- **Constraints**: Giới hạn về công nghệ, budget, timeline

### 2. Modeling

```
Các mô hình thường dùng:
├── Use Case Diagrams     → Actor và system interactions
├── Activity Diagrams     → Business workflows
├── State Diagrams        → Object states và transitions
├── Data Flow Diagrams    → Data movement trong hệ thống
└── Entity Relationship   → Data structure và relationships
```

### 3. Conflict Resolution

Khi yêu cầu xung đột:
1. Xác định nguồn gốc xung đột
2. Đánh giá impact của từng option
3. Escalate lên stakeholders để quyết định
4. Document quyết định và lý do

### 4. Feasibility Analysis

| Khía cạnh | Câu hỏi |
|-----------|---------|
| Technical | Công nghệ có hỗ trợ không? |
| Economic | Chi phí có trong budget? |
| Schedule | Có thể hoàn thành đúng deadline? |
| Resource | Có đủ người và kỹ năng? |

## Checklist

- [ ] Phân loại tất cả yêu cầu
- [ ] Tạo models phù hợp
- [ ] Giải quyết conflicts
- [ ] Đánh giá feasibility
- [ ] Review với technical team
