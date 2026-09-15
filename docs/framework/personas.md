# CapOps personas

This page defines the ten perspectives needed for Capacity Operations (CapOps) decisions. Personas describe contributions and decision rights, not mandatory job titles. One person may cover several perspectives, and a large organization may distribute one perspective across several teams.

## Executive sponsor

- **Contributes:** Strategic direction, risk appetite, support for cross-functional participation, and authority to resolve portfolio conflicts.
- **Supports decisions:** Which outcomes take priority, which systemic exposures require investment, and which risks exceed delegated authority.
- **Consumes:** Business impact, feasible options, costs, critical decision deadlines, and unresolved cross-portfolio risks.
- **Provides:** Priority rules, escalation thresholds, delegated authority, and sponsorship for agreed improvements.
- **Accountability remains:** With the executive for decisions within that executive's mandate. Sponsorship does not make the executive the technical approver of every deployment or remove workload owners' obligations.

## CapOps practitioner or lead

- **Contributes:** Central practice stewardship, common definitions, evidence reconciliation, review facilitation, and follow-through across teams.
- **Supports decisions:** Which gaps need review, which records are decision-ready, and which practice improvements should be proposed.
- **Consumes:** Demand versions, quota and mechanism evidence, allocation records, deployment outcomes, and workload risk assessments.
- **Provides:** Consolidated capacity posture, linked risk and decision records, action tracking, reporting definitions, and improvement proposals.
- **Accountability remains:** With the practitioner for practice quality and coordination within delegated scope. Business risk, purchases, technical approvals, and operational changes remain with their authorized owners unless explicitly delegated.

## Business and product owner

- **Contributes:** Outcomes, demand drivers, customer obligations, criticality, delivery timing, and flexibility in scope or schedule.
- **Supports decisions:** Whether to stage a launch, defer lower-priority demand, fund an alternative, or accept residual business exposure.
- **Consumes:** Capacity options, likely service or milestone impacts, cost estimates, evidence limitations, and decision deadlines.
- **Provides:** Owned business forecasts, priority, acceptable degraded service, change notices, and authorized trade-off decisions.
- **Accountability remains:** With the relevant business owner for demand intent and business risk acceptance within that owner's authority. Technical suitability and commercial approval still need their respective owners.

## Enterprise and solution architect

- **Contributes:** Translation from business requirements to services, resource families, dependencies, placement constraints, and alternatives.
- **Supports decisions:** Primary and alternative architectures, modernization, location choices, and acceptable patterns for scale and recovery.
- **Consumes:** Demand ranges, security and regulatory requirements, performance evidence, capacity risks, and switching costs.
- **Provides:** Technical profiles, dependency maps, constraint rationale, alternative qualification criteria, and architecture decisions.
- **Accountability remains:** With the designated architecture authority for design suitability and exceptions. Architectural approval alone does not approve expenditure or prove deployable capacity.

## Platform and cloud engineering

- **Contributes:** Implementation knowledge, quota scope mapping, deployment validation, allocation enforcement, platform standards, and automation.
- **Supports decisions:** Which resource configurations can be deployed safely, when limit changes are needed, and how to implement approved capacity actions.
- **Consumes:** Approved placements, dimensioned forecasts, priorities, mechanism conditions, policies, and operational requirements.
- **Provides:** Limit and usage evidence, configuration tests, deployment outcomes, controlled implementation plans, and platform constraints.
- **Accountability remains:** With engineering owners for platform controls and authorized execution. Engineering cannot silently reprioritize business demand or accept a commercial commitment outside its mandate.

## Operations and reliability

- **Contributes:** Observed load, scaling behavior, deployment failure analysis, incidents, operational dependencies, and service performance.
- **Supports decisions:** Alert thresholds, safe headroom, remediation, change timing, rollback, and operational readiness.
- **Consumes:** Workload objectives, forecasts, allocation policies, recovery plans, and approved changes.
- **Provides:** Timestamped telemetry, classified failures, runbooks, exercised scale limits, and evidence of operational impact.
- **Accountability remains:** With authorized service and operations owners for operational acceptance and changes. Operations may recommend a risk response; business risk acceptance remains with the appropriate risk owner.

