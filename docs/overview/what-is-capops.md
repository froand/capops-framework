# What is CapOps?

This page defines Capacity Operations (CapOps) and the boundaries of the practice so teams can use a common language without overstating what planning can deliver.

CapOps, or Capacity Operations, is an operational framework and cultural practice for forecasting, securing, allocating, governing, monitoring, optimizing, and validating cloud and infrastructure capacity so workloads can be deployed, scaled, and recovered where and when the business needs them.

## Status and independence

CapOps is a **proposed, independent community framework and cultural practice**, not an established industry standard. It is not an official Microsoft product or methodology, a Microsoft capacity-guarantee program, or a FinOps Foundation extension. It does not imply endorsement by either organization. CapOps complements FinOps; it neither replaces FinOps nor guarantees that capacity will be available.

## Why it matters

An approved budget and a valid architecture do not alone establish whether a workload can obtain the required resources at its delivery or recovery deadline. Capacity decisions connect business priorities with technical requirements, location constraints, commercial terms, and operational evidence.

This is not a claim that cloud capacity is generally unavailable. Exposure depends on a particular combination of service, resource family, quantity, region, zone, date, and other dependencies. A small flexible workload and a tightly constrained migration can need different levels of review.

## What the practice includes

- **Understand and forecast:** Maintain a customer-side view of usage, expected demand, limits, commitments, deployment evidence, and uncertainty. Translate business plans into technical quantities and dates.
- **Plan, secure, and allocate:** Evaluate feasible placements, quota, supported capacity mechanisms, and priorities. Assign each allocation and commitment a consumer, owner, time window, and review decision.
- **Operate and optimize:** Monitor actual conditions, reclaim unnecessary resources, modernize rigid dependencies, and update plans when assumptions change.
- **Validate and learn:** Test production, peak, and recovery assumptions, record what the evidence does and does not establish, and improve the next decision.

“Secure capacity” describes a set of actions, not an unconditional outcome. Depending on the workload, those actions can include planning, quota requests, supported capacity reservations, architecture flexibility, allocation, and established provider-engagement mechanisms. Engagement helps clarify requirements and supported options; engagement alone is not a capacity commitment.

## Essential distinctions

| Evidence or mechanism | What it means | What it does not establish |
|---|---|---|
| Quota | An administrative permission or service limit | Available physical supply |
| Demand forecast | An estimate of future requirements with assumptions | A provider commitment |
| Financial reservation or commitment | Commercial terms that may reduce cost | Reserved deployment capacity unless explicitly included |
| Capacity reservation | A supported mechanism with defined scope and conditions | Unconditional availability outside those conditions |
| Regional service availability | A service is offered in a location | Fulfillment of every family, zone, quantity, and date |
| Resilience architecture | A design for surviving or recovering from disruption | Sufficient destination capacity during recovery |
| Multi-region design | Additional placement options and reduced concentration in some scenarios | Guaranteed capacity or independent failure conditions |

Customer-side visibility is not a view of a provider's physical inventory. Unknown supply should remain unknown in reports rather than being inferred from quota or successful deployments elsewhere.

## Start with a bounded decision

Choose a workload with a meaningful delivery or recovery obligation. Record its business outcome, required service and resource family, quantity and unit, region and zone constraints, need-by date, ramp, duration, priority, and permitted flexibility. Separate normal production, peak, and recovery profiles.

Name the workload decision owner and the people responsible for technical validation, commercial approval, and operational execution. Compare feasible options, record the remaining risk and the last useful decision date, then review actual results. Expand the practice using evidence from that work, not a requirement to create a new organizational department.

## Risks and common mistakes

- Calling a workload “secured” without stating the mechanism, dimensions, validity period, and exclusions.
- Treating a dashboard or procurement transaction as the entire practice.
- Transferring business risk acceptance to a coordinator who lacks that authority.
- Reserving more than needed without evaluating cost, release terms, competing demand, or recovery obligations.

## Related content

- [Why CapOps?](why-capops.md)
- [CapOps principles](principles.md)
- [CapOps and FinOps](capops-and-finops.md)
- [Framework overview](../framework/framework-overview.md)
- [Glossary](../glossary.md)
