# Establish capacity governance

Establish Capacity Operations (CapOps) governance by adding decision-ready capacity evidence to existing controls. The deliverable is a working set of guardrails and accountable handoffs, not a new board. Use the [governance model](../operating-model/governance.md) as a starting point, adapting it to local authority and business exposure.

## Prerequisites

- A sponsor and named business, architecture, platform, commercial, and continuity authorities.
- Existing delivery, investment, risk, and incident policies.
- An initial set of workload profiles and known capacity risks.
- Agreement on where decisions, exceptions, obligations, and evidence are retained.

## Steps and evidence

1. **Define scope and triggers.** Identify capacity-sensitive workloads and changes using business impact, location constraints, resource specificity, growth, recovery, and lead time. Record locally chosen criteria rather than universal thresholds.
2. **Map decision rights.** Complete the [responsibility matrix](../templates/responsibility-matrix.md). Separate demand priority, technical suitability, contractual obligation, allocation, readiness, and business-risk acceptance. Identify deputies and escalation routes.
3. **Set minimum evidence.** Require demand dimensions, business dates, normal/peak/recovery profiles, assumptions, evidence timestamps, viable alternatives, and option deadlines. An evidence record must say what it does not establish.
4. **Embed checkpoints.** Add capacity questions to business case, architecture, procurement, material-change, and launch reviews. Require refreshed evidence when assumptions change. Preserve existing release and investment authority.
5. **Define commitment controls.** Before acquisition, name the consumer, technical and commercial owners, scope, funding, conditions, and exit criteria. Reconcile assignments, actual use, and renewal or release throughout the lifecycle.
6. **Create bounded exceptions.** Record the guardrail deviation, alternatives considered, affected services, compensating controls, risk acceptor, expiry, and revalidation plan. Expired exceptions require a new decision or a change of action.
7. **Connect six neighboring practices.** Share economic options with FinOps, the technology financial-management practice; patterns with architecture; operational signals with reliability; recovery scenarios with continuity; terms with procurement; and priority conflicts with portfolio planning.
8. **Test the workflow.** Walk one normal request, one urgent deadline, and one exception through the controls. Verify that the appropriate authority receives the evidence in time and that decisions reach the implementing team.
9. **Inspect outcomes and adjust.** Review actual bypasses, delays, stale evidence, and incidents. Remove redundant approvals and correct failed controls with an owner and a verification test.

## Worked fictional example

A fictional product team changes from a general resource family to a specialized family after its original design approval. The old approval does not cover the new demand.

A material-change guardrail sends the revised profile to architecture for suitability and platform engineering for scoped acquisition evidence. Procurement confirms terms if an obligation is needed. The business owner chooses whether to preserve the launch date by reducing initial scope. If the organization permits an exception, its risk authority records the exact gap, compensating action, expiry, and stop condition.

The practice lead facilitates these handoffs but cannot approve the commercial obligation or accept the service's recovery risk. The result is an updated delivery decision, not merely a completed governance checklist.

## Exit and review criteria

Governance is established when scoped teams can show actual decisions passing through the controls, acknowledged owners, usable evidence requirements, tracked exceptions, and verified handoffs. Publishing a policy alone is not enough.

Review after incidents, repeated exceptions, changes in delegated authority, or the strategic review cycle. Use organization-defined measures such as overdue decisions or expired exceptions, with clear scope and denominator. Do not claim that governance eliminates capacity constraints.

## Common mistakes

- Adding a late approval after architecture and contracts can no longer change.
- Requiring the same evidence burden for every routine request.
- Treating a service-catalog entry, quota approval, forecast, financial discount, or multi-region design as deployability proof.
- Requiring indefinite exceptions without renewal decisions.
- Automating approvals before their evidence rules and authority boundaries are stable.

## Related content

- [Governance principles and guardrails](../operating-model/governance.md)
- [Roles and responsibilities](../operating-model/roles-and-responsibilities.md)
- [Decision record template](../templates/decision-record.md)
- [Manage capacity commitments](manage-capacity-commitments.md)
