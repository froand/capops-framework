# Create a capacity-risk register

A Capacity Operations (CapOps) risk register connects uncertain capacity events to business consequences and timely choices. It is not a list of utilization alerts. Use it to decide what to mitigate, what evidence to obtain, and who may accept residual exposure.

## Prerequisites

- Owned demand and workload profiles with dates and technical dimensions.
- Evidence about limits, deployments, mechanisms, allocations, and dependencies.
- The organization's risk appetite, impact categories, and approval boundaries.
- Access to business owners and technical or commercial specialists who can compare options.

Use the [risk-register template](../templates/capacity-risk-register.md). If the organization already has a risk system, add the capacity-specific fields there instead of maintaining an unlinked duplicate.

## Steps and evidence

1. **Write an event and consequence.** Use “If [uncertain event], then [business consequence] by [milestone].” Distinguish an uncertain future risk from an active issue; an active deployment failure may require incident handling.
2. **Specify the demand at risk.** Record workload, service, family, quantity and unit, permitted location, required date, duration, and scenario. Link shared dependencies and correlated risks.
3. **Separate facts from assumptions.** Link evidence source, observed date, conditions, coverage, and refresh trigger. Treat unknown or stale evidence as an investigation need, not proof of shortage or availability.
4. **Assess business exposure.** Use local impact and likelihood methods with rationale and confidence. Do not invent a probability of physical availability from a quota value or service listing. Prioritize critical dependencies and deadlines even when likelihood is uncertain.
5. **Develop viable options.** Compare acquisition, demand phasing, alternate architecture or location, prioritization, and acceptance. Record performance, location, cost, implementation, and contractual constraints.
6. **Calculate option deadlines.** Work backward from the required date using evidenced implementation or acquisition lead time, validation time, and a locally chosen uncertainty allowance. Record the last responsible decision deadline for each viable option and an earlier escalation trigger where appropriate.
7. **Assign distinct ownership.** Name the risk owner, mitigation executors, decision authority, and business risk acceptor. The practice lead maintains process quality but does not automatically accept workload or commercial risk.
8. **Track decisions and verification.** Link the decision, action dates, residual risk, next review, and closure evidence. “Request submitted” or “quota approved” may complete an action without resolving deployability risk.

## Worked fictional example

A fictional data-processing launch requires 60 units of a specialized family in an approved location in ten weeks. Current evidence establishes 40 units. A limit increase has been approved, but the additional 20 units have not been validated or covered by an applicable capacity mechanism.

The risk is: “If the additional 20 matching units cannot be deployed by the launch window, the processing backlog may miss the business reporting milestone.” The record does not claim a confirmed shortage.

One alternative takes six weeks to implement, two weeks to validate, and one week of locally selected uncertainty allowance. Its latest decision is therefore one week from now. A second option is to reduce initial launch volume with explicit business approval. The owner seeks technical evidence while the business authority decides before the alternative becomes infeasible. All quantities and lead times are illustrative.

Closing the risk requires evidence that the approved demand or changed business plan is satisfied under the decision's conditions. Merely receiving the limit increase is insufficient. If a smaller launch is chosen, retain any residual backlog exposure and revisit trigger.

## Exit and review criteria

Every material record must have a stated event, business consequence, scoped evidence, owner, option, decision authority, deadline, and next action. Critical unknowns must remain visible. Reconcile linked records so the same shared dependency is not counted as several independent mitigations.

Review at material changes and before decision deadlines, not only monthly. Close after the stated verification passes; accepted risk remains tracked until its expiry or the exposure ends. Reopen when demand, mechanism conditions, destination contention, or evidence validity changes.

## Common mistakes

- Writing “capacity risk” without explaining the business consequence.
- Using a numerical risk score to conceal an imminent decision deadline.
- Calling an approved quota or financial commitment a completed mitigation.
- Assigning every risk to the practice lead.
- Closing a risk after purchase without checking assignment, consumption eligibility, and recovery effects.

## Related content

- [Capacity risk management](../capabilities/capacity-risk-management.md)
- [Risk-register template](../templates/capacity-risk-register.md)
- [Decision record template](../templates/decision-record.md)
- [Operating cadence](../operating-model/operating-cadence.md)
