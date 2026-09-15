# Multi-region design

Use this scenario to compare placement alternatives and operating states in a multi-region architecture. Multiple regions create options, not an unconditional capacity guarantee.

## Business context

A fictional appointment-booking platform serves customers from two approved regions. Both regions handle normal traffic. The business wants booking to remain usable after either region is lost, but can temporarily disable nonessential recommendations.

All example loads, dates, and limits are illustrative and must be replaced with measured workload data.

## Capacity challenge

Normal traffic distribution conceals the surviving region's scale requirement. Compute, data replication, connection limits, and recovery/reprocessing capacity must all support the changed state. A service catalog entry in both regions establishes neither configuration equivalence nor supply for the needed quantity and date.

## Demand dimensions

| State or dimension | Example demand |
| --- | --- |
| Normal operation | 30 general-purpose workers in Region A and 30 in Region B |
| Region A unavailable | 60 production workers in Region B, plus 12 temporary recovery/reprocessing workers |
| Region B unavailable | The mirrored requirement in Region A; do not assume identical test results |
| Resource shape | Worker memory and processing profile, database throughput, connection concurrency, and network bandwidth |
| Timing | Architecture choice by 2027-06-04; failover rehearsal before a 2027-07-01 launch |
| Failure-domain placement | Explicit within-region separation and recovery placement for each dependency |
| Accepted degradation | Recommendations may pause; booking confirmation must still meet its locally defined response target |
| Flexibility | Alternative worker families or a third approved destination only after data, latency, and operating validation |

The 72-worker surviving-state total is not a plan to run 72 workers in each region continuously. The design decision must identify which capacity runs continuously, which is held through supported mechanisms, and which remains availability-dependent.

## Important assumptions

- Data consistency and routing behavior are tested for both failure directions.
- The failed region cannot be relied on for identity, deployment artifacts, or traffic management needed to recover.
- Pausing recommendations really frees the limiting resource; it may not relieve database pressure.
- Destination demand includes other services recovering from the same event.
- Quota is permission, and forecasting is planning; neither provides the missing deployment capacity.

## Relevant CapOps capabilities

- **Workload placement:** compare business constraints with technical alternatives.
- **Capacity resilience:** model full and degraded operating states.
- **Capacity forecasting:** quantify failover and reprocessing demand separately from steady usage.
- **Capacity acquisition and allocation:** identify scoped arrangements and who can consume them.
- **Capacity governance:** require a decision on any gap between the design promise and evidence.

## Recommended actions

1. Document normal, degraded, failover, and failback states. For each, specify minimum functionality and demand for the complete service chain.
2. Benchmark each approved configuration independently. Keep alternative-family tests current after application or data changes.
3. Decide how much surviving-region demand is pre-running, held using a supported arrangement, or dependent on future deployment. Show the uncovered portion explicitly.
4. Coordinate with portfolio owners using the same destination and allocation pool. Model their simultaneous recovery rather than assuming their demand disappears.
5. Test both failover directions, including allocation, data catch-up, routing, and user-visible service behavior.
6. Approve a degraded-service trigger if capacity or dependency checks fail. Validate failback so returning traffic does not create an unplanned second peak.

## Potential alternatives

Compare a smaller continuously running fallback service, greater steady headroom, a third approved placement, or a longer restoration target. Multi-region operation may not be appropriate for every service; a simpler design can be reasonable when its recovery objectives and residual risk are explicitly accepted.

## FinOps considerations

Model duplicate services, data transfer, replication, operational tooling, exercises, and unused held capacity. A lower compute unit price in an alternate location is not a complete cost comparison. Financial commitments must be assessed against where usage actually lands in both normal and failure states.

## Residual risks

A correlated dependency failure can affect both regions. Data movement or connection recovery can become the bottleneck even when worker capacity exists. Placement alternatives can narrow if regulatory or latency constraints change.

## Common mistakes

- Equating two regional deployments with enough capacity to absorb either one's traffic.
- Counting one pool as both growth headroom and simultaneous recovery headroom.
- Testing only the preferred failover direction.
- Treating every service in a second region as feature-, configuration-, and quantity-equivalent.
- Ignoring failback demand and temporary duplicate writes.

## Example decision record

| Field | Illustrative record |
| --- | --- |
| Decision | Retain two-region operation; approve a booking-only degraded mode until each surviving-state demand profile is validated |
| Accountable owner | Booking service owner; architecture lead owns placement tests and continuity lead owns portfolio coordination |
| Decision deadline | 2027-06-04 |
| Evidence required | Both directional load tests, dependency map, destination allocation records, data-consistency results, cost comparison |
| Trade-off | Accept temporary feature loss rather than represent normal 30-worker deployments as full failover capacity |
| Residual risk accepted | Correlated dependency failure and capacity beyond the tested envelope remain unresolved |
| Revisit | Before launch, after each material load change, and after every failover exercise |
| Release condition | Remove additional headroom only after revalidating the surviving-state design |

## Related content

- [Workload placement](../capabilities/workload-placement.md)
- [Capacity resilience](../capabilities/capacity-resilience.md)
- [Disaster recovery](disaster-recovery.md)
- [Regulated workloads](regulated-workloads.md)
