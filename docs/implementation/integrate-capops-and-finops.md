# Integrate CapOps and FinOps

Capacity Operations (CapOps) and FinOps, the technology financial-management practice, need a shared decision record without losing their distinct questions. FinOps asks, “Can we afford it?” CapOps asks, “Can we get it where and when we need it?” These are introductory prompts, not exhaustive definitions of either practice. An organization must answer both.

## Prerequisites

- An owned, versioned demand forecast with normal, peak, and recovery scenarios.
- Cost allocation, budget, contract, and consumption evidence for the selected scope.
- Technical evidence for placement, capacity mechanisms, and alternatives.
- Named business, technical, finance, and commercial decision authorities.

Use approved internal references for sensitive commercial terms. Do not place confidential pricing or contracts in public documentation.

## Steps and evidence

1. **Agree shared identifiers and units.** Link workload, demand version, cost owner, technical consumer, obligation, and decision. Define whether quantities mean assigned, running, requested, or forecast resources.
2. **Separate three ledgers.** Keep financial obligations and discount eligibility; technical entitlements and their exact conditions; and actual assignments and consumption distinct, but linked. One mechanism may affect more than one ledger, or only one.
3. **Create common scenarios.** Use the same dates, growth, peak duration, retirements, and recovery assumptions for cost and capacity analysis. Model idle periods and temporary migration coexistence explicitly.
4. **Evaluate deployability first as a constraint, not an assumption.** Document service, family, quantity, location, period, mechanism conditions, prerequisites, and evidence freshness. A financial reservation may offer a discount without holding deployable capacity. A capacity mechanism may create idle-cost exposure or other obligations.
5. **Compare the full options.** Include expected consumption, unused obligation exposure, acquisition and engineering effort, migration or exit costs, lead time, performance validation, continuity implications, and business delivery trade-offs.
6. **Assign approvals separately.** Technical owners validate suitability and configuration. Finance and commercial authorities approve the economic or contractual choice. Business owners choose priority and acceptable service trade-offs. The practice lead coordinates rather than absorbing these authorities.
7. **Manage allocation through use.** Identify who funds shared or protected capacity, which consumers may use it, and who can authorize reassignment or release. Check recovery needs before optimizing apparently idle resources.
8. **Reconcile and learn.** Compare realized consumption and charges with scenario assumptions. Investigate unused obligations, demand shifts, eligibility mismatches, and deployment failures. Update both forecasts from the same observed change.

## Worked fictional example

A fictional service needs 60 compatible compute units during a time-bound launch. The team compares three options; commercial amounts are deliberately omitted.

| Option | Economic analysis | Capacity and delivery analysis |
|---|---|---|
| Discount-only financial commitment | May lower eligible usage costs but creates an obligation under its terms | Does not by itself establish deployability of the 60 units |
| Applicable capacity mechanism | Include all documented charges, idle exposure, term, and exit rules | Validate exact family, location, quantity, dates, eligibility, prerequisites, and assurance conditions |
| Phased launch using established resources | Model a smaller initial obligation and any engineering or business cost | Reduces initial demand but changes the business outcome and still needs readiness evidence |

The business owner prefers phasing if the matching mechanism cannot be confirmed before the decision deadline. FinOps evaluates the cost consequences of that scenario rather than assuming the original 60-unit launch. Procurement does not purchase a discount-only commitment as a substitute for technical evidence. All quantities are illustrative.

## Exit and review criteria

Integration is working when one demand change flows into both economic and technical analysis, a joint decision records separate approvals, and every obligation has consumers, owners, review dates, and release or renewal criteria. There must be no unexplained contradiction between the cost forecast and capacity forecast.

Review after demand or term changes, eligibility failures, sustained idle assignments, deployment incidents, and monthly reconciliation. Suggested measures are locally defined: unused-obligation exposure, consumption against assignment, forecast variance, and business milestones with unresolved deployability gaps. Do not combine unlike units into one efficiency percentage.

## Common mistakes

- Assuming the cheapest option can be deployed.
- Assuming a capacity mechanism always includes a financial discount, or the reverse.
- Treating all idle capacity as waste without checking recovery and future demand.
- Counting a reassignment as a realized saving while the contractual charge remains.
- Reporting savings without the business or reliability consequences of the change.

## Related content

- [CapOps and FinOps overview](../overview/capops-and-finops.md)
- [Manage capacity commitments](manage-capacity-commitments.md)
- [Capacity commitment register](../templates/capacity-commitment-register.md)
- [CapOps scorecard](../templates/capops-scorecard.md)
