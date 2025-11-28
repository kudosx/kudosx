# TES02-BP02: Mocking Strategies

Strategies để mock dependencies trong unit tests.

## When to Mock

| Mock | Don't Mock |
|------|------------|
| External APIs | Pure functions |
| Databases | Domain logic |
| File system | Value objects |
| Time/random | Simple utilities |
| Third-party services | |

## Jest Mocking

### Mock Functions

```typescript
// Create mock function
const mockCallback = jest.fn();
mockCallback.mockReturnValue(42);

// Assert calls
expect(mockCallback).toHaveBeenCalled();
expect(mockCallback).toHaveBeenCalledWith('arg1', 'arg2');
expect(mockCallback).toHaveBeenCalledTimes(1);
```

### Mock Modules

```typescript
// Mock entire module
jest.mock('./emailService', () => ({
  sendEmail: jest.fn().mockResolvedValue({ success: true })
}));

// In test
import { sendEmail } from './emailService';

it('should send welcome email', async () => {
  await createUser({ email: 'test@example.com' });
  expect(sendEmail).toHaveBeenCalledWith(
    expect.objectContaining({ to: 'test@example.com' })
  );
});
```

### Mock Implementation

```typescript
const mockUserRepository = {
  findById: jest.fn(),
  save: jest.fn(),
  delete: jest.fn()
};

describe('UserService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should return user when found', async () => {
    mockUserRepository.findById.mockResolvedValue({
      id: '1',
      name: 'John'
    });

    const service = new UserService(mockUserRepository);
    const user = await service.getUser('1');

    expect(user.name).toBe('John');
  });

  it('should throw when user not found', async () => {
    mockUserRepository.findById.mockResolvedValue(null);

    const service = new UserService(mockUserRepository);

    await expect(service.getUser('1')).rejects.toThrow('User not found');
  });
});
```

## Spy

```typescript
// Spy on existing method
const spy = jest.spyOn(console, 'log');

doSomething();

expect(spy).toHaveBeenCalledWith('Expected log message');
spy.mockRestore();
```

## Partial Mocks

```typescript
// Mock only specific methods
jest.mock('./userService', () => ({
  ...jest.requireActual('./userService'),
  sendNotification: jest.fn()
}));
```

## Time Mocking

```typescript
describe('Token expiration', () => {
  beforeEach(() => {
    jest.useFakeTimers();
  });

  afterEach(() => {
    jest.useRealTimers();
  });

  it('should expire after 1 hour', () => {
    const token = createToken();

    // Fast-forward 1 hour
    jest.advanceTimersByTime(60 * 60 * 1000);

    expect(isTokenExpired(token)).toBe(true);
  });
});
```

## Mock Patterns

### Stub
Returns fixed data:
```typescript
mockService.getUser.mockReturnValue({ id: '1', name: 'John' });
```

### Fake
Working implementation:
```typescript
class FakeUserRepository {
  private users = new Map();

  save(user) { this.users.set(user.id, user); }
  findById(id) { return this.users.get(id); }
}
```

### Mock
Verifies interactions:
```typescript
expect(mockService.save).toHaveBeenCalledWith(expectedUser);
```

## Checklist

- [ ] Mock external dependencies
- [ ] Don't mock what you don't own (use adapter)
- [ ] Clear mocks between tests
- [ ] Verify mock interactions
- [ ] Use appropriate mock type (stub/fake/mock)
