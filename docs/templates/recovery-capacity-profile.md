# Recovery-capacity profile template

Copy this Capacity Operations (CapOps) profile for each material failure scenario and affected workload group. Keep it linked to normal and peak profiles. Replace prompts and repeat demand rows for every restoration phase and resource dimension. Label partial tests and unvalidated assumptions; a completed form is not recovery readiness.

## Scenario and authority

| Field | Entry |
|---|---|
| Profile identifier, version, and updated date | Stable reference and history |
| Failure scenario | What is unavailable, what survives, and why workloads recover together |
| Affected workloads and business functions | Service profiles, criticality, and minimum acceptable degraded service |
| Business owner and risk acceptor | Authority for recovery objectives and residual-risk acceptance |
| Continuity owner and test execution owner | Named responsibilities and deputies |
| Primary and recovery locations | Permitted regions or zones and restrictions |
| Recovery time objective | Approved restoration time and reference; not a capacity quantity |
| Recovery point objective | Approved acceptable data loss and reference |
| Restoration order and dependencies | Required sequence and parallel work; dependency owners |
| Peak overlap assumption | Whether the event can coincide with source or destination peak demand |
| Related demand, decisions, and commitments | Stable references and versions |

## Phase-specific technical demand

| Slice identifier | Workload and restoration phase | Service and resource family | Quantity and unit | Location | Start, ramp, and duration | Total or incremental; overhead included? | Evidence and owner |
|---|---|---|---|---|---|---|---|
| Enter slice | Restore, rebuild, essential service, or full service | Exact technical shape | Number or range with unit | Destination scope | Time relative to recovery start | State baseline and temporary work | Sizing model, test date, limitations, named owner |

## Concurrent portfolio demand

Use one set per compatible resource, location, and time slice. Do not add different units or count the same shared entitlement twice.

| Shared slice and time window | Destination resident demand | Recovery demand by workload | Additional rebuild or coexistence demand | Total concurrent requirement | Non-overlap or sequencing assumption | Supporting evidence and remaining gap |
|---|---|---|---|---|---|---|
| Family, location, unit, and period | Normal or peak; quantity and source | Individual contributions, not an unexplained total | Exclude overhead already counted above | Reproducible sum of compatible contributions | Business-approved sequence and dependency feasibility | Source dates, exclusions, and validation action |

## Enabling dependencies and capacity posture

| Dependency or mechanism | Required capability or quantity | Shared consumers and conflicts | Evidence and observed date | Conditions and limitations | Owner and next refresh |
|---|---|---|---|---|---|
| Compute, storage, network, identity, data, or other dependency | Phase-specific requirement | Other recoveries and resident workloads | Scoped test or observation | Restore ordering and performance assumptions | Named owner |
| Quota permission | Administrative scope and limit | Combined requests | Current limit evidence | Not proof of physical supply | Platform owner |
| Capacity mechanism and allocation | Exact eligible scope and quantity | Assignments and protected use | Current terms, state, and allocation ledger | Prerequisites, sharing rules, and residual risk | Technical and commercial owners |

## Validation plan and result

| Field | Entry |
|---|---|
| Method and test identifier | Document review, controlled deployment, partial restore, or portfolio exercise |
| Authorized scope and scale | Exact workloads, resources, quantities, locations, and phases tested |
| Exclusions and extrapolation limits | What the exercise cannot establish |
| Preconditions and safeguards | Access, approvals, budget, dependency readiness, stop conditions, and rollback |
| Evidence collection plan | Requests, errors, deployment timing, restore timing, throughput, and service checks |
| Observed result and date | Actual tested scope, contention, failures, objective comparison, and evidence links |
| Technical validator and business acceptance | Separate authorities and conditions |
| Cleanup and remaining obligations | Resources removed or retained, assignments updated, and charges or contracts reconciled |

## Gaps, decisions, and revalidation

| Gap or assumption | Business consequence | Options and decision deadline | Risk and decision references | Action owner and due date | Acceptance evidence | Next review or invalidating trigger |
|---|---|---|---|---|---|---|
| Enter gap | Function or objective exposed | Feasible options and last responsible date | Linked authority and residual risk | Named executor | Test or observed correction | Destination growth, new consumers, architecture change, term change, or planned test |

Backup, replication, multiple regions, and recovery architecture do not prove destination capacity. Forecasts, quota, discounts, and service listings are also insufficient. Even a successful recovery exercise provides time- and scope-bounded evidence, not a guarantee about future requests.

## Related content

- [Validate recovery-capacity assumptions](../implementation/validate-recovery-capacity.md)
- [Workload capacity profile](workload-capacity-profile.md)
- [Capacity-risk register](capacity-risk-register.md)
