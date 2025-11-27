# DEP02-BP01: Docker Best Practices

Viết Dockerfile tối ưu và secure.

## Optimized Dockerfile

```dockerfile
# Use specific version, not latest
FROM node:20-alpine AS base

# Create non-root user
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nextjs

WORKDIR /app

# ---- Dependencies ----
FROM base AS deps

# Copy only package files first (better caching)
COPY package.json package-lock.json ./
RUN npm ci --only=production

# ---- Build ----
FROM base AS build

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

# ---- Production ----
FROM base AS production

ENV NODE_ENV=production

# Copy built assets
COPY --from=deps /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist

# Use non-root user
USER nextjs

EXPOSE 3000

CMD ["node", "dist/server.js"]
```

## Multi-Stage Build Benefits

```
Stage 1: deps      → Production dependencies only
Stage 2: build     → Full deps + build
Stage 3: production → Minimal image (no dev deps, no source)
```

| Stage | Size | Contents |
|-------|------|----------|
| deps | ~200MB | Production node_modules |
| build | ~800MB | All deps + source + build |
| production | ~150MB | Only runtime files |

## Layer Caching

```dockerfile
# ❌ Bad: Invalidates cache on any code change
COPY . .
RUN npm ci
RUN npm run build

# ✅ Good: Dependencies cached until package.json changes
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build
```

## Security Best Practices

### 1. Use Non-Root User
```dockerfile
RUN adduser --system --uid 1001 appuser
USER appuser
```

### 2. Use Specific Versions
```dockerfile
# ❌ Bad
FROM node:latest
FROM node:20

# ✅ Good
FROM node:20.10.0-alpine3.18
```

### 3. Scan for Vulnerabilities
```bash
docker scan myimage:latest
```

### 4. Use .dockerignore
```
# .dockerignore
node_modules
.git
.env
*.log
coverage
.next
```

## Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1
```

## Environment Variables

```dockerfile
# Build-time args
ARG NODE_ENV=production

# Runtime env
ENV NODE_ENV=$NODE_ENV \
    PORT=3000

# Don't put secrets in Dockerfile!
# Pass at runtime: docker run -e SECRET_KEY=xxx
```

## Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build:
      context: .
      target: production
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://db:5432/app
    depends_on:
      - db
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=app
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
    secrets:
      - db_password

volumes:
  postgres_data:

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

## Checklist

- [ ] Multi-stage build
- [ ] Specific base image versions
- [ ] Non-root user
- [ ] .dockerignore configured
- [ ] Health check defined
- [ ] No secrets in image
- [ ] Minimal final image size
