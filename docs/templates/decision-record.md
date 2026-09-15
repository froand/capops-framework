# Capacity decision record template

Copy these tables for a material Capacity Operations (CapOps) decision, including a hold, deferral, or exception. Replace prompts and preserve the evidence available when the choice was made. Separate technical suitability, commercial approval, and business-risk acceptance if different authorities own them. Link sensitive evidence rather than copying it into a public record.

## Decision context

| Field | Entry |
|---|---|
| Decision identifier, version, and state | Proposed, approved, held, superseded, or closed; history reference |
| Question to decide | A specific choice, not a general status update |
| Workload, business outcome, and criticality | Profile reference and consequence of doing nothing |
| Demand and forecast versions | Normal, peak, recovery, or named combined scenario |
| Technical demand | Service, family, quantity and unit, location or zone, required window, ramp, and duration |
| Constraints and dependencies | Performance, regulatory, commercial, operational, and shared recovery restrictions |
| Decision authority and deputy | Named authority for this specific decision |
| Related risks and commitments | Stable record references |

## Evidence and assumptions

| Claim or assumption | Fact, inference, or unknown | Source and observed date | Exact scope and conditions | Limitations and freshness rule | Evidence owner |
|---|---|---|---|---|---|
| Enter claim | State category | Approved reference and date | Time, location, family, quantity, and mechanism | What it does not establish; next check | Named owner |

Keep forecast, quota permission, financial obligation, capacity entitlement, allocation, and successful deployment evidence distinct. A service listing, discount, or recovery architecture does not establish deployable capacity.

## Options and timing

| Option, including doing nothing | Technical feasibility | Cost or obligation and business effect | Implementation or acquisition lead time | Validation time and uncertainty allowance | Last responsible decision deadline | Residual risk |
|---|---|---|---|---|---|---|
| Enter option | Evidence, prerequisites, and constraints | Include delay, reduced service, and exit costs where relevant | Estimate and supporting reference | Locally justified assumptions | Required date less applicable lead time | What remains unestablished |

## Authorized outcome

| Field | Entry |
|---|---|
| Chosen option and rationale | Explain why it is preferable under the stated assumptions |
| Alternatives rejected | Reasons, including infeasibility before their deadlines |
| Technical approval | Authority, scope, date, conditions, or not applicable with reason |
| Commercial or budget approval | Authority, obligation, date, conditions, or not applicable |
| Business-risk acceptance | Named acceptor, delegated basis, consequence, expiry, or escalation required |
| Decision date and validity | When it was made and how long its conditions apply |
| Residual risks and disagreements | Linked records and material dissenting evidence |
| Communication and receiving owners | Who must act and who acknowledged the handoff |

## Execution and verification

| Action | Executor | Due date | Prerequisites | Acceptance evidence | Result and verification owner | Revisit trigger |
|---|---|---|---|---|---|---|
| Specific authorized action | Named owner | Date before option window closes | Approvals and dependencies | Test or observed outcome | Reference, date, and result | Demand change, failed condition, stale evidence, or expiry |

## Exception fields, when applicable

| Field | Entry |
|---|---|
| Guardrail and precise deviation | Which control is not met and affected scope |
| Reason and compliant alternatives considered | Evidence for why an exception is needed |
| Compensating controls | Actionable measures, owners, and verification |
| Exception approver and residual exposure | Authority for the actual risk, not merely the facilitator |
| Expiry and revalidation plan | Date, owner, and evidence required for closure or a new decision |
| Stop or escalation condition | What invalidates permission to continue |

Do not silently renew a decision or exception after its assumptions change. A completed action is not a verified outcome until its acceptance evidence is reviewed.

## Related content

- [Governance](../operating-model/governance.md)
- [Risk-register guide](../implementation/create-a-capacity-risk-register.md)
- [Monthly review template](monthly-review-template.md)
