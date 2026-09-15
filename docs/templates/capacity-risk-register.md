# Capacity-risk register template

Copy the index and one detail set per Capacity Operations (CapOps) risk. Use stable identifiers to connect demand, dependencies, decisions, and mitigations. Record an uncertain event and business consequence, not simply “capacity issue.” Replace prompts; label unknowns with an evidence owner and next action.

## Register index

| Risk identifier | Workload or shared dependency | Uncertain event | Business consequence and required date | Criticality and rationale | Risk owner | Next decision deadline | State and next review |
|---|---|---|---|---|---|---|---|
| Enter identifier | Profile and affected consumers | If this event occurs | Then this outcome is exposed by this date | Local assessment; include uncertainty | Named internal owner | Date and linked option | Investigating, mitigating, accepted, realized, or closed; review date |

## Risk detail

| Field | Entry |
|---|---|
| Risk identifier and version | Link to index and change history |
| Demand and scenario | Normal, peak, recovery, or named combined scenario; demand version |
| Technical scope | Service, family, quantity and unit, location or zone, dates, ramp, and duration |
| Business impact | Delivery, service, continuity, financial, or regulatory consequence |
| Facts and evidence | Source references, observed dates, scope, and limitations |
| Assumptions and unknowns | What has not been established; owner and validation action |
| Evidence freshness | Validity rule, next check, and invalidating changes |
| Correlated risks | Shared pool, destination, dependency, or competing portfolio demand |
| Local risk assessment | Impact and likelihood method, rationale, confidence, and criticality |
| Business risk acceptor | Named authority and delegated boundary; not automatically the practice lead |
| Residual exposure | What remains after the proposed mitigation |

## Options and decision timing

| Option | Feasibility evidence | Cost and business trade-off | Acquisition or implementation lead time | Validation time and uncertainty allowance | Last responsible decision deadline | Authority |
|---|---|---|---|---|---|---|
| Acquire, change, phase, defer, or accept | Exact scope, assumptions, and evidence date | Include obligations and consequence of doing nothing | Estimate and source | Locally justified planning assumptions | Required date minus all applicable lead time | Named decision maker |

## Mitigation and closure

| Action | Owner | Due date | Decision reference | Acceptance evidence | Result and observed date | Residual risk and next review |
|---|---|---|---|---|---|---|
| Specific mitigation or investigation | Named executor | Before relevant deadline | Approval and conditions | Test or result needed to close | Completed, failed, partial, or pending; reference | Remaining exposure and owner |

| Acceptance or closure field | Entry |
|---|---|
| Accepted risk and rationale | Exact scope and why alternatives were not chosen |
| Approver, date, and expiry | Authority and time-bounded acceptance |
| Escalation trigger | Deadline, missing evidence, changed demand, or breached condition |
| Closure decision | Evidence that the exposure ended or closure test passed |
| Reopen trigger | Material change or invalidated evidence |

Do not infer physical availability from quota or a forecast. A financial obligation, service listing, multiple regions, or recovery design does not close a deployability gap. Accepted risk is still risk; a completed request is not automatically a verified mitigation.

## Related content

- [Create a risk register](../implementation/create-a-capacity-risk-register.md)
- [Decision record](decision-record.md)
- [Recovery-capacity profile](recovery-capacity-profile.md)
