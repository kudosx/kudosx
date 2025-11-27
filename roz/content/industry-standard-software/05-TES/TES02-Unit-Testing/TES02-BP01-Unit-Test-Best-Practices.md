# TES02-BP01: Unit Test Best Practices

Viết unit tests hiệu quả và maintainable.

## AAA Pattern

```typescript
// Arrange - Act - Assert
describe('calculateTotal', () => {
  it('should apply discount correctly', () => {
    // Arrange
    const items = [
      { price: 100, quantity: 2 },
      { price: 50, quantity: 1 }
    ];
    const discount = 0.1;

    // Act
    const result = calculateTotal(items, discount);

    // Assert
    expect(result).toBe(225); // (200 + 50) * 0.9
  });
});
```

## Test Naming

```typescript
// Pattern: should_expectedBehavior_when_condition
describe('UserService', () => {
  it('should throw ValidationError when email is invalid', () => {});
  it('should return user when id exists', () => {});
  it('should create user when all fields are valid', () => {});
});

// Or: Given-When-Then style
describe('UserService.createUser', () => {
  describe('given valid user data', () => {
    it('then creates user successfully', () => {});
    it('then sends welcome email', () => {});
  });

  describe('given invalid email', () => {
    it('then throws ValidationError', () => {});
  });
});
```

## One Assert Per Test

```typescript
// ❌ Bad: Multiple assertions
it('should create user correctly', () => {
  const user = createUser({ name: 'John', email: 'john@example.com' });
  expect(user.id).toBeDefined();
  expect(user.name).toBe('John');
  expect(user.email).toBe('john@example.com');
  expect(user.createdAt).toBeDefined();
});

// ✅ Good: Focused assertions (or use objectContaining)
it('should create user with provided name', () => {
  const user = createUser({ name: 'John', email: 'john@example.com' });
  expect(user.name).toBe('John');
});

// ✅ Also good: Single assertion for object
it('should create user with correct properties', () => {
  const user = createUser({ name: 'John', email: 'john@example.com' });
  expect(user).toMatchObject({
    name: 'John',
    email: 'john@example.com'
  });
});
```

## Test Data Builders

```typescript
// Use builders for complex test data
class UserBuilder {
  private user: Partial<User> = {
    id: 'default-id',
    name: 'Default Name',
    email: 'default@example.com',
    role: 'user'
  };

  withName(name: string) {
    this.user.name = name;
    return this;
  }

  withRole(role: string) {
    this.user.role = role;
    return this;
  }

  build(): User {
    return this.user as User;
  }
}

// Usage
const adminUser = new UserBuilder().withRole('admin').build();
const johnUser = new UserBuilder().withName('John').build();
```

## Test Independence

```typescript
// ❌ Bad: Tests depend on each other
let user: User;

it('should create user', () => {
  user = createUser({ name: 'John' });
  expect(user).toBeDefined();
});

it('should update user', () => {
  // Depends on previous test!
  const updated = updateUser(user.id, { name: 'Jane' });
  expect(updated.name).toBe('Jane');
});

// ✅ Good: Independent tests
describe('updateUser', () => {
  it('should update user name', () => {
    const user = createUser({ name: 'John' });
    const updated = updateUser(user.id, { name: 'Jane' });
    expect(updated.name).toBe('Jane');
  });
});
```

## Edge Cases

```typescript
describe('divide', () => {
  // Happy path
  it('should divide two numbers', () => {
    expect(divide(10, 2)).toBe(5);
  });

  // Edge cases
  it('should throw when dividing by zero', () => {
    expect(() => divide(10, 0)).toThrow('Division by zero');
  });

  it('should handle negative numbers', () => {
    expect(divide(-10, 2)).toBe(-5);
  });

  it('should handle decimal results', () => {
    expect(divide(10, 3)).toBeCloseTo(3.33, 2);
  });
});
```

## Checklist

- [ ] Tests follow AAA pattern
- [ ] Test names are descriptive
- [ ] One concept per test
- [ ] Tests are independent
- [ ] Edge cases covered
- [ ] No test logic (if/loops)
