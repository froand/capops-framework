# Monthly review template

Copy these tables for each monthly Capacity Operations (CapOps) review. Link the maintained records rather than duplicating their full contents. Replace prompts with evidence and decisions. Remove unused example rows, not required checks. Escalate urgent items before the meeting if their decision deadlines cannot wait.

## Review context

| Field | Entry |
|---|---|
| Review identifier, date, and observation period | Stable reference, time zone, and evidence cut-off |
| Scope and forecast versions | Workloads, locations, scenarios, and versions considered |
| Facilitator and record owner | Practice steward and publication owner |
| Decision authorities and deputies | Required business, technical, commercial, release, or continuity authorities |
| Evidence freshness and gaps | Local rule, stale sources, unknowns, and assigned investigations |
| Previous review and urgent decisions | Links and changes already decided through incident or deadline escalation |

## Decisions required and outcomes

| Decision identifier and question | Business consequence and scope | Evidence and freshness | Options and recommendation | Authority | Last responsible decision deadline | Outcome and conditions |
|---|---|---|---|---|---|---|
| Enter decision | Workload, scenario, service, family, quantity, location, date | References and material limitations | Feasible options and trade-offs | Named approver | Option-specific date | Approve, change, hold, exception, or escalate; link record |

## Demand changes

| Workload and demand version | Previous scenario demand | New scenario demand | Business reason | Effective window and ramp | Retirement or overlap assumptions | Owner validation |
|---|---|---|---|---|---|---|
| Profile reference | Quantity, unit, family, location, period | Same dimensions or explicit change | Launch, growth, peak, recovery, or retirement | Dates and duration | Concurrent demand and dependencies | Name, date, and outstanding gaps |

## Risks, commitments, and recovery

| Record reference | Material change or gap | Business exposure | Evidence and scope | Choice required | Authority and deadline | Resulting action |
|---|---|---|---|---|---|---|
| Risk record | Changed event, assumption, or mitigation | Milestone and residual risk | Source and observed date | Mitigate, investigate, or accept | Named authority and date | Owner, due date, closure test |
| Commitment record | Acquired, unassigned, idle, expiring, or incompatible | Obligation and consumer effect | Terms, assignment, consumption | Retain, assign, reassign, amend, renew, or release | Commercial or technical authority | Owner and verification |
| Recovery profile | Concurrent demand or validation gap | Affected business functions | Scenario, test scale, exclusions, date | Protect, sequence, test, change objective, or accept | Continuity or business authority | Owner and verification |
| Exception record | New, changed, or expiring deviation | Residual exposure | Conditions and compensating controls | Close, replace, or seek new approval | Risk authority and expiry | Action and revisit trigger |

## Follow-through and incident learning

| Action or finding | Previous decision | Executor | Due date | Evidence required for closure | Observed result | Reopen or escalation trigger |
|---|---|---|---|---|---|---|
| Specific action | Linked authority and conditions | Named owner | Date | Test or verified record change | Pending, partial, failed, or verified; reference | Changed assumption, failed test, or missed deadline |

## Operational and executive reporting

| Audience | Content to publish | Evidence and decision links | Owner and publication date |
|---|---|---|---|
| Operational teams | Scoped gaps, allocation changes, errors, freshness issues, obligations, and actions with deadlines | Detailed records and acceptance tests | Named owner |
| Executives and portfolio authorities | Milestones exposed, conflicting priorities, continuity gaps, residual risks, and funding or sequencing decisions | Short decision briefs with traceable supporting evidence | Named owner |

Any scorecard measure needs an organization-defined target, explicit scope, denominator where applicable, and data freshness. A “secured” total without mechanism conditions and demand dimensions must not be used as readiness proof.

## Related content

- [Run a monthly review](../implementation/monthly-capops-review.md)
- [Decision record](decision-record.md)
- [CapOps scorecard](capops-scorecard.md)
