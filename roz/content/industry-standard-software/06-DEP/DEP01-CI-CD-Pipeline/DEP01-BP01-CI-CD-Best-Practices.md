# DEP01-BP01: CI/CD Best Practices

Xây dựng CI/CD pipeline hiệu quả.

## CI/CD Flow

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  Code   │───▶│  Build  │───▶│  Test   │───▶│ Deploy  │───▶│ Monitor │
│  Push   │    │         │    │         │    │ Staging │    │         │
└─────────┘    └─────────┘    └─────────┘    └────┬────┘    └─────────┘
                                                  │
                                             ┌────▼────┐
                                             │ Deploy  │
                                             │  Prod   │
                                             └─────────┘
```

## GitHub Actions Example

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Type check
        run: npm run type-check

      - name: Unit tests
        run: npm run test:unit

      - name: Build
        run: npm run build

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build
          path: dist/

  test-e2e:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Download build
        uses: actions/download-artifact@v4
        with:
          name: build
          path: dist/

      - name: E2E tests
        run: npm run test:e2e

  deploy-staging:
    needs: [build, test-e2e]
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Deploy to staging
        run: ./scripts/deploy.sh staging

  deploy-production:
    needs: [build, test-e2e]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy to production
        run: ./scripts/deploy.sh production
```

## Pipeline Stages

### 1. Build Stage
```yaml
- name: Build
  run: |
    npm ci --production=false
    npm run build
    npm prune --production
```

### 2. Test Stage
```yaml
- name: Test
  run: |
    npm run test:unit -- --coverage
    npm run test:integration
  env:
    DATABASE_URL: ${{ secrets.TEST_DATABASE_URL }}
```

### 3. Security Scan
```yaml
- name: Security scan
  uses: snyk/actions/node@master
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

### 4. Deploy Stage
```yaml
- name: Deploy
  uses: aws-actions/amazon-ecs-deploy-task-definition@v1
  with:
    task-definition: task-definition.json
    service: my-service
    cluster: my-cluster
```

## Best Practices

| Practice | Lý do |
|----------|-------|
| **Fast feedback** | Pipeline < 10 minutes |
| **Fail fast** | Lint/tests trước, deploy sau |
| **Parallel jobs** | Tăng tốc độ |
| **Cache dependencies** | Giảm build time |
| **Environment variables** | Config không hardcode |
| **Secrets management** | Không commit secrets |

## Branch Protection

```yaml
# Require before merge to main
- Status checks pass
- Code review approved
- No merge conflicts
- Branch up to date
```

## Deployment Strategies

| Strategy | Mô tả | Risk |
|----------|-------|------|
| **Rolling** | Từng instance một | Medium |
| **Blue-Green** | Switch traffic instantly | Low |
| **Canary** | % traffic to new version | Low |
| **Feature Flags** | Toggle features | Low |

## Checklist

- [ ] Auto trigger on push/PR
- [ ] Lint và tests trong pipeline
- [ ] Build artifacts cached
- [ ] Secrets không trong code
- [ ] Deploy to staging before prod
- [ ] Rollback strategy defined
