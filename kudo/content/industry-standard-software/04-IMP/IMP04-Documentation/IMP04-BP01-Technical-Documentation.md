# IMP04-BP01: Technical Documentation

Viết technical documentation rõ ràng và hữu ích.

## Documentation Types (Diátaxis)

```
                    PRACTICAL
                       │
         Tutorials ────┼──── How-to Guides
              │        │           │
   LEARNING ──┼────────┼───────────┼── WORKING
              │        │           │
      Explanation ─────┼──── Reference
                       │
                  THEORETICAL
```

| Type | Purpose | Example |
|------|---------|---------|
| **Tutorials** | Learning-oriented | "Getting Started" |
| **How-to** | Task-oriented | "How to deploy" |
| **Reference** | Information-oriented | "API Reference" |
| **Explanation** | Understanding-oriented | "Architecture Overview" |

## README Template

```markdown
# Project Name

Brief description of the project.

## Features

- Feature 1
- Feature 2

## Quick Start

\`\`\`bash
npm install
npm run dev
\`\`\`

## Installation

Detailed installation instructions...

## Usage

\`\`\`typescript
import { something } from 'package';
// Example code
\`\`\`

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `3000` |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT
```

## Code Comments

### When to Comment

```typescript
// ✅ Explain "why", not "what"
// Using binary search because the array is always sorted
// and we need O(log n) performance for large datasets
const index = binarySearch(sortedArray, target);

// ✅ Warn about non-obvious behavior
// WARNING: This function has side effects - it modifies the original array
function sortInPlace(arr) { }

// ✅ TODO with context
// TODO(john): Refactor this after we migrate to the new API
// Tracking: JIRA-123
```

### When NOT to Comment

```typescript
// ❌ Don't explain obvious code
// increment counter by 1
counter++;

// ❌ Don't leave commented-out code
// const oldFunction = () => { ... }

// ❌ Don't write redundant JSDoc
/**
 * Gets user by ID
 * @param id - The user ID  <- Obvious from parameter name
 * @returns User  <- Obvious from return type
 */
function getUserById(id: string): User { }
```

## API Documentation

```typescript
/**
 * Creates a new user account.
 *
 * @remarks
 * This method sends a verification email upon successful creation.
 * The user must verify their email within 24 hours.
 *
 * @param data - User registration data
 * @returns The created user object
 *
 * @throws {ValidationError} If email format is invalid
 * @throws {DuplicateError} If email already exists
 *
 * @example
 * ```typescript
 * const user = await createUser({
 *   email: 'user@example.com',
 *   password: 'securePassword123'
 * });
 * ```
 */
async function createUser(data: CreateUserInput): Promise<User> { }
```

## Architecture Documentation

```markdown
# Authentication System

## Overview
Brief description of the authentication system.

## Components
```
┌─────────┐     ┌─────────┐     ┌─────────┐
│ Client  │────▶│   API   │────▶│   DB    │
└─────────┘     └─────────┘     └─────────┘
                    │
                    ▼
               ┌─────────┐
               │  Redis  │
               └─────────┘
```

## Flow
1. User submits credentials
2. API validates credentials
3. JWT token generated
4. Token stored in Redis
5. Token returned to client

## Security Considerations
- Passwords hashed with bcrypt
- Tokens expire after 1 hour
- Rate limiting on login endpoint
```

## Checklist

- [ ] README có đủ Quick Start
- [ ] API endpoints đều documented
- [ ] Architecture diagrams up-to-date
- [ ] Examples cho complex features
- [ ] Changelog maintained
