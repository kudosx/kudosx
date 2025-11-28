# OPS04: How do you implement observability in your workload?

## References

- [AWS OPS04](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops-04.html)
- [OpenTelemetry](https://opentelemetry.io/)
- [RED/USE Methods](https://www.brendangregg.com/usemethod.html)

## Date

2025-11-27

## Focus Area

Prepare

## Tổng quan

OPS04 tập trung vào implementing observability để hiểu internal state của workload thông qua metrics, logs, traces.

## Three Pillars of Observability

| Pillar | Mô tả | Tools |
|--------|-------|-------|
| **Metrics** | Numerical data over time | Prometheus, CloudWatch |
| **Logs** | Discrete events with context | CloudWatch Logs, Loki |
| **Traces** | Request flow across services | X-Ray, Jaeger |

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [OPS04-BP01](OPS04-BP01-Identify-KPIs.md) | Identify KPIs | Xác định KPIs aligned với business |
| [OPS04-BP02](OPS04-BP02-Application-Telemetry.md) | Application telemetry | Thu thập telemetry từ apps |
| [OPS04-BP03](OPS04-BP03-User-Experience-Telemetry.md) | User experience telemetry | Đo lường user experience |
| [OPS04-BP04](OPS04-BP04-Dependency-Telemetry.md) | Dependency telemetry | Monitor dependencies |
| [OPS04-BP05](OPS04-BP05-Distributed-Tracing.md) | Distributed tracing | Enable tracing across services |

## RED Method (Request-focused)

```
Rate    = requests per second
Errors  = failed requests per second
Duration = latency distribution (p50, p95, p99)
```

## USE Method (Resource-focused)

```
Utilization = % time resource is busy
Saturation  = amount of queued work
Errors      = error events count
```

## Checklist

- [ ] KPIs defined and tracked
- [ ] Application metrics collected
- [ ] Structured logging implemented
- [ ] Distributed tracing enabled
- [ ] Dashboards created
- [ ] Alerting configured
