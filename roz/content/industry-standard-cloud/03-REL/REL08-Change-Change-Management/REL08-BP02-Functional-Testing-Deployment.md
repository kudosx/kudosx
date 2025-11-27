# REL08-BP02: Integrate functional testing in deployment

## Description

Run functional tests như part of deployment pipeline.

## Implementation Guidance

- Include unit tests in CI pipeline
- Run integration tests before deploy
- Implement smoke tests post-deploy
- Gate deployments on test results
- Track test coverage

## Risk Level

High - Deploying without tests causes production issues.

## Related Best Practices

- [REL08-BP03](REL08-BP03-Resiliency-Testing-Deployment.md)
- [OPS05-BP02](../../01-OPS/OPS05-Prepare-Development-And-Integration/OPS05-BP02-Test-And-Validate.md)
