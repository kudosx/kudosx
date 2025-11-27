# TES03-BP01: API Testing

Testing REST APIs với Supertest.

## Setup

```typescript
import request from 'supertest';
import app from '../app';

describe('User API', () => {
  // Test database setup
  beforeAll(async () => {
    await setupTestDatabase();
  });

  beforeEach(async () => {
    await clearDatabase();
  });

  afterAll(async () => {
    await closeDatabase();
  });
});
```

## Testing CRUD Operations

### GET - List Resources

```typescript
describe('GET /api/users', () => {
  it('should return list of users', async () => {
    // Arrange
    await createUser({ name: 'John' });
    await createUser({ name: 'Jane' });

    // Act
    const response = await request(app)
      .get('/api/users')
      .expect(200);

    // Assert
    expect(response.body.data).toHaveLength(2);
    expect(response.body.data[0]).toHaveProperty('name');
  });

  it('should support pagination', async () => {
    const response = await request(app)
      .get('/api/users?page=1&per_page=10')
      .expect(200);

    expect(response.body.meta).toMatchObject({
      page: 1,
      per_page: 10
    });
  });
});
```

### GET - Single Resource

```typescript
describe('GET /api/users/:id', () => {
  it('should return user when exists', async () => {
    const user = await createUser({ name: 'John' });

    const response = await request(app)
      .get(`/api/users/${user.id}`)
      .expect(200);

    expect(response.body.data.name).toBe('John');
  });

  it('should return 404 when not found', async () => {
    await request(app)
      .get('/api/users/nonexistent')
      .expect(404);
  });
});
```

### POST - Create Resource

```typescript
describe('POST /api/users', () => {
  it('should create user with valid data', async () => {
    const userData = {
      name: 'John Doe',
      email: 'john@example.com'
    };

    const response = await request(app)
      .post('/api/users')
      .send(userData)
      .expect(201);

    expect(response.body.data).toMatchObject(userData);
    expect(response.body.data.id).toBeDefined();
  });

  it('should return 422 for invalid data', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ name: '' })
      .expect(422);

    expect(response.body.error.code).toBe('VALIDATION_ERROR');
  });
});
```

### PUT/PATCH - Update Resource

```typescript
describe('PATCH /api/users/:id', () => {
  it('should update user', async () => {
    const user = await createUser({ name: 'John' });

    const response = await request(app)
      .patch(`/api/users/${user.id}`)
      .send({ name: 'Jane' })
      .expect(200);

    expect(response.body.data.name).toBe('Jane');
  });
});
```

### DELETE - Remove Resource

```typescript
describe('DELETE /api/users/:id', () => {
  it('should delete user', async () => {
    const user = await createUser({ name: 'John' });

    await request(app)
      .delete(`/api/users/${user.id}`)
      .expect(204);

    // Verify deletion
    await request(app)
      .get(`/api/users/${user.id}`)
      .expect(404);
  });
});
```

## Testing Authentication

```typescript
describe('Protected routes', () => {
  let authToken: string;

  beforeEach(async () => {
    const user = await createUser({ role: 'admin' });
    authToken = generateToken(user);
  });

  it('should return 401 without token', async () => {
    await request(app)
      .get('/api/admin/users')
      .expect(401);
  });

  it('should return data with valid token', async () => {
    await request(app)
      .get('/api/admin/users')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);
  });

  it('should return 403 for insufficient permissions', async () => {
    const regularUser = await createUser({ role: 'user' });
    const userToken = generateToken(regularUser);

    await request(app)
      .get('/api/admin/users')
      .set('Authorization', `Bearer ${userToken}`)
      .expect(403);
  });
});
```

## Testing Error Handling

```typescript
describe('Error handling', () => {
  it('should return proper error format', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'invalid' })
      .expect(422);

    expect(response.body).toMatchObject({
      error: {
        code: expect.any(String),
        message: expect.any(String)
      }
    });
  });
});
```

## Checklist

- [ ] Test all endpoints
- [ ] Test success and error cases
- [ ] Test authentication/authorization
- [ ] Test validation
- [ ] Clean database between tests
- [ ] Use realistic test data
