# Industry Standard Resources

AWS Well-Architected Framework làm khung tham chiếu chính.

## Date

2025-11-27 (v4.0 - Folder per Question)

---

## Pillar Overview

| Index | Pillar | Name | Questions | Files |
|-------|--------|------|-----------|-------|
| 01 | OPS | Operational Excellence | 11 | 77 |
| 02 | SEC | Security | 11 | 70 |
| 03 | REL | Reliability | 13 | 13 |
| 04 | PERF | Performance Efficiency | 5 | 5 |
| 05 | COST | Cost Optimization | 3 | 3 |
| 06 | SUS | Sustainability | 3 | 3 |

**Total: 171 files** (OPS và SEC có BP files chi tiết)

---

## Naming Convention

```
{INDEX}-{PILLAR}/{PILLAR}{QUESTION}-{FocusArea}-{QuestionName}/
├── README.md                                    # Question overview
├── {PILLAR}{QUESTION}-BP01-{Best-Practice}.md   # Best Practice 1
├── {PILLAR}{QUESTION}-BP02-{Best-Practice}.md   # Best Practice 2
└── ...

Examples:
- 01-OPS/OPS01-Organization-Operations-Priorities/README.md
- 01-OPS/OPS01-Organization-Operations-Priorities/OPS01-BP01-Evaluate-External-Customer-Needs.md
- 02-SEC/SEC11-Application-Security/README.md
- 03-REL/REL12-Failure-Reliability-Testing/README.md
```

---

## Main Resources

* [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
* [AWS Well-Architected Map](https://wa.aws.amazon.com/wat.map.en.html)
* [Google SRE Book](https://sre.google/sre-book/table-of-contents/)

---

## 01-OPS - Operational Excellence

### Focus Areas: Organization, Prepare, Operate, Evolve

| Question | Focus Area | Title |
|----------|------------|-------|
| OPS01 | Organization | Operations Priorities |
| OPS02 | Organization | Operating Model |
| OPS03 | Organization | Organizational Culture |
| OPS04 | Prepare | Implement Observability |
| OPS05 | Prepare | Development And Integration |
| OPS06 | Prepare | Mitigation Of Deployment Risks |
| OPS07 | Prepare | Operational Readiness |
| OPS08 | Operate | Workload Observability |
| OPS09 | Operate | Operations Health |
| OPS10 | Operate | Event Response |
| OPS11 | Evolve | Operations Evolution |

### References

- [AWS OE Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/)
- [DORA State of DevOps 2024](https://dora.dev/research/2024/dora-report/)
- [Team Topologies](https://teamtopologies.com/)

---

## 02-SEC - Security

### Focus Areas: Security, IAM, Detection, Infrastructure, Data, Incident, Application

| Question | Focus Area | Title |
|----------|------------|-------|
| SEC01 | Security | Secure Operations |
| SEC02 | IAM | Identity Management |
| SEC03 | IAM | Permissions Management |
| SEC04 | Detection | Security Events |
| SEC05 | Infrastructure | Network Protection |
| SEC06 | Infrastructure | Compute Protection |
| SEC07 | Data | Data Classification |
| SEC08 | Data | Protection At Rest |
| SEC09 | Data | Protection In Transit |
| SEC10 | Incident | Response |
| SEC11 | Application | Security |

### References

- [AWS Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/)
- [OWASP Top 10:2025](https://owasp.org/Top10/)
- [NIST SP 800-207](https://csrc.nist.gov/publications/detail/sp/800-207/final)

---

## 03-REL - Reliability

### Focus Areas: Foundations, Workload, Change, Failure

| Question | Focus Area | Title |
|----------|------------|-------|
| REL01 | Foundations | Service Quotas |
| REL02 | Foundations | Network Topology |
| REL03 | Workload | Service Architecture |
| REL04 | Workload | Distributed Systems |
| REL05 | Workload | Mitigate Failures |
| REL06 | Change | Resource Monitoring |
| REL07 | Change | Demand Handling |
| REL08 | Change | Change Management |
| REL09 | Failure | Data Backup |
| REL10 | Failure | Fault Isolation |
| REL11 | Failure | Component Failures |
| REL12 | Failure | Reliability Testing |
| REL13 | Failure | Disaster Recovery |

### References

- [AWS Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- [LitmusChaos](https://litmuschaos.io/)

---

## 04-PERF - Performance Efficiency

### Focus Areas: Selection, Compute, Storage, Networking, Process

| Question | Focus Area | Title |
|----------|------------|-------|
| PERF01 | Selection | Architecture Selection |
| PERF02 | Compute | Compute |
| PERF03 | Storage | Data Management |
| PERF04 | Networking | Networking |
| PERF05 | Process | Process And Culture |

### References

- [AWS Performance Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/)
- [Google API Design Guide](https://cloud.google.com/apis/design)

---

## 05-COST - Cost Optimization

### Focus Areas: Practice, Expenditure, Resources

| Question | Focus Area | Title |
|----------|------------|-------|
| COST01 | Practice | Cloud Financial Management |
| COST02 | Expenditure | Usage Awareness |
| COST03 | Resources | Cost Effective |

### References

- [AWS Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/)
- [FinOps Framework](https://www.finops.org/framework/)

---

## 06-SUS - Sustainability

### Focus Areas: Region, Alignment, Software

| Question | Focus Area | Title |
|----------|------------|-------|
| SUS01 | Region | Region Selection |
| SUS02 | Alignment | Alignment To Demand |
| SUS03 | Software | Software Architecture |

### References

- [AWS Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/)
- [Green Software Foundation](https://greensoftware.foundation/)

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2025-11-27 | 1.0 | Initial structure |
| 2025-11-27 | 2.0 | Restructured with AWS question numbers |
| 2025-11-27 | 3.0 | Flat structure: INDEX-PILLAR/PILLARXX-FocusArea-QuestionName.md |
| 2025-11-27 | 4.0 | **Folder per Question with README.md + BP files** |
