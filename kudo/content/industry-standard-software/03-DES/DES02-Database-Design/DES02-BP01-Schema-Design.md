# DES02-BP01: Schema Design

Thiết kế database schema theo best practices.

## Normalization Forms

### 1NF (First Normal Form)
- Mỗi column chứa atomic values
- Không có repeating groups

```sql
-- ❌ Bad: Multiple values in one column
CREATE TABLE orders (
    id INT,
    products VARCHAR(255)  -- "iPhone, MacBook, iPad"
);

-- ✅ Good: Separate table for order items
CREATE TABLE orders (id INT PRIMARY KEY);
CREATE TABLE order_items (
    order_id INT,
    product_id INT
);
```

### 2NF (Second Normal Form)
- Đạt 1NF
- Không có partial dependency

### 3NF (Third Normal Form)
- Đạt 2NF
- Không có transitive dependency

```sql
-- ❌ Bad: City depends on zip_code, not directly on customer_id
CREATE TABLE customers (
    id INT,
    zip_code VARCHAR(10),
    city VARCHAR(100)  -- Transitive dependency
);

-- ✅ Good: Separate zip_codes table
CREATE TABLE customers (id INT, zip_code VARCHAR(10));
CREATE TABLE zip_codes (zip_code VARCHAR(10), city VARCHAR(100));
```

## Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Tables | snake_case, plural | `users`, `order_items` |
| Columns | snake_case | `created_at`, `user_id` |
| Primary Key | `id` hoặc `{table}_id` | `id`, `user_id` |
| Foreign Key | `{referenced_table}_id` | `user_id`, `order_id` |
| Index | `idx_{table}_{columns}` | `idx_users_email` |
| Constraints | `{type}_{table}_{column}` | `fk_orders_user_id` |

## Data Types Best Practices

```sql
-- Use appropriate types
id          BIGINT          -- Auto-increment IDs
uuid        UUID            -- External identifiers
email       VARCHAR(255)    -- Variable length strings
price       DECIMAL(10,2)   -- Financial data (NOT FLOAT!)
status      VARCHAR(20)     -- Enum-like values
created_at  TIMESTAMPTZ     -- Timestamps with timezone
is_active   BOOLEAN         -- True/False flags
metadata    JSONB           -- Semi-structured data
```

## Essential Columns

```sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    -- ... business columns ...
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    deleted_at TIMESTAMPTZ  -- Soft delete
);
```

## Checklist

- [ ] Schema đạt ít nhất 3NF
- [ ] Naming conventions nhất quán
- [ ] Data types phù hợp
- [ ] Có created_at, updated_at
- [ ] Foreign keys được định nghĩa
- [ ] Constraints phù hợp (NOT NULL, UNIQUE)
