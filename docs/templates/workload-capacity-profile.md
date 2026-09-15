# Workload capacity profile

Use this Capacity Operations (CapOps) profile as the maintained reference for one workload, not a single request. Copy all tables, replace prompts, and link demand versions, risks, and decisions. Keep normal, peak, and recovery rows separate. Repeat technical rows for each resource dimension and time slice; a profile is not complete merely because compute is documented.

## Context and authority

| Field | Entry |
|---|---|
| Profile identifier, version, and updated date | Stable reference and change history |
| Workload and business service | Name, outcome, and supported business process |
| Business owner and deputy | Authority for priority, milestones, and business-risk acceptance |
| Technical, platform, and operations owners | Named contacts and decision boundaries |
| Continuity and commercial owners | Recovery authority, budget or contract authority, and references |
| Criticality and consequence | Organization-defined classification and impact of disruption |
| Milestones and critical periods | Required dates, time zone, launches, migrations, and peaks |
| Placement constraints | Permitted regions or zones, regulatory restrictions, and rationale |
| Service and recovery objectives | Performance requirement, recovery time objective, and recovery point objective |
| Related records | Demand, architecture, forecast, risks, decisions, and commitments |

## Scenario demand

| Slice identifier | Profile | Service and resource family | Quantity and unit | Location | Required window, ramp, duration | Sizing and performance evidence | Total, incremental, and overlap rules |
|---|---|---|---|---|---|---|---|
| Normal slice | Normal | Exact shape | Baseline or range | Primary scope | Ongoing and planned changes | Reference, test conditions, date | Define baseline |
| Peak slice | Peak | Exact shape | Peak total or explicit uplift | Required scope | Start, ramp, end | Business driver and validation | State whether peak can overlap recovery |
| Recovery slice | Recovery | Exact shape | Phase-specific requirement | Destination scope | Restore, rebuild, and steady recovery periods | Recovery-profile reference | Include overhead or link separate rows |

## Dependency and concurrency map

| Dependency | Owner | Required resource, limit, or capability | Normal and peak demand | Recovery requirement and restoration order | Shared consumers and correlated event | Evidence, date, and gap |
|---|---|---|---|---|---|---|
| Enter dependency | Named owner | Compute, storage, network, identity, data, or other dependency | Quantity and unit or readiness condition | Include rebuild and rollback needs | Which workloads compete at the same time? | Reference and scope limitations |

## Flexibility and lifecycle changes

| Option or change | Permitted business outcome | Technical and location suitability | Validation evidence and date | Implementation and validation lead time | Latest decision date | Owner and status |
|---|---|---|---|---|---|---|
| Alternative placement or family | What may change and what may not | Tested equivalence and constraints | Tested, partly tested, or unvalidated | Evidence-backed estimates | Calculated from required date | Technical and business owners |
| Migration or retirement | Temporary coexistence or confirmed demand removal | Dependencies and cleanup criteria | Approved plan and completion evidence | Ramp and decommissioning period | Deadline for preserving options | Delivery owner |

## Capacity posture

| Dimension or claim | Exact scope and quantity | Evidence reference and observed date | Conditions and exclusions | Owner | Next refresh |
|---|---|---|---|---|---|
| Quota | Administrative permission scope | Limit observation or request result | Does not prove physical supply | Platform owner | Date or event |
| Financial commitment | Eligible economic scope and term | Contract and approval | Does not imply deployable entitlement | Commercial owner | Review date |
| Capacity entitlement | Family, location, period, quantity | Current terms and mechanism status | Prerequisites, restrictions, and residual risk | Technical owner | Change or expiry trigger |
| Assignment and consumption | Named consumers, assigned and used quantities | Ledger and observation | Shared or protected use | Platform and consumer owners | Reconciliation date |
| Deployment validation | Exact tested request | Outcome and test date | Scope and time limitations | Operations owner | Material-change trigger |

## Decisions and review

| Gap or decision | Business consequence | Risk and decision references | Authority | Action, owner, and due date | Closure evidence | Revisit trigger |
|---|---|---|---|---|---|---|
| Enter item | Milestone or service exposure | Linked records | Named risk or decision authority | Specific action | Test or observed outcome | Changed demand, evidence expiry, incident, or scheduled review |

“Secured” must be conditional and traceable. Forecasts, quota, financial discounts, service catalogs, multi-region design, and recovery architecture alone do not establish deployable capacity.

## Related content

- [Review critical workloads](../implementation/review-critical-workloads.md)
- [Capacity demand submission](capacity-demand-template.md)
- [Recovery-capacity profile](recovery-capacity-profile.md)
