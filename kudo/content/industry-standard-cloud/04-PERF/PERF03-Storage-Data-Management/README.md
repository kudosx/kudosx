# PERF03: How do you select and use storage resources?

## References

- [AWS PERF03](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-03.html)
- [PostgreSQL Performance](https://www.postgresql.org/docs/current/performance-tips.html)
- [Redis Documentation](https://redis.io/docs/)

## Date

2025-11-27

## Focus Area

Storage / Data Management

## Tổng quan

PERF03 tập trung vào storage và data management.

## Best Practices

### PERF03-BP01: Understand storage characteristics
IOPS, throughput, latency.

### PERF03-BP02: Make decisions based on access patterns
Hot vs cold data.

### PERF03-BP03: Collect storage-related metrics
Monitor storage performance.

### PERF03-BP04: Select appropriate storage options
Storage tiering.

### PERF03-BP05: Ensure that availability and durability requirements are met
Replication, backups.

## Database Optimization

- Index optimization
- Query optimization
- Connection pooling
- Read replicas
- Caching layers

## Caching Strategies

| Type | Use Case |
|------|----------|
| Application cache | Frequent reads |
| CDN | Static assets |
| Database cache | Query results |

## Checklist

- [ ] Storage requirements analyzed
- [ ] Access patterns documented
- [ ] Caching implemented
- [ ] Database optimized
- [ ] Connection pooling configured
