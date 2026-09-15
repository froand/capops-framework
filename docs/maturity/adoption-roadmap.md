# Adoption roadmap

This roadmap helps an organization introduce Capacity Operations (CapOps) as a proposed practice within existing delivery and governance arrangements. It is an evidence-gated sequence, not a promise of adoption speed, a staffing formula, or a project with a universal end date. Use the [assessment](assessment.md) to decide where to begin.

## Choose scope by consequence

Select a bounded set of workloads where a capacity decision could affect a business milestone, location obligation, scaling need, or recovery objective. Include enough shared dependencies to avoid assessing each workload in isolation. Name the sponsor, practice steward, and business owners without requiring new dedicated positions.

Define success as improved decisions and verified actions. Examples include establishing a viable alternate placement before a deadline or discovering and resolving competing recovery demand. Set local evidence and review criteria; do not promise that a pilot will deliver a particular saving or availability outcome.

## Sequence the work

| Step | Practical work | Evidence required before widening scope |
|---|---|---|
| **Establish responsibility** | Agree a mandate, decision rights, pilot scope, shared terminology, and an initial thirteen-dimension assessment. | Named authorities acknowledge responsibilities; critical unknowns have investigation owners and dates. |
| **Make demand and risk visible** | Profile workloads; translate business drivers into technical demand; separate normal, peak, and recovery; build a rolling forecast and risk register. | Owners validate scoped demand and evidence freshness; each material gap has options and a last responsible decision deadline. |
| **Make decisions repeatable** | Run a monthly decision review; use existing design, commercial, and delivery checkpoints; introduce commitment and exception records. | Actual decisions show evidence, authority, conditions, actions, and later verification; no critical gap is hidden by an average score. |
| **Integrate neighboring practices** | Share evidence with FinOps, architecture, reliability, continuity, procurement, and portfolio planning. Test shared recovery assumptions. | A cross-functional decision changes a plan, allocation, obligation, or recovery action; handoffs and remaining disagreements are visible. |
| **Improve using outcomes** | Reconcile assignments with use; test alternatives; revise forecasts; modernize inflexible dependencies; automate stable evidence checks. | Observed outcomes support the change; controls protect consumers, recovery needs, access boundaries, and approval rights. |
| **Connect strategic choices** | Use scenarios to influence investment, sourcing, continuity objectives, and portfolio sequence across near, medium, and long horizons. | Leaders explicitly compare business options and residual risk, with revisit triggers for strategic assumptions. |

These steps may overlap. Address an urgent recovery weakness immediately rather than waiting for a supposedly earlier maturity phase. High maturity in one dimension does not authorize skipping prerequisites in another.

## Use small, evidence-backed iterations

For each improvement, state the problem, business consequence, target behavior, owner, dependency, and acceptance evidence. Keep the number of concurrent changes within the team's ability to implement and verify them. [Conduct a CapOps iteration](../implementation/conduct-a-capops-iteration.md) describes this loop.

A fictional product group might begin with one launch and its shared recovery destination. Its first iteration establishes separate demand profiles and discovers that rollback and recovery consume the same pool. A second iteration tests a staged restoration plan and records residual limitations. The group broadens scope only after it can repeat these decisions, not after reaching an arbitrary number of meetings.

## Decide when to expand or pause

Expand when owners can maintain evidence, decisions arrive before options expire, actions close with verification, and neighboring teams can use the records. Pause expansion when critical evidence is unreliable, responsibility remains disputed, or added reporting prevents teams from executing mitigations.

Review the roadmap through the existing strategic capacity review. Retire unused measures and redundant approvals. Reassess after reorganizations, new resource dependencies, material business growth, or continuity changes.

## Common mistakes

- Starting with enterprise-wide tooling before agreeing demand definitions and decision rights.
- Targeting Strategic everywhere rather than fixing the most consequential gaps.
- Centralizing all business risk acceptance in the practice lead.
- Treating documented forecasts, quota approvals, or recovery designs as evidence that capacity is secured unconditionally.
- Claiming improvement from planned work without checking its operational result.

## Related content

- [Get started with CapOps](../implementation/getting-started.md)
- [Maturity model](maturity-model.md)
- [Assessment method](assessment.md)
- [Operating cadence](../operating-model/operating-cadence.md)
