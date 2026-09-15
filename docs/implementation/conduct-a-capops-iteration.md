# Conduct a CapOps iteration

An iteration of Capacity Operations (CapOps) makes a bounded improvement to a capacity decision or control and tests whether it worked. It follows the continuous lifecycle without requiring every workload to move through each stage in sequence. Use it for a forecast gap, a shared-allocation conflict, a recovery assumption, or a practice improvement.

## Prerequisites

- A problem stated in business terms with a workload or process owner.
- Current demand, risk, and evidence records, including known gaps.
- A decision authority and an implementation team.
- An achievable scope, locally chosen observation period, and access to validation evidence.

An iteration has an exit test, not a promised duration. Do not delay an urgent operational response to fit an improvement cycle.

## Steps through the lifecycle

| Stage | Concrete action | Evidence or output |
|---|---|---|
| **Discover** | Identify the business consequence and scope; trace relevant resources, owners, and dependencies. | Baseline workload profile and problem statement |
| **Forecast** | Translate the business change into time-, location-, family-, and quantity-specific demand; separate normal, peak, and recovery scenarios. | Versioned forecast with assumptions and owner validation |
| **Plan** | Compare options, prerequisites, change lead times, costs, uncertainty, and the last responsible decision deadline for each option. | Recommendation, risk record, and acceptance criteria |
| **Secure** | Execute only approved planning or acquisition actions; confirm any mechanism's exact conditions and remaining prerequisites. | Scoped quota, commercial, entitlement, or deployment evidence, distinguished from each other |
| **Allocate** | Assign eligible capacity to named consumers under approved priorities; check shared and recovery use for conflict. | Allocation record with authorization and dates |
| **Monitor** | Compare actual use, errors, constraints, and evidence freshness with the decision assumptions. | Signals tied to workload and decision records |
| **Optimize** | Test whether reclaim, reassignment, sizing changes, or modernization improve the chosen outcome without harming workload needs. | Authorized changes and before-and-after evidence |
| **Validate recovery** | Check the change against the recovery scenario and shared destination dependencies; test material assumptions safely. | Updated recovery profile, test result, and residual gaps |
| **Learn** | Compare actual outcome with acceptance criteria; explain what changed and update the forecast, control, or next action. | Review decision with verified outcomes and remaining exposure |

“Secure” is not a declaration of unconditional availability. A forecast or quota permission is not proof of physical capacity; a discounted financial commitment may provide no deployable entitlement. Record what the evidence actually establishes.

## Plan verification before execution

Specify the baseline, desired observable behavior, comparison scope, evidence owner, and test conditions. Measures and targets are organization-defined. If evaluating a deployment change, use the same resource and time assumptions or explain the difference. If evaluating a workflow, inspect actual decisions and handoffs rather than counting completed meetings.

Record changes that need commercial, technical, continuity, or business approval separately. Limit automated actions to established guardrails and preserve rollback or stop conditions.

## Worked fictional example

A fictional analytics team discovers 24 assigned compute units but only 16 in current use. The initial proposal is to reclaim eight. Investigation shows that six are scheduled for an upcoming peak and two are genuinely unneeded after a completed retirement.

The iteration's objective becomes “release the two unneeded assignments without reducing the approved peak or recovery posture.” The business owner confirms the retirement; platform engineering checks mechanism compatibility and sharing; the commercial owner checks whether release affects billing or an obligation. The team releases the eligible two units, reconciles the ledger and billing evidence where relevant, and verifies the next approved peak profile. It does not report all eight initially idle units as a saving. Quantities are illustrative.

## Exit and review criteria

Close the iteration when the authority has reviewed evidence against the agreed acceptance criteria, records reflect the resulting state, and residual risks have owners and deadlines. A failed hypothesis is a valid learning result, but not a successful mitigation. Roll back or select a new option if the change fails safety or business criteria.

Choose the next iteration from the most consequential remaining gap, considering dependencies. Reopen the decision after material demand, mechanism, architecture, or recovery changes.

## Common mistakes

- Using a rigid linear checklist instead of revisiting a changed assumption.
- Optimizing idle capacity without checking future demand, contractual terms, or recovery.
- Closing a risk because a task is done rather than because its closure test passed.
- Claiming causation from one improved metric without checking other changes.
- Expanding scope until no result can be verified.

## Related content

- [CapOps lifecycle](../framework/lifecycle.md)
- [Decision record template](../templates/decision-record.md)
- [Manage capacity commitments](manage-capacity-commitments.md)
- [Validate recovery capacity](validate-recovery-capacity.md)
