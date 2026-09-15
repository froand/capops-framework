# Workload placement

This page explains how Capacity Operations (CapOps) evaluates where and on what configuration a workload can run. It distinguishes a genuine, qualified alternative from a location or resource family that is merely listed as available.

## Definition

Workload placement selects technically, operationally, legally, and economically acceptable providers or infrastructure environments, regions, zones, services, and resource families for production, growth, and recovery.

## Purpose

Keep a credible primary capacity path and a documented set of alternatives whose switching effort and limitations are understood.

## Why it matters

A narrow dependency on one family or location can restrict the response to a deployment problem. However, more options are not automatically better: an alternate placement can introduce data movement, latency, licensing, operational, or recovery problems. Flexibility must be qualified against the complete workload, not inferred from compute compatibility alone.

Multi-region architecture can reduce concentration risk and create options. It does not guarantee capacity or prove that destinations have independent dependencies.

## Desired outcomes

- Hard constraints are distinguishable from preferences and inherited assumptions.
- Primary and alternative placements meet agreed acceptance criteria.
- Switching lead time is reflected in decision deadlines.
- Single-family, single-location, and shared-dependency exposures have owners.

## Inputs

- Business criticality, dates, demand quantities, and acceptable degraded service.
- Performance requirements, dependency maps, data classification, and location restrictions.
- Service and family compatibility information from current public sources.
- Deployment, load, data-path, and recovery test evidence.
- Cost, licensing, migration effort, operating skills, and supported mechanism constraints.

## Activities

1. List mandatory constraints and record their owner and rationale. Separate legal or safety requirements from design preferences.
2. Build candidate configurations across service, family, region, zone, topology, and deployment pattern. Consider modernization rather than only moving an unchanged legacy design.
3. Reject candidates that fail mandatory constraints before scoring preferences. Obtain specialist review for compliance, security, and contractual questions.
4. Define tests for performance equivalence, dependency compatibility, operational access, recovery behavior, and data movement.
5. Compare acceptable candidates by capacity path, cost, switching time, complexity, and failure concentration. Use organization-defined weights only after hard constraints pass.
6. Record the selected primary placement and each alternative's readiness state: identified, under evaluation, qualified for a stated scope, or invalidated.
7. Revalidate on material architecture, demand, mechanism, policy, or dependency changes. Keep a decision deadline that allows the chosen fallback to be prepared and executed.

## Outputs

- A placement decision with constraint rationale and rejected options.
- A qualification matrix for primary and alternate configurations.
- Switching runbooks, effort estimates, and readiness evidence.
- A concentration-risk view and unresolved acceptance actions.

## Roles involved

The designated architecture authority owns design suitability. Engineering and operations test deployability and operability. Business owners decide scope and timing trade-offs. Continuity teams assess recovery fit; FinOps and procurement assess cost and terms. Specialists approve constraints in their mandates. The CapOps practitioner coordinates evidence and deadlines, not unilateral changes to approved placement.

## Dependencies on other capabilities

- [Capacity forecasting](capacity-forecasting.md) specifies quantities and timing for each candidate.
- [Capacity resilience](capacity-resilience.md) validates destination and failure-domain assumptions.
- [Capacity acquisition](capacity-acquisition.md) checks whether supported mechanisms actually match the candidate.
- [Capacity optimization](capacity-optimization.md) can remove legacy dependencies and expand the candidate set.

## Suggested measurements

Targets and qualification freshness rules are **organization-defined**.

| Measure | Definition | Limitation |
|---|---|---|
| Qualified-alternative coverage | In-scope critical workloads with at least one current alternative qualified against stated acceptance criteria / all in-scope critical workloads × 100 | An alternative is not reserved supply; show workloads for which mandatory constraints prohibit alternatives |
| Concentration exposure | Critical workloads with only one qualified placement for the assessed scenario / all critical workloads assessed for that scenario × 100 | Workload counts do not express business impact; list critical shared dependencies separately |
| Switching readiness | Alternatives exercised within their maximum allowed switching time / all alternatives exercised in the period × 100 | Excludes untested alternatives; publish their count and avoid extrapolating a small test to full-scale switching |

## Maturity indicators

- **Reactive:** Teams search for another region or family only after deployment is blocked.
- **Aware:** Potential alternatives are documented, but qualification and constraint ownership are uneven.
- **Managed:** Placement decisions include hard constraints, tested scope, switching lead time, and review triggers.
- **Optimized:** Repeated qualification and operational feedback keep alternatives current and remove unnecessary rigidity.
- **Strategic:** Portfolio architecture deliberately balances concentration, economics, operability, and sourcing flexibility.

## Practical example

A fictional regulated service is restricted to two approved locations. Its preferred family is not the only possible configuration, but an alternate family requires more instances to meet throughput. Engineering benchmarks the complete service, including storage and network paths. The architect qualifies the alternate quantity, procurement checks licensing implications, and the forecast records the new resource shape. A second location remains an option, not evidence of future fulfillment.

## Risks and common mistakes

- Counting regions on a service catalog as ready placements.
- Assuming two families have equivalent performance because their resource counts match.
- Moving compute without validating data, network, identity, or licensing dependencies.
- Accepting an alternative whose preparation time exceeds the decision window.
- Treating multi-region complexity as inherently valuable without a business case.

## Related content

- [Plan capacity domain](../domains/plan-capacity.md)
- [Capacity risk management](capacity-risk-management.md)
- [Quota management](quota-management.md)
- [Architecture flexibility principle](../overview/principles.md#7-architecture-flexibility-reduces-capacity-risk)
