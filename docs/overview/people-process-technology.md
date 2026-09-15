# CapOps is about people, process, and technology

This page explains how people, process, and technology work together in Capacity Operations (CapOps). It helps teams design a sustainable practice rather than treat a dashboard or reservation mechanism as the solution.

## People supply context and retain accountability

Business owners know the consequence of a missed date. Architects establish acceptable configurations. Engineering and operations provide deployment, performance, and recovery evidence. FinOps and procurement clarify economic and contractual constraints. Continuity owners define recovery obligations. A provider representative explains supported mechanisms without becoming the customer's business risk owner.

Use **central stewardship with federated accountability**. Central stewardship maintains definitions, common records, review quality, and cross-portfolio visibility. Workload teams remain accountable for the demand and decisions they control. A CapOps practitioner can be an existing team member; the framework does not require a dedicated job title for every perspective.

## Process turns signals into decisions

Connect capacity work to existing planning and delivery processes:

| Process connection | Capacity contribution | Decision produced |
|---|---|---|
| Portfolio and product planning | Demand drivers, timing, priority, flexibility | Which demand to pursue, stage, or defer |
| Architecture and delivery checkpoints | Technical demand and tested alternatives | Whether the proposed placement and schedule are credible |
| Commercial approval | Mechanism scope, cost, consumer, release terms | Whether and under what conditions to commit |
| Operational review | Usage, quota, deployment failures, expiring evidence | What action must occur before the next risk deadline |
| Continuity review | Recovery profiles, destination contention, test findings | Which readiness gaps to fund, resolve, or accept |
| Post-incident learning | Assumptions contradicted by actual behavior | Which forecast, guardrail, or design to change |

Every review needs an intended decision, authorized owner, required evidence, and follow-up date. The output should be more than meeting notes or a status color.

## Technology supports evidence and controlled execution

Start with tools that can link workload identity, demand versions, measured use, quota scope, commitments, and decisions. Preserve source timestamps, units, collection scope, and quality indicators. Customer-side telemetry cannot reveal a provider's complete physical inventory.

Automate stable tasks such as collection, reconciliation, reminders, and policy checks before automating purchases, allocation changes, or resource release. Higher-impact actions need explicit authorization, least-privilege access, bounded scope, an audit record, and a safe recovery path. An automated forecast remains a forecast.

## Establish a minimum working practice

1. Select a material workload and name its business decision owner and technical contacts.
2. Agree on a demand schema and the evidence needed for its next decision.
3. Maintain one linked forecast, risk record, and decision record rather than separate contradictory copies.
4. Run the review early enough to execute an alternative; assign each action to a person with authority to carry it out.
5. Inspect actual deployment or recovery results and adjust the schema, process, or tooling.

For example, a launch team may discover that changing launch dates never reaches its infrastructure forecast. The first improvement is a product-to-demand change trigger with an owner, not a more elaborate capacity dashboard.

## Risks and common mistakes

- Buying tools before defining decisions and ownership.
- Centralizing every approval in a practice team that cannot judge workload-specific consequences.
- Confusing participation in a review with authority to accept business or commercial risk.
- Creating duplicate workflows that bypass architecture, financial, or continuity controls.
- Treating missing telemetry as zero usage or assuming automation removes the need for human review.

## Related content

- [Personas](../framework/personas.md)
- [Operating model](../operating-model/operating-model.md)
- [Capacity governance](../capabilities/capacity-governance.md)
- [Capacity visibility](../capabilities/capacity-visibility.md)
- [Automation](../capabilities/automation.md)
