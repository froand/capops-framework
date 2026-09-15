# Run a monthly CapOps review

A monthly Capacity Operations (CapOps) review reconciles demand, evidence, risks, and obligations to make decisions that cannot be resolved by routine operations. It does not replace incident response, release authority, or portfolio governance. This guide turns the [capacity-review model](../operating-model/capacity-review.md) into an executable review.

## Prerequisites

- Current workload profiles, forecast versions, risk register, and commitment records.
- Named evidence owners and the authorities needed for the decisions on the agenda.
- Previous decisions, outstanding actions, exceptions, and closure evidence.
- Agreed local freshness rules and reporting definitions.

Use the [monthly review template](../templates/monthly-review-template.md). Choose preparation and publication lead times that fit the organization's decision deadlines; no fixed meeting length or participant count is required.

## Steps and evidence

1. **Triage before the meeting.** Identify incidents and deadlines that cannot wait. Send them to the existing urgent authority immediately. Carry the outcome into the shared record.
2. **Collect changes, not entire status histories.** Ask business owners to validate changes in dates, quantities, priorities, retirements, and scenario assumptions. Ask technical and commercial owners to refresh matching evidence.
3. **Reconcile the records.** Match demand to service, family, quantity, location, and time. Check quota separately from capacity entitlement, assignments separately from consumption, and financial obligations separately from deployment evidence. Flag stale or missing evidence.
4. **Prepare decision items.** For each item, state the business consequence, required decision, feasible options, recommendation, cost or obligation implications, residual risk, decision authority, and last responsible decision deadline.
5. **Review previous actions.** Accept closure only when its evidence test passed. Reopen mitigations whose assumptions failed; update the forecast and risks rather than repeatedly carrying “in progress.”
6. **Decide in priority order.** Start with approaching deadlines and critical exposure, then allocation conflicts, acquisition or release choices, recovery gaps, and practice improvements. Do not rank only by utilization or cost.
7. **Record the authority's outcome.** Capture approval, change, hold, exception, or escalation. Separate technical approval, commercial approval, and business risk acceptance when they belong to different authorities. A missing approver is a block, not implied consent.
8. **Publish two views.** Operational teams receive scoped actions, evidence links, owners, due dates, and record changes. Executives receive business milestones exposed, portfolio conflicts, residual risks, and decisions requiring their authority.
9. **Verify follow-through.** Confirm receiving owners acknowledge actions. Review outcomes at the next material trigger or review; do not wait a month to discover that an option's deadline has passed.

## Suggested decision order

| Review segment | Question to answer |
|---|---|
| Demand and milestone changes | Must the forecast, priority, placement, or delivery scope change? |
| Material risks | Which option must be chosen before its implementation window closes? |
| Commitments and allocations | Acquire, retain, assign, reassign, renew, amend, or release under whose authority? |
| Recovery and shared dependencies | Does concurrent demand require protection, restoration sequencing, or business acceptance? |
| Incidents and previous actions | Did mitigation work, and which assumption or control must change? |
| Practice health | Which evidence or ownership gap is most important to fix next? |

## Worked fictional example

A fictional launch moves forward by three weeks. Its preferred technical option now requires a decision before the next monthly review. Separately, an allocation report shows ten idle units in a matching family.

Reconciliation finds that six of those units support a scheduled recovery exercise and four have no approved future consumer. The review does not assume all ten are free. The platform authority evaluates reassignment of four; the business owner chooses a phased launch for the remainder; the commercial authority evaluates any new obligation independently. The recovery owner retains the six pending validation. These quantities are illustrative.

The executive summary describes the changed launch scope and remaining exposure. The operational record names the four-unit reassignment, compatibility checks, execution owner, due date, and verification evidence.

## Exit and review criteria

Every due decision has an outcome or an explicitly owned escalation. Actions have owners, dates, and closure tests. Forecast, risks, commitments, and exceptions reflect the decisions. Missing evidence remains visible rather than being converted into a positive coverage indicator.

Evaluate review quality using organization-defined measures such as timely decisions, overdue actions, stale evidence, or recurring unresolved conflicts. Define scope, denominator, and exclusions; attendance is not evidence of effectiveness.

## Common mistakes

- Reading dashboards aloud without a decision question.
- Presenting all idle allocations as releasable.
- Reporting an overall “secured” percentage without scenario, dimensions, mechanism conditions, and denominator.
- Treating a forecast or quota approval as proof of physical capacity.
- Deferring urgent decisions because the agenda is full.

## Related content

- [Monthly review template](../templates/monthly-review-template.md)
- [Operating cadence](../operating-model/operating-cadence.md)
- [CapOps scorecard template](../templates/capops-scorecard.md)
- [Decision record template](../templates/decision-record.md)
