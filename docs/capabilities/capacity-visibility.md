# Capacity visibility

This page explains how Capacity Operations (CapOps) assembles a trustworthy customer-side operating picture. Use it to identify what is observed, which records disagree, and where missing evidence could affect a decision.

## Definition

Capacity visibility is the collection and reconciliation of demand, usage, administrative limits, commitments, allocations, dependencies, deployment outcomes, and risk for an explicitly defined workload population.

## Purpose

Give business and technical reviewers a shared evidence base without presenting customer telemetry as provider physical inventory.

## Why it matters

A workload can appear healthy in a usage report while its next growth step exceeds quota, its commitment expires before a launch, or its recovery destination is already assigned elsewhere. These signals are useful only when their resource dimensions, time windows, and ownership can be joined.

## Desired outcomes

- Material workloads and shared dependencies have named owners and current profiles.
- Reviewers can distinguish measured consumption, expected demand, permissions, and mechanism evidence.
- Unknown or stale evidence has an action owner rather than an implied green status.
- A decision can be traced to the source and version of its supporting records.

## Inputs

- Workload inventory, business criticality, and technical ownership.
- Usage measurements with units, collection period, and location scope.
- Demand forecasts, quota records, commitment terms, and allocation ledgers.
- Deployment attempts and failures with correlation identifiers and available cause evidence.
- Architecture dependencies, recovery profiles, and data-access restrictions.

## Activities

1. Declare the population and freshness policy: which workloads, accounts, services, locations, and observation periods are in scope.
2. Create stable workload identifiers and map resources and shared services to them. Record unassigned resources for investigation.
3. Normalize service, family, quantity, unit, region, zone, and timestamps. Preserve native scope where a limit or mechanism cannot be safely translated.
4. Keep separate fields for usage, quota limit, requested demand, capacity-mechanism evidence, and internal allocations. Do not collapse them into “available capacity.”
5. Reconcile ownership and date mismatches, including decommissioned workloads that still have commitments.
6. Classify deployment evidence as confirmed cause, suspected cause, or unresolved. Distinguish resource constraints from permission, configuration, or policy failures.
7. Show missing and stale records prominently; route material gaps to risk management before the decision deadline.

## Outputs

- A timestamped workload capacity view with source links and quality indicators.
- A map of shared dependencies and location or family concentration.
- A reconciliation queue for orphaned records, incompatible units, and stale evidence.
- Evidence packages for forecasts, allocation reviews, and risk decisions.

## Roles involved

Platform engineering and operations own collection and technical interpretation. Workload owners confirm resource mappings and business criticality. Architects validate dependency relationships. FinOps and procurement reconcile commercial records. The CapOps practitioner stewards the combined schema and quality process; source owners remain responsible for correcting their records.

## Dependencies on other capabilities

- [Capacity forecasting](capacity-forecasting.md) supplies versioned future demand and consumes the observed baseline.
- [Capacity allocation](capacity-allocation.md) identifies actual consumers and competing assignments.
- [Capacity risk management](capacity-risk-management.md) determines when an evidence gap requires a business decision.
- [Automation](automation.md) supports repeatable collection while retaining provenance and access controls.

## Suggested measurements

Targets and freshness thresholds are **organization-defined**. Publish the assessed population and observation date with each measure.

| Measure | Definition | Limitation |
|---|---|---|
| Profile coverage | In-scope critical workloads with an owner, dependency map, and current capacity profile / all in-scope critical workloads × 100 | An incomplete inventory inflates coverage; report newly discovered and excluded workloads |
| Evidence freshness | Required records updated within their source-specific freshness threshold / all required records at the snapshot × 100 | Frequent collection does not establish semantic correctness or physical supply |
| Reconciliation age | Median and oldest elapsed days since unresolved mismatches were first detected, with open-item count | The median can hide one critical stale record; show overdue decision-linked items individually |

## Maturity indicators

- **Reactive:** Resource details are gathered after a blocked deployment; ownership is reconstructed manually.
- **Aware:** A scoped inventory exists, but demand, limits, and commitments are reconciled only for selected reviews.
- **Managed:** Required fields, source owners, freshness rules, and correction workflows produce repeatable evidence.
- **Optimized:** Automated reconciliation detects drift and quality problems; reviewers verify whether alerts lead to useful corrections.
- **Strategic:** Portfolio and architecture decisions use traceable dependency and concentration evidence while retaining unknowns.

Assess these indicators through recent records and decisions, not dashboard appearance. Visibility maturity can differ between platforms or business units.

## Practical example

A fictional migration team joins wave demand, resource-family mappings, quota approvals, and deployment test results. The view reveals that the quota approval applies to the intended region but the test used another zone. The team does not mark the wave ready. Engineering validates the intended zone, and the workload owner keeps the unmet evidence requirement visible until the next placement decision.

## Risks and common mistakes

- Inferring provider inventory from quota headroom or regional service listings.
- Joining records only by resource name while ignoring location, unit, scope, or date.
- Treating a failed collector as zero consumption.
- Exposing identifiers or detailed operational data to audiences that only need summarized business impact.
- Counting a successful small test as validation of an untested larger quantity.

## Related content

- [Understand capacity domain](../domains/understand-capacity.md)
- [Quota management](quota-management.md)
- [Reporting and key performance indicators](reporting-and-kpis.md)
- [Capacity resilience](capacity-resilience.md)
