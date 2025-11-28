# DES03-BP02: API Documentation

Document API với OpenAPI (Swagger) specification.

## OpenAPI Structure

```yaml
openapi: 3.0.3
info:
  title: My API
  version: 1.0.0
  description: API description

servers:
  - url: https://api.example.com/v1
    description: Production

paths:
  /users:
    get:
      summary: List users
      # ...

components:
  schemas:
    User:
      # ...
```

## Endpoint Documentation

```yaml
paths:
  /users:
    get:
      tags:
        - Users
      summary: List all users
      description: Returns a paginated list of users
      operationId: listUsers
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: per_page
          in: query
          schema:
            type: integer
            default: 20
            maximum: 100
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
                  meta:
                    $ref: '#/components/schemas/Pagination'
        '401':
          $ref: '#/components/responses/Unauthorized'

    post:
      tags:
        - Users
      summary: Create a new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '422':
          $ref: '#/components/responses/ValidationError'
```

## Schema Definition

```yaml
components:
  schemas:
    User:
      type: object
      required:
        - id
        - email
      properties:
        id:
          type: integer
          format: int64
          example: 123
        email:
          type: string
          format: email
          example: user@example.com
        name:
          type: string
          example: John Doe
        created_at:
          type: string
          format: date-time

    CreateUserRequest:
      type: object
      required:
        - email
        - password
      properties:
        email:
          type: string
          format: email
        password:
          type: string
          minLength: 8
        name:
          type: string
```

## Authentication

```yaml
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - BearerAuth: []
```

## Tools

| Tool | Purpose |
|------|---------|
| **Swagger UI** | Interactive API documentation |
| **Redoc** | Beautiful API docs |
| **Postman** | API testing & docs |
| **Stoplight** | API design & docs |

## Checklist

- [ ] Mọi endpoint đều được document
- [ ] Request/response schemas đầy đủ
- [ ] Examples cho mỗi endpoint
- [ ] Error responses được document
- [ ] Authentication được mô tả
- [ ] API docs được publish