## Business continuity and disaster recovery

- **Contributes:** Business impact analysis, recovery scenarios, minimum viable service requirements, and portfolio-level recovery coordination.
- **Supports decisions:** Recovery sequence, recovery objectives, exercise scope, shared destination assumptions, and prioritization during a disruption.
- **Consumes:** Dependency maps, production and peak profiles, destination allocations, supported mechanisms, and exercise results.
- **Provides:** Recovery capacity profiles, simultaneous recovery scenarios, test acceptance criteria, unresolved gaps, and revalidation triggers.
- **Accountability remains:** With continuity owners for the continuity process and evidence, and with business service owners for recovery requirements and accepted shortfalls. Platform teams remain responsible for implementing their recovery actions.

## FinOps practitioner

- **Contributes:** Cost and usage analysis, unit economics, financial accountability, commitment economics, and value-based trade-off analysis.
- **Supports decisions:** Whether an alternative is economically viable, how idle commitments should be treated, and which optimization proposals merit approval.
- **Consumes:** Technical demand, time windows, allocation and commitment records, placement alternatives, and recovery obligations.
- **Provides:** Comparable cost scenarios, financial exposure, attribution, and economic assumptions with their limitations.
- **Accountability remains:** With FinOps for its analysis and assigned financial processes, and with authorized budget or business owners for expenditure and value decisions. A financial approval is not capacity evidence.

## Procurement and commercial management

- **Contributes:** Contract interpretation, purchase processes, supplier coordination, renewal management, and commercial controls.
- **Supports decisions:** Which terms are acceptable, who may commit funds, and whether a commitment can be changed, transferred, renewed, or ended.
- **Consumes:** Approved requirements, timing, technical matching, funding authority, consumer ownership, and residual-risk analysis.
- **Provides:** Applicable contractual scope, purchase records, notice periods, obligations, expiry dates, and approved commercial decisions.
- **Accountability remains:** With authorized commercial signatories for contractual actions. Procurement should not infer technical coverage from a product name or replace technical acceptance.

## Cloud or service-provider representative

- **Contributes:** Explanation of supported public mechanisms, their documented scope, and coordination through established engagement channels.
- **Supports decisions:** Which supported paths merit evaluation and what information is needed to assess a request.
- **Consumes:** Approved demand dimensions, timelines, permitted alternatives, and appropriately scoped technical questions.
- **Provides:** Documented mechanism information, formal responses where applicable, known requirements within authorized disclosure, and next steps.
- **Accountability remains:** With the provider for obligations actually established under applicable terms and with the customer for its own placement, spending, risk, and readiness decisions. A conversation or forecast submission does not establish a provider commitment.

## Put the personas to work

For a decision, name one accountable owner with appropriate authority, then identify responsible executors and consulted perspectives. Record any delegation explicitly. Different decisions within the same plan can have different owners: a product owner changes a launch date, an architect accepts a design alternative, a commercial approver authorizes a purchase, and operations executes a deployment.

Central stewardship should reconcile conflicting information and surface unresolved decisions. Federated workload teams should keep demand, evidence, and risk records current. Use substitutes and escalation paths so a decision does not stall when one contributor is unavailable.

## Risks and common mistakes

- Making the CapOps lead accountable for every decision without corresponding authority.
- Treating a provider representative as responsible for the customer's delivery or recovery plan.
- Omitting continuity, procurement, or business owners until a decision is already irreversible.
- Requiring ten new job titles rather than ensuring ten perspectives are represented.
- Confusing “consulted” with “approved” or leaving multiple people vaguely accountable for one trade-off.

## Related content

- [People, process, and technology](../overview/people-process-technology.md)
- [Capacity governance](../capabilities/capacity-governance.md)
- [Capacity allocation](../capabilities/capacity-allocation.md)
- [Operating model](../operating-model/operating-model.md)
