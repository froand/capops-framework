# Cloud migration

Use this scenario to make a large migration conditional on evidence of deployability, rather than treating an approved migration budget as delivery readiness. It illustrates the proposed CapOps practice, not a provider program.

## Business context

A fictional distributor plans to move 240 virtual machines from a leased facility in six waves. The lease expiry creates a business deadline, but an interrupted order-processing service would be more costly than a short extension. Procurement must therefore keep the extension decision open until migration evidence supports closing it.

All quantities, dates, and thresholds below are illustrative assumptions, not industry statistics or statements about provider capacity.

## Capacity challenge

The target estate mixes general-purpose workers and memory-intensive databases. Wave overlap, data-copy workers, rollback environments, and destination recovery capacity make the migration peak different from the eventual steady state. An unused quota allowance is permission to deploy, not evidence that the required physical resources can be supplied.

## Demand dimensions

| Dimension | Example demand to record |
| --- | --- |
| Business unit and service | Order processing first; reporting and archival services later |
| Resource shape | 180 general-purpose and 60 memory-intensive virtual machines; map each to measured memory, processing, storage, and network needs |
| Placement | Approved primary region with two failure domains; separate approved recovery region for critical services |
| Quantity and concurrency | Six waves of 40; model cumulative target demand plus 20 temporary migration workers, without counting the same worker in two categories |
| Timing | First wave on 2027-03-01; weekly windows; lease decision on 2027-02-12 |
| Recovery and rollback | Separate profiles for the first 12 critical machines, shared dependencies, and the source systems retained for rollback |
| Flexibility | Reporting can move later; database substitutions require application-owner testing |

## Important assumptions

- The source inventory is complete, but its machine sizes are not automatically the right target sizes.
- A target service's presence in a regional catalog does not establish quantity or deployment-date fulfillability.
- Submitted forecasts are planning information, not provider commitments.
- Source capacity remains available for rollback only while the lease, licenses, data synchronization, and operating support remain valid.
- Recovery demand is assessed alongside other workloads using the destination, not as an isolated migration exercise.

## Relevant CapOps capabilities

- **Capacity visibility:** reconcile inventory, application dependencies, and temporary resources.
- **Capacity forecasting:** build a time-phased wave profile and identify the highest overlap.
- **Quota management and capacity acquisition:** track permission separately from supported capacity arrangements and their conditions.
- **Workload placement and capacity resilience:** qualify substitute configurations and destination recovery.
- **Capacity risk management:** attach lease, launch, and rollback decisions to explicit evidence deadlines.

## Recommended actions

1. Map each wave to business services and dependency chains. Include identity, connectivity, storage throughput, deployment tooling, and operational support.
2. Compare the move-as-is option with tested modernization before locking the demand profile. Remove unused source resources rather than forecasting them forever.
3. Submit required quota changes and evaluate supported capacity mechanisms early. Record requested, accepted, allocated, and tested quantities as different states.
4. Rehearse the first wave with representative data and the intended deployment configuration. Test substitutions, migration throughput, and rollback, not only resource creation.
5. Hold a readiness decision before every wave. If required evidence is missing, reduce the wave, change placement within approved boundaries, or defer it.
6. Retain rollback capacity until the service owner accepts the migrated workload. Release temporary resources and update the next forecast from actual consumption.

## Potential alternatives

Extending the source lease buys time but adds expense. Smaller waves reduce simultaneous demand but lengthen dual operation. Replatforming selected services may reduce dependence on a narrow machine family, but introduces testing and schedule risk. These are business choices to compare, not automatic improvements.

## FinOps considerations

Compare complete transition costs: source extension, duplicate environments, data movement, testing, idle held capacity, and eventual steady-state usage. A financial discount does not establish deployment capacity unless the specific product explicitly includes that benefit. Avoid buying a long commitment for temporary migration workers merely because they appear in the peak forecast.

## Residual risks

Future waves can still encounter resource constraints after a successful first wave. Application behavior may change under production data, and a dependency may become the bottleneck after compute deployment succeeds. The source extension may also have a notice period that precedes final technical certainty.

## Common mistakes

- Treating 240 machines as one homogeneous request without dates or dependency order.
- Decommissioning the source immediately after deployment rather than after acceptance and rollback review.
- Assuming quota approval, a forecast acknowledgement, or a discount protects the lease-exit date.
- Counting the same recovery headroom as available to several simultaneous migrations.

## Example decision record

| Field | Illustrative record |
| --- | --- |
| Decision | Proceed with a 40-machine first wave only after rehearsal acceptance; retain the source extension option for later waves |
| Accountable owner | Migration sponsor; platform lead owns deployment evidence and service owners accept application results |
| Decision deadline | 2027-02-12, before the lease-extension notice expires |
| Evidence required | Versioned wave profile, quota approvals, actual capacity-arrangement state where supported, representative migration and rollback results, destination dependency checks |
| Trade-off | Accept bounded dual-running expense rather than making an unsupported exit-date commitment |
| Residual risk accepted | Subsequent waves may be delayed; sponsor owns the resulting lease and sequencing exposure |
| Revisit | After each wave, or immediately if the target configuration changes or rehearsal fails |
| Release condition | Source and temporary capacity released only after service acceptance and rollback expiry |

## Related content

- [Build a demand forecast](../implementation/build-a-demand-forecast.md)
- [Workload capacity profile](../templates/workload-capacity-profile.md)
- [Capacity-risk register](../templates/capacity-risk-register.md)
- [Legacy resource modernization](legacy-resource-modernization.md)
