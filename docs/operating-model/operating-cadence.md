# Operating cadence

The Capacity Operations (CapOps) cadence is a set of decision opportunities, not a calendar of status meetings. Monitoring and shared records carry routine status. Human attention is reserved for choices, conflicting priorities, expiring assumptions, and risk acceptance. The [operating model](operating-model.md) supplies the owners; this page connects their decisions to triggers.

## Seven review types

| Review type and trigger | Evidence to bring | Intended decisions | Authority and recorded result |
|---|---|---|---|
| **Continuous monitoring**: ongoing signals and material change events | Dimension-specific consumption, allocation, quota, deployment failures, stale evidence, commitment expiry, and forecast deviation | Investigate a failed request; reclaim or protect an allocation; invoke an incident response; refresh a forecast; escalate a deadline | Service operations within delegated guardrails; action or incident record with owner and urgency |
| **Monthly CapOps review**: recurring reconciliation of demand and supply posture | Demand changes, risks approaching decision deadlines, options, allocation and commitment exceptions, recovery gaps, and previous action evidence | Prioritize mitigations; approve an in-scope allocation change; select an acquisition recommendation; release idle obligations where authorized; escalate unresolved trade-offs | Existing operational or delivery authorities; decision log, updated risks and forecast, action dates |
| **Quarterly strategic capacity review**: portfolio and investment planning, with earlier review for material changes | Near-, medium-, and long-horizon scenarios, concentration and legacy-family dependencies, commercial exposure, continuity scenarios, and maturity gaps | Sequence the portfolio; fund flexibility or modernization; adjust investment and sourcing assumptions; change guardrails; set capability improvement priorities | Sponsor and portfolio or investment authorities; strategic decisions and revised planning assumptions |
| **Project-stage capacity checkpoints**: business case, design, procurement, and delivery changes | Current demand version, placement constraints, technical validation, mechanism terms, acquisition lead time, evidence freshness, and residual risk | Proceed, change design or scope, defer an obligation, or require an expiring exception before moving to the next stage | Existing stage-gate authority with relevant domain approvals; checkpoint decision and conditions |
| **Migration and launch readiness reviews**: before irreversible cutover, launch, or expansion | Actual deployment evidence, current limits, exact resource and location match, tested alternatives, rollback demand, dependencies, and recovery posture | Go, phase, reduce scope, move the window, or hold; define rollback and abort conditions | Existing release authority; time-scoped readiness decision with named execution owner |
| **Recovery-capacity validation**: continuity schedule, architecture changes, or material destination-demand changes | Normal, peak, and recovery profiles; concurrent portfolio scenarios; restoration order; test scope and results; shared destination contention | Accept the tested scope, modify restoration order, protect capacity, change recovery objectives through business approval, or register an unvalidated gap | Business continuity and service authorities for acceptance, reliability owner for test result; recovery profile and decisions |
| **Post-incident review**: capacity-related failure, near miss, or recovery exercise finding | Request errors and scope, actual demand, evidence available before the event, decision history, lead times, and response outcomes | Correct an assumption; change a guardrail; retire an ineffective alert; improve a control; revalidate before closing learning actions | Incident and affected service owners; evidence-backed corrective actions and a verification review |

Reviews may be asynchronous or combined with existing forums if the right authority can decide in time. Recovery validation includes practical tests or explicitly bounded evidence review, not merely reading an architecture document.

## Let the decision deadline override the calendar

The **last responsible decision deadline** is the latest time an option can be chosen while its implementation and validation can still finish before the business need. Derive it from the required date, evidenced acquisition or change lead time, validation time, and a locally chosen uncertainty allowance. Record which option the deadline applies to; alternatives can have different deadlines.

For a fictional launch, an alternative design needs six weeks of engineering and two weeks of validation. If the launch is eight weeks away, the design decision is due now, not at next month's review. These durations are illustrative planning assumptions, not recommended thresholds. If the deadline has passed, explicitly choose a changed milestone, a remaining feasible option, or authorized risk acceptance; do not keep the item in a routine status queue.

## Prepare once, decide at the right level

The evidence owner updates the shared record before review. The practice lead checks for a clear question, viable options, recommendation, decision authority, and evidence freshness. Participants should read the changes rather than hear every team narrate a report.

Conclude each review with:

- A recorded decision or an explicit reason a decision remains blocked.
- An owner for every action, its due date, and the evidence required to close it.
- Updated business impact and residual risk.
- An escalation path if missing evidence or authority threatens the deadline.
- A next review date or event trigger.

## Review the cadence itself

Use locally defined measures such as decisions made before their deadlines, overdue mitigation actions, recurring stale evidence, and decisions reopened because assumptions were wrong. Explain the denominator and scope before comparing teams. Do not infer better capacity outcomes from a larger number of reviews.

Common failures are waiting for the monthly meeting during an incident, using quarterly planning to approve an urgent release, and treating a successful test as permanent recovery assurance.

## Related content

- [Capacity review](capacity-review.md)
- [Run a monthly review](../implementation/monthly-capops-review.md)
- [Validate recovery capacity](../implementation/validate-recovery-capacity.md)
- [CapOps scorecard template](../templates/capops-scorecard.md)
