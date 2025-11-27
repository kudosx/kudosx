# OPS11: How do you evolve operations?

## References

- [AWS OPS11](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops-11.html)
- [Google SRE - Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)

## Date

2025-11-27

## Focus Area

Evolve

## Tổng quan

OPS11 tập trung vào continuous improvement của operations thông qua learning, feedback loops, và blameless postmortems.

## Best Practices

| BP | Name | Description |
|----|------|-------------|
| [OPS11-BP01](OPS11-BP01-Continuous-Improvement.md) | Continuous improvement | Process để liên tục cải tiến |
| [OPS11-BP02](OPS11-BP02-Implement-Feedback-Loops.md) | Implement feedback loops | Feedback loops từ customers |
| [OPS11-BP03](OPS11-BP03-Define-Improvement-Drivers.md) | Define improvement drivers | Xác định drivers |
| [OPS11-BP04](OPS11-BP04-Validate-Insights.md) | Validate insights | Validate trước khi action |
| [OPS11-BP05](OPS11-BP05-Operations-Metrics-Reviews.md) | Operations metrics reviews | Regular review |
| [OPS11-BP06](OPS11-BP06-Document-Lessons-Learned.md) | Document lessons learned | Document và share |
| [OPS11-BP07](OPS11-BP07-Allocate-Improvement-Time.md) | Allocate improvement time | Dedicated time |

## Blameless Postmortem Template

```markdown
# Postmortem: [Incident Title]

## Summary
Brief description of what happened.

## Timeline
- HH:MM - Event A
- HH:MM - Event B

## Root Cause
What caused the incident (5 whys analysis).

## Impact
- Duration: X hours
- Users affected: X

## Lessons Learned
What we learned from this incident.

## Action Items
- [ ] Action 1 - Owner - Due date
- [ ] Action 2 - Owner - Due date
```

## Continuous Improvement Cycle

```
Plan → Do → Check → Act → (repeat)
```

## Checklist

- [ ] Continuous improvement process established
- [ ] Feedback loops implemented
- [ ] Postmortem process defined
- [ ] Lessons learned documented
- [ ] Improvement time allocated (e.g., 20% time)
- [ ] Regular retrospectives conducted
