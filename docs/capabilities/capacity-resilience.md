# Capacity resilience

This page explains how Capacity Operations (CapOps) makes recovery and scale assumptions explicit and testable. It is for service and continuity owners deciding whether their planned recovery path has credible resource support under a stated disruption scenario.

## Definition

Capacity resilience defines, prepares, and validates the resources needed to sustain minimum service, absorb peaks, fail over, restore, or rebuild workloads, including competition for destination resources.

## Purpose

Expose and address capacity gaps that backups, replication, or failover architecture alone do not resolve.

## Why it matters

A service may have a valid recovery design but still require resources that are not running, assigned, or supported by a relevant mechanism at the destination. Several workloads can independently assume they will use the same headroom. Recovery therefore needs a portfolio scenario, not just successful isolated exercises.

Resilience design is not recovery capacity. Multi-region architecture creates placement options but does not establish future supply, complete dependencies, or independent failure conditions.

## Desired outcomes

- Production, peak, and recovery profiles are separate and linked.
- Minimum viable service and restoration sequence have business approval.
- Destination baseline load and simultaneous recovery demand are reconciled.
- Test evidence states its scope, limits, date, results, and next validation trigger.

## Inputs

- Business impact analysis and required recovery time objective (RTO), the target elapsed time to restore agreed service.
- Recovery point objective (RPO), the acceptable data-loss window, and the data movement or replication assumptions it creates.
- Production and peak profiles, architecture dependencies, and destination baseline use.
- Recovery sequence, restoration throughput, quota, mechanism, and allocation evidence.
- Exercise permissions, safe test boundaries, prior findings, and acceptable degraded service.

## Activities

1. Define the disruption scenario, affected workloads, minimum viable service, RTO, RPO, and the authority that may accept a gap.
2. Build three profiles. **Production** describes normal operating resources; **peak** describes additional demand and scaling time; **recovery** describes destination and rebuild resources by stage. Recovery may be smaller, larger, or differently shaped than production.
3. Include compute, storage space and throughput, network paths, identity, control services, licenses, images, data restoration, operational access, and any specialized resources.
4. Model simultaneous portfolio recovery. Add the destination's surviving baseline and agreed concurrent recovery demand; account for dependencies, startup bursts, priority, and resources that cannot be shared.
5. Document how each requirement is met: already operating resources, protected allocations, a supported mechanism, or resources to be requested at recovery time. State uncertainty for the last category.
6. Exercise the agreed scenario safely. Measure quantity, configuration, dependency sequence, restoration time, achieved service, and contention. A tabletop review can test decisions but not full deployment or performance.
7. Resolve gaps through architecture, supported mechanisms, allocation, sequencing, or revised business objectives. Record residual risk and retest after material changes.

## Outputs

- A scenario-specific recovery capacity profile and dependency sequence.
- A portfolio destination-demand model with explicit concurrency assumptions.
- Exercise evidence, achieved service, untested conditions, and capacity gaps.
- Authorized remediation or risk acceptance with owners, deadlines, and revalidation triggers.

## Roles involved

Business service owners set recovery needs and accept business shortfalls within their authority. Continuity owners coordinate scenarios and validation. Architects define the recovery design. Engineering and operations execute safe tests and maintain runbooks. FinOps and procurement assess standby economics and terms. The CapOps practitioner reconciles portfolio contention and evidence, not the business's recovery-risk acceptance.

## Dependencies on other capabilities

- [Capacity forecasting](capacity-forecasting.md) supplies production, peak, and destination demand.
- [Capacity allocation](capacity-allocation.md) protects recovery rights and resolves competing consumers.
- [Quota management](quota-management.md) verifies destination and rebuild administrative limits.
- [Capacity acquisition](capacity-acquisition.md) evaluates supported mechanisms for unmet recovery needs.
- [Workload placement](workload-placement.md) qualifies recovery configurations and dependencies.

## Suggested measurements

Targets, required scenarios, and evidence freshness are **organization-defined**. No measure proves future destination capacity.

| Measure | Definition | Limitation |
|---|---|---|
| Current recovery-profile coverage | Critical services with current business-approved resource profiles and owned capacity paths / all in-scope critical services × 100 | Profile completion does not equal an exercised path; show untested services separately |
| Exercise objective attainment | Completed exercises meeting all agreed resource, service, and recovery-time criteria / all completed exercises in the period × 100 | State scenario and scale; exclude neither failures nor partial results, and show cancelled or overdue tests separately |
| Portfolio scenario validation | Required simultaneous-recovery scenarios with current exercised capacity evidence / all required simultaneous-recovery scenarios × 100 | A limited exercise cannot establish full portfolio scale; document simulated versus deployed portions |

## Maturity indicators

- **Reactive:** Recovery resource requirements are discovered during a disruption.
- **Aware:** Individual services document destination needs, but shared demand and prerequisites are incomplete.
- **Managed:** Owned recovery profiles, capacity paths, scoped exercises, and remediation deadlines support critical services.
- **Optimized:** Exercises cover material portfolio concurrency and trigger updates to allocation, architecture, and capacity mechanisms.
- **Strategic:** Business continuity, investment, and portfolio placement decisions jointly account for recovery exposure and minimum viable service.

## Practical example

Two fictional services each need an illustrative 40 compatible units for minimum recovery service. Their destination already uses 50 units. A scenario in which both recover therefore needs 130 units before any startup overhead, not 90 from considering either service alone. If the documented path supports only 110, continuity and business owners must decide on additional support, sequencing, reduced service, or accepted exposure. A successful 10-unit test does not close the 20-unit portfolio gap.

## Risks and common mistakes

- Assuming backup success proves restoration capacity or completion time.
- Counting one reserve for several simultaneous recoveries.
- Omitting destination baseline load, rebuild overhead, or control-service dependencies.
- Claiming future availability from a successful test on a different date, configuration, or scale.
- Removing apparently idle standby resources without business and continuity approval.

## Related content

- [Capacity risk management](capacity-risk-management.md)
- [Capacity optimization](capacity-optimization.md)
- [Plan capacity domain](../domains/plan-capacity.md)
- [The lifecycle](../framework/lifecycle.md)
