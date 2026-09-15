# Roles and responsibilities

Capacity Operations (CapOps) distributes decisions to the people authorized to make them. This page turns the [framework personas](../framework/personas.md) into decision-specific accountability. A persona is a contribution, not necessarily a separate job. Use the [responsibility matrix](../templates/responsibility-matrix.md) to replace role labels with names and deputies.

## Accountability follows the decision

Each decision has one accountable internal authority for the stated scope. The responsible party carries out the work; contributors supply evidence or expertise. If a decision requires separate business, technical, and financial approvals, record those as distinct decisions rather than naming several indistinguishable owners.

| Decision or output | Accountable authority | Responsible execution | Required contributions |
|---|---|---|---|
| Practice mandate and risk appetite | Executive sponsor | Practice lead prepares scope and options | Business, architecture, finance, continuity |
| Practice standards, record quality, and facilitation | Practice lead | Named practice contributors | Workload and evidence owners |
| Demand volume, priority, business dates, and acceptable service reduction | Business or product owner | Workload planning team | Architecture, delivery, operations |
| Technical sizing, placement suitability, and equivalence of alternatives | Delegated architecture authority | Solution architect | Platform, security, compliance, workload engineering |
| Quota request and technical capacity-mechanism configuration | Platform service owner | Platform engineering | Workload owner, architect, provider representative |
| Contractual acquisition or renewal | Delegated commercial or budget authority | Procurement and commercial management | FinOps, platform service owner, workload owner |
| Allocation and reassignment within approved priorities | Platform service owner | Platform engineering | Business consumers, finance, operations |
| Cross-workload priority conflict or delivery deferral | Portfolio authority | Portfolio planning team | Affected business owners, sponsor, architecture |
| Cost attribution and economic recommendation | Finance or FinOps authority within its mandate | FinOps practitioner | Procurement, consumers, platform |
| Deployment or migration readiness | Existing delivery release authority | Delivery and platform teams | Business owner, architect, operations |
| Recovery objective and acceptance of a continuity gap | Business service owner under continuity policy | Continuity owner prepares recommendation | Reliability, architecture, affected business owners |
| Recovery test execution and technical result | Operations or reliability service owner | Recovery execution team | Continuity, platform, dependency owners |
| Risk acceptance beyond delegated limits | Existing risk authority or sponsor | Risk owner assembles evidence | Business, compliance, architecture, finance as relevant |
| Commitment release | Authority for the obligation being released | Commercial or platform operator, as applicable | All affected consumers and recovery owners |
| Operational evidence quality | Owner of the producing service or data source | Operations and platform teams | Practice lead, workload teams |
| Executive capacity narrative | Practice lead for consolidation; each decision remains with its authority | Practice reporting contributors | Business risk owners validate impact and recommendation |

These assignments are a starting pattern, not a mandated organization chart. Local policies may reserve contract, continuity, or risk decisions for different authorities.

## Handoffs must be explicit

A complete handoff identifies the demand version, evidence scope, receiving owner, required decision, and deadline. The sender retains the action until the receiver acknowledges it. A provider representative may explain public mechanisms and coordinate a supported request, but is not the customer's internal risk acceptor or allocation authority.

The practice lead can challenge missing evidence, convene contributors, and escalate a missed deadline. The lead cannot silently:

- Change a business priority to fit available resources.
- Declare an untested alternative technically equivalent.
- Treat a forecast or quota approval as a capacity commitment.
- Authorize contractual spend outside delegated limits.
- Accept recovery risk for a business service.

## Resolve disagreement without inventing a board

1. State the conflicting decisions separately: for example, technical feasibility versus affordability.
2. Preserve each authority's evidence and constraints in a decision record.
3. Identify an option satisfying both, or send the explicit trade-off to the existing portfolio or risk authority before the last responsible decision deadline.
4. Record the outcome, dissenting evidence if material, residual exposure, action owners, and revisit trigger.

For a fictional shared commitment, platform engineering may authorize a technically compatible reassignment. If that reassignment would jeopardize another product's launch, the affected business owners and portfolio authority must first resolve priority. A practice lead's desire to improve utilization is not sufficient authorization.

## Avoid responsibility gaps

Name a deputy for time-sensitive decisions. Review ownership after reorganizations, workload transfers, and contract renewal. Shared infrastructure still needs a service owner; “the business” and “the cloud team” are not actionable assignments. A combined role should document separate approval acts where local segregation-of-duties rules require them.

## Related content

- [Operating model](operating-model.md)
- [Governance and exceptions](governance.md)
- [Responsibility matrix template](../templates/responsibility-matrix.md)
- [Decision record template](../templates/decision-record.md)
