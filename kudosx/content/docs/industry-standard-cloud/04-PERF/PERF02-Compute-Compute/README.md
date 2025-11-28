# PERF02: How do you select and use compute resources?

## References

- [AWS PERF02](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-02.html)

## Date

2025-11-27

## Focus Area

Compute

## Tổng quan

PERF02 tập trung vào selecting compute resources (EC2, containers, serverless).

## Best Practices

### PERF02-BP01: Select the best compute options
Evaluate VMs vs containers vs serverless.

### PERF02-BP02: Understand available compute configuration options
Instance types, sizing.

### PERF02-BP03: Collect compute-related metrics
CPU, memory, network.

### PERF02-BP04: Determine required configuration by right-sizing
Right-sizing.

### PERF02-BP05: Use available elasticity
Auto-scaling.

### PERF02-BP06: Re-evaluate compute needs based on metrics
Continuous optimization.

## Compute Options

| Type | Use Case | Pros |
|------|----------|------|
| VMs | General workloads | Flexibility |
| Containers | Microservices | Portability |
| Serverless | Event-driven | No ops |

## Checklist

- [ ] Compute options evaluated
- [ ] Right-sizing performed
- [ ] Auto-scaling configured
- [ ] Metrics collected
