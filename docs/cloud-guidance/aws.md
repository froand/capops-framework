# CapOps for Amazon Web Services

Use this page to distinguish Amazon Web Services (AWS) compute permissions, pricing commitments, and capacity mechanisms. The examples of product behavior below concern Amazon Elastic Compute Cloud (Amazon EC2), not every AWS service.

Last reviewed: 2026-09-15.

**Provider capabilities and commercial terms can change.** Recheck the direct AWS documentation and your applicable terms before selecting a mechanism. This is public guidance for the proposed CapOps framework, not live regional inventory, a deployment commitment, or an AWS-endorsed method.

## Mechanisms are not interchangeable

| Mechanism | Documented behavior | Capacity implication |
| --- | --- | --- |
| Amazon EC2 service quotas | Account resource limits apply by Region; requests exceeding applicable limits fail. Adjustable limits can be requested through Service Quotas. [1] | Permission is necessary but does not prove supply; reservation creation can separately fail for insufficient capacity. [4] |
| Regional Reserved Instances | A billing discount for matching usage in the Region; no capacity reservation. Eligible configurations have size flexibility under documented conditions. [2], [3] | Financial coverage only; do not record regional Reserved Instances as held deployment capacity. |
| Zonal Reserved Instances | A discount plus capacity reserved in the specified Availability Zone. Matching instance family, size, platform, tenancy, and zone matter; there is no zonal instance-size flexibility. [3], [8] | A documented capacity benefit for the qualifying configuration, not a blanket property of all Reserved Instances. |
| Savings Plans | Discount pricing in return for a specified hourly spend commitment for a one- or three-year term; no capacity reservation. [5], [6] | Financial flexibility is not physical supply. |
| EC2 On-Demand Capacity Reservations | Reserve an instance count with matching attributes in one Availability Zone; available for immediate use or through a future-dated request path. [5] | Track requested, scheduled, and active capacity separately, and verify workload consumption. |

A Reserved Instance is not itself a running physical instance. Its **regional or zonal scope** determines whether the purchase includes the documented zonal capacity benefit. It is therefore inaccurate to say either that all Reserved Instances reserve capacity or that none do. [2], [3]

## Scope, matching, and readiness

An EC2 Capacity Reservation is specific to instance type, platform, Availability Zone, tenancy, and instance count. The instance must match those attributes to consume it. With `open` matching, existing or new matching instances can automatically use the capacity. With `targeted` matching, matching instances must explicitly target the reservation. [4], [5]

Choose matching behavior deliberately. An open reservation intended for disaster recovery (DR) can be consumed by normal matching instances. A reservation that exists but is fully occupied is not additional recovery headroom. Use allocation evidence and workload policies to distinguish ownership from unused capacity.

Capacity becomes usable only when the reservation is `active`. Creation can fail because of physical-capacity shortage or insufficient On-Demand Instance quota for the selected family. Active unused reservations count toward applicable limits; a quota increase alone does not make a failed capacity request accepted. [4], [5]

## Immediate use and future-dated requests

For immediate-use Capacity Reservations, AWS documents no term commitment and permits modification and cancellation. Future-dated Capacity Reservations instead undergo assessment and carry their own advance-request, eligible-family, minimum-size, and commitment-duration requirements. They are intended for incremental instances rather than covering already-running instances. Cancellation charges can apply under the documented conditions. [4], [5]

Do not copy the immediate-use lifecycle into a future-dated procurement decision. Record the request state, intended start, applicable commitment, cancellation exposure, and the evidence required at readiness. A submitted future request is not an active reservation.

## Supported scope and limits

The current EC2 overview documents restrictions such as no use with Dedicated Hosts, no support for spread or partition placement groups, and no assurance that a hibernated instance can resume. Cluster placement groups and Dedicated Instances have different documented treatment. These distinctions require checking the exact launch configuration rather than assuming that matching processor counts suffice. [5]

