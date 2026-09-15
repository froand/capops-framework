# Review critical workloads

This Capacity Operations (CapOps) review asks whether a critical workload's capacity assumptions support its business obligations. It covers normal operation, peaks, changes, and recovery, including dependencies outside the workload team. Criticality is organization-defined; it is not inferred solely from resource size or spending.

## Prerequisites

- A business owner who can explain the impact of delayed deployment, reduced service, or failed recovery.
- A current architecture and dependency view, including shared platform services.
- Demand, deployment, quota, mechanism, contract, and incident evidence.
- Existing release, risk, compliance, and continuity authorities.

Start with the [workload capacity profile](../templates/workload-capacity-profile.md) and link its gaps to the risk register.

## Steps and evidence

1. **Confirm business obligations.** Record the service outcome, critical periods, required dates, location restrictions, minimum acceptable degraded service, recovery time objective, and recovery point objective. The latter two describe restoration time and acceptable data loss; neither specifies capacity by itself.
2. **Map the whole dependency chain.** Include compute, storage capacity and throughput, networking, identity, name resolution, data services, orchestration, and any specialized resources. Name the owner of each shared dependency.
3. **Verify demand translation.** Compare the sizing model with current performance evidence and expected business changes. Record service, family, quantity and unit, location, dates, ramp, duration, and uncertainty.
4. **Separate the profiles.** Document normal, peak, and recovery requirements as distinct scenarios. Include migration coexistence, rollback, restore, and rebuild overhead where applicable. State which profiles may overlap.
5. **Assess current posture.** Inspect limits, applicable capacity-mechanism scope, commitments, assignments, and observed deployments. Record source, timestamp, coverage, prerequisites, and next refresh trigger. A service listing or approved quota does not prove the desired resources can be deployed.
6. **Validate alternatives.** Test performance equivalence, permitted location, dependencies, operational support, and change lead time for alternate families, placements, schedules, or service patterns. Label untested options as unvalidated.
7. **Check portfolio contention.** Ask whether other critical workloads depend on the same placement, allocation pool, recovery destination, or enabling service during the same event. Use concurrent scenarios rather than independent assurances.
8. **Make a business decision.** Present gap, consequence, viable options, funding or commercial implications, and last responsible decision deadlines. The appropriate authority chooses proceed, change, hold, or an expiring exception; do not let a profile author accept the business risk implicitly.
9. **Verify actions and establish triggers.** Update the profile after tests, assignment changes, or acquisition. Define re-review after material growth, architecture changes, mechanism expiry, incidents, or changed recovery dependencies.

## Worked fictional example

A fictional order-processing service has ample compute for its normal and promotional peaks, but recovery rebuilds its search data from retained records. The initial recovery plan models replacement application instances only.

Dependency review reveals a temporary storage-throughput requirement and a shared identity service in the recovery destination. A second critical service uses the same rebuild path. The reviewers model both recoveries together, add rebuild overhead, and test the restoration order. They do not declare readiness from the existence of replication or two locations.

The business owner chooses to restore essential ordering before historical search, subject to a validated degraded-service plan. The continuity owner updates restoration assumptions; reliability and platform owners own technical verification. Residual exposure stays in the register until its closure test passes.

## Exit and review criteria

The review is complete when obligations and dependencies have acknowledged owners, each profile has scoped evidence or a visible gap, alternatives have validation status, and the authority has recorded decisions on material exposure. Completion is not synonymous with readiness: a workload can have a completed review and a hold decision.

Set organization-defined freshness and review triggers appropriate to change rate and business consequence. Revalidate before irreversible release actions if evidence no longer matches the intended workload.

## Common mistakes

- Reviewing only the largest or most expensive resource.
- Equating backup, replication, or multi-region architecture with recovery capacity.
- Using a historical successful deployment as proof of future supply.
- Omitting rebuild overhead, shared dependencies, or rollback demand.
- Accepting technically incompatible alternatives merely because their unit counts match.

## Related content

- [Workload profile template](../templates/workload-capacity-profile.md)
- [Validate recovery capacity](validate-recovery-capacity.md)
- [Capacity resilience](../capabilities/capacity-resilience.md)
- [Capacity-risk register](../templates/capacity-risk-register.md)
