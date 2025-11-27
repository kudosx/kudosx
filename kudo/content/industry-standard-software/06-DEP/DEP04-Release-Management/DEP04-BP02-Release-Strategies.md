# DEP04-BP02: Release Strategies

Các chiến lược deployment và rollback.

## Deployment Strategies

### 1. Rolling Deployment

```
Time →
Instance 1: [v1] [v1→v2] [v2] [v2] [v2]
Instance 2: [v1] [v1] [v1→v2] [v2] [v2]
Instance 3: [v1] [v1] [v1] [v1→v2] [v2]
```

**Pros**: Zero downtime, gradual rollout
**Cons**: Mixed versions during deployment

### 2. Blue-Green Deployment

```
        ┌─────────────┐
        │ Load        │
        │ Balancer    │
        └──────┬──────┘
               │
       ┌───────┴───────┐
       │               │
   ┌───▼───┐       ┌───▼───┐
   │ Blue  │       │ Green │
   │ (v1)  │       │ (v2)  │
   │ACTIVE │       │STANDBY│
   └───────┘       └───────┘
```

**Process**:
1. Deploy v2 to Green (standby)
2. Test Green environment
3. Switch traffic to Green
4. Blue becomes new standby

**Pros**: Instant rollback, full testing before switch
**Cons**: Requires 2x resources

### 3. Canary Deployment

```
Traffic distribution:
┌─────────────────────────────────────┐
│████████████████████████████████ 95% │ → v1 (stable)
│██ 5%                                │ → v2 (canary)
└─────────────────────────────────────┘

Progressive rollout:
Day 1:  5% traffic to v2
Day 2: 25% traffic to v2
Day 3: 50% traffic to v2
Day 4: 100% traffic to v2
```

**Pros**: Early detection of issues, controlled risk
**Cons**: Complex monitoring needed

### 4. Feature Flags

```typescript
// Feature flag example
if (featureFlags.isEnabled('new-checkout', userId)) {
  return renderNewCheckout();
} else {
  return renderOldCheckout();
}

// Gradual rollout
featureFlags.setRolloutPercentage('new-checkout', 10);
```

**Pros**: Decouple deployment from release, A/B testing
**Cons**: Code complexity, technical debt if not cleaned

## Rollback Strategies

### Automatic Rollback

```yaml
# AWS ECS example
deployment:
  rollback:
    enabled: true
    events:
      - DEPLOYMENT_FAILURE
      - SERVICE_FAILURE

# Health check triggers rollback
healthCheck:
  healthyThreshold: 2
  unhealthyThreshold: 5
  interval: 30
```

### Manual Rollback

```bash
# Kubernetes
kubectl rollout undo deployment/my-app

# Docker
docker service update --rollback my-service

# AWS ECS
aws ecs update-service --cluster my-cluster \
  --service my-service \
  --task-definition my-app:previous-version
```

### Database Rollback

```sql
-- Always write reversible migrations
-- up.sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- down.sql
ALTER TABLE users DROP COLUMN phone;
```

## Release Checklist

### Pre-Release
- [ ] All tests pass
- [ ] Code review approved
- [ ] Security scan passed
- [ ] Performance tested
- [ ] Documentation updated
- [ ] Changelog updated

### Release
- [ ] Deploy to staging
- [ ] Smoke tests pass
- [ ] Deploy to production (canary)
- [ ] Monitor metrics
- [ ] Gradual rollout

### Post-Release
- [ ] Verify all metrics normal
- [ ] Clean up feature flags
- [ ] Update documentation
- [ ] Notify stakeholders

## Monitoring During Release

| Metric | Alert Threshold |
|--------|-----------------|
| Error rate | > 1% |
| Latency p99 | > 500ms |
| CPU usage | > 80% |
| Memory usage | > 85% |

## Checklist

- [ ] Deployment strategy chosen
- [ ] Rollback plan documented
- [ ] Health checks configured
- [ ] Monitoring in place
- [ ] Team notified of release
