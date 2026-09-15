# Secure and allocate capacity

This Capacity Operations (CapOps) domain establishes an owned capacity path for prioritized demand. It separates administrative permissions, supported capacity mechanisms, commercial obligations, and internal allocation decisions.

## Objective

Match demand criticality and timing to supported mechanisms and feasible alternatives, then assign available or committed resources to consumers under explicit conditions. “Secure” does not mean unconditional availability.

## Business outcome

Decision owners understand which demand is supported by which evidence, what remains exposed, and who can act before a deadline. Competing consumers receive deliberate priority decisions rather than conflicting promises.

## Included capabilities

- **Primary:** [Quota management](../capabilities/quota-management.md), [capacity acquisition](../capabilities/capacity-acquisition.md), and [capacity allocation](../capabilities/capacity-allocation.md).
- **Supporting:** [Workload placement](../capabilities/workload-placement.md) defines valid configurations; [capacity governance](../capabilities/capacity-governance.md) establishes authority and lifecycle controls.

## Main activities

1. Match demand to all applicable administrative scopes and verify limit approvals.
2. Evaluate supported mechanisms against exact service, family, location, quantity, date, duration, and eligibility requirements.
3. Compare acquisition with staging, modernization, schedule changes, and other qualified alternatives.
4. Obtain technical and commercial approvals from the relevant authorities.
5. Record mechanism conditions, consumer ownership, use and release rules, expiry, and residual exposure.
6. Allocate by time window and priority, protecting agreed recovery obligations and avoiding double assignment.
7. Reconcile actual consumption and review commitments before material changes or expiry.

Provider engagement coordinates supported processes; it does not by itself provide stronger deployment assurance. Product-specific claims belong in provider guidance and must be checked against current public documentation.

## Primary inputs

- Approved demand versions and qualified primary and alternative placements.
- Business criticality, acceptable interruption or delay, and decision deadlines.
- Current quota scope and use, resource constraints, and existing allocations.
- Documented mechanism terms, eligibility, cost scenarios, and funding authority.
- Recovery profiles and authorized priority rules.

## Expected outputs

- A separate register of administrative permissions and pending limit actions.
- Approved mechanism records with matching demand and documented exclusions.
- Time-bound allocation records, consumers, owners, and reclaim conditions.
- Commercial obligations, review dates, renewal or expiry decisions, and execution evidence.
- Risk records for unmatched demand, insufficient mechanisms, and remaining uncertainty.

## Participating personas

Engineering validates and executes technical actions. Procurement and designated commercial approvers own contractual actions; FinOps assesses economic exposure. Business or portfolio owners approve demand priorities and risk acceptance. Continuity owners validate recovery protections. The CapOps practitioner maintains the cross-record view rather than universally approving purchases or reprioritization.

## Example decisions

- Whether fixed-date critical demand warrants a supported capacity reservation under its documented conditions.
- Whether lower-priority batch work should move to a later window.
- Whether an unused allocation can be reassigned without breaking recovery obligations or commercial terms.
- Whether unmet mechanism requirements require a return to placement planning.

## Risks and common mistakes

- Treating quota approval as physical supply or a financial discount as reserved capacity.
- Labeling all demand “secured” because one supporting resource is covered.
- Assigning the same pool to simultaneous production and recovery consumers.
- Assuming a reservation can be moved, cancelled, or renewed on unchanged terms.

## Related content

- [Domain catalog](../framework/domains.md)
- [Operate and optimize capacity](operate-and-optimize-capacity.md)
- [Capacity acquisition](../capabilities/capacity-acquisition.md)
- [Capacity allocation](../capabilities/capacity-allocation.md)
- [CapOps and FinOps](../overview/capops-and-finops.md)
