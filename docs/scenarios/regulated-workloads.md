# Regulated workloads

Use this scenario to distinguish mandatory placement restrictions from preferences and to make the resulting concentration risk visible. It is not legal advice; the organization's legal, security, and compliance owners must interpret applicable obligations.

## Business context

A fictional records-processing organization must keep a classified dataset within a set of approved locations. Its initial application design uses one memory-intensive resource family in one region. Product teams want faster onboarding, while compliance owners require evidence before approving additional locations or service configurations.

All quantities, dates, and restrictions in this example are fictional planning inputs, not descriptions of any jurisdiction's law.

## Capacity challenge

The approved placement boundary narrows alternatives. A preference for a familiar resource family has been mixed with genuine data-location requirements, making the workload more rigid than the obligations require. Capacity restrictions cannot be solved by silently relaxing controls.

## Demand dimensions

| Dimension | Example demand |
| --- | --- |
| Service | Controlled records ingestion, validation, storage, and retrieval |
| Resource shape | 18 memory-intensive processing workers with encrypted storage and independently specified network throughput |
| Quantity | 18 baseline workers, up to 30 during onboarding; recovery demand documented separately |
| Placement | Two approved failure domains within the primary region; a second location is under review, not yet an available fallback |
| Timing | Onboarding wave on 2027-09-06; alternative-location approval decision by 2027-08-09 |
| Constraints | Documented dataset-location, access, key-management, retention, and audit requirements supplied by accountable control owners |
| Flexibility | Different tested processing family inside the approved boundary; slower ingestion when business-approved |

## Important assumptions

- The control register distinguishes legal obligations, contractual terms, internal policy, and design preference.
- Availability of a service in a location does not prove that every configuration is compliant or that the needed quantity is deployable.
- Quota approval is not physical capacity, and a demand forecast is not a commitment.
- Two failure domains inside one region do not remove regional concentration risk.
- Alternate-location approval must cover data flows and dependencies, not just the processing workers.

## Relevant CapOps capabilities

- **Workload placement:** build an approved placement and substitution matrix.
- **Capacity governance:** require control-owner approval for changes and expiring exceptions.
- **Capacity forecasting and acquisition:** express constrained demand early and evaluate supported mechanisms.
- **Capacity resilience:** test recovery within the permitted boundary.
- **Capacity risk management:** record what cannot currently be mitigated through placement flexibility.

## Recommended actions

1. Trace each restriction to its accountable owner and evidence. Mark preferences explicitly so they can be challenged without weakening mandatory controls.
2. Build a matrix of approved region, failure domain, resource shape, service configuration, and data path combinations.
3. Benchmark a second resource family within the same boundary. Validate controls and supportability as well as performance.
4. Check quota and specific capacity arrangements for the approved combinations. Do not treat an unapproved second region as secured recovery capacity.
5. Agree an onboarding envelope and a business-approved backlog policy. Define maximum delay and notification requirements.
6. Obtain a decision on concentration risk, recovery expectations, and any temporary exception. Review expiry dates and stop new intake if a required control fails.

## Potential alternatives

Reduce intake rate, schedule processing outside the onboarding peak, modernize a family-specific dependency, or pursue approval for another location. A private or hybrid environment can be assessed, but it introduces its own facility, operational, and control evidence requirements; ownership alone is not proof of compliance or capacity.

## FinOps considerations

Compare duplicate compliant environments, held capacity, assessment work, support costs, and delayed onboarding. A cheaper unapproved placement is not a valid saving. Avoid long commitments while the approved architecture may change. Explicitly fund the control validation needed to make a substitution genuinely usable.

## Residual risks

The approved boundary may remain too narrow for the desired growth and recovery targets. Approval timelines may exceed the business window, and controls can change. A compliant configuration may still be unavailable in the requested quantity.

## Common mistakes

- Calling a preferred machine family a regulatory requirement without evidence.
- Assuming a provider's regional catalog or certification proves workload compliance.
- Routing data to an unapproved fallback during an incident.
- Reporting multi-zone redundancy as proven regional recovery capacity.
- Granting an exception without an accountable owner, expiry, or compensating action.

## Example decision record

| Field | Illustrative record |
| --- | --- |
| Decision | Keep onboarding within the approved 30-worker envelope; qualify a second family before seeking an exception to location controls |
| Accountable owner | Records service owner; compliance owner approves control interpretation and placement changes |
| Decision deadline | 2027-08-09 |
| Evidence required | Control-to-placement matrix, family-substitution test, scoped quota and capacity records, recovery test and documented gaps |
| Trade-off | Accept a bounded onboarding backlog rather than use an unapproved location |
| Residual risk accepted | Regional concentration remains until an alternative is approved and validated |
| Revisit | On alternative approval, backlog reaching its agreed limit, or any control change |
| Release condition | Retire the former configuration only after replacement control and recovery evidence is accepted |

## Related content

- [Workload placement](../capabilities/workload-placement.md)
- [Establish capacity governance](../implementation/establish-capacity-governance.md)
- [Capacity-risk register](../templates/capacity-risk-register.md)
- [Multi-region design](multi-region-design.md)
