# CapOps for Azure

Use this page to distinguish administrative permission, financial discounts, and supported compute-capacity reservations in Microsoft Azure. It maps public product behavior to the proposed CapOps practice; it is not a Microsoft methodology or a statement of current regional inventory.

Last reviewed: 2026-09-15.

**Provider capabilities and commercial terms can change.** Recheck the linked Microsoft Learn documentation, the exact deployment configuration, and applicable terms before acquisition or renewal. A documentation review is not an availability check or a contractual interpretation.

## Mechanisms are not interchangeable

| Mechanism | Documented purpose and scope | CapOps interpretation |
| --- | --- | --- |
| Azure virtual machine quota | Virtual central processing unit (vCPU) quotas include total regional and virtual machine (VM) family tiers for each subscription; deployment must fit both. There is also a regional VM-count quota. [1] | Track permission for the actual family and region. An approved quota does not prove physical capacity. |
| Azure Reservations, including Reserved VM Instances | Financial commitments apply discounts to matching usage according to product attributes and billing scope. Reserved VM Instances do not provide a capacity guarantee. [2], [3] | Record a financial commitment separately from evidence of deployability; a discount scope is not a physical placement allocation. |
| Azure On-demand Capacity Reservation | Reserves a specified quantity of one supported VM size in a region, optionally in one availability zone. Successful reservations have documented capacity coverage within the applicable service-level agreement (SLA). [3] | Record the accepted reservation, exact size, region/zone, quantity, consumer configuration, and coverage limits. Do not describe an unaccepted request as secured capacity. |
| Capacity reservation group | A regional container for capacity reservations and the association point used by consuming VMs. Creating an empty group reserves no capacity. [3], [4] | Verify the reservations inside the group, not just that a group exists. |

The quota dimension and reservation dimension differ: a **family-level quota** does not make capacity interchangeable across a family. Each capacity reservation covers **one VM size and quantity**, not an arbitrary selection of sizes with an equivalent processor total. [1], [3]

## Reservation scope and consumption

A capacity reservation group defines its region and, when specified, eligible zones. Each reservation in a zonal group selects one eligible zone. A group permits one reservation per size per zone, or one per size when zones are not specified. If a group has no specified zones, consuming VMs must also be deployed without specifying a zone; this is not a reservation that can be freely reassigned to any chosen zone. [3], [4]

A consuming VM must reference the capacity reservation group and match the reservation's size and location. Merely deploying a similar VM in the same region does not consume the reservation. Association and actual allocation are different states: the documented properties distinguish associated VMs from allocated VMs. Inspect both before allocating the same headroom to another workload. [3]

Azure permits deployment beyond the reserved quantity, but the additional instances depend on extra quota and capacity and are outside the capacity reservation SLA. Do not count overallocated instances as additional reserved headroom. [3]

## Creation prerequisites and limits

Creation requires the requested size to be supported in the target location, enough available family and regional quota, and sufficient physical capacity for the request. Reservation creation succeeds for the complete requested quantity or fails; an empty group or a submitted request is not partial capacity acceptance. [4]

Support is specific to VM series, sizes, deployment types, and configuration constraints. The overview documents exclusions including Spot VMs, Dedicated Host deployments, availability sets, and proximity placement groups. Accelerator support must be checked for the exact graphics processing unit (GPU) VM series rather than inferred from another GPU series. The public creation guide describes checking the `CapacityReservationSupported` capability; that capability indicates support, not live supply for a requested quantity. [3], [4]

This page describes the documented VM mechanism. It does not extend that mechanism to every managed database, artificial intelligence (AI) service, storage product, or model endpoint. Validate each chosen service independently. Likewise, a VM compute reservation is not proof that all network, storage, identity, and application dependencies can be deployed or recovered. The overview explicitly notes that other VM components must also be allocated. [3]

## Practical decision checklist

1. **Specify demand:** subscription boundary, service, exact size, region, zone or non-zonal placement, quantity, needed date, duration, and recovery concurrency.
2. **Separate evidence:** record quota permission, financial commitments, accepted capacity reservations, running resources, and successful workload tests in different fields.
3. **Check eligibility:** review the current supported-size and deployment-constraint documentation for the entire configuration. Do not copy a static supported-family list into an evergreen control.
4. **Check creation readiness:** validate quota headroom, including transition overlap, and require successful reservation state before marking the requested quantity as reserved.
5. **Test consumption:** verify the deployment configuration targets the intended group and that allocation consumes the expected reservation.
6. **Validate dependencies and recovery:** test deployment and restoration at the intended scale; include existing destination demand and simultaneous portfolio recovery.
7. **Approve the economics:** assign ownership for idle capacity, discount matching, changes, and release. Keep the business risk of an unreserved remainder visible.
8. **Keep alternatives:** qualify another size, zone, region, schedule, or reduced workload only within approved architecture and data boundaries. A fallback forecast is not a guarantee either.

## FinOps and lifecycle considerations

On-demand Capacity Reservations have no one- or three-year term requirement. Charges begin for successfully provisioned reserved capacity, including unused capacity, at the applicable underlying VM rate. When a matching VM consumes a reservation, the compute capacity is not billed twice. Eligible Reserved VM Instance discounts can apply; other components such as disks and networking still need separate cost treatment. [3]

Changing quantity is supported, but changing size or location requires a different reservation. Deletion requires disassociating VMs first. Revalidate the acquisition and consumption path when changing configuration, and review the risk of giving up existing capacity before replacement capacity is accepted. [3]

## Risks and common mistakes

- Confusing a successful quota request, financial reservation purchase, or group creation with accepted physical capacity.
- Assuming every size in a family or every service uses the same mechanism.
- Treating catalog availability or a forecast acknowledgement as quantity/date fulfillability.
- Ignoring consumption mismatches, overallocated quantities, or unused reservation charges.
- Treating a scoped capacity SLA as an end-to-end application or disaster recovery (DR) guarantee.
- Reusing one destination allocation for several simultaneous recovery plans.

## References

The following public Microsoft Learn pages were fetched and reviewed on the date above:

1. [vCPU quotas][1] — subscription, regional, and family quotas; quota versus physical capacity.
2. [What are Azure Reservations?][2] — financial commitments and matching discount scope.
3. [On-demand capacity reservation in Azure][3] — size/location/quantity scope, support limits, consumption, SLA boundary, pricing, and lifecycle.
4. [Create a capacity reservation][4] — group versus reservation creation, quota prerequisites, support checks, and all-or-nothing quantity acceptance.

[1]: https://learn.microsoft.com/en-us/azure/virtual-machines/quotas
[2]: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations
[3]: https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-overview
[4]: https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-create

## Related content

- [Quota management](../capabilities/quota-management.md)
- [Capacity acquisition](../capabilities/capacity-acquisition.md)
- [Cloud migration](../scenarios/cloud-migration.md)
- [Disaster recovery](../scenarios/disaster-recovery.md)
