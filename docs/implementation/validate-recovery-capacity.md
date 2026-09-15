# Validate recovery-capacity assumptions

Capacity Operations (CapOps) treats recovery demand as a distinct profile that must be examined and tested. Backup, replication, a recovery architecture, and multiple regions do not by themselves establish destination capacity. This guide produces a scoped recovery-capacity profile, validation evidence, and explicit residual-risk decisions.

## Prerequisites

- Business-approved recovery time and recovery point objectives: restoration time and acceptable data loss.
- Named continuity, reliability, platform, dependency, and business owners.
- Current normal, peak, recovery, allocation, and commitment records.
- An authorized test plan with cost limits, access controls, operational safeguards, abort conditions, and cleanup ownership.

Use the [recovery-capacity profile](../templates/recovery-capacity-profile.md). A documentary review can identify gaps, but must not be described as a full-scale recovery test.

## Steps and evidence

1. **Define the failure scenario.** State what is unavailable, which workloads are affected together, which destination remains usable, and which business functions must be restored first. Include the possibility that destination services continue their normal or peak operation.
2. **Translate objectives into demand.** For each restoration phase, record service, family, quantity and unit, location, required start, ramp, duration, and dependencies. Include restore and rebuild work, temporary coexistence, performance needs, and eventual cleanup.
3. **Build the concurrent portfolio view.** Sum only compatible resources in the same time and location slice. Include destination resident load and shared enabling services. Do not assume that every workload can use the same spare pool independently.
4. **Inspect mechanism and limit evidence.** Confirm administrative permissions, matching technical entitlements, existing allocations, documented conditions, and competing use. Record evidence age and refresh triggers. A forecast, quota approval, financial discount, or service listing is not proof of physical supply.
5. **Choose a safe validation method.** Use a dependency review, controlled deployment, partial restoration, or portfolio exercise appropriate to the question. Record the scale and exclusions before execution. Do not extrapolate a small test to full demand without a justified model and visible uncertainty.
6. **Execute and observe.** Capture request outcomes, resource dimensions, actual allocation, initialization and data-restore timing, throughput, dependency readiness, errors, contention, and abort actions. Separate a successful resource deployment from successful restoration of the business service.
7. **Compare with objectives and assumptions.** Identify whether capacity, data movement, configuration, sequencing, or another dependency limited recovery. Describe what the evidence establishes only for the tested scope and time.
8. **Decide and remediate.** Options include protecting appropriate capacity, changing restoration order, validating an alternate placement, reducing initial service, or changing business objectives through authorized approval. Record residual risk and option deadlines.
9. **Clean up and revalidate.** Confirm temporary resources and assignments are removed or retained intentionally, obligations remain correctly recorded, and normal operations are unaffected. Set event and calendar triggers for the next validation.

## Worked fictional example

In one fictional failure scenario, two services recover together into the same destination using a performance-validated compute family.

| Concurrent demand in the tested phase | Compatible compute units |
|---|---:|
| Existing destination workload, which continues running | 20 |
| Service A recovery | 36 |
| Service B recovery | 24 |
| Additional temporary rebuild work, not included above | 10 |
| Total scenario demand | **90** |

These figures are illustrative. Other resource dimensions, such as storage throughput, must be evaluated separately rather than converted to compute units.

If evidence covers only 70 matching units, the remaining 20 are an unresolved scenario gap, not proof that supply is impossible. Quota permission for 100 does not close the gap. The team considers staged restoration or a matching capacity mechanism. Staging is acceptable only if dependency order and business recovery objectives still work.

A controlled test of 30 units can validate configuration and some dependencies, but cannot be reported as a successful 90-unit portfolio recovery. The result records the tested quantity, exclusions, and next validation action.

## Exit and review criteria

The assessment is complete when the scenario, profiles, shared dependencies, method, results, cleanup, limitations, and residual decisions are recorded. Recovery readiness requires the organization's acceptance criteria to be met for the intended scope; review completion alone is not readiness.

Revalidate after material destination-demand growth, architecture or family changes, new shared consumers, mechanism changes, a failed exercise, or the locally chosen continuity schedule. Evidence is time-scoped: a successful test does not guarantee that future recovery requests will be fulfilled.

## Common mistakes

- Assuming recovery demand equals normal production demand.
- Ignoring the destination's resident peak, concurrent failures, or rebuild overhead.
- Treating shared headroom as independently available to every workload.
- Claiming a small deployment test validates full business recovery.
- Releasing recovery allocations as idle without continuity and business approval.

## Related content

- [Recovery-capacity profile template](../templates/recovery-capacity-profile.md)
- [Review critical workloads](review-critical-workloads.md)
- [Capacity resilience](../capabilities/capacity-resilience.md)
- [Risk-register guide](create-a-capacity-risk-register.md)
