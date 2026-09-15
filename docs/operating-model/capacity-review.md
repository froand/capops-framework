# Capacity review

A Capacity Operations (CapOps) review turns evidence into decisions about business exposure. It reconciles what workloads need with what can be credibly planned, acquired, allocated, or changed. Use this page to design the review and the [monthly review guide](../implementation/monthly-capops-review.md) to run it.

## A decision-ready evidence pack

Begin with the decisions due, not a utilization chart. Each item should state:

1. The business milestone and consequence of doing nothing.
2. Required service, resource family, quantity and unit, location, date, duration, and normal, peak, or recovery scenario.
3. What changed since the previous demand or decision version.
4. Evidence source, observed date, applicability, freshness rule, and unresolved assumptions.
5. Feasible options, including demand reduction, sequencing, alternate placement, acquisition, or acceptance within authority.
6. The recommended choice, cost and operational consequences, accountable decision maker, and last responsible decision deadline.

Keep quota permission, contractual terms, technical entitlement, allocation, and observed deployment separate. A financial commitment can have no capacity entitlement. A capacity mechanism may apply only under specified conditions. “No issue reported” is not evidence that a future deployment can be fulfilled.

## Reconcile before choosing

| Question | What to examine | Decision the answer enables |
|---|---|---|
| Has business demand changed? | New initiatives, dates, ramp, usage baseline, retirements, and scenario assumptions | Reforecast, phase delivery, or re-prioritize |
| Is the reported coverage meaningful? | Exact demand-to-mechanism match, exclusions, competing allocations, and evidence age | Acquire, protect, reassign, validate, or mark a gap |
| Are alternatives still viable? | Performance testing, location approval, engineering effort, and latest start date | Fund or activate an alternative before it expires |
| Are commitments being used as intended? | Assignment versus consumption, idle obligations, expiry, release terms, and future recovery use | Retain, reassign, amend, renew, or release |
| Can affected services recover together? | Destination resident demand, shared dependencies, recovery order, rebuild overhead, and test limitations | Change sequence, protect headroom, or accept an explicit recovery gap |
| Did previous actions work? | Completed deployment or test evidence, not just task closure | Close the risk, retain residual exposure, or choose a different mitigation |

## Two reporting views, one traceable record

**Operational reporting** exposes the detail needed to act: requests that failed, relevant limits, unassigned commitments, actual consumers, stale forecast assumptions, destination conflicts, deadlines, and assigned actions. A team must be able to follow a signal back to a workload and evidence source.

**Executive reporting** presents business consequences and choices: milestones exposed, services with unvalidated recovery, portfolio conflicts, obligations that require funding decisions, and residual risks outside delegated appetite. It should identify who must decide and by when, not simply aggregate red and green indicators.

For either view, label the observation period, owner, data gaps, and organization-defined target. If reporting “covered demand,” specify which scenario and time-location-family-quantity slices are counted, which mechanism supports each, and the denominator. Do not average incompatible units or mix normal and recovery demand into an unexplained percentage.

## Example of a useful review item

A fictional order service expects 70 compatible compute units at a launch window in a permitted location. Current evidence establishes 40 running units; a quota increase permits additional requests, but the additional 30 units have not been established through a matching capacity mechanism or deployment validation. An alternate family passed performance tests but needs application changes.

The review does not label all 70 units “secured.” It asks the business and release authorities to choose among implementing the alternative, phasing the launch, or another supported acquisition path before their respective deadlines. Procurement and the technical owner separately confirm any new obligation and its mechanism conditions.

## Close with evidence, not minutes alone

Publish decisions, action owners, deadlines, risk updates, and revisit triggers. Carry forward unresolved items explicitly and escalate missed decision windows. Keep the detailed record accessible to implementers; give executives a short summary linked to that record.

Avoid reviewing every workload equally, using stale screenshots as enduring proof, hiding unknowns in a green total, or interpreting a successful deployment as a promise about future inventory.

## Related content

- [Operating cadence](operating-cadence.md)
- [Monthly review template](../templates/monthly-review-template.md)
- [CapOps scorecard template](../templates/capops-scorecard.md)
- [Capacity risk register guide](../implementation/create-a-capacity-risk-register.md)
