# CapOps scorecard template

Use this Capacity Operations (CapOps) scorecard to support decisions, not to produce a single maturity or readiness rating. Copy the catalog and one definition table per selected measure. Replace prompts and remove measures that do not drive an action. Every target, freshness interval, and escalation threshold is organization-defined; no example below is an industry benchmark.

## Reporting context

| Field | Entry |
|---|---|
| Scorecard identifier, version, and period | Reporting window, time zone, and evidence cut-off |
| Scope | Business units, workloads, services, families, locations, and scenarios |
| Operational audience | People who investigate, allocate, validate, or execute |
| Executive audience | Authorities who resolve business, portfolio, funding, or residual-risk decisions |
| Consolidation owner and source owners | Names; consolidation does not transfer source accountability |
| Known coverage and freshness gaps | Missing or stale sources and their investigation owners |

## Suggested measure catalog

Choose measures that fit the assessed scope. Operational and executive views should link to the same underlying records.

| Measure | Audience and decision | Definition starting point | Evidence source | Interpretation guardrail |
|---|---|---|---|---|
| Decisions made before their last responsible deadline | Operational and executive: improve timing or escalate authority gaps | Count of due decisions made by their option deadline divided by all decisions due in the period | Decision records and option lead-time calculations | Preserve missed and unresolved decisions in the denominator; explain changed deadlines |
| Demand with matching documented capacity-mechanism coverage | Operational: acquire, validate, or change a scenario | For one compatible time-location-family-unit slice, matched eligible quantity divided by required quantity | Demand, mechanism terms, and non-duplicated allocation ledger | Report conditions, outstanding prerequisites, overlap rules, and unknowns; not an unconditional availability percentage |
| Milestones with unresolved capacity exposure | Executive: phase, fund alternatives, defer, or accept risk | Count and business consequence of in-scope milestones with open material gaps | Forecast, business plans, and risk register | Define materiality locally; do not equate risk count with probability |
| Capacity-related deployment failures | Operational: investigate scoped errors and correct assumptions | Count of investigated capacity-related failed attempts and, if useful, rate over defined relevant attempts | Request results and reviewed incident categorization | Separate quota, configuration, and physical-capacity evidence; deduplicate retries consistently |
| Unused commitment or allocation exposure | Operational and commercial: retain, reassign, or release | Unused assigned quantity or continuing financial obligation, reported separately by compatible unit and period | Commitment, allocation, consumption, and approved financial records | Idle can support peaks or recovery; technical release is not automatically a saving |
| Recovery scenarios with current validation evidence | Operational and executive: test, protect, sequence, or accept a gap | Count of in-scope scenarios meeting locally defined validation and freshness criteria, with total scenarios shown | Recovery profiles, test scope, results, and exclusions | Partial tests and concurrent portfolio gaps remain visible; no future capacity guarantee |
| Overdue mitigation actions and expired exceptions | Operational and executive: execute, escalate, or obtain a new decision | Count by criticality, due date, and business impact | Risk, action, and exception records | Do not close an action without acceptance evidence or silently extend an exception |
| Stale or missing critical evidence | Operational: refresh or qualify a decision | Count of required evidence items outside local validity rules or missing, with total required items | Evidence register and workload profiles | Unknown is not green and does not prove either availability or shortage |
| Forecast deviation by scenario | Operational: revise drivers, sizing, or dates | Locally specified comparison of actual demand with the matching forecast version and scenario | Demand versions and observed use | Define units, date shifts, zero demand, and changed resource families before computing a rate |

## Definition and current result: copy per measure

| Field | Entry |
|---|---|
| Measure identifier and name | Link to selected catalog entry or a locally defined measure |
| Business question and resulting decision | What someone will do differently when it changes |
| Accountable measure owner | Named authority for interpretation and action |
| Source owner and collection method | Producing system, approved reference, and reconciliation process |
| Population and scenario | Workloads, family, location, period, and normal, peak, or recovery scope |
| Numerator or measured quantity | Reproducible rule and compatible unit |
| Denominator, if applicable | Complete population; explicitly not applicable for a count |
| Exclusions and deduplication | Shared allocations, retries, overlap, missing records, and scope boundaries |
| Observed period and collection date | When the result applies and when collected |
| Freshness rule and next refresh | Locally justified interval and invalidating events |
| Current value and data completeness | Value plus unknown or stale portion; do not replace missing data with zero |
| Comparison value and comparability | Prior period or scenario; explain changes in scope or definition |
| Organization-defined target and rationale | Chosen value, decision authority, and business reason |
| Escalation threshold and action | Locally chosen condition, recipient, and deadline |
| Evidence limitations | What the measure cannot establish |
| Next definition review | Trigger to revise or retire a misleading measure |

## Decision and follow-through log

| Measure and observed change | Business interpretation | Decision required | Authority and deadline | Action owner | Verification evidence and next review |
|---|---|---|---|---|---|
| Identifier, value, and date | Scope, uncertainty, and affected outcome | Specific choice | Named authority and latest decision date | Named executor | Observable result and revisit trigger |

Do not average measures or maturity levels to hide critical weaknesses. A forecast, quota approval, financial discount, service listing, multiple regions, or recovery design is not a substitute for appropriately scoped deployment and mechanism evidence.

## Related content

- [Reporting and key performance indicators](../capabilities/reporting-and-kpis.md)
- [Run a monthly review](../implementation/monthly-capops-review.md)
- [Maturity assessment](maturity-assessment.md)
