# Capacity governance

This page defines decision rights and lifecycle controls for Capacity Operations (CapOps). It helps teams embed capacity evidence into existing delivery and commercial processes without assigning every approval to a central practice lead.

## Definition

Capacity governance establishes who may decide, which evidence is required, what boundaries apply, and how exceptions and commitments are reviewed throughout the workload lifecycle.

## Purpose

Make material capacity choices explicit before architecture, funding, allocation, or delivery decisions become difficult to reverse.

## Why it matters

Capacity exposure often crosses decision boundaries: a product date changes, engineering uses a different family, and a financial commitment still applies to the old plan. Governance connects these changes to the right authority and evidence rather than relying on an informal approval or a permanently green status.

## Desired outcomes

- Material decisions have an authorized owner and traceable rationale.
- Delivery checkpoints examine current demand, placement, and recovery evidence.
- Commitments and allocations have lifecycle controls and consumers.
- Exceptions are deliberate, time-bound, and revisited before exposure becomes unacceptable.

## Inputs

- Business risk appetite, delegated authorities, and existing approval processes.
- Workload criticality, forecasts, architecture decisions, and recovery objectives.
- Mechanism and commercial terms, allocation policies, and operating constraints.
- Risk records, incident findings, and evidence-quality issues.
- Current standards, control exceptions, and review dates.

## Activities

1. Define decision categories and accountable authorities: business priority and risk, technical suitability, commercial commitment, operational change, and continuity acceptance.
2. Apply proportionate checkpoints at demand intake, architecture selection, purchase approval, migration or launch readiness, material change, and retirement.
3. Specify evidence for each checkpoint. For critical launch readiness, examine the demand version, primary placement, alternatives, limits, mechanism scope, peak profile, recovery profile, and unresolved risks.
4. Manage commitments through justification, approval, acquisition, assignment, consumption, periodic review, renewal or change, and release or expiry. Require consumer and commercial ownership where applicable.
5. Establish expiring exceptions with rationale, compensating measures, action owner, risk owner, review trigger, and decision deadline. Escalate expired exceptions rather than renewing them silently.
6. Link controls to delivery workflows and verify that enforcement matches policy. Keep emergency changes authorized and review them afterward.
7. Use incident and exercise findings to amend controls that are missing, ineffective, or unnecessarily burdensome.

## Outputs

- A decision-rights matrix and evidence requirements by checkpoint.
- Approved guardrails, lifecycle controls, and escalation rules.
- Decision records and an exception register with expiry and ownership.
- Control-review actions based on observed outcomes.

## Roles involved

The executive sponsor establishes authority and resolves systemic conflicts. The CapOps practitioner stewards the practice and review records. Business owners retain priority and risk decisions; architecture authorities retain design approval; authorized signatories retain financial and contractual approval; engineering and operations retain controlled execution; continuity owners retain their review obligations.

## Dependencies on other capabilities

- [Capacity risk management](capacity-risk-management.md) supplies the exposure and escalation rationale.
- [Capacity acquisition](capacity-acquisition.md) supplies mechanism conditions and commitment obligations.
- [Capacity allocation](capacity-allocation.md) implements authorized consumer and priority decisions.
- [Reporting and key performance indicators](reporting-and-kpis.md) shows overdue decisions and control gaps.
- [Automation](automation.md) enforces approved rules without inventing new decision authority.

## Suggested measurements

Targets, materiality, and required evidence are **organization-defined**. Compliance with a control is not proof of capacity availability.

| Measure | Definition | Limitation |
|---|---|---|
| Checkpoint evidence coverage | Material changes with required current evidence and authorized decision before execution / all material changes executed in the period × 100 | Emergency exceptions must be identified, not omitted; a completed checklist can still contain weak evidence |
| Expired exception share | Open exceptions past their approved expiry / all open exceptions at the snapshot × 100 | Undefined if none are open; also report count, criticality, and days overdue |
| Lifecycle control coverage | Active commitments with required ownership, consumer, review, and exit records / all active commitments at the snapshot × 100 | Record presence does not verify whether release is contractually possible or technically safe |

## Maturity indicators

- **Reactive:** Approvals and exceptions are reconstructed after a failure or unexpected obligation.
- **Aware:** Capacity review is encouraged, but evidence requirements and delegated authority are incomplete.
- **Managed:** Material decisions use documented checkpoints, accountable owners, and expiring exceptions.
- **Optimized:** Control effectiveness and burden are reviewed using incidents, exceptions, and delivery evidence.
- **Strategic:** Capacity governance is integrated into portfolio and architecture choices, with federated accountability and explicit cross-business trade-offs.

## Practical example

A fictional product team moves a launch to another location. Its existing approval references the original location and demand version, so the change triggers architecture and mechanism rematching. The commercial owner checks whether obligations can change; the continuity owner re-examines recovery. The product owner may accept a documented temporary limitation within delegated authority, but the CapOps lead cannot sign that business risk on the product owner's behalf.

## Risks and common mistakes

- Centralizing all decisions in a lead who lacks business or commercial authority.
- Treating a policy check as evidence of physical supply.
- Creating controls that gather documents but do not support an actual decision.
- Allowing permanent exceptions or bypassing commercial release terms.
- Keeping a governance approval valid after its demand or placement assumptions change.

## Related content

- [Manage the CapOps practice domain](../domains/manage-the-capops-practice.md)
- [Personas and accountability](../framework/personas.md)
- [Operating model](../operating-model/operating-model.md)
- [Capacity resilience](capacity-resilience.md)
