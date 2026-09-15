# Capacity demand template

Copy these tables for each Capacity Operations (CapOps) demand submission. Replace the prompts, give the submission a stable identifier, and preserve versions when dates or quantities change. Use `unknown` with an investigation owner rather than leaving a decision-critical field silently blank. Link confidential evidence in an approved system; do not paste it into a public copy.

## Business context and ownership

| Field | Entry |
|---|---|
| Demand identifier and version | Stable identifier, version, and change date |
| Workload and profile reference | Service name and link to owned workload profile |
| Business owner and technical contact | Names, authority, and deputies |
| Business outcome and demand driver | Milestone plus transactions, users, data, or other sizing driver |
| Required date and critical period | Date, time zone, business window, and consequence of delay |
| Priority and business consequence | Locally defined criticality and impact of reduced or delayed service |
| Demand horizon | Near, medium, or long; record the locally defined date range |
| Permitted flexibility | Approved changes to quantity, schedule, family, service pattern, or location |
| Non-negotiable constraints | Location, regulatory, performance, dependency, or operational restrictions |
| Previous submission superseded | Reference and explanation of the change; avoid duplicate demand |

## Technical demand slices

Repeat a row for each compatible service-family-location-time slice. Do not combine different units or assume equal unit counts imply equivalent performance.

| Slice identifier | Scenario | Service and family | Quantity and unit | Location and zone constraints | Start, ramp, and duration | Total or incremental | Sizing evidence |
|---|---|---|---|---|---|---|---|
| Enter slice | Normal, peak, recovery, or named combined scenario | Exact technical shape | Number or range with unit | Primary and permitted scope | Dates and growth steps | State relationship to baseline | Test or model reference and observed date |

## Assumptions and dependencies

| Item | Assumption or requirement | Evidence and date | Overlap or dependency | Owner and validation action |
|---|---|---|---|---|
| Baseline and business translation | Usage baseline and conversion model | Reference, period, and limitations | Resources included or excluded | Named owner and next check |
| Peak | Uplift and duration; total or incremental | Test or business-plan reference | Can it overlap recovery or migration? | Named owner |
| Recovery | Restoration phases and separate destination profile | Recovery-profile reference | Concurrent services and destination resident load | Continuity and dependency owners |
| Retirement or migration | Units added, retained temporarily, or removed | Approved retirement or wave plan | Conditions before subtracting demand | Named owner and deadline |
| Uncertainty | Scenario range and confidence rationale | Supporting observation | Factors that would invalidate sizing | Evidence owner |
| Alternative | Family, location, service pattern, schedule, or reduced demand | Validation status and cost reference | Prerequisites and implementation lead time | Technical and business authorities |

## Supply-posture evidence

| Evidence type | Scope and quantity | Reference and observed date | Conditions or exclusions | Freshness rule and next check |
|---|---|---|---|---|
| Quota permission | Applicable administrative scope | Limit and request outcome | Permission only; not physical capacity | Date or event trigger |
| Financial obligation | Eligible economic scope | Terms and approval reference | Do not infer deployable entitlement | Commercial review |
| Capacity mechanism | Exact eligible family, location, dates, and quantity | Current terms and mechanism reference | Documented conditions and remaining prerequisites | Technical and commercial refresh |
| Allocation and deployment | Assigned consumer and observed request scope | Ledger and deployment result | Observation applies to its tested time and scope | Operational trigger |

## Decision handoff

| Field | Entry |
|---|---|
| Material gap and risk reference | What remains unestablished and its business consequence |
| Recommended option | Rationale, alternatives, and residual risk |
| Last responsible decision deadline | Option-specific date and lead-time calculation |
| Decision authority and requested action | Who may approve, change, hold, or accept the stated risk |
| Implementation owner and due date | Who acts after approval |
| Acceptance evidence | What must be observed before the action or risk closes |
| Review trigger and next review | Demand change, stale evidence, deadline, or scheduled review |
| Business and technical validation | Names, dates, scope, and unresolved disagreements |

A forecast, quota, financial discount, or service listing is not a capacity guarantee. If using “secured,” state the mechanism, exact conditions, and residual limitations.

## Related content

- [Build a demand forecast](../implementation/build-a-demand-forecast.md)
- [Workload capacity profile](workload-capacity-profile.md)
- [Capacity-risk register](capacity-risk-register.md)
