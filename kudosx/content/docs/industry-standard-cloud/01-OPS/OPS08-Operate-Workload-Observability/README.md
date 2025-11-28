# OPS08: How do you understand the health of your workload?

## References

- [AWS OPS08](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops-08.html)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)

## Date

2025-11-27

## Focus Area

Operate

## Tổng quan

OPS08 tập trung vào việc hiểu health của workload thông qua metrics, dashboards, và alerting.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [OPS08-BP01](OPS08-BP01-Identify-KPIs.md) | Identify KPIs | Xác định KPIs cho workload |
| [OPS08-BP02](OPS08-BP02-Define-Metrics.md) | Define workload metrics | Định nghĩa metrics |
| [OPS08-BP03](OPS08-BP03-Collect-Analyze-Metrics.md) | Collect and analyze metrics | Thu thập và phân tích |
| [OPS08-BP04](OPS08-BP04-Establish-Baselines.md) | Establish baselines | Thiết lập baseline |
| [OPS08-BP05](OPS08-BP05-Learn-Patterns.md) | Learn expected patterns | Hiểu patterns bình thường |
| [OPS08-BP06](OPS08-BP06-Alert-When-At-Risk.md) | Alert when at risk | Alerting khi có anomalies |

## SLI/SLO/SLA

| Term | Definition |
|------|------------|
| **SLI** | Service Level Indicator - metric đo lường |
| **SLO** | Service Level Objective - target cho SLI |
| **SLA** | Service Level Agreement - commitment với customers |

## Example SLOs

| Service | SLI | SLO |
|---------|-----|-----|
| API | Availability | 99.9% |
| API | Latency p99 | < 200ms |
| API | Error rate | < 0.1% |

## Checklist

- [ ] KPIs defined
- [ ] Metrics collected
- [ ] Dashboards created
- [ ] Baselines established
- [ ] SLOs defined
- [ ] Alerting configured
