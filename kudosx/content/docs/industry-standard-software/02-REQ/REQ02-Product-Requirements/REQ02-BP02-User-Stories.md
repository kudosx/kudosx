# REQ02-BP02: User Stories

Viết user stories và acceptance criteria theo chuẩn Agile.

## User Story Template

```markdown
# US-XXX: [Title]

**Story ID**: US-XXX
**Epic**: [EPIC-XX Name](./EPIC.md)
**Priority**: P0 | P1 | P2
**Story Points**: X
**Status**: Draft | Ready | In Progress | Done

---

## User Story

```
As a [type of user]
I want [goal/desire]
So that [benefit/value]
```

---

## Acceptance Criteria

### AC-001: [Scenario name]

```gherkin
Scenario: [Scenario name]
  Given [precondition]
  When [action]
  Then [expected result]
  And [additional result]
```

---

## Data/Reference

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value | Value | Value |

---

## Technical Notes

- Note 1
- Note 2

---

## Dependencies

- Service A
- External API B

---

## UI/UX Notes

- UX guideline 1
- UX guideline 2
```

---

## User Story Format

```
As a [type of user]
I want [goal/desire]
So that [benefit/value]
```

### Components

| Part | Mô tả | Ví dụ |
|------|-------|-------|
| **As a** | Ai là người dùng | new user, verified user, borrower |
| **I want** | Họ muốn làm gì | register, view packages, make payment |
| **So that** | Lợi ích họ nhận được | access services, choose loan, stay on track |

---

## INVEST Criteria

| Criteria | Mô tả | Checklist |
|----------|-------|-----------|
| **I**ndependent | Không phụ thuộc story khác | Có thể develop/test riêng |
| **N**egotiable | Có thể thương lượng | Chi tiết có thể thay đổi qua discussion |
| **V**aluable | Mang lại giá trị | Benefit cho user hoặc business |
| **E**stimable | Có thể estimate | Team hiểu scope để đưa ra story points |
| **S**mall | Đủ nhỏ | Hoàn thành trong 1 sprint |
| **T**estable | Có thể test | Có acceptance criteria rõ ràng |

---

## Acceptance Criteria (Gherkin Format)

### Structure

```gherkin
Scenario: [Descriptive scenario name]
  Given [precondition - context/state]
  And [additional precondition if needed]
  When [action - trigger]
  And [additional action if needed]
  Then [expected outcome]
  And [additional outcome if needed]
```

### Best Practices for AC

1. **Cover happy path first**: Scenario thành công trước
2. **Add edge cases**: Validation, error handling
3. **Use concrete values**: "0901234567" thay vì "valid phone"
4. **Include error messages**: Text cụ thể user sẽ thấy
5. **Multiple scenarios**: 3-6 ACs per story

---

## Real-World Examples

### Example 1: User Registration (US-001)

```markdown
## User Story

```
As a new user
I want to register an account using my phone number
So that I can access loan services
```

## Acceptance Criteria

### AC-001: Successful registration with valid phone

```gherkin
Scenario: Successful registration with valid phone
  Given I am on the registration page
  And I have not registered before
  When I enter my valid phone number "0901234567"
  And I tap "Get OTP"
  Then I should receive an OTP within 30 seconds
  And I should see the OTP input screen
```

### AC-002: Successful OTP verification

```gherkin
Scenario: Successful OTP verification
  Given I have received the OTP
  When I enter the correct OTP within 60 seconds
  Then I should proceed to the KYC screen
  And my account status should be "pending_kyc"
```

### AC-003: Invalid phone number

```gherkin
Scenario: Invalid phone number
  Given I am on the registration page
  When I enter an invalid phone number "123"
  Then I should see error "Số điện thoại không hợp lệ"
  And the "Get OTP" button should be disabled
```

### AC-004: Phone already registered

```gherkin
Scenario: Phone already registered
  Given I am on the registration page
  And phone "0901234567" is already registered
  When I enter "0901234567"
  And I tap "Get OTP"
  Then I should see message "Số điện thoại đã được đăng ký. Vui lòng đăng nhập."
  And I should see a link to login page
```

### AC-005: OTP expired

```gherkin
Scenario: OTP expired
  Given I have received the OTP
  When I wait more than 60 seconds
  And I enter the OTP
  Then I should see error "OTP đã hết hạn"
  And I should see "Gửi lại OTP" button
```

## Technical Notes

- Phone format: `0[3|5|7|8|9]xxxxxxxx`
- OTP: 6 digits, expires in 60 seconds
- Rate limit: 5 OTP requests/phone/day
- Block after 10 consecutive failures
```

### Example 2: Make Payment (US-013)

```markdown
## User Story

```
As a borrower
I want to pay my loan installment
So that I stay on track with repayment
```

## Acceptance Criteria

### AC-001: Pay via Momo wallet

```gherkin
Scenario: Pay via Momo wallet
  Given I have sufficient Momo balance
  When I tap "Pay Now" on due installment
  And I select "Momo Wallet"
  And I confirm with Momo PIN
  Then payment should be processed
  And I should see success confirmation
  And loan balance should update immediately
