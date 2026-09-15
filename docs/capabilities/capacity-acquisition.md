# Capacity acquisition

This page explains how Capacity Operations (CapOps) evaluates ways to obtain required resources. It connects technical matching, business criticality, commercial approval, and residual risk without assuming a universal capacity mechanism.

## Definition

Capacity acquisition is the evaluation and authorized use of supported mechanisms and sourcing options for a specific demand requirement, including their scope, conditions, evidence, obligations, and remaining uncertainty.

## Purpose

Choose a proportionate capacity path before the latest useful decision date and document exactly what that path does and does not support.

## Why it matters

A fixed-date critical workload and a flexible batch task may require different responses. Options can include deployment under normal service conditions, supported capacity reservations, private-infrastructure procurement, staged demand, or a qualified architectural alternative. No universal hierarchy makes one mechanism right for every workload.

Provider engagement can clarify supported paths and coordinate requests. It is not stronger assurance by itself. A forecast, quota approval, and financial discount remain distinct from a documented capacity mechanism.

## Desired outcomes

- Each chosen mechanism matches an explicit demand version and technical scope.
- Required technical, financial, and contractual approvals are distinguishable.
- Uncovered quantities, dates, and dependencies remain visible.
- Every commitment has consumers, owners, review dates, and exit conditions.

## Inputs

- Approved demand dimensions, criticality, required dates, ramp, and duration.
- Qualified configurations and the time and cost to switch to alternatives.
- Applicable quota, eligibility, and dependency requirements.
- Current authoritative public mechanism documentation and applicable commercial terms.
- Existing commitments, allocation records, budget authority, and recovery obligations.

## Activities

1. Define the requirement: service, family, quantity and unit, region, zone, date, ramp, duration, priority, and permitted flexibility.
2. Compare each supported option with that requirement. Record eligibility, technical matching, quantity limits, dates, exclusions, operational dependencies, and evidence source.
3. Separate any commercial discount from any deployment-related commitment. Use “capacity assurance” or “capacity guarantee” only when the specific mechanism's current public documentation supports the term and conditions are stated.
4. Evaluate alternatives such as staging, scheduling, modernization, or pre-positioning resources where justified. Include idle-resource costs, switching effort, and inability to reacquire after release.
5. Obtain approval from the technical authority and designated financial or commercial approver. The business risk owner accepts any remaining delivery or recovery exposure.
6. Execute through supported processes and verify the resulting state. Store a record of the actual mechanism, not just the request.
7. Assign consumers, monitoring, review, renewal or change, and release or expiry actions. If requirements change, rematch the mechanism rather than assuming continued coverage.

## Outputs

- An options comparison with technical fit, cost, lead time, and residual exposure.
- An authorized decision tied to the selected demand version.
- Mechanism or procurement evidence, conditions, and verification results.
- A commitment lifecycle record and unmatched-demand risk actions.

## Roles involved

Architects and engineering assess technical matching and execution. FinOps evaluates economic trade-offs. Procurement and authorized signatories own contractual actions. Business owners approve priority and business risk. Provider representatives explain supported mechanisms within their authority. The CapOps practitioner connects the records and review deadlines; it cannot create provider obligations through coordination.

## Dependencies on other capabilities

- [Capacity forecasting](capacity-forecasting.md) defines the demand version being evaluated.
- [Workload placement](workload-placement.md) identifies technically acceptable alternatives.
- [Quota management](quota-management.md) checks administrative prerequisites separately.
- [Capacity allocation](capacity-allocation.md) assigns the acquired or committed pool without double-counting consumers.
- [Capacity governance](capacity-governance.md) establishes approvals and lifecycle controls.

## Suggested measurements

Targets are **organization-defined**. Report mechanism types separately rather than inventing one assurance score.

| Measure | Definition | Limitation |
|---|---|---|
| Mechanism-matched demand | Required units matched to a verified supported capacity mechanism / required units in one compatible service, family, location, and time bucket × 100 | This is conditional mechanism coverage, not a fulfillment probability; disclose exclusions and supporting-resource gaps |
| Decision readiness | Acquisition decisions with documented options, technical fit, approval, and residual risk by deadline / all acquisition decisions due in the period × 100 | A complete decision can still accept exposure; do not label it “secured” |
| Lifecycle ownership | Active commitment records with consumer, technical owner, commercial owner where applicable, review date, and exit condition / all active commitment records × 100 | Record completeness does not prove the terms are still appropriate or resources usable |

## Maturity indicators

- **Reactive:** Teams seek resources after a deadline is threatened, with unclear terms or ownership.
- **Aware:** Selected mechanisms are understood, but matching and post-acquisition verification vary.
- **Managed:** Critical acquisitions use documented comparisons, authorized approvals, verification, and owned lifecycle records.
- **Optimized:** Demand changes and usage evidence trigger rematching, renewal, reallocation, or release reviews.
- **Strategic:** Portfolio and architecture choices account for sourcing flexibility, conditional mechanisms, commercial exposure, and acquisition lead times.

## Practical example

A fictional launch needs 60 compatible workers for a fixed window. The team evaluates a documented capacity mechanism for 40 workers and a staged launch using those 40. It does not report the original 60 as fully covered. The product owner approves staged scope, the commercial authority approves applicable terms, and engineering verifies the mechanism's configuration. Later growth remains a separate forecast and acquisition decision.

## Risks and common mistakes

- Inferring mechanism support from another service, family, region, or zone.
- Treating informal reassurance, a forecast submission, or a discount purchase as capacity evidence.
- Ignoring storage, networking, licensing, or control-service prerequisites.
- Buying capacity without a consumer or assuming unused commitments can be cancelled.
- Counting one commitment against several simultaneous demand lines.

## Related content

- [Secure and allocate capacity domain](../domains/secure-and-allocate-capacity.md)
- [CapOps and FinOps](../overview/capops-and-finops.md)
- [Capacity risk management](capacity-risk-management.md)
- [Capacity optimization](capacity-optimization.md)
