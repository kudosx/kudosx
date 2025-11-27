# TES04-BP01: Playwright Best Practices

E2E testing với Playwright.

## Setup

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30000,
  retries: 2,
  use: {
    baseURL: 'http://localhost:3000',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { browserName: 'chromium' } },
    { name: 'firefox', use: { browserName: 'firefox' } },
    { name: 'webkit', use: { browserName: 'webkit' } },
  ],
});
```

## Locator Strategies

```typescript
// ✅ Recommended: data-testid (most stable)
await page.locator('[data-testid="submit-button"]').click();

// ✅ Good: Role-based (accessible)
await page.getByRole('button', { name: 'Submit' }).click();

// ✅ Good: Label-based
await page.getByLabel('Email').fill('test@example.com');

// ⚠️ Avoid: CSS selectors (fragile)
await page.locator('.btn-primary').click();

// ❌ Bad: XPath (hard to maintain)
await page.locator('//button[@class="submit"]').click();
```

## Page Object Model

```typescript
// pages/LoginPage.ts
export class LoginPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.page.getByLabel('Email').fill(email);
    await this.page.getByLabel('Password').fill(password);
    await this.page.getByRole('button', { name: 'Login' }).click();
  }

  async expectError(message: string) {
    await expect(this.page.getByRole('alert')).toContainText(message);
  }
}

// tests/login.spec.ts
import { LoginPage } from './pages/LoginPage';

test('successful login', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.goto();
  await loginPage.login('user@example.com', 'password');

  await expect(page).toHaveURL('/dashboard');
});
```

## Testing User Flows

```typescript
test.describe('Checkout Flow', () => {
  test('user can complete purchase', async ({ page }) => {
    // Login
    await page.goto('/login');
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('password');
    await page.getByRole('button', { name: 'Login' }).click();

    // Add item to cart
    await page.goto('/products');
    await page.getByTestId('product-1').click();
    await page.getByRole('button', { name: 'Add to Cart' }).click();

    // Checkout
    await page.getByRole('link', { name: 'Cart' }).click();
    await page.getByRole('button', { name: 'Checkout' }).click();

    // Fill shipping info
    await page.getByLabel('Address').fill('123 Main St');
    await page.getByRole('button', { name: 'Continue' }).click();

    // Place order
    await page.getByRole('button', { name: 'Place Order' }).click();

    // Verify success
    await expect(page.getByTestId('order-confirmation')).toBeVisible();
  });
});
```

## Assertions

```typescript
// Element visibility
await expect(page.locator('.modal')).toBeVisible();
await expect(page.locator('.spinner')).not.toBeVisible();

// Text content
await expect(page.locator('h1')).toHaveText('Welcome');
await expect(page.locator('.message')).toContainText('Success');

// URL
await expect(page).toHaveURL('/dashboard');
await expect(page).toHaveURL(/\/users\/\d+/);

// Element state
await expect(page.getByRole('button')).toBeEnabled();
await expect(page.getByRole('checkbox')).toBeChecked();

// Count
await expect(page.getByRole('listitem')).toHaveCount(5);
```

## Waiting Strategies

```typescript
// ✅ Auto-waiting (built-in)
await page.getByRole('button').click(); // Waits automatically

// ✅ Wait for specific condition
await page.waitForURL('/dashboard');
await page.waitForSelector('[data-testid="loaded"]');

// ✅ Wait for network
await page.waitForResponse('/api/users');
await page.waitForLoadState('networkidle');

// ❌ Avoid: Fixed timeouts
await page.waitForTimeout(2000); // Don't do this
```

## Test Data

```typescript
// Use API to setup data
test.beforeEach(async ({ request }) => {
  await request.post('/api/test/reset');
  await request.post('/api/test/seed', {
    data: { users: 10, products: 20 }
  });
});

// Or use fixtures
test.use({
  storageState: 'tests/.auth/user.json' // Pre-authenticated state
});
```

## Checklist

- [ ] Use data-testid for critical elements
- [ ] Implement Page Object Model
- [ ] Test critical user flows
- [ ] Handle loading states
- [ ] Run on multiple browsers
- [ ] Screenshot/video on failure
