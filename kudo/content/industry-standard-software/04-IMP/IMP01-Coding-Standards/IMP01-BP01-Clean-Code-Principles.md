# IMP01-BP01: Clean Code Principles

Viết code sạch, dễ đọc, dễ maintain.

## Meaningful Names

```typescript
// ❌ Bad
const d = 86400; // seconds in a day
const list = users.filter(u => u.a > 18);

// ✅ Good
const SECONDS_PER_DAY = 86400;
const adultUsers = users.filter(user => user.age > 18);
```

### Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Variables | camelCase, noun | `userName`, `totalCount` |
| Functions | camelCase, verb | `getUser()`, `calculateTotal()` |
| Classes | PascalCase, noun | `UserService`, `OrderRepository` |
| Constants | UPPER_SNAKE | `MAX_RETRIES`, `API_URL` |
| Booleans | is/has/can prefix | `isActive`, `hasPermission` |

## Functions

### Keep Functions Small

```typescript
// ❌ Bad: Function does too many things
function processOrder(order) {
  // validate order (20 lines)
  // calculate total (15 lines)
  // apply discount (10 lines)
  // save to database (10 lines)
  // send notification (15 lines)
}

// ✅ Good: Single responsibility
function processOrder(order) {
  validateOrder(order);
  const total = calculateTotal(order);
  const finalPrice = applyDiscount(total, order.discountCode);
  await saveOrder({ ...order, total: finalPrice });
  await notifyCustomer(order);
}
```

### Function Arguments

```typescript
// ❌ Bad: Too many arguments
function createUser(name, email, age, address, phone, role) {}

// ✅ Good: Use object parameter
function createUser({ name, email, age, address, phone, role }: CreateUserParams) {}
```

## Comments

```typescript
// ❌ Bad: Comment explains what code does
// increment i by 1
i++;

// ✅ Good: Comment explains why
// We skip the first element because it's the header row
for (let i = 1; i < rows.length; i++) {}

// ✅ Better: Self-documenting code
const DATA_ROWS_START_INDEX = 1;
for (let i = DATA_ROWS_START_INDEX; i < rows.length; i++) {}
```

## Error Handling

```typescript
// ❌ Bad: Silent failure
function getUser(id) {
  try {
    return db.findUser(id);
  } catch (e) {
    return null;
  }
}

// ✅ Good: Meaningful error handling
function getUser(id: string): User {
  try {
    const user = db.findUser(id);
    if (!user) {
      throw new UserNotFoundError(id);
    }
    return user;
  } catch (error) {
    logger.error('Failed to get user', { id, error });
    throw error;
  }
}
```

## DRY (Don't Repeat Yourself)

```typescript
// ❌ Bad: Repeated validation logic
function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

function validateUserEmail(user) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(user.email);
}

// ✅ Good: Single source of truth
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function isValidEmail(email: string): boolean {
  return EMAIL_REGEX.test(email);
}
```

## Checklist

- [ ] Names are meaningful and pronounceable
- [ ] Functions do one thing
- [ ] Functions have ≤ 3 parameters
- [ ] No magic numbers/strings
- [ ] No commented-out code
- [ ] Error handling is appropriate
- [ ] Code is DRY