This EC2 guidance is not a blanket statement about managed artificial intelligence (AI), database, or other service capacity. Even where a service launches instances on a customer's behalf, validate its documented consumption path and restrictions; do not extrapolate an EC2 reservation to model availability, service throughput, or every underlying dependency. [5]

## Practical decision checklist

1. **Define the requirement:** account, Region, Availability Zone, instance type, platform, tenancy, count, date, duration, and recovery state.
2. **Check the right limits:** assess applicable family and regional On-Demand quotas, existing consumption, and reservation demand. Keep permission evidence separate from capacity state.
3. **Choose the mechanism:** price flexibility may favor a financial commitment; a zonal deployment requirement needs an explicitly documented capacity benefit.
4. **Select the acquisition path:** compare immediate-use and future-dated terms, including request assessment and cancellation exposure.
5. **Control consumption:** test matching attributes and `open` or `targeted` behavior with the intended deployment process.
6. **Validate end-to-end readiness:** include data, storage, network, identity, and simultaneous recovery demand at the destination.
7. **Assign ownership:** record allocation priority, cost owner, review date, expiry or cancellation action, and residual uncovered demand.
8. **Prepare a tested alternative:** use another qualified instance configuration, zone, Region, or schedule if allowed. A multi-Region design creates alternatives, not a guarantee.

## FinOps and lifecycle considerations

Provisioned Capacity Reservations are charged at the equivalent On-Demand rate whether occupied or unused. A matching running instance is billed instead of a second charge for the same reserved capacity. Applicable Savings Plans and Regional Reserved Instance discounts can apply under matching rules; **Zonal Reserved Instance discounts do not apply to Capacity Reservations**. [7]

Assess utilization and commercial coverage separately. An unused capacity reservation may be an intentional risk treatment, while an unused financial commitment may indicate demand mismatch. Do not release recovery headroom or renew a long commitment solely to improve a single utilization percentage. Check future-dated cancellation terms before setting an automated cleanup policy. [5], [7]

## Risks and common mistakes

- Omitting the regional-versus-zonal distinction when recording Reserved Instances.
- Treating Savings Plans or quota approval as deployment capacity.
- Letting ordinary workloads occupy an open reservation intended as spare recovery capacity.
- Assuming a scheduled future request is already usable, or applying immediate-use cancellation rules to it.
- Treating a regional service listing as proof of quantity and launch-date fulfillability.
- Reserving compute while leaving required storage, network, and application dependencies unvalidated.

## References

These authoritative AWS pages were fetched and reviewed on the date above:

1. [Amazon EC2 service quotas][1] — limits, regional scope, and increase requests.
2. [Reserved Instances for Amazon EC2 overview][2] — billing construct and matching attributes.
3. [Regional and zonal Reserved Instances][3] — financial-only regional scope versus qualifying zonal capacity benefit.
4. [Create a Capacity Reservation][4] — active-state readiness, creation prerequisites, matching, and future-dated assessment.
5. [Reserve compute capacity with EC2 On-Demand Capacity Reservations][5] — mechanism comparison, scope, quotas, restrictions, and future-dated conditions.
6. [What are Savings Plans?][6] — financial commitment purpose and term.
7. [Capacity Reservation pricing and billing][7] — used and unused billing, discount eligibility, and cancellation-charge treatment.
8. [Use your Reserved Instances][8] — instance type, platform, Availability Zone, and tenancy matching.

[1]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html
[2]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html
[3]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-scope.html
[4]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html
[5]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html
[6]: https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html
[7]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-pricing-billing.html
[8]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-reserved-instances.html

## Related content

- [Capacity acquisition](../capabilities/capacity-acquisition.md)
- [Capacity allocation](../capabilities/capacity-allocation.md)
- [Seasonal demand](../scenarios/seasonal-demand.md)
- [Disaster recovery](../scenarios/disaster-recovery.md)
