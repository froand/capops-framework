# Capacity-constrained prioritization

Use this scenario to allocate a finite capacity pool transparently when not every proposed project can proceed at once. Fairness requires explicit criteria, evidence, and an appeal path, not simply equal shares or first arrival.

## Business context

A fictional organization has three projects competing for one qualified compute pool. A mandatory records change, a commercial pilot, and a modernization initiative all have sponsors. The executive portfolio owner must choose which work proceeds and who owns the business consequences of deferral.

All quantities, dates, and priority criteria below are illustrative organizational choices, not recommended universal ranking rules.

## Capacity challenge

The pool is already partly allocated to production and continuity. Additional quota or budget cannot create physical supply inside it. Project sponsors report preferred allocations without distinguishing minimum useful capacity, peak duration, or which work can run sequentially.

## Demand dimensions

| Allocation or request | Example profile |
| --- | --- |
| Qualified pool | 120 compatible worker units in an approved location; current evidence is time-scoped |
| Existing production | 80 units that cannot be displaced without service-owner approval |
| Continuity allocation | 20 units assigned against simultaneous recovery assumptions; not routinely available to projects |
| Project pool | 20 remaining units, with matching storage and network prerequisites checked separately |
| Mandatory records change | 12 units for two weeks before an internally approved control deadline |
| Commercial pilot | 18 units preferred for four weeks; launch can be deferred with sponsor acceptance |
| Modernization initiative | 16 units preferred; an eight-unit sequential phase is technically useful but takes longer |
| Timing and placement | Shared demand begins 2027-03-08; alternatives require a different qualified location or later window |

The three preferred project requests total 46 units. The 20-unit project pool cannot satisfy them concurrently; allocations must not hide this gap.

## Important assumptions

- Worker units are comparable only after configuration and dependency compatibility checks.
- Continuity headroom has an owner and cannot be borrowed by silently excluding portfolio recovery.
- The mandatory deadline has evidence; an urgent label alone is insufficient.
- Modernization's smaller phase produces a useful outcome rather than stranding half a job.
- Forecasts, quota increases, and discussions about future capacity are not accepted additions to the current pool.

## Relevant CapOps capabilities

- **Capacity allocation:** apply eligibility, priorities, time limits, and reclaim rules.
- **Capacity governance:** establish who can approve conflicts and exceptions.
- **Capacity risk management:** quantify the consequence and owner of each deferral.
- **Capacity forecasting:** identify later windows and avoid duplicate requests.
- **Capacity optimization:** remove idle allocations and sequence useful work without weakening continuity.

## Recommended actions

1. Reconcile the pool against production, maintenance, and simultaneous recovery demand. Record configuration-specific usable capacity and evidence date.
2. Ask each sponsor for minimum useful demand, preferred demand, timing, dependencies, deferral impact, and willingness to accept a smaller phase.
3. Publish locally agreed criteria before ranking: mandatory obligations, existing service impact, business value, readiness, reversibility, and waiting time. Record weights and evidence if a scoring model is used.
4. Review the result with affected owners. Do not let a numerical score conceal a critical dependency or an unsupported deadline.
5. Allocate 12 units to the records change and eight to a useful modernization phase; defer the commercial pilot in this example. Document consequences, owners, and an appeal deadline.
6. Make allocations time-bounded. Reclaim unused project capacity after notice, review repeated deferrals for starvation, and rerun the decision when evidence or priorities change.

## Potential alternatives

Delay all projects until more qualified supply exists, buy or qualify another pool, shorten a pilot, or sequence the records change before the commercial launch. Borrowing continuity capacity is a separate explicit risk decision, not a routine optimization. Equal shares can be unfair if no project can produce a useful result with its share.

## FinOps considerations

Compare the opportunity cost of delay with alternative capacity expense, engineering work, and any stranded financial commitment. A project that can pay more does not automatically outrank a mandatory obligation. Charge allocation should not incentivize teams to hoard resources or exaggerate forecasts.

## Residual risks

The delayed pilot may lose commercial value. The records work may overrun, and repeatedly favoring urgent work can starve modernization. New evidence can invalidate either the pool estimate or the business ranking, requiring a visible revised decision.

## Common mistakes

- Treating the full 120 units as available to new projects.
- Ranking by executive influence or request arrival without an agreed policy.
- Splitting capacity equally even when the fragments are unusable.
- Keeping allocations after a project is no longer ready to consume them.
- Converting speculative supply into promised delivery dates.
- Accepting repeated deferral without reviewing fairness and cumulative business harm.

## Example decision record

| Field | Illustrative record |
| --- | --- |
| Decision | Allocate 12 units to the records change and eight to phased modernization; defer the 18-unit pilot request |
| Accountable owner | Executive portfolio owner; each project sponsor accepts its revised scope or delay |
| Decision deadline | 2027-03-01; evidence-based appeals due by 2027-03-03 |
| Evidence required | Dated allocation ledger, recovery concurrency profile, project minimums, obligation evidence, readiness checks, and documented ranking rationale |
| Trade-off | Preserve production and continuity allocations while accepting commercial delay and slower modernization |
| Residual risk accepted | Lost pilot opportunity and possible records-work overrun; named sponsors retain these risks |
| Revisit | Weekly, on a missed start or completion, or when another qualified allocation becomes available |
| Release condition | Project allocations expire after two weeks unless renewed through the same visible process |

## Related content

- [Capacity allocation](../capabilities/capacity-allocation.md)
- [Capacity governance](../capabilities/capacity-governance.md)
- [Capacity-risk register](../templates/capacity-risk-register.md)
- [Disaster recovery](disaster-recovery.md)
