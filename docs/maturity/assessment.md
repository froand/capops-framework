# CapOps assessment

A Capacity Operations (CapOps) assessment identifies where decision-making is reliable and where improvement is needed. It is not a readiness certificate or an averaged league table. Apply the [maturity-model rubric](maturity-model.md) to all thirteen dimensions and preserve the evidence behind each conclusion.

## Set the scope before scoring

Name the business unit, workload group, services, locations, observation period, assessor, and accountable sponsor. Identify critical services and dimensions from business impact and continuity obligations before seeing the scores. Define locally what representative evidence and sufficient recency mean for this scope; do not adopt a universal sample size or freshness period.

Use the [assessment template](../templates/maturity-assessment.md), keeping separate rows for visibility, forecasting, quota management, acquisition, allocation, workload placement, governance, optimization, resilience, risk management, reporting, automation, and organizational ownership.

## Collect evidence of operation

Inspect records and speak with the people who produced or used them. Interview statements indicate where to look; they do not replace evidence.

| Evidence family | Questions to verify |
|---|---|
| Inventory and telemetry | Can a selected workload be traced to service, family, quantity, location, owner, and collection date? What is missing? |
| Demand and forecasting | Can an actual change be traced from business demand through a forecast version into a decision? Were normal, peak, and recovery scenarios distinguished? |
| Limits and mechanisms | Do decisions distinguish quota permission, financial obligation, capacity entitlement, assignment, and deployment evidence? |
| Commitments and allocation | Can the assessor follow an obligation from approval to consumer, use, review, and release or renewal? |
| Governance and risk | Did an authority decide before the option's deadline? Were exceptions revisited and mitigation closure tests met? |
| Recovery validation | What was tested, when, and at what scale? Were destination resident demand and simultaneous recovery dependencies included or excluded explicitly? |
| Reporting and automation | What action changed because of a measure or automated signal? Are errors, access boundaries, and approval gates evidenced? |
| Ownership and learning | Who accepted the business trade-off? Do incident actions show verified changes, not just closed tasks? |

Sample ordinary decisions as well as incidents and successful examples. Include exceptions and evidence that contradicts the claimed level. For long-horizon strategic decisions, record the age and continuing applicability of the assumptions instead of demanding that every artifact be recent.

## Determine a defensible level

1. Compare observed behavior with all five cells for the dimension.
2. Confirm ownership, repeatability, evidence quality, and actual decision use, not just document existence.
3. Choose the highest level supported throughout the stated scope. If only one team qualifies, split the scope rather than generalizing.
4. Record evidence references, observation dates, gaps, confidence rationale, and the level's unmet conditions.
5. Mark missing evidence as **insufficient evidence** and excluded work as **not assessed**. Neither is proof of a low or high maturity level.
6. Ask accountable owners to review factual accuracy; retain disagreements and their evidence in the record.

## Turn findings into decisions

Keep the thirteen-dimension profile visible. Do not average away a critical weakness or offset it with stronger automation or reporting. A critical unknown requires investigation and explicit business-risk handling even if every assessed dimension is strong.

For example, a fictional service group demonstrates Managed allocation through an accurate consumer ledger. Its recovery exercise reveals that two workloads counted the same unallocated destination capacity. Resilience cannot be scored Managed merely because recovery diagrams exist. Record the lower evidenced behavior, the conflict, an accountable continuity action, and a decision deadline tied to business exposure.

Prioritize a bounded improvement with a named owner, business reason, target evidence, dependencies, and review trigger. A target of Managed may be appropriate; the target is organization-defined and should not imply that higher labels guarantee availability.

## Reassess and report

Reassess after a material scope change, an incident invalidating assumptions, completion of an improvement, or the locally chosen review cycle. Report changes with their evidence, not only before-and-after labels. The assessment is complete when all thirteen dimensions are either assessed or explicitly unresolved, critical gaps have accountable decisions, and actions have measurable acceptance evidence.

Common mistakes include treating a tool purchase as a maturity increase, granting credit for planned work, and describing one successful recovery test as permanent proof of capacity.

## Related content

- [Maturity model and evidence rubric](maturity-model.md)
- [Maturity assessment template](../templates/maturity-assessment.md)
- [Adoption roadmap](adoption-roadmap.md)
- [Review critical workloads](../implementation/review-critical-workloads.md)
