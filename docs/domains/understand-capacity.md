# Understand capacity

This Capacity Operations (CapOps) domain establishes what the organization knows about demand, use, constraints, and exposure. It makes the difference between observed facts and unverified assumptions visible before planning or approval.

## Objective

Create a customer-side consolidated view of workload demand, consumption, administrative limits, supported commitments, dependencies, deployment outcomes, and business risk. Record scope and freshness so reviewers know what the evidence can support.

## Business outcome

Decision-makers can identify which milestones or recovery obligations need action, who owns them, and what evidence is missing. This view is not a provider physical-inventory system and should not be presented as one.

## Included capabilities

- **Primary:** [Capacity visibility](../capabilities/capacity-visibility.md) and [capacity risk management](../capabilities/capacity-risk-management.md).
- **Supporting:** [Reporting and key performance indicators](../capabilities/reporting-and-kpis.md) makes the evidence decision-ready; [automation](../capabilities/automation.md) can collect and reconcile it consistently.

## Main activities

1. Select a workload population and name its business and technical owners.
2. Normalize records by workload, service, family, resource unit, region, zone, and time window.
3. Keep consumption, quota, forecasts, mechanism coverage, and allocation separate.
4. Map shared dependencies, including recovery destinations and specialized resources.
5. Classify deployment failures using available evidence; leave unresolved causes unknown.
6. Convert material uncertainty into a risk with impact, options, owner, and a decision deadline.

## Primary inputs

- Workload and service inventories with ownership and criticality.
- Observed use, deployment attempts, scaling events, and incident evidence.
- Demand submissions, current forecasts, quota records, and commitment terms.
- Architecture dependencies, location restrictions, and recovery requirements.
- Source timestamps, missing-data notices, and collection permissions.

## Expected outputs

- A scoped workload capacity view with links to its source evidence.
- An evidence-quality backlog for stale, missing, or contradictory records.
- A dependency and concentration view that preserves resource and location specificity.
- Prioritized risk records linked to business milestones and decision owners.

Each output should state its population and observation period. A blank field must not silently become zero demand or zero risk.

## Participating personas

The CapOps practitioner stewards the combined view. Platform engineering and operations supply resource and deployment evidence. Business and product owners supply criticality and impact. Architects explain dependencies; continuity teams supply recovery context; FinOps and procurement reconcile commitments. Workload owners remain accountable for the accuracy of their demand and accepted business exposure.

## Example decisions

- Whether a launch profile is sufficiently complete to enter forecasting.
- Whether a deployment failure is an administrative limit issue, a confirmed resource constraint, or still unclassified.
- Whether a recovery destination shared by several critical services requires a portfolio review.
- Whether stale mechanism evidence must be refreshed before acquisition or allocation is approved.

## Risks and common mistakes

- Summing incompatible units or treating quota headroom as deployable supply.
- Inferring current physical inventory from a regional service catalog.
- Building a complete-looking dashboard that hides unobserved workloads.
- Collecting sensitive operational detail beyond what a decision needs.

## Related content

- [Domain catalog](../framework/domains.md)
- [Plan capacity](plan-capacity.md)
- [Capacity visibility](../capabilities/capacity-visibility.md)
- [Capacity risk management](../capabilities/capacity-risk-management.md)
