# CapOps Framework

This page shows how to use the proposed Capacity Operations (CapOps) Framework as a connected operating practice. It provides a starting map, not a requirement to adopt every capability or create a new department.

## Framework building blocks

| Building block | Question it answers | How to use it |
|---|---|---|
| [Principles](../overview/principles.md) | What should guide a trade-off? | Challenge assumptions during a decision |
| [Domains](domains.md) | Which business outcomes are we trying to achieve? | Organize work without creating organizational silos |
| [Capabilities](capabilities.md) | What repeatable work produces those outcomes? | Specify evidence, actions, owners, and outputs |
| [Personas](personas.md) | Whose contribution and authority are needed? | Assign decision-specific responsibility |
| [Lifecycle](lifecycle.md) | How does evidence turn into execution and learning? | Connect the work and revisit changed assumptions |
| [Operating model](../operating-model/operating-model.md) | How does the organization sustain the practice? | Connect reviews to delivery, finance, and continuity |
| [Maturity model](../maturity/maturity-model.md) | Where is evidence of reliable practice missing? | Prioritize improvements by capability and business exposure |

The five domains are **Understand capacity**, **Plan capacity**, **Secure and allocate capacity**, **Operate and optimize capacity**, and **Manage the CapOps practice**. They group outcomes, not teams or isolated project phases. For example, recovery capacity is planned before acquisition and revalidated during operation.

## Lifecycle

The lifecycle is **Discover → Forecast → Plan → Secure → Allocate → Monitor → Optimize → Validate recovery → Learn**.

The lifecycle is iterative. A changed launch date can reopen forecasting; an incompatible resource family can reopen planning; a failed recovery exercise can reopen acquisition and allocation. “Secure” means evaluating and using supported mechanisms and alternatives, not declaring unconditional availability.

## The minimum connected evidence

Maintain linked records rather than a single status field:

- **Workload profile:** Business owner, criticality, production, peak, and recovery requirements, dependencies, and acceptable flexibility.
- **Demand forecast:** Versioned requirements by service, family, quantity and unit, region, zone, date, ramp, duration, and priority.
- **Capacity path:** Applicable limits, placement alternatives, supported mechanisms, validation evidence, and unresolved assumptions.
- **Commitment and allocation records:** Consumers, approvers, technical and commercial scope, dates, and release or expiry conditions.
- **Risk and decision records:** Business impact, feasible options, decision deadline, authorized decision, actions, and residual risk.
- **Observed results:** Actual demand, deployment and recovery outcomes, evidence freshness, and follow-up improvements.

Different records may live in existing systems. Link them through stable identifiers and version references so reviewers can reconstruct why a decision was reasonable at the time.

## Conduct a bounded implementation

1. Select a workload or portfolio slice with a consequential near-term decision.
2. Establish business, technical, commercial, and continuity decision owners.
3. Assess current evidence for the capabilities that decision needs. Do not substitute a portfolio maturity average for a missing critical control.
4. Produce the minimum records above and compare actionable alternatives.
5. Execute the authorized choice, monitor assumptions, and verify the outcome.
6. Use observed gaps to select the next improvement, preserving practices that already work.

For a migration, the first iteration might combine visibility, forecasting, quota management, placement, and risk management. For a recovery gap, resilience and allocation might lead. Neither sequence is a universal adoption order.

## Risks and common mistakes

- Mistaking the framework for a product, provider commitment, or established industry standard.
- Measuring document completion instead of whether a decision was made with adequate evidence and lead time.
- Allowing central practice ownership to displace federated workload accountability.
- Implementing every capability at equal depth regardless of business risk.
- Assuming maturity in forecasting compensates for an untested recovery capacity path.

## Related content

- [What is CapOps?](../overview/what-is-capops.md)
- [Domains](domains.md)
- [Capabilities](capabilities.md)
- [Personas](personas.md)
- [Lifecycle](lifecycle.md)
- [Conduct a CapOps iteration](../implementation/conduct-a-capops-iteration.md)
