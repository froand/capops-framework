# Capacity allocation

This page explains how Capacity Operations (CapOps) assigns defined capacity pools to competing consumers. Use it when internal priorities, time windows, or recovery obligations could otherwise result in conflicting assignments.

## Definition

Capacity allocation assigns consumer rights to available, pre-positioned, or committed capacity within a defined technical scope and time window. It records priorities, protections, expiry, and the conditions for reclaim or reassignment.

## Purpose

Translate business priorities into enforceable, traceable assignments without promising more than the underlying pool can support.

## Why it matters

Acquiring capacity does not decide who may use it. A shared pool can be counted by several projects, held by a delayed workload, or silently consumed by routine demand before recovery is needed. An allocation ledger makes these conflicts visible while alternatives remain possible.

An internal allocation is not proof of provider physical capacity. Future intended allocations must be labeled as planned unless their underlying state is established.

## Desired outcomes

- Consumer assignments are dimensionally compatible with their source pool.
- Concurrent demand does not receive incompatible promises.
- Priority conflicts and protected recovery rights are decided by authorized owners.
- Unused allocations are reviewed, not retained indefinitely by default.

## Inputs

- Verified pool or mechanism scope, quantity, dates, and applicable conditions.
- Prioritized workload demand and required time windows.
- Existing assignments, observed use, forecast changes, and release notices.
- Recovery protections, minimum service requirements, and preemption constraints.
- Delegated priority authority, consumer ownership, and commercial transfer rules.

## Activities

1. Define the allocation pool by resource type, unit, location, eligibility, and valid time interval. Do not pool configurations solely because their names are similar.
2. Reconcile existing assignments and physical or mechanism evidence; distinguish planned, approved, consumed, and released states.
3. Compare overlapping consumer demand, including shared recovery scenarios. Any deliberate overbooking requires explicit scenario assumptions, approved risk, and an enforceable fallback.
4. Apply published local priority criteria such as business impact, deadline, acceptable deferral, and recovery obligation. Escalate conflicts to the authorized portfolio or service owner.
5. Record each assignment's consumer, quantity, dates, priority, constraints, protected portion, reclaim notice, and approver.
6. Enforce approved boundaries through supported platform controls where possible. Test that allocation policy and operational behavior agree.
7. Reconcile actual use and review idle or expiring assignments. Reassignment or release must respect commercial terms and must update the forecast and commitment record.

## Outputs

- A time-bound allocation ledger linked to demand and underlying pool evidence.
- Authorized priority decisions, including deferred or reduced demand.
- Consumer notifications, enforcement actions, and reclaim or renewal dates.
- Exceptions for overbooking, unprotected recovery demand, or uncertain future pools.

## Roles involved

Business and portfolio owners approve priority trade-offs. Workload owners confirm dates, minimum need, and relinquishment. Platform engineering enforces assignments; operations observes use. Continuity owners validate protected recovery rights. Procurement checks whether a mechanism permits reassignment. The CapOps practitioner reconciles the ledger and surfaces contention rather than deciding every consumer's priority.

## Dependencies on other capabilities

- [Capacity acquisition](capacity-acquisition.md) establishes the underlying mechanism or resource pool.
- [Capacity forecasting](capacity-forecasting.md) supplies quantity and time-window demand.
- [Capacity resilience](capacity-resilience.md) defines recovery consumers and simultaneous use.
- [Capacity governance](capacity-governance.md) establishes priority authority and exception rules.

## Suggested measurements

Targets and reclaim thresholds are **organization-defined**. Use homogeneous pool units and compatible time buckets.

| Measure | Definition | Limitation |
|---|---|---|
| Assignment ratio | Assigned unit-hours / allocatable pool unit-hours during the same interval × 100 | A ratio above 100 flags overlap, but approved time-sharing must be interpreted under its scenario; the pool may still have external conditions |
| Idle allocation share | Assigned unit-hours with no observed qualifying use and no approved reserve purpose / total assigned unit-hours in the period × 100 | Missing telemetry is unknown, not idle; exclude protected standby only when its purpose is documented |
| Priority decision timeliness | Allocation conflicts decided before their action deadline / all conflicts requiring a decision in the period × 100 | Low reported conflict volume can mean conflicts are not being recorded |

## Maturity indicators

- **Reactive:** Consumers compete informally and allocations are reconstructed after contention.
- **Aware:** Major commitments have consumers, but overlaps and reclaim dates are reviewed manually.
- **Managed:** An owned ledger, explicit priority rules, protected recovery assignments, and approval records govern shared pools.
- **Optimized:** Actual use and demand changes drive controlled reallocation; exceptions and idle assignments are resolved with evidence.
- **Strategic:** Portfolio sequencing and continuity priorities jointly shape allocations, with tested fallback behavior under contention.

## Practical example

An illustrative fictional pool has 100 compatible units. A critical launch requests 70 and a flexible analysis job requests 50 for the same window. The portfolio owner approves 70 for launch and 30 for analysis, with the remaining analysis work deferred. If 20 units must instead remain protected for recovery, that changes the allocatable production pool; it is not an invisible third promise. The ledger and consumer plans are updated together.

## Risks and common mistakes

- Double-counting one pool across projects, regions, or recovery scenarios.
- Making first-come-first-served the default without business approval.
- Reclaiming idle capacity that has a valid continuity purpose.
- Assuming internal reassignment transfers a commercial obligation.
- Treating an expired allocation as released without verifying actual resources and records.

## Related content

- [Secure and allocate capacity domain](../domains/secure-and-allocate-capacity.md)
- [Capacity optimization](capacity-optimization.md)
- [Automation](automation.md)
- [Personas and accountability](../framework/personas.md)
