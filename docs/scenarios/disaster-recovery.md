# Disaster recovery

Use this scenario to validate disaster recovery (DR) capacity for a portfolio, not just an individual application's failover procedure. Backups and replication are necessary evidence for some designs, but are not evidence of destination compute and dependency capacity.

## Business context

A fictional service cooperative runs enrollment, billing, and reporting in one primary region. Their recovery plans nominate the same destination region. Each application previously passed an isolated exercise, but the continuity owner now needs a decision about a simultaneous primary-region loss.

The quantities, dates, and recovery targets here are illustrative organization-defined choices, not universal requirements.

## Capacity challenge

The destination already supports normal business. Recovery adds multiple workloads, shared identity and network services, restoration workers, and temporary reprocessing demand. Three individually feasible plans can compete for the same headroom during a correlated event.

## Demand dimensions

| Recovery component | Example profile |
| --- | --- |
| Existing destination business | 24 worker equivalents that continue to run during recovery |
| Enrollment | 20 general-purpose worker equivalents needed within two hours |
| Billing | 16 memory-intensive worker equivalents needed within six hours |
| Reporting | 12 workers deferrable for up to 24 hours with sponsor approval |
| Temporary recovery work | Eight additional restoration/reprocessing workers during the first six hours |
| Placement | Approved destination region; explicit failure-domain and data-location constraints per service |
| Dependencies | Identity, naming, keys, network throughput, storage restore rates, deployment tooling, licenses, and responders |
| Concurrency | First six hours require 24 + 20 + 16 + 8 = 68 worker equivalents, with separate resource-shape and dependency checks |

Worker equivalents are a modeling shorthand, not interchangeable machines. The detailed profile retains memory, processing, storage, and connectivity requirements for each recovery set.

## Important assumptions

- Recovery time is measured from the declared event, including allocation, restore, validation, and routing.
- Reporting can actually be paused; its data dependencies must not block enrollment or billing.
- Existing destination workloads cannot be evicted merely because the DR plan omitted them.
- Quota and a successful earlier test do not guarantee physical capacity during a future event.
- Any held capacity is identified by configuration and quantity; do not count one allocation as dedicated to several simultaneous recovery sets.

## Relevant CapOps capabilities

- **Capacity resilience:** validate combined recovery states and sequencing.
- **Capacity visibility and forecasting:** inventory destination commitments, concurrent demand, and temporary restore resources.
- **Capacity allocation:** approve minimum service levels, priorities, and reclaim conditions.
- **Capacity acquisition:** assess supported arrangements for the exact recovery resources.
- **Capacity risk management:** make gaps against recovery objectives visible to the continuity owner.

## Recommended actions

1. Define the event being tested: application failure, failure-domain loss, or region loss. Each has a different concurrency envelope.
2. Build recovery sets around dependency order, not organizational boundaries. Restore shared foundations before dependent workloads.
3. Model each time interval, including existing destination demand and restoration overlap. Test storage and network throughput, not only worker counts.
4. Establish evidence for destination permissions and any supported capacity arrangement. Record what remains dependent on deployment-time availability.
5. Rehearse simultaneous allocation and restore, or document the limits of a smaller exercise. A tabletop review alone does not validate deployment or throughput.
6. Approve degraded service, deferral, and stop conditions. Re-test after architecture, volume, destination allocation, or recovery-objective changes.

## Potential alternatives

Maintain more running destination capacity, spread recovery sets across approved destinations, extend a noncritical recovery objective, or reduce service functionality during recovery. More destinations add operating and data complexity and do not automatically guarantee capacity. A smaller service may reduce compute demand while preserving its essential business function.

## FinOps considerations

Treat unused recovery capacity as an explicit risk treatment rather than automatically labeling it waste. Compare the carrying cost with an approved business-impact assessment and the cost of alternative recovery designs. Include replication, restore tests, retained licenses, data movement, and emergency operations. Record who may release a recovery allocation and who accepts the increased risk.

## Residual risks

The actual incident can exceed the tested failure envelope. Shared control services, staffing, or connectivity may fail together. Test results establish what worked at a point in time; they do not prove future inventory or end-to-end recovery in every event.

## Common mistakes

- Adding only displaced production demand and omitting destination business or restore workers.
- Summing unlike machine shapes into an apparently sufficient processor total.
- Testing workloads one at a time and calling the portfolio recovered.
- Assuming redundancy or replication creates recovery capacity.
- Reclaiming a dormant recovery allocation without continuity approval.

## Example decision record

| Field | Illustrative record |
| --- | --- |
| Decision | Prioritize enrollment and billing; defer reporting for up to 24 hours; validate the six-hour combined demand envelope |
| Accountable owner | Business continuity owner, with service-owner acceptance of degraded operation |
| Decision deadline | 2027-05-07, before the next recovery-readiness review |
| Evidence required | Recovery-set map, interval demand calculation, quota and allocation records, concurrent restore exercise, measured data and network throughput |
| Trade-off | Carry additional destination headroom and accept delayed reporting rather than claim all services recover immediately |
| Residual risk accepted | Wider correlated failures and untested demand above the envelope remain possible |
| Revisit | After each exercise, a material demand change, or any reallocation of destination headroom |
| Release condition | Continuity owner approves an alternative treatment before protected allocations are reduced |

## Related content

- [Capacity resilience](../capabilities/capacity-resilience.md)
- [Capacity-risk register](../templates/capacity-risk-register.md)
- [Multi-region design](multi-region-design.md)
- [Capacity-constrained prioritization](capacity-constrained-prioritization.md)
