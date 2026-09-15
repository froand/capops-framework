# CapOps governance

Capacity Operations (CapOps) governance defines evidence, authority, and boundaries for capacity decisions. It should expose choices while there is still time to act, not introduce a new board at the end of delivery. This page describes the guardrails behind the [operating model](operating-model.md); the [implementation guide](../implementation/establish-capacity-governance.md) explains how to adopt them.

## Scope controls to business exposure

Define which workloads and changes are capacity-sensitive using local business criticality, resource specificity, location constraints, growth, recovery objectives, and acquisition lead times. A routine request inside a tested pattern may follow automated guardrails. A new family, large demand step, inflexible location, shared recovery destination, or material contractual obligation may need additional evidence and approval.

Do not prescribe universal utilization, coverage, spending, or maturity thresholds. Record the organization's chosen trigger, rationale, authority, and review date.

## Minimum guardrails

| Guardrail | Required evidence | Enforcement point |
|---|---|---|
| Business demand has an accountable owner | Outcome, priority, dates, demand version, sizing assumptions, and acceptable flexibility | Intake and business case |
| Technical claims are dimension-specific | Service, family, quantity and unit, permitted region or zone, time window, dependencies, and evidence freshness | Design and material change |
| Normal, peak, and recovery are separate | Scenario profiles, overlap assumptions, destination resident load, and concurrent portfolio recovery dependencies | Design and continuity review |
| “Secured” is qualified | Exact mechanism, entitlement and exclusions, dates, assignment, outstanding prerequisites, and validation scope | Acquisition and readiness |
| Commitments have a lifecycle | Business consumer, budget authority, technical owner, term, allocation, consumption, review, and release or renewal criteria | Before acquisition and throughout use |
| Decisions are traceable and timely | Options, rationale, risk acceptor, last responsible decision deadline, action owners, and revisit trigger | Existing approval workflows |
| Exceptions expire | A bounded deviation, compensating controls, approver, expiry, and revalidation plan | Before departing from a guardrail |

A forecast communicates expected demand, quota grants permission to request, and a financial discount changes economics. None alone proves deployable capacity. A service listing does not establish availability of every requested resource; multi-region or recovery architecture does not establish destination supply.

## Place checkpoints where choices remain

- **Business case:** test whether dates, location constraints, and specialized resources create an early decision. Record the business consequences of a phased or delayed outcome.
- **Architecture:** validate sizing and alternatives, including dependencies and recovery demand. Identify how long a design change would take.
- **Commercial commitment:** confirm authority, exact mechanism terms, funding, assignment, and an exit strategy before accepting obligations.
- **Delivery and readiness:** refresh evidence against the demand actually being released, including rollback and restoration requirements. A previous gate's evidence can expire.
- **Operational change and renewal:** assess consumer changes, idle allocations, new contention, and whether the obligation should continue.

The checkpoint result is proceed, change, hold, or a bounded exception. “Review complete” without a decision is not an approval.

## Handle exceptions as controlled decisions

1. Identify the guardrail and the exact scope of the deviation.
2. Explain why compliant options are not currently feasible, with evidence and their decision deadlines.
3. Record business impact, affected consumers, compensating controls, and residual risk.
4. Obtain approval from the authority for that risk or obligation; the practice lead only facilitates unless explicitly delegated.
5. Set an expiry, evidence refresh date, owner, and event-based revisit triggers.
6. At expiry, close with verified evidence, choose another option, or obtain a new decision. Do not silently extend.

If an urgent incident requires action first, follow the existing incident authority and record the decision as soon as practical. Retrospective documentation is not a way to bypass normal procurement, safety, regulatory, or continuity controls.

## Learn from failed assumptions

After an incident or near miss, reconstruct what was known when the decision was made. Distinguish a changed external condition from missing demand, stale evidence, incorrect scope, competing allocation, or a delayed decision. Assign corrective actions to the owner of the failing process or control and specify how effectiveness will be checked.

For example, if a fictional recovery exercise finds that two services counted the same destination headroom, update both profiles and the shared allocation control. Adding a generic “check capacity” task without correcting the double count does not resolve the finding.

## Related content

- [Roles and responsibilities](roles-and-responsibilities.md)
- [Decision record template](../templates/decision-record.md)
- [Establish capacity governance](../implementation/establish-capacity-governance.md)
- [Manage capacity commitments](../implementation/manage-capacity-commitments.md)
