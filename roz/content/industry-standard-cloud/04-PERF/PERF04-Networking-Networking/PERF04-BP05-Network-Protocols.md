# PERF04-BP05: Choose network protocols to improve performance

## Description

Select protocols như HTTP/2, gRPC cho better performance.

## Implementation Guidance

- Use HTTP/2 for multiplexing
- Consider gRPC for internal services
- Evaluate WebSocket for real-time
- Enable compression
- Use connection pooling

## Risk Level

Low - Protocol choice affects latency.

## Related Best Practices

- [PERF04-BP07](PERF04-BP07-Optimize-Network-Config.md)
- [PERF04-BP01](PERF04-BP01-Network-Impact-Performance.md)
