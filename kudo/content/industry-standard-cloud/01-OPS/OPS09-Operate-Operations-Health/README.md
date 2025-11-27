# OPS09: How do you understand the health of your operations?

## References

- [AWS OPS09](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops-09.html)
- [DORA Metrics](https://dora.dev/)

## Date

2025-11-27

## Focus Area

Operate

## Tổng quan

OPS09 tập trung vào hiểu health của operations activities, không chỉ workload.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [OPS09-BP01](OPS09-BP01-Identify-KPIs.md) | Identify KPIs | KPIs cho operations |
| [OPS09-BP02](OPS09-BP02-Define-Metrics.md) | Define operations metrics | Metrics cho operations |
| [OPS09-BP03](OPS09-BP03-Collect-Analyze-Metrics.md) | Collect and analyze metrics | Thu thập và phân tích |
| [OPS09-BP04](OPS09-BP04-Establish-Baselines.md) | Establish baselines | Baseline cho operations |
| [OPS09-BP05](OPS09-BP05-Learn-Patterns.md) | Learn expected patterns | Hiểu patterns |
| [OPS09-BP06](OPS09-BP06-Alert-When-At-Risk.md) | Alert when at risk | Alert khi có issues |
| [OPS09-BP07](OPS09-BP07-Validate-Insights.md) | Validate insights | Verify insights |

## DORA Metrics

| Metric | Description |
|--------|-------------|
| **Deployment Frequency** | How often deploys to production |
| **Lead Time for Changes** | Time from commit to production |
| **Change Failure Rate** | % of deployments causing failures |
| **Time to Restore Service** | MTTR for incidents |

## Checklist

- [ ] Operations KPIs defined
- [ ] DORA metrics tracked
- [ ] Operations dashboards created
- [ ] Team performance reviewed regularly
- [ ] Continuous improvement based on metrics
