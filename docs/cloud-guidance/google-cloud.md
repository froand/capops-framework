# CapOps for Google Cloud

Use this page to distinguish Google Cloud allocation quotas, committed use discounts, and Compute Engine reservations. Its detailed consumption guidance concerns Compute Engine virtual machines (VMs); it must not be generalized to every managed service.

Last reviewed: 2026-09-15.

**Provider capabilities and commercial terms can change.** Verify the current resource, reservation type, consumption path, and terms before making a commitment. This is public guidance for the proposed CapOps framework, not current regional inventory or a promise of deployment.

## Mechanisms are not interchangeable

| Mechanism | Documented purpose and scope | CapOps interpretation |
| --- | --- | --- |
| Compute Engine allocation quotas | Limits on resources accessible to a project, with regional and global dimensions depending on the resource. Remaining quota does not guarantee resource availability in a region or zone. [1] | Record the exact resource and location limits separately from deployment evidence. |
| Resource-based committed use discounts (CUDs) | Discount pricing for a resource commitment with a specified region, configuration, and one- or three-year term; discount sharing is governed by Cloud Billing settings. [2] | A financial commitment is not itself a zonal capacity reservation. Some resource purchases require separate attached reservations. [3] |
| Compute flexible CUDs | Discounts on eligible hourly spend at the Cloud Billing account level, with documented service and resource eligibility. [2] | Broader financial coverage does not reserve zonal capacity. [3] |
| Compute Engine on-demand reservations | Attempt to reserve a count of matching resources in one zone; creation checks availability and requires unused quota. [4], [6] | Record successful reservation creation, exact properties, consumers, and remaining reserved quantity. |

Google explicitly distinguishes commitments from reservations: a commitment alone does not reserve zonal resources. For resource-based commitments containing graphics processing units (GPUs) and most Local SSD (solid-state drive) resources, matching reservations must be attached. The discount and the attached capacity mechanism remain distinct records with related conditions, not interchangeable names for one promise. [3]

## Scope and exact consumption matching

Reservations are zonal resources. An on-demand reservation cannot be treated as a region-wide pool that is automatically usable in another zone. VM consumption requires the documented matching configuration, including zone, machine type, minimum central processing unit (CPU) platform, GPU type and count, Local SSD type and count, and any applicable placement policy. Project eligibility and reservation affinity must also match. [4], [6]

There are two important consumption choices:

- **Automatically consumed reservations:** eligible new and already-running VMs with matching properties can consume them. This is not necessarily spare capacity for a future workload. [5]
- **Specifically targeted reservations:** new instances must match and target the intended reservation. A mismatched configuration is not rescued by a similar machine family or equivalent total processor count. [5]

Single-project reservations are consumed within their project. Shared reservations can be made available to permitted consumer projects within the same organization, subject to organization policy, quota, and other documented restrictions. Financial CUD sharing and reservation sharing are separate mechanisms: enabling a billing discount scope does not by itself grant access to shared capacity. [2], [4]

## Supported scope and acquisition limits

On-demand reservations apply to supported configurations using the standard provisioning model. Reservation consumption does not apply to Spot VMs, preemptible instances, Flex-start VMs, or sole-tenant nodes under the documented restrictions. Not all machine types or accelerator configurations support the same reservation path. Check the current selector and restriction lists rather than extrapolating from one family. [4], [5], [6]

Future reservation paths also exist. They have separate request-review, provisioning, consumption, and end-of-period behavior. Select the applicable path from Google's current reservation-type guidance rather than assuming that on-demand deletion and usage rules apply to every future reservation. [6]

This page does not establish capacity for managed artificial intelligence (AI) models, application programming interfaces (APIs), or all training and prediction services. Where another product documents consumption of Compute Engine reservations, check that product's own workload, sharing-policy, and configuration requirements. The Compute Engine overview itself identifies service-specific conditions; those must not be replaced with an assumption that a GPU reservation covers every managed AI offering. [4]

## Practical decision checklist

1. **Specify demand:** project, service, zone, machine type, CPU platform, accelerators, local storage, count, required date, duration, and recovery concurrency.
2. **Check quotas:** verify resource and location limits for the owner and any consumer projects; distinguish quota approval from resource availability.
3. **Choose the reservation type:** validate support for the provisioning model and all optional hardware or placement properties.
4. **Separate commercial approval:** evaluate resource-based or flexible CUDs against actual eligible usage; determine whether attached reservations are required.
5. **Verify creation and access:** require successful capacity evidence and the intended project-sharing policy before reporting the quantity as reserved.
6. **Test consumption:** compare the real deployment template and reservation affinity against the reservation, then verify consumption and remaining headroom.
7. **Validate the service chain:** test data, storage, network, identity, and destination recovery demand, including other workloads using the same shared pool.
8. **Assign review and release:** document owner, idle-cost budget, attached-commitment restrictions, deletion rules, and tested alternatives. A second zone or region remains an option, not a guarantee.

## FinOps and lifecycle considerations

Reservations incur charges for reserved resources whether they are consumed or unused. A consuming VM does not cause duplicate charging for the same reserved resources. Applicable discount treatment must be checked against current eligibility and commitment rules; do not assume every financial commitment covers every reserved resource. [3], [4]

For resource-based commitments that require attached reservations, deletion, modification, and automatic-deletion choices are constrained during the commitment lifecycle, with documented replacement procedures. Other reservation cases have different behavior. Build cleanup and renewal decisions around the actual attachment and reservation type rather than a generic “delete unused capacity” rule. [3], [4]

For specifically targeted reservations, deletion and later VM restart also depend on consumption and matching-reservation requirements. Confirm the documented release workflow before dismantling an allocation needed for recovery. [4]

## Risks and common mistakes

- Treating CUD purchases as zonal reservations, or overlooking mandatory attached-reservation requirements.
- Confusing financial sharing with permission to consume another project's reservation.
- Reserving one shape while deployment templates specify another CPU platform, accelerator count, local storage configuration, or affinity.
- Counting an automatically consumed reservation as unused disaster recovery (DR) headroom.
- Inferring managed AI capacity from Compute Engine behavior.
- Treating catalog availability, quota, a forecast, or a multi-region design as quantity/date assurance.

## References

These authoritative Google Cloud pages were fetched and reviewed on the date above:

1. [Compute Engine allocation quotas][1] — resource limits and the explicit distinction from availability.
2. [Committed use discounts overview][2] — resource-based versus flexible financial commitments and billing scope.
3. [Reservations with committed use discounts][3] — commitments do not reserve capacity; attachment requirements and lifecycle restrictions.
4. [Compute Engine reservations overview][4] — scope, matching properties, sharing, requirements, restrictions, billing, and deletion behavior.
5. [Consume reservations][5] — automatic and specifically targeted matching; consumption restrictions.
6. [Choose a reservation type][6] — on-demand and future paths, supported provisioning models, and zonal scope.

[1]: https://docs.cloud.google.com/compute/resource-usage
[2]: https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview
[3]: https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments
[4]: https://docs.cloud.google.com/compute/docs/instances/reservations-overview
[5]: https://docs.cloud.google.com/compute/docs/instances/reservations-consume
[6]: https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type

## Related content

- [Quota management](../capabilities/quota-management.md)
- [Capacity acquisition](../capabilities/capacity-acquisition.md)
- [AI and GPU capacity](../scenarios/ai-and-gpu-capacity.md)
- [Multi-region design](../scenarios/multi-region-design.md)
