# DES02-BP02: Indexing Strategy

Chiến lược đánh index để tối ưu query performance.

## Index Types

| Type | Use Case | Example |
|------|----------|---------|
| **B-Tree** | Default, equality/range queries | `WHERE age > 18` |
| **Hash** | Equality only | `WHERE id = 123` |
| **GIN** | Full-text search, arrays, JSONB | `WHERE tags @> '{a}'` |
| **GiST** | Geometric, full-text | PostGIS queries |
| **BRIN** | Large sequential data | Time-series data |

## When to Create Index

```sql
-- ✅ Index these columns:
-- 1. Primary keys (automatic)
-- 2. Foreign keys
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- 3. Columns used in WHERE
CREATE INDEX idx_users_email ON users(email);

-- 4. Columns used in ORDER BY
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);

-- 5. Columns used in JOIN
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
```

## Composite Index

```sql
-- Order matters! Left-to-right
CREATE INDEX idx_orders_status_created
ON orders(status, created_at);

-- ✅ Uses index
SELECT * FROM orders WHERE status = 'pending';
SELECT * FROM orders WHERE status = 'pending' AND created_at > '2024-01-01';

-- ❌ Does NOT use index efficiently
SELECT * FROM orders WHERE created_at > '2024-01-01';
```

## Covering Index

```sql
-- Include all columns needed by query
CREATE INDEX idx_users_email_name
ON users(email) INCLUDE (first_name, last_name);

-- Query satisfied entirely from index (no table lookup)
SELECT first_name, last_name FROM users WHERE email = 'test@example.com';
```

## Partial Index

```sql
-- Index only subset of data
CREATE INDEX idx_orders_pending
ON orders(created_at)
WHERE status = 'pending';

-- Smaller index, faster queries for pending orders
SELECT * FROM orders WHERE status = 'pending' AND created_at > '2024-01-01';
```

## Index Maintenance

```sql
-- Check index usage
SELECT
    indexrelname,
    idx_scan,
    idx_tup_read
FROM pg_stat_user_indexes
WHERE schemaname = 'public'
ORDER BY idx_scan DESC;

-- Remove unused indexes
DROP INDEX IF EXISTS idx_unused;

-- Rebuild fragmented indexes
REINDEX INDEX idx_orders_created_at;
```

## Anti-patterns

| Anti-pattern | Vấn đề |
|--------------|--------|
| Index mọi column | Slow writes, wasted space |
| Missing FK index | Slow JOINs |
| Wrong column order | Index not used |
| Too many indexes | Write performance degradation |

## Checklist

- [ ] Foreign keys đều có index
- [ ] Columns trong WHERE có index
- [ ] Composite index đúng thứ tự
- [ ] Monitor index usage
- [ ] Remove unused indexes
- [ ] Regular maintenance (REINDEX)
