# CapOps principles

These ten proposed Capacity Operations (CapOps) principles guide choices when a procedure cannot resolve a trade-off. Use them to challenge assumptions and identify the right decision owner, not as a claim of guaranteed outcomes.

## 1. Capacity is a business asset

Capacity supports delivery, operation, growth, and recovery. Its value depends on what the business can do with it at a particular place and time, not simply on the number of resources purchased.

**Apply it:** Attach a business outcome, accountable consumer, criticality, and required date to material demand. Evaluate the impact of a shortfall alongside the cost of holding unused capacity. A reserve with no current utilization can still have an explicit continuity purpose; an idle allocation with no purpose needs review.

## 2. Capacity planning is continuous

Demand changes as roadmaps, performance, schedules, and architectures change. The evidence behind a capacity plan can also expire. One approval should not silently remain valid after its assumptions change.

**Apply it:** Refresh forecasts at an agreed cadence and on material events such as a migration delay, a launch increase, a deployment failure, or a changed recovery design. Version the plan and record what changed, who reviewed it, and which decision must be revisited.

## 3. Demand must be expressed in business and technical terms

“Support a new product launch” is meaningful to a portfolio owner but insufficient for resource planning. “Add 100 instances” lacks timing, service characteristics, and business context.

**Apply it:** Translate business drivers into service, family, quantity and unit, region, zone, date, ramp, duration, priority, and flexibility. Record the conversion assumptions and distinguish baseline, growth, migration, launch, seasonal, artificial intelligence (AI), peak, recovery, and decommissioning effects. Avoid counting the same event in several categories.

## 4. Capacity decisions are shared across business, architecture, engineering, operations, finance, procurement, and continuity roles

Each role contributes a different constraint or source of evidence. Shared decisions do not mean shared ambiguity: someone must have authority to approve a particular trade-off.

**Apply it:** Keep business risk acceptance with the business risk owner, technical suitability with the responsible architecture authority, operational changes with authorized operators, and financial or contractual commitments with their designated approvers. A CapOps lead coordinates the record and follow-through rather than inheriting every accountability.

## 5. Quota does not equal physical capacity

Quota is an administrative permission or service limit. Physical capacity is the underlying ability to fulfill a deployment. A quota increase can remove one blocker without changing the underlying supply.

**Apply it:** Track requested and approved limits separately from deployment evidence and capacity mechanisms. Check every applicable quota scope and dependency. Do not mark demand as fulfilled or supported by a capacity reservation merely because a quota request was approved.

## 6. Forecasting does not equal a guarantee

A forecast estimates expected demand and communicates uncertainty. It is neither an order nor a provider commitment, even when shared through established engagement channels.

**Apply it:** Mark forecast versions, confidence, assumptions, and decision dates. Where criticality requires more than planning visibility, examine supported mechanisms and their exact terms. Preserve the residual risk if the mechanism is unavailable, incomplete, conditional, or insufficient for the required scope.

## 7. Architecture flexibility reduces capacity risk

Tested alternatives can reduce dependence on a single service, family, location, or deployment pattern. An alternative is only useful if it satisfies performance, security, data, operational, and timing requirements.

**Apply it:** Qualify alternatives before they are needed and record the time and cost to switch. Multi-region architecture creates options but does not automatically guarantee capacity; alternate regions may share constraints or lack required dependencies. Avoid adding complexity whose operating burden exceeds its business value.

## 8. Recovery capacity is part of resilience planning

Backups, replication, and failover logic do not establish that a destination can run the restored service. Recovery needs compute, storage, network, control services, quotas, and operational access, potentially while other workloads recover.

**Apply it:** Define production, peak, and recovery profiles separately. Validate the sequence, minimum viable service, destination load, and simultaneous portfolio recovery assumptions. Record test scope and date: a successful exercise is evidence for that exercise, not future physical inventory.

## 9. Capacity commitments require ownership and lifecycle management

A commitment can outlive a workload, change consumer, or cease to match a planned configuration. Commercial discounts and supported capacity reservations can have different scopes and release rules.

**Apply it:** Manage justification, approval, acquisition, assignment, consumption, review, renewal or change, and release or expiry. Give every record a technical consumer, commercial owner where relevant, review date, and exit criteria. Never promise cancellation or transfer without checking applicable terms.

## 10. Capacity risk should be visible and decision-ready

“Capacity risk is high” does not tell a decision-maker what to do. A useful risk links a specific uncertainty to an affected service or milestone and a deadline for choosing a response.

**Apply it:** Record impact, evidence and freshness, options, action owner, risk owner, decision deadline, residual exposure, and re-entry triggers. Show unknowns and overdue decisions explicitly. Scope measurements by compatible resources and time periods rather than producing a misleading portfolio-wide percentage.

## Applying the principles

At an architecture, delivery, commitment, or recovery review, identify which principles are in tension. For example, holding recovery capacity may improve readiness while increasing cost. Record the evidence, alternatives, authorized decision, and review trigger rather than declaring one principle universally dominant.

Local guidance may add detail, but should not redefine quota as supply, a forecast as a commitment, or regional service availability as fulfillment of a required quantity and date.

## Risks and common mistakes

- Using principle compliance as a substitute for testing the actual workload.
- Imposing identical controls on low-impact and business-critical demand.
- Assigning responsibility without the authority, funding, or lead time to act.
- Treating a completed checklist as permanently current evidence.

## Related content

- [People, process, and technology](people-process-technology.md)
- [Personas and accountability](../framework/personas.md)
- [Capacity governance](../capabilities/capacity-governance.md)
- [Capacity risk management](../capabilities/capacity-risk-management.md)
