# Operate and optimize capacity

This Capacity Operations (CapOps) domain keeps capacity plans aligned with actual operation. It covers observation, controlled changes, reclaim, modernization, and the feedback needed to preserve performance and recovery obligations.

## Objective

Detect meaningful changes in demand and constraints, improve useful utilization, and maintain valid capacity evidence throughout the workload lifecycle.

## Business outcome

The organization can redirect unnecessary capacity and reduce rigid dependencies without silently weakening service or continuity objectives. Operational findings reach planning and commercial decisions while action is still possible.

## Included capabilities

- **Primary:** [Capacity optimization](../capabilities/capacity-optimization.md) and [automation](../capabilities/automation.md).
- **Supporting:** [Capacity visibility](../capabilities/capacity-visibility.md), [capacity allocation](../capabilities/capacity-allocation.md), [capacity resilience](../capabilities/capacity-resilience.md), and [reporting and key performance indicators](../capabilities/reporting-and-kpis.md).

## Main activities

1. Compare actual usage and deployment outcomes with forecast and allocation assumptions.
2. Route administrative-limit failures, resource constraints, and unknown failures to distinct actions.
3. Investigate idle assignments, overdue commitments, and threshold breaches.
4. Evaluate rightsizing, scheduling, reclaim, reallocation, and family modernization.
5. Validate performance and recovery before release; define rollback and stop conditions.
6. Automate repeatable collection and low-risk controls within approved boundaries.
7. Feed changes and incident findings into forecasts, placement decisions, and recovery tests.

## Primary inputs

- Timestamped usage, service performance, scaling, and deployment evidence.
- Production, peak, and recovery profiles with approved service objectives.
- Allocation, commitment, and commercial records with lifecycle dates.
- Forecast ranges, architecture dependencies, and optimization proposals.
- Change controls, maintenance windows, and previous incident findings.

## Expected outputs

- Classified operational exceptions with owners and action deadlines.
- Approved optimization changes and before-and-after evidence.
- Reclaimed or reassigned allocations, with commercial obligations tracked separately.
- Updated forecasts, capacity profiles, and mechanism records.
- Recovery-validation results and a backlog of remaining gaps.

Released customer resources do not prove that the same quantity can later be reacquired. Any decision that depends on reacquisition should retain that uncertainty.

## Participating personas

Operations and reliability own monitoring and authorized operational changes. Platform engineering implements controls and configuration changes. Workload owners approve changes to business service obligations. Architects qualify modernization options. Continuity owners assess recovery impact. FinOps and procurement review economic and contractual effects; the CapOps practitioner connects the resulting evidence to portfolio decisions.

## Example decisions

- Whether an idle allocation is excess demand or an intentional recovery reserve.
- Whether a new resource family is sufficiently tested to replace a rigid dependency.
- Whether repeated scaling failures justify revising headroom or the placement plan.
- Whether an automated reclaim action must pause because its ownership data is stale.

## Risks and common mistakes

- Optimizing average utilization while ignoring bursts, scaling delay, or recovery.
- Declaring savings from a released allocation while its financial obligation remains.
- Automating destructive actions from incomplete telemetry.
- Treating a successful single-workload recovery test as evidence for simultaneous portfolio recovery.

## Related content

- [Domain catalog](../framework/domains.md)
- [Capacity optimization](../capabilities/capacity-optimization.md)
- [Automation](../capabilities/automation.md)
- [Capacity resilience](../capabilities/capacity-resilience.md)
- [The lifecycle](../framework/lifecycle.md)
