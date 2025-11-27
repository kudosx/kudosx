# DES03-BP01: RESTful API Design

Thiết kế REST API theo industry standards.

## URL Structure

```
https://api.example.com/v1/users/123/orders?status=pending
└──────────┬────────┘ └┬┘└──────┬───────┘ └──────┬──────┘
         Base URL    Ver  Resource Path    Query Params
```

## Resource Naming

```
# ✅ Good - Nouns, plural
GET    /users              # List users
GET    /users/123          # Get user 123
POST   /users              # Create user
PUT    /users/123          # Update user 123
DELETE /users/123          # Delete user 123

# ✅ Nested resources
GET    /users/123/orders   # User's orders

# ❌ Bad - Verbs, singular
GET    /getUser/123
POST   /createUser
DELETE /deleteUser/123
```

## HTTP Methods

| Method | Purpose | Idempotent | Request Body |
|--------|---------|------------|--------------|
| GET | Read | Yes | No |
| POST | Create | No | Yes |
| PUT | Replace | Yes | Yes |
| PATCH | Partial Update | Yes | Yes |
| DELETE | Delete | Yes | No |

## HTTP Status Codes

```
2xx Success
├── 200 OK              # General success
├── 201 Created         # Resource created
├── 204 No Content      # Success, no body (DELETE)

4xx Client Error
├── 400 Bad Request     # Invalid request
├── 401 Unauthorized    # Authentication required
├── 403 Forbidden       # No permission
├── 404 Not Found       # Resource not found
├── 409 Conflict        # Resource conflict
├── 422 Unprocessable   # Validation error

5xx Server Error
├── 500 Internal Error  # Server error
├── 502 Bad Gateway     # Upstream error
├── 503 Unavailable     # Service down
```

## Response Format

```json
// Success response
{
  "data": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com"
  }
}

// List response with pagination
{
  "data": [...],
  "meta": {
    "total": 100,
    "page": 1,
    "per_page": 20
  }
}

// Error response
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": [
      { "field": "email", "message": "Must be valid email" }
    ]
  }
}
```

## Versioning

```
# URL versioning (recommended)
GET /v1/users
GET /v2/users

# Header versioning
GET /users
Accept: application/vnd.api+json; version=1
```

## Filtering, Sorting, Pagination

```
# Filtering
GET /orders?status=pending&user_id=123

# Sorting
GET /orders?sort=created_at&order=desc

# Pagination
GET /orders?page=2&per_page=20

# Combined
GET /orders?status=pending&sort=-created_at&page=1&per_page=20
```

## Checklist

- [ ] Resources là nouns, plural
- [ ] HTTP methods đúng purpose
- [ ] Status codes phù hợp
- [ ] Response format nhất quán
- [ ] API versioning
- [ ] Pagination cho list endpoints
