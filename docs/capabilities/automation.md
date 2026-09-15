# Automation

This page explains how Capacity Operations (CapOps) uses software to improve repeatability without surrendering decision authority. It distinguishes evidence collection from actions that can spend money, change priority, or affect a running service.

## Definition

Automation executes repeatable collection, reconciliation, policy evaluation, notification, and authorized capacity actions using explicit rules, bounded permissions, and auditable results.

## Purpose

Improve the timeliness and consistency of established workflows while retaining human ownership of business, technical, commercial, and continuity decisions.

## Why it matters

Manual reconciliation can become stale between reviews, but a fast workflow can also repeat a bad assumption at scale. An automated quota check proves only an administrative condition; an automated forecast remains an estimate; an automated release can remove resources that cannot readily be reacquired. Control quality matters more than the amount of automation.

## Desired outcomes

- Repeated collection and validation use consistent scope, units, and source timestamps.
- Workflow failures, stale inputs, and policy exceptions are visible.
- High-impact actions remain within explicit approval and permission boundaries.
- Operators can stop, investigate, and safely recover an automation failure.

## Inputs

- An established manual process with clear entry criteria and accepted outputs.
- Supported data interfaces, schemas, source owners, and freshness requirements.
- Versioned governance rules, delegated authority, and approval records.
- Workload criticality, protected recovery allocations, and commercial constraints.
- Test cases, failure scenarios, retry rules, audit requirements, and recovery procedures.

## Activities

1. Classify actions by impact. Collection and reminders may be low risk; purchases, allocation changes, resource release, and recovery actions require stronger controls.
2. Define preconditions and postconditions for each workflow. Reject missing units, unknown ownership, expired approvals, or stale evidence rather than substituting permissive defaults.
3. Use least-privilege identities, protected credentials, bounded resource scope, and separate authority for approval and execution where required.
4. Make repeated execution safe: use stable operation identifiers, check current state, prevent duplicate purchases or assignments, and bound retries and concurrency.
5. Test with representative fixtures and failure cases, including partial success, unavailable dependencies, rate limits, stale data, and conflicting updates. Use dry runs and gradual rollout before impactful execution.
6. Require approval when an action exceeds delegated limits or changes business, commercial, or recovery exposure. Maintain an emergency stop and a manual fallback.
7. Record input versions, rule version, approver, executor, action, target, and verified result. Alert on failures and periodically verify that approved policy still matches behavior.

## Outputs

- Versioned workflows with declared scope, owners, permissions, and approval gates.
- Repeatable data-quality checks and policy results.
- Auditable execution records, including partial and failed actions.
- Tested stop, recovery, and manual fallback procedures.

## Roles involved

Platform engineering owns implementation and controlled identities. Operations owns monitoring, intervention, and authorized execution. Security reviewers assess permissions and credential handling where applicable. Business, commercial, and continuity owners approve actions in their mandates. The CapOps practitioner defines evidence and workflow needs; neither the practitioner nor the automation gains authority merely by implementing a rule.

## Dependencies on other capabilities

- [Capacity governance](capacity-governance.md) defines approved rules, limits, and exception authority.
- [Capacity visibility](capacity-visibility.md) provides stable schemas and quality requirements.
- [Quota management](quota-management.md) supplies scope-aware administrative checks.
- [Capacity allocation](capacity-allocation.md) provides consumer rights and protected assignments.
- [Capacity optimization](capacity-optimization.md) defines safe reclaim criteria and validation.

## Suggested measurements

Targets, delegated limits, and service thresholds are **organization-defined**. Higher automation coverage is not inherently better.

| Measure | Definition | Limitation |
|---|---|---|
| Verified workflow success | Executions meeting all postconditions / all workflow executions in the period × 100 | Group retries under a stable operation; include partial failures, and distinguish no-op validation from changes |
| Timely collection | Required collection runs producing valid, complete records within their freshness threshold / all required runs due in the period × 100 | Timely but incorrectly mapped data can still be wrong; pair with reconciliation checks |
| Safe-action coverage | Enabled impactful workflows with current tests, bounded permissions, approval rules, audit, and stop/recovery procedures / all enabled impactful workflows × 100 | Documentation alone is insufficient; report which controls were exercised and when |

## Maturity indicators

- **Reactive:** Unowned scripts or manual commands run during incidents with limited auditability.
- **Aware:** Selected collection tasks are automated, but permissions, tests, and failure handling vary.
- **Managed:** Owned workflows have versioning, validated inputs, bounded access, tests, approval gates, and verified results.
- **Optimized:** Failure exercises and production feedback improve recovery, idempotency, and control accuracy.
- **Strategic:** Policy-driven workflows connect portfolio demand and execution while preserving explicit human authority and independent evidence review.

## Practical example

A fictional workflow compares a frozen demand version with effective quota and opens an action for a scope-specific shortfall. It does not mark quota as physical capacity or automatically buy resources. A later reclaim workflow finds an idle allocation, but the recovery-protection field is missing. It pauses and requests owner review rather than treating missing data as permission to release. Both runs record their inputs and outcomes.

## Risks and common mistakes

- Automatically purchasing, reprioritizing, or deleting resources without delegated authority.
- Retrying an action that succeeded partially and creating duplicate commitments.
- Using stale owner or recovery data to justify reclaim.
- Relying on undocumented interfaces or embedding credentials in code or reports.
- Measuring automation volume while ignoring failure containment and business impact.

## Related content

- [Operate and optimize capacity domain](../domains/operate-and-optimize-capacity.md)
- [Reporting and key performance indicators](reporting-and-kpis.md)
- [Capacity risk management](capacity-risk-management.md)
- [People, process, and technology](../overview/people-process-technology.md)
