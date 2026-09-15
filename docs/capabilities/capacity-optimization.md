# Capacity optimization

This page explains how Capacity Operations (CapOps) improves useful capacity consumption and flexibility. It focuses on changes that can be validated without sacrificing agreed performance, delivery, or recovery obligations.

## Definition

Capacity optimization evaluates and implements changes to resource size, scheduling, allocation, architecture, and lifecycle state to improve useful utilization and reduce unnecessary or rigid dependencies.

## Purpose

Make existing capacity more useful, release genuinely unnecessary demand, and qualify less restrictive configurations while preserving service outcomes.

## Why it matters

Low utilization can indicate waste, temporary demand, a burst buffer, or intentional recovery standby. These need different decisions. Conversely, high average utilization can conceal poor throughput, saturation at peaks, or insufficient time to scale. Financial savings and capacity improvements should be assessed together but not treated as identical outcomes.

## Desired outcomes

- Idle allocations with no justified purpose are reclaimed or reassigned.
- Workload performance and recovery obligations remain within approved bounds.
- Legacy family or location dependencies are reduced where alternatives are practical.
- Resource release and remaining commercial obligations are tracked separately.

## Inputs

- Usage distributions, service throughput, latency, scaling delay, and saturation evidence.
- Production, peak, and recovery profiles with critical dependencies.
- Commitment and allocation terms, consumer ownership, and expiry dates.
- Workload schedules, migration plans, retirement approvals, and modernization candidates.
- Cost scenarios, change windows, validation criteria, and rollback constraints.

## Activities

1. Classify low-use resources as expected standby, temporary overlap, burst headroom, unexplained idle, or telemetry unknown.
2. Identify changes such as rightsizing, batching, time-shifting, sharing compatible pools, removing unused deployments, or qualifying modern resource families.
3. Evaluate the complete service outcome and constraints. Include licenses, storage and network bottlenecks, scaling delay, and the cost of holding or reacquiring capacity.
4. Obtain approval from workload, operational, continuity, and commercial owners as required. A financial target does not authorize removing a recovery reserve.
5. Test a bounded change against throughput, peak, and recovery acceptance criteria. Establish stop conditions and a realistic rollback path before release.
6. Verify the effect after implementation. Update demand forecasts, allocation records, and commitment reviews, including obligations that continue despite resource release.
7. Reassess after demand changes; an optimization valid in one season or scenario may not be valid in another.

## Outputs

- A prioritized optimization backlog with expected benefit and service risk.
- Approved changes, validation evidence, and rollback or follow-up actions.
- Revised resource demand, released assignments, or qualified configurations.
- Separate technical capacity and economic outcome records.

## Roles involved

Operations and engineering analyze behavior and implement controlled changes. Workload owners approve service trade-offs. Architects qualify modernization. Continuity owners assess recovery impact. FinOps measures economics and procurement confirms contractual actions. The CapOps practitioner coordinates portfolio opportunities and evidence rather than authorizing every resource release.

## Dependencies on other capabilities

- [Capacity visibility](capacity-visibility.md) provides measured behavior and ownership.
- [Capacity resilience](capacity-resilience.md) distinguishes required standby from unnecessary use.
- [Capacity allocation](capacity-allocation.md) updates consumer assignments after reclaim.
- [Workload placement](workload-placement.md) qualifies new configurations.
- [Capacity forecasting](capacity-forecasting.md) incorporates verified efficiency changes rather than assumed savings.

## Suggested measurements

Targets and service acceptance bounds are **organization-defined**. Compare like-for-like periods or explain workload changes.

| Measure | Definition | Limitation |
|---|---|---|
| Useful work density | Completed qualifying work units / consumed homogeneous resource-hours in the observation window | Define qualifying work and quality criteria; increased density is not beneficial if latency or correctness deteriorates |
| Verified reclaim realization | Unit-hours actually removed from assignments after validation / unit-hours approved for reclaim in the same interval × 100 | Excludes protected standby; release does not prove future reacquisition or financial savings |
| Change acceptance rate | Completed optimization changes meeting all agreed performance and recovery checks / all completed optimization changes in the period × 100 | Publish failed, rolled-back, and untested changes; small samples are not evidence of broad effectiveness |

## Maturity indicators

- **Reactive:** Teams remove resources during cost pressure or add them after saturation without validating full effects.
- **Aware:** Optimization candidates are listed, but reserve purposes and commercial obligations are inconsistently understood.
- **Managed:** Changes have owners, service and recovery acceptance criteria, controlled execution, and verified outcomes.
- **Optimized:** Evidence-based scheduling, reclaim, and modernization are repeated with feedback from production and recovery tests.
- **Strategic:** Architecture and portfolio investment deliberately improve useful work and flexibility while balancing financial and continuity exposure.

## Practical example

A fictional batch platform runs nightly work on a legacy family. Engineers qualify a supported modern family and measure the full job, including storage throughput. The job can finish within its agreed window using fewer resource-hours, but the team retains a tested fallback during transition. After acceptance, it updates the forecast and releases the old allocation. FinOps records that an existing financial commitment may continue even though technical demand has fallen.

## Risks and common mistakes

- Pursuing maximum utilization without considering bursts or recovery.
- Treating missing measurements as evidence of waste.
- Releasing a resource before confirming rollback or reacquisition limitations.
- Reporting projected efficiency or savings as realized results.
- Assuming a modernization change improves capacity options without qualifying its dependencies.

## Related content

- [Operate and optimize capacity domain](../domains/operate-and-optimize-capacity.md)
- [CapOps and FinOps](../overview/capops-and-finops.md)
- [Capacity acquisition](capacity-acquisition.md)
- [Automation](automation.md)
