# CapOps responsibility matrix template

Use this Capacity Operations (CapOps) matrix to put names behind decisions in the [responsibility model](../operating-model/roles-and-responsibilities.md). Copy the tables, replace suggested roles with local authorities and deputies, and obtain acknowledgment. A role need not be a separate job. Do not make the practice lead accountable for every workload, contract, technical decision, and risk.

For each row, name one accountable authority for the stated decision. The responsible executor performs the work; contributors provide required evidence; informed parties receive the result. Split a row when separate business, technical, and financial approvals are required.

## Scope and mandate

| Field | Entry |
|---|---|
| Matrix identifier, version, and effective date | Stable reference and history |
| Scope | Business units, workloads, platforms, locations, and exclusions |
| Sponsor and practice steward | Names and mandate reference |
| Delegation and approval policy | Existing business, technical, financial, release, and risk boundaries |
| Handoff rule | How receiving owners acknowledge actions and evidence |
| Urgent escalation path | Existing incident or risk authority when normal timing is insufficient |
| Next ownership review | Date and triggers such as reorganization or workload transfer |

## Decision-specific assignments

| Decision or output | Accountable authority: replace with name | Responsible executor | Evidence contributors | Informed parties | Deputy and escalation | Required record |
|---|---|---|---|---|---|---|
| Practice mandate and risk appetite | Executive sponsor | Practice lead | Business, finance, architecture, continuity | Scoped teams | Name and route | Mandate decision |
| Practice standards and facilitation | Practice lead | Practice contributors | Data and workload owners | Decision authorities | Name and route | Standards and review records |
| Business demand, priority, and milestones | Business or product owner | Workload planning team | Architecture, delivery, operations | Portfolio and platform teams | Name and route | Validated demand version |
| Technical sizing and placement suitability | Architecture authority | Solution architect | Platform, compliance, operations | Business owner | Name and route | Technical decision and tests |
| Quota and mechanism configuration | Platform service owner | Platform engineering | Architecture, workload, provider representative | Commercial and operations owners | Name and route | Scoped request and result |
| Contractual acquisition or renewal | Commercial or budget authority | Procurement | FinOps, technical owner, business consumer | Platform and finance teams | Name and route | Approved obligation and terms |
| Allocation within approved priorities | Platform service owner | Platform engineering | Workload consumers, operations | Cost and continuity owners | Name and route | Assignment and change ledger |
| Cross-workload priority conflict | Portfolio authority | Portfolio planning | Affected business owners, architecture, finance | Sponsor and implementers | Name and route | Sequencing decision |
| Economic analysis and cost attribution | Finance or FinOps authority | FinOps practitioner | Consumers, procurement, platform | Business and portfolio owners | Name and route | Scenario cost analysis |
| Deployment or migration readiness | Existing release authority | Delivery team | Business, platform, architecture, operations | Affected service owners | Name and route | Go, change, hold, or exception |
| Recovery objectives and continuity-risk acceptance | Business service owner within policy | Continuity owner | Reliability, architecture, dependency owners | Sponsor and affected consumers | Name and route | Objective and residual-risk decision |
| Recovery test execution and technical result | Reliability or operations owner | Recovery execution team | Continuity, platform, dependency owners | Business service owner | Name and route | Test result and exclusions |
| Risk acceptance beyond delegated limits | Existing risk authority or sponsor | Risk owner | Relevant business, technical, commercial, and compliance owners | Affected teams | Name and route | Bounded acceptance or hold |
| Commitment release | Authority for the obligation being released | Authorized commercial or platform operator | Consumers, continuity, finance | Allocation and service owners | Name and route | Technical and commercial closure |
| Source evidence quality | Producing service or data owner | Evidence collector | Consuming teams | Practice lead | Name and route | Freshness and reconciliation evidence |
| Consolidated executive reporting | Practice lead for accurate consolidation | Reporting contributors | Business risk and evidence owners | Sponsor and portfolio authority | Name and route | Decision brief linked to evidence |
| Incident learning and corrective controls | Affected service or control owner | Assigned corrective-action executor | Incident contributors and practice lead | Affected consumers | Name and route | Verification-backed learning action |

FinOps is the technology financial-management practice. A provider representative can contribute mechanism information and request coordination, but does not replace the customer's accountable internal decision authority.

## Acknowledgment and unresolved gaps

| Assignment or gap | Authority acknowledgment and date | Delegated boundary | Conflict or missing owner | Resolution owner and deadline | Evidence of completed handoff |
|---|---|---|---|---|---|
| Enter row reference | Named acceptance | What may and may not be approved | State disagreement explicitly | Named resolver and date | Receiving team acknowledgment |

Do not treat silence as approval. A responsibility gap affecting a decision deadline must be escalated through the existing authority, not silently absorbed by the facilitator.

## Related content

- [Roles and responsibilities](../operating-model/roles-and-responsibilities.md)
- [Operating model](../operating-model/operating-model.md)
- [Decision record](decision-record.md)
