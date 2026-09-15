# Legacy resource modernization

Use this scenario to reduce dependence on a narrow resource family without assuming that newer technology is automatically compatible, cheaper, or more available.

## Business context

A fictional reporting company operates a nightly reconciliation service on 80 machines from one legacy family. Its internal platform standard is changing, but the application has never been qualified on another family. Business owners need accurate morning reports and a credible rollback plan more than a rapid technical refresh.

The machine counts, dates, and acceptance thresholds are illustrative. No provider retirement, inventory constraint, or cost reduction is implied.

## Capacity challenge

The estate's narrow compatibility envelope makes both expansion and recovery harder to plan. Existing financial commitments and operational habits favor keeping the current machines, while a full replacement could create a temporary overlap peak. Modernization needs capacity for testing and parallel validation before any legacy capacity is reclaimed.

## Demand dimensions

| Dimension | Example demand |
| --- | --- |
| Business service | Nightly reconciliation with a business-defined completion window and exact financial-result checks |
| Existing footprint | 80 legacy-family machines; measured usage indicates 20 are candidates for retirement, pending dependency checks |
| Candidate footprint | Memory and processing requirements benchmarked on two alternative families; no assumed one-for-one size equivalence |
| Transition overlap | Ten candidate machines for the pilot while the current production allocation remains intact |
| Placement | Approved primary region and a separately validated recovery destination |
| Timing | Pilot during January 2027; replacement decision by 2027-02-19 before renewing relevant commitments |
| Dependencies | Operating system, processor architecture, storage behavior, software licenses, job scheduler, and result-validation tooling |
| Flexibility | Incremental batches, application tuning, or a longer transition with an explicit exception |

## Important assumptions

- The 20 retirement candidates cannot be removed until owners confirm they are not recovery, month-end, or infrequent jobs.
- A newer family is an alternative to test, not a promise of physical supply.
- Quota for the existing family does not establish permission or capacity for a replacement family.
- A forecast for replacement demand is not an accepted capacity arrangement.
- Releasing the old configuration can make rollback dependent on new deployment; distinguish retained capacity from a plan to recreate it.

## Relevant CapOps capabilities

- **Capacity visibility:** expose legacy dependencies and true utilization patterns.
- **Capacity optimization:** retire obsolete work and reduce resource demand before acquisition.
- **Workload placement:** qualify alternative families and recovery configurations.
- **Capacity forecasting:** model pilot, dual-run, and release phases.
- **Capacity governance:** manage time-limited exceptions and commitment renewal decisions.

## Recommended actions

1. Inventory workload-to-family dependencies and ask application owners which are technical requirements, support conditions, or historical preferences.
2. Validate retirement candidates across normal, month-end, and recovery schedules. Remove only demand that is demonstrably unnecessary.
3. Define acceptance criteria before benchmarking: output correctness, completion time, operational behavior, supportability, and recovery.
4. Run a representative pilot on both candidate families. Include the actual deployment and restore paths rather than extrapolating from processor specifications.
5. Obtain separate quota and capacity evidence for transition overlap. Move in reversible batches with a clear rollback-retention deadline.
6. Align financial commitment renewals with accepted migration evidence. Release legacy resources and update templates only after the owner accepts correctness and recovery results.

## Potential alternatives

Optimize the application on its current family while qualification continues, refactor the most restrictive component, or retain a smaller legacy exception for one unsupported job. A complete replatforming may provide more flexibility but requires additional functional and operational validation. Keeping everything unchanged preserves familiarity while retaining concentration risk.

## FinOps considerations

Compare dual-running expense, engineering effort, license changes, unused financial commitments, and future operating cost per completed reconciliation. Do not retain unnecessary machines solely to make a commitment appear utilized. Equally, do not release a required rollback allocation solely to improve a utilization measure.

## Residual risks

Rare calculations, data volumes, or software behavior may differ on the replacement. Legacy capacity may no longer be deployable after release. An alternative family can later acquire its own constraints, so qualification must remain a maintained capability rather than a one-time exercise.

## Common mistakes

- Replacing machines one for one based only on core count.
- Labeling all low-utilization resources waste without checking recovery and periodic workloads.
- Renewing a long commitment before deciding the target configuration.
- Claiming modernization guarantees availability or savings.
- Deleting the old environment before result and rollback acceptance.

## Example decision record

| Field | Illustrative record |
| --- | --- |
| Decision | Qualify two candidate families with a ten-machine pilot; migrate in accepted batches rather than replace all 80 machines at once |
| Accountable owner | Reconciliation service owner; application lead owns result correctness and platform lead owns deployment and recovery evidence |
| Decision deadline | 2027-02-19 |
| Evidence required | Dependency inventory, representative and month-end replay results, candidate benchmarks, quota and capacity records, cost and commitment comparison |
| Trade-off | Accept temporary dual-running and qualification work to reduce long-term dependence on one configuration |
| Residual risk accepted | Unrepresented jobs may require a bounded legacy exception; replacement capacity remains configuration-specific |
| Revisit | After the pilot, at each batch acceptance, and before any commitment renewal |
| Release condition | Retire each legacy batch only after accepted results, recovery validation, and its rollback window end |

## Related content

- [Capacity optimization](../capabilities/capacity-optimization.md)
- [Workload placement](../capabilities/workload-placement.md)
- [Cloud migration](cloud-migration.md)
- [Capacity-risk register](../templates/capacity-risk-register.md)
