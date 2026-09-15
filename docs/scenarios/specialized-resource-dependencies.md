# Specialized resource dependencies

Use this scenario to assess a dependency chain in which the usable resource is a complete working configuration, not an isolated server count. It applies to specialized compute, storage, networking, and privately hosted infrastructure.

## Business context

A fictional engineering organization needs a simulation campaign before a design review. Its solver requires tightly coupled workers, a validated software version, licensed concurrency, and fast shared scratch storage. A privately hosted cluster has nominally spare servers, but not every server is connected to the required fabric or has the required memory.

All specifications, dates, and test thresholds are illustrative inputs for this fictional workload.

## Capacity challenge

Capacity is limited by the weakest required dependency. Enough processing cores across the estate does not prove that a compatible, connected group can run the solver. Adding servers before storage, network, power, or software readiness is established can increase cost without increasing completed work.

## Demand dimensions

| Dimension | Example demand |
| --- | --- |
| Business outcome | Complete a validated simulation campaign before the 2027-10-22 design decision |
| Compute group | 16 workers concurrently; each needs 32 processing cores and 512 gibibytes of memory |
| Topology | Workers must share the qualified low-latency fabric and supported network configuration |
| Data path | 40 terabytes of scratch space; throughput requirement derived from a representative solver run |
| Software dependency | The fictional license agreement permits 16 concurrent worker slots; version and feature entitlements must be checked |
| Physical placement | Approved rack group in the primary facility, including power, cooling, cabling, and maintenance constraints |
| Timing and duration | Seven-day campaign from 2027-10-11, with setup, validation, and cleanup outside the run itself |
| Flexibility | Eight-worker execution only if completion time and result validation are acceptable; alternative facility requires separate qualification |

## Important assumptions

- The solver's memory and interconnect requirements are measured, not inherited unquestioningly from an old design.
- Logical quotas and a server catalog do not establish a complete physical allocation.
- Vendor delivery forecasts and purchase orders are not equivalent to commissioned infrastructure.
- Maintenance and recovery headroom remain unavailable for routine research unless their owners approve the risk.
- A smaller cluster may not scale execution time linearly; test before rescheduling the business review.

## Relevant CapOps capabilities

- **Capacity visibility:** inventory compatibility and dependency status, not just free resources.
- **Workload placement:** identify complete, qualified placement combinations.
- **Capacity acquisition:** coordinate physical delivery, installation, licensing, and acceptance.
- **Capacity optimization:** identify data stalls and configuration inefficiency.
- **Capacity risk management:** connect a delayed dependency to the campaign decision deadline.

## Recommended actions

1. Draw the service chain from dataset preparation through compute, fabric, scratch storage, result validation, and archive. Give each prerequisite an owner.
2. Build a compatibility matrix for candidate workers. Distinguish installed, healthy, connected, licensed, schedulable, and performance-validated capacity.
3. Test the full chain with a representative problem. Measure elapsed useful work and storage contention rather than accepting an isolated processor benchmark.
4. Sequence procurement and commissioning around the slowest prerequisite. Obtain qualified facilities approval for changes to power, cooling, or physical installation.
5. Assign a bounded campaign window with checkpoint, cancellation, and reclaim rules. Coordinate with other research and continuity users of the same infrastructure.
6. Decide by the review deadline whether to use the full group, run a reduced campaign, or move the design review. Record what the alternative does not validate.

## Potential alternatives

Reduce the simulation parameter sweep, use a validated lower-resolution model for early screening, run an eight-worker campaign, or move to another qualified environment. More memory on fewer workers may help one bottleneck but worsen runtime or licensing economics. An alternative is useful only if its scientific and business outputs remain acceptable.

## FinOps considerations

Include software entitlements, storage, network equipment, facilities changes, idle partially commissioned hardware, and the cost of delayed design decisions. Purchased equipment can be financially committed before it is usable. A low server unit price does not establish a low cost per validated simulation.

## Residual risks

Component failure, installation delays, software incompatibility, or shared-storage contention can block the campaign. A successful small test may not represent full-group communication behavior. Reserving an internal calendar slot does not replace health and readiness checks.

## Common mistakes

- Adding cores across incompatible hosts and calling the total usable capacity.
- Ordering compute before confirming the network, storage, and facility plan.
- Treating software licenses or internal quotas as physical supply.
- Assuming a vendor delivery estimate is an accepted service-ready date.
- Dividing the job into smaller pieces without validating the solver's behavior.

## Example decision record

| Field | Illustrative record |
| --- | --- |
| Decision | Approve the 16-worker campaign only after full-chain acceptance; prepare an eight-worker reduced-scope fallback |
| Accountable owner | Engineering program owner; infrastructure lead owns technical acceptance and facilities lead owns installation approval |
| Decision deadline | 2027-10-04 |
| Evidence required | Compatibility matrix, license confirmation, full-chain benchmark, facility acceptance, campaign and recovery-allocation schedule |
| Trade-off | Fund prerequisite validation before acquiring more workers; accept narrower simulation coverage if the fallback is needed |
| Residual risk accepted | Full campaign completion remains exposed to component failures and untested problem complexity |
| Revisit | At acceptance, after a dependency change, or immediately on a missed commissioning milestone |
| Release condition | Return worker and scratch allocations after result validation, archival, and secure cleanup |

## Related content

- [Capacity visibility](../capabilities/capacity-visibility.md)
- [Capacity acquisition](../capabilities/capacity-acquisition.md)
- [Workload capacity profile](../templates/workload-capacity-profile.md)
- [Artificial intelligence and graphics processing unit capacity](ai-and-gpu-capacity.md)
