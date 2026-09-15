# Manage capacity commitments through their lifecycle

Capacity Operations (CapOps) connects a commitment to a business need, an authorized obligation, eligible consumers, actual use, and an exit decision. A commitment is not just a purchase. This guide manages acquisition, assignment, consumption, review, and release without confusing financial benefits with deployable entitlement.

## Prerequisites

- Validated demand with service, family, quantity, location, dates, duration, and scenario.
- Current public mechanism documentation and approved access to applicable commercial terms.
- Named business consumer, technical owner, commercial owner, budget authority, and operator.
- A shared [commitment register](../templates/capacity-commitment-register.md) linked to forecasts and decisions.

Terms vary. Some commitments are financial only; some mechanisms provide defined capacity rights; some combine aspects of both. Do not assume cancellation, transfer, compatibility, renewal, or deployment assurance unless the applicable terms establish it.

## Steps and evidence

| Lifecycle stage | Concrete actions | Evidence and decision |
|---|---|---|
| **Evaluate and plan** | Compare demand phasing, alternate architecture, existing eligible capacity, and new mechanisms. Calculate latest acquisition and alternative-design decision dates. | Demand version, option comparison, term references, exact scope, constraints, and recommendation |
| **Acquire** | Obtain commercial and technical approvals separately; verify prerequisite limits, dates, eligible scope, funding, and creation result. | Authorized obligation and mechanism identifier, documented conditions, actual start and end, unresolved prerequisites |
| **Assign** | Identify eligible workload consumers, quantity, priority, allowed use, location, period, and protected recovery demand. Check conflicts before binding or sharing. | Allocation ledger, consumer acknowledgment, technical compatibility evidence |
| **Consume** | Deploy or use through the supported path; verify the intended entitlement or financial benefit applies and observe actual use. | Deployment result, eligibility or benefit evidence where applicable, consumption and charge records |
| **Review** | Reconcile forecast, assignment, consumption, unused obligations, expiry, incident findings, and future recovery need. | Retain, reassign, amend, renew, or release recommendation with authority and deadline |
| **Release or close** | Check all consumers, peak and recovery plans, dependency effects, and contractual exit rules before authorized release. Verify technical and commercial outcomes independently. | Release confirmation, updated allocation, obligation status, remaining charges, and closure evidence |

Renewal is a new demand and option decision, not an automatic continuation. If terms prevent immediate release, record the remaining obligation and its owner rather than marking the commitment closed.

## Keep the ledgers consistent

Track financial obligation, technical entitlement, assignment, and consumption separately. Their quantities may differ for legitimate reasons, but the reason must be visible. Where capacity cannot be shared or transferred, do not create a pooled allocation merely because a spreadsheet makes it convenient.

Evidence must match the time, location, family, and quantity of the demand. Quota permission and successful configuration of a financial discount do not establish deployable capacity. “Secured” must state the mechanism's documented conditions and remaining risks, never unconditional availability.

Integrate reviews with FinOps, the technology financial-management practice, and procurement. FinOps evaluates economics and attribution; procurement verifies obligations and terms; platform engineering validates technical scope and configuration; business owners authorize priority or service changes.

## Worked fictional example

A fictional platform holds a documented capacity entitlement for 50 compatible compute units within a specific scope and term. The terms in this example permit reassignment among eligible consumers.

| Ledger view | Units | Interpretation |
|---|---:|---|
| Technical entitlement | 50 | Subject to the mechanism's recorded conditions |
| Assignment to Service A | 30 | Twenty-four currently consumed; six remain needed for its approved peak |
| Assignment to Service B | 15 | Twelve currently consumed; three become unnecessary after a confirmed retirement |
| Unassigned | 5 | Must have an owner and a retain, assign, or release decision |
| Actual consumption | 36 | 24 + 12, not the same as assigned or entitled quantity |

The 14 units not currently consumed are not all releasable. Six support Service A's peak, and the other eight need demand, recovery, eligibility, and contractual checks. After those checks, authorities may authorize reassignment or release where permitted. A technical release does not establish a financial saving until the applicable obligation and charges are verified. All quantities are illustrative.

## Exit and review criteria

A managed commitment has a reason to exist, named owners and consumers, validated scope and terms, linked approvals, observable use, review dates, and a release or renewal decision deadline. A released commitment closes only when affected allocations and remaining obligations are reconciled.

Review on demand changes, consumer transfers, idle assignments, eligibility failures, incidents, term changes, and before renewal or cancellation deadlines. Use organization-defined measures and targets; specify whether utilization uses entitlement, assignment, or charged quantity as its denominator.

## Common mistakes

- Purchasing a discount as if it reserved deployable resources.
- Leaving acquired capacity without an accountable consumer.
- Reclaiming apparent idle capacity without peak and recovery checks.
- Assuming technical reassignment automatically transfers cost responsibility.
- Missing a renewal or cancellation window because only monthly utilization was monitored.

## Related content

- [Capacity commitment register](../templates/capacity-commitment-register.md)
- [Integrate CapOps and FinOps](integrate-capops-and-finops.md)
- [Capacity allocation](../capabilities/capacity-allocation.md)
- [Decision record template](../templates/decision-record.md)
