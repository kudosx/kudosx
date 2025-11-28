# TES01-BP01: Test Pyramid

Chiến lược phân bổ các loại test hiệu quả.

## Test Pyramid

```
              ┌───────┐
             /   E2E   \          Few, Slow, Expensive
            /───────────\
           /             \
          / Integration   \       Some, Medium
         /─────────────────\
        /                   \
       /      Unit Tests     \    Many, Fast, Cheap
      /─────────────────────────\
```

## Test Types Comparison

| Type | Speed | Cost | Confidence | Quantity |
|------|-------|------|------------|----------|
| Unit | Fast (ms) | Low | Lower | Many (70%) |
| Integration | Medium (s) | Medium | Medium | Some (20%) |
| E2E | Slow (min) | High | High | Few (10%) |

## Unit Tests

```typescript
// Fast, isolated, test single unit
describe('calculateDiscount', () => {
  it('should return 10% discount for orders over $100', () => {
    const result = calculateDiscount(150);
    expect(result).toBe(15);
  });

  it('should return 0 discount for orders under $100', () => {
    const result = calculateDiscount(50);
    expect(result).toBe(0);
  });
});
```

**Characteristics**:
- Test single function/class
- Mock external dependencies
- Run in milliseconds
- Target: 70-80% of tests

## Integration Tests

```typescript
// Test multiple components working together
describe('User API', () => {
  it('should create user and send welcome email', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'test@example.com', name: 'Test' });

    expect(response.status).toBe(201);
    expect(emailService.send).toHaveBeenCalledWith(
      expect.objectContaining({ to: 'test@example.com' })
    );
  });
});
```

**Characteristics**:
- Test component interactions
- May use real database (in-memory)
- Run in seconds
- Target: 15-20% of tests

## E2E Tests

```typescript
// Test complete user flows
test('user can complete checkout', async ({ page }) => {
  await page.goto('/products');
  await page.click('[data-testid="add-to-cart"]');
  await page.click('[data-testid="checkout"]');
  await page.fill('[name="email"]', 'test@example.com');
  await page.click('[data-testid="place-order"]');

  await expect(page.locator('.order-confirmation')).toBeVisible();
});
```

**Characteristics**:
- Test complete user journeys
- Run against real system
- Run in minutes
- Target: 5-10% of tests

## Coverage Goals

| Metric | Target | Critical Paths |
|--------|--------|----------------|
| Line Coverage | 70-80% | 90%+ |
| Branch Coverage | 60-70% | 80%+ |
| Function Coverage | 80-90% | 95%+ |

## What NOT to Test

- Third-party libraries
- Framework code
- Trivial code (getters/setters)
- Generated code

## Anti-Ice Cream Cone

```
❌ Bad (Ice Cream Cone)        ✅ Good (Pyramid)
         ┌───┐                      ┌───┐
        /     \                    / E2E \
       /  E2E  \                  /───────\
      /─────────\                /   Int   \
     / Integration\             /───────────\
    /───────────────\          /    Unit     \
   /      Unit       \        /───────────────\
```

## Checklist

- [ ] Test pyramid được tuân thủ
- [ ] Unit tests cho business logic
- [ ] Integration tests cho API/DB
- [ ] E2E tests cho critical flows
- [ ] Coverage targets đạt được