```

### AC-002: Insufficient balance

```gherkin
Scenario: Insufficient balance
  Given my Momo balance is less than payment amount
  When I try to pay via Momo
  Then I should see "Số dư không đủ"
  And I should see option to top up Momo
  And I should see alternative payment methods
```

## Payment Methods

| Method | Processing Time | Fee |
|--------|-----------------|-----|
| Momo Wallet | Instant | Free |
| Bank Card | 30 seconds | 0.5% |
| Bank Transfer | 1-24 hours | Free |
| Linked Account | Instant | Free |
```

### Example 3: View Loan Packages (US-005)

```markdown
## User Story

```
As a verified user
I want to view available loan packages
So that I can choose one that fits my needs
```

## Acceptance Criteria

### AC-001: Display loan packages

```gherkin
Scenario: Display loan packages
  Given I am a verified user
  When I navigate to "Apply for Loan"
  Then I should see at least 3 loan packages
  And each package should show: name, amount range, term, interest rate
  And packages should be sorted by popularity
```

### AC-002: Filter by amount

```gherkin
Scenario: Filter by amount
  Given I am viewing loan packages
  When I set filter "Amount: 10-20 triệu"
  Then I should see only packages that include this amount range
  And filter should be visually indicated
```

### AC-003: Loan calculator

```gherkin
Scenario: Loan calculator
  Given I am viewing a loan package
  When I adjust the slider for amount to "15,000,000"
  And I select term "12 tháng"
  Then I should see monthly payment calculated
  And I should see total interest amount
  And I should see total repayment amount
```

## Loan Packages Data

| Gói | Hạn mức | Kỳ hạn | Lãi suất/năm |
|-----|---------|--------|--------------|
| Tiêu dùng nhanh | 1-20 triệu | 3-12 tháng | 18-24% |
| Tiêu dùng lớn | 20-100 triệu | 6-36 tháng | 15-20% |
| Kinh doanh | 50-500 triệu | 12-60 tháng | 12-18% |

## Technical Notes

- Calculator formula: PMT = P * [r(1+r)^n] / [(1+r)^n - 1]
- Real-time calculation on slider change
- APR displayed clearly
```

---

## Story Mapping

```
                    User Journey
    ┌─────────────────────────────────────────────────────────┐
    │  Register → KYC → Apply → Approve → Manage → Repay     │
    └─────────────────────────────────────────────────────────┘
         │       │       │        │         │        │
MVP      ├─US-001├─US-002├─US-005 ├─US-008  ├─US-011 ├─US-013
         │       │       │        │         │        │
v1.1     ├─US-001├─US-003├─US-006 ├─US-009  ├─US-012 ├─US-014
         │       │       │        │         │        │
v1.2     └─      └─US-004└─US-007 └─US-010  └─       └─US-015
```

---

## Splitting Large Stories

Khi story quá lớn (> 8 points), split theo:

### 1. Workflow Steps
```
Epic: User Registration
├── US-001: Enter phone number
├── US-002: Verify OTP
└── US-003: Set password
```

### 2. Happy/Unhappy Paths
```
Epic: Payment
├── US-013a: Pay successfully
├── US-013b: Handle insufficient balance
└── US-013c: Handle payment failure
```

### 3. Data Variations
```
Epic: Payment Methods
├── US-013a: Pay via Momo wallet
├── US-013b: Pay via bank card
└── US-013c: Pay via bank transfer
```

### 4. CRUD Operations
```
Epic: Loan Management
├── US-011: View loan dashboard (Read)
├── US-012: View loan details (Read)
└── US-019: Request loan renewal (Create)
```

---

## Common Patterns

### Pattern 1: List → Detail → Action

```
US-005: View loan packages (List)
US-005b: View package detail (Detail)
US-006: Submit application (Action)
```

### Pattern 2: Input → Validate → Process → Result

```
AC-001: Enter valid data → Success
AC-002: Enter invalid data → Validation error
AC-003: System error → Error handling
```

### Pattern 3: Real-time Feedback

```gherkin
Scenario: Real-time calculation
  Given I am on the calculator
  When I change the amount slider
  Then monthly payment should update immediately
  And no page refresh should occur
```

---

## Checklist

### User Story
- [ ] Follows "As a... I want... So that..." format
- [ ] Has clear benefit statement
- [ ] Meets INVEST criteria
- [ ] Story points assigned (1, 2, 3, 5, 8)
- [ ] Priority assigned (P0, P1, P2)

### Acceptance Criteria
- [ ] Uses Gherkin Given-When-Then format
- [ ] Covers happy path
- [ ] Covers edge cases (validation, errors)
- [ ] Uses concrete values and error messages
- [ ] 3-6 scenarios per story

### Supporting Sections
- [ ] Data tables if applicable
- [ ] Technical notes for developers
- [ ] Dependencies listed
- [ ] UI/UX notes for designers
