# REL08-BP04: Deploy using immutable infrastructure

## Description

Use immutable deployments thay vì in-place updates.

## Implementation Guidance

- Build new images for each deployment
- Never modify running instances
- Use blue-green or canary deployments
- Implement infrastructure as code
- Version all artifacts

## Risk Level

Medium - Mutable infrastructure creates drift.

## Related Best Practices

- [REL08-BP05](REL08-BP05-Deploy-With-Automation.md)
- [OPS06-BP03](../../01-OPS/OPS06-Prepare-Mitigation-Of-Deployment-Risks/OPS06-BP03-Safe-Deployment-Strategies.md)
