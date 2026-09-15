# CapOps for hybrid and private infrastructure

Use this page to apply the proposed CapOps practice where physical assets, facilities, virtualization or container platforms, and cloud services form one delivery chain. Owning equipment moves some capacity responsibilities to the organization; it does not remove them.

Last reviewed: 2026-09-15.

**Provider and vendor capabilities, support conditions, and commercial terms can change.** Check the documentation for the exact hardware, firmware, platform release, and contract before acting. The public examples below are deliberately narrow; they do not establish compatibility, available stock, or a capacity guarantee for an arbitrary private environment.

## Distinguish the kinds of evidence

| Evidence or mechanism | What to establish | What it must not be mistaken for |
| --- | --- | --- |
| Purchase order or supplier forecast | Ordered configuration, stated lead time, acceptance terms, and dependency owners | Installed and accepted service-ready capacity |
| Financial or software commitment | Payment obligation, entitlement scope, supported use, and renewal conditions | Physical hardware, licensed concurrency beyond the agreement, or a recovery allocation |
| Internal service catalog | Offered configuration and request process | Confirmed quantity, location, and completion date |
| Logical quota | Administrative allowance in a particular platform scope | More hosts, network bandwidth, rack power, or storage throughput |
| Scheduler request or local reservation | Exact product semantics, consumers, admission behavior, and failure-state coverage | A universal guarantee across virtualization, container, hardware, and cloud platforms |
| Commissioned allocation | Healthy and compatible resources, dependency readiness, allocation policy, and acceptance tests | Proof that every future simultaneous failure can be absorbed |

The first step is to define what “available” means locally. Keep planned, ordered, delivered, installed, accepted, allocated, and currently healthy resources separate. A financial approval or forecast is not a completed commissioning record.

## Public platform example: Kubernetes

Kubernetes `ResourceQuota` objects constrain aggregate resource use or object counts within a namespace. They are admission controls, not physical capacity purchases. The documentation notes that if namespace quotas collectively exceed cluster capacity, contention can still occur. [1]

For central processing unit (CPU) and memory resources, the scheduler uses Pod resource requests when selecting a node. Even low observed utilization does not imply another Pod can be scheduled if requests would exceed the available scheduling capacity. Resource limits govern runtime usage rather than procuring more nodes. [2]

For CapOps, inspect namespace policy, declared requests, schedulable node capacity, actual workload demand, and recovery headroom separately. A quota increase might allow an object to be admitted without making its Pods schedulable. Do not claim a universal overcommit ratio or apply CPU assumptions to every specialized device. Product version, resource type, and configuration matter.

## Public hardware example: NVIDIA DGX H100/H200

DGX H100 and DGX H200 are NVIDIA system model names, not generic capacity units. NVIDIA's system guide identifies configuration-specific power and network dependencies. It states that supported network cables and adaptors must be obtained separately and that compatibility depends on the networking firmware. The same guide describes reduced performance when only three power supply units have power, illustrating why continued operation is not necessarily full useful capacity. [3]

The power-capping guidance describes several sources of graphics processing unit (GPU) power limits, with the most conservative applicable limit selected. Treat the actual configured power state as part of the benchmarked workload configuration; do not assume that a count of installed accelerators describes their operating envelope. [4]

These are examples from one hardware family, not installation instructions or claims about all servers. Facilities and hardware changes require qualified owners following the exact vendor procedures and applicable safety requirements. For artificial intelligence (AI) workloads, record device memory, software compatibility, data throughput, network topology, and usable performance alongside the physical GPU count.

## Scope and limits of the hybrid plan

Maintain a capacity ledger by site, failure domain, resource family, configuration, quantity, and readiness date. For each critical workload, link compute to storage, network, licensing, identity, power, cooling, rack space, delivery, installation, and operational support.

Define the failure state being funded. Normal-state spare processing is not automatically usable after a host, rack, storage system, or site fails. Replication and redundant components are not proof of sufficient recovery capacity. Include existing destination workloads, restore traffic, and simultaneous portfolio recovery.

Cloud bursting is an architecture option to validate, not an automatic release valve. Review data-transfer time, connectivity, approved placement, application compatibility, cloud quota, and cloud capacity mechanisms independently. A local reservation or entitlement does not extend to the cloud destination.

## Practical decision checklist

1. **Translate business demand:** specify useful throughput, concurrency, location, date, duration, and minimum service level rather than only a hardware count.
2. **Audit the asset states:** distinguish ordered, installed, commissioned, healthy, and schedulable capacity; give each transition an accountable owner.
3. **Check the complete dependency chain:** validate the bill of materials, firmware and software compatibility, facilities readiness, storage performance, network path, and license conditions.
4. **Separate policy from supply:** inspect platform quotas, requests, reservations, and priorities under their actual product definitions. Do not aggregate incompatible resource shapes.
5. **Model degraded states:** assess capacity after the chosen failures and maintenance events, including changed power or performance behavior where applicable.
6. **Test acceptance and recovery:** run representative workload and concurrent recovery tests; document the scale and conditions not exercised.
7. **Compare alternatives:** rightsize, reschedule, modernize, expand, replace, or use a separately validated environment. Include lead times and implementation risk.
8. **Approve lifecycle decisions:** assign cost, allocation, renewal, spare-parts, support, decommissioning, and residual-risk owners. Recheck evidence before release or major expansion.

## FinOps and lifecycle considerations

Compare complete service economics rather than purchase price alone: capital or lease costs, licenses, energy, space, connectivity, maintenance, spares, staffing, and stranded or partially commissioned assets. Use the organization's accounting treatment rather than implying one universal financial model.

Keep intentional resilience headroom visible so optimization does not silently remove it. Conversely, avoid retaining obsolete resources only to justify sunk cost. Renewal and refresh decisions should include whether modernization broadens qualified placement and whether the transition needs temporary dual capacity.

## Risks and common mistakes

- Counting purchased or delivered equipment as usable before commissioning.
- Treating namespace quota, scheduler admission, or a catalog entry as physical supply.
- Summing free processors across incompatible memory, network, or device configurations.
- Assuming component redundancy preserves full performance or establishes site-level disaster recovery (DR) capacity.
- Excluding power, cooling, cabling, software, or storage from the acquisition critical path.
- Treating cloud fallback as immediately deployable without cloud-specific evidence.
- Optimizing away the same headroom that several recovery plans already depend on.

## References

These public authoritative platform and vendor pages were fetched and reviewed on the date above:

1. [Kubernetes resource quotas][1] — namespace admission limits and contention despite quota.
2. [Kubernetes resource management for Pods and containers][2] — scheduling requests, resource limits, and node-capacity checks.
3. [NVIDIA DGX H100/H200 system introduction][3] — configuration-specific power behavior and supported network cable/firmware dependencies.
4. [NVIDIA DGX H100/H200 power capping][4] — multiple power-limit sources and conservative limit selection.

[1]: https://kubernetes.io/docs/concepts/policy/resource-quotas/
[2]: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
[3]: https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html
[4]: https://docs.nvidia.com/dgx/dgxh100-user-guide/power-capping.html

## Related content

- [Capacity visibility](../capabilities/capacity-visibility.md)
- [Capacity acquisition](../capabilities/capacity-acquisition.md)
- [Specialized resource dependencies](../scenarios/specialized-resource-dependencies.md)
- [Legacy resource modernization](../scenarios/legacy-resource-modernization.md)
