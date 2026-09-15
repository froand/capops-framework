# Reporting and key performance indicators (KPIs)

This page explains how Capacity Operations (CapOps) turns evidence into operational and executive reporting. It defines measures for decisions rather than prescribing a universal scorecard or numerical benchmark.

## Definition

Reporting communicates capacity posture, changes, risks, and decisions to a defined audience. A key performance indicator (KPI) is a selected measure tied to an intended outcome and an action threshold, not every available telemetry value.

## Purpose

Help the right owner act before a deployment, commitment, allocation, or recovery decision becomes overdue.

## Why it matters

A high portfolio percentage can conceal a critical uncovered workload, incompatible resource units, or old evidence. Executives need business impact and choices; operators need precise scope and next actions. Both views should be derived from the same records, with their limitations visible.

## Desired outcomes

- Reports identify a decision owner, deadline, options, and evidence.
- Metric definitions remain comparable across periods or disclose changes.
- Unknowns, exclusions, and critical outliers are visible alongside totals.
- Reporting prompts action and records whether that action occurred.

## Inputs

- Versioned demand, usage, limit, mechanism, allocation, and commitment records.
- Risk decisions, action deadlines, exceptions, and recovery-validation results.
- Deployment operations with classified causes and deduplication rules.
- Business priorities, audience needs, local targets, and metric ownership.
- Source freshness, missing-data indicators, and historical definition versions.

## Activities

1. Start with a decision question, such as “Which launch needs a placement choice this month?” Select evidence that can change that decision.
2. Create a metric contract: name, purpose, owner, formula, unit, numerator, denominator, population, time window, data source, freshness, exclusions, limitations, threshold, and action.
3. Distinguish measured, estimated, unknown, and not-applicable values. Show denominator counts and avoid displaying zero percent when the denominator is zero.
4. Segment by criticality, service, family, location, and need-by window where relevant. Sum only compatible units; do not invent a global “secured capacity” percentage.
5. Present an operational view of specific blockers and actions, a monthly view of decisions and lifecycle changes, and an executive view of business exposure and priority trade-offs.
6. Review trends against definition and population changes. Annotate workload additions, changed cause classification, forecast revisions, and source outages.
7. Track which decisions the report produced. Retire measures that add noise without changing action, while retaining required audit evidence.

## Outputs

- A metric dictionary and versioned scorecard with explicit scope.
- Operational action lists linked to resource-level evidence.
- Executive decision summaries with business impact and residual risk.
- Reporting-quality issues and evidence of resulting decisions.

## Roles involved

The CapOps practitioner stewards report definitions and traceability. Data owners validate sources. Operations and engineering interpret technical measures. Business owners and executives decide priorities and risk responses. FinOps validates economic interpretation; continuity owners validate recovery conclusions. Producing a report does not transfer accountability for its decisions to the reporting team.

## Dependencies on other capabilities

- [Capacity visibility](capacity-visibility.md) provides reconciled sources and quality indicators.
- [Capacity risk management](capacity-risk-management.md) supplies materiality, deadlines, and residual exposure.
- [Capacity acquisition](capacity-acquisition.md) supplies mechanism evidence rather than vague secured labels.
- [Capacity resilience](capacity-resilience.md) supplies scenario-specific validation results.
- [Capacity governance](capacity-governance.md) defines decision authority and review requirements.

## Suggested measurements

All KPI targets are **organization-defined**. The examples below are candidate definitions, not industry benchmarks or evidence that a particular target produces a guaranteed outcome.

| Candidate measure | Definition and denominator | Limitation and intended action |
|---|---|---|
| Critical demand review coverage | Critical workload demand profiles reviewed against required evidence by deadline / all critical profiles due in the period × 100 | A reviewed profile can contain accepted risk; use it to find missing decisions, not claim supply |
| Capacity-path gap | Required units not matched to the agreed capacity path / total required units in one homogeneous service, family, location, and time bucket × 100 | Define what evidence qualifies for each path; report conditional mechanisms separately and show dependencies |
| Capacity-related deployment failure rate | Operations confirmed blocked by underlying resource capacity / all deployment operations attempted in the same scope and period × 100 | Exclude quota and configuration causes from the numerator; publish unknown causes and retry-grouping rules |
| Unused commitment share | Committed unit-hours with no qualifying consumption or approved reserve purpose / all committed unit-hours in the compatible period × 100 | Distinguish capacity mechanisms from financial commitments; unused technical capacity is not necessarily avoidable cost |
| Decision timeliness | Material decisions made before their last feasible action date / all material decisions due in the reporting period × 100 | Show impact of late decisions; changing deadlines retrospectively invalidates the comparison |
| Legacy dependency exposure | Assessed critical workloads with a locally identified legacy-family dependency and no qualified alternative / all assessed critical workloads × 100 | Define “legacy” using support and architecture evidence, not resource age alone; show impact, not only count |

Recovery coverage and forecast accuracy should use the scoped definitions on their capability pages. Do not roll all measures into one score that can offset a serious recovery weakness with good reporting coverage.

## Maturity indicators

- **Reactive:** Reports are assembled for escalations with inconsistent definitions and missing denominators.
- **Aware:** A recurring scorecard exists, but population changes and unknowns are not consistently disclosed.
- **Managed:** Metric contracts, source owners, audience-specific decisions, and versioned reporting are established.
- **Optimized:** Teams reconcile metric anomalies, assess resulting actions, and remove misleading or unused measures.
- **Strategic:** Portfolio decisions use comparable business and technical evidence while preserving critical outliers and uncertainty.

## Practical example

A fictional monthly review shows nine of ten critical demand profiles reviewed. The report also names the unreviewed tenth profile: a fixed-date launch whose alternative decision expires this week. Executives receive the impact and choice; engineering receives the missing family, zone, quantity, and test details. The 90% illustrative coverage does not justify a green portfolio status or imply that the other nine profiles have guaranteed capacity.

## Risks and common mistakes

- Combining quota, forecasts, discounts, and mechanisms into one coverage field.
- Reporting successful operations only and omitting failures or unknown causes.
- Hiding critical outliers behind averages or maturity scores.
- Treating evidence freshness as proof of evidence accuracy.
- Publishing operational identifiers or provider information beyond the audience's legitimate need.

## Related content

- [Capacity forecasting](capacity-forecasting.md)
- [Capacity optimization](capacity-optimization.md)
- [Manage the CapOps practice domain](../domains/manage-the-capops-practice.md)
- [Operating cadence](../operating-model/operating-cadence.md)
