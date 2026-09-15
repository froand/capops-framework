# Build a capacity demand forecast

This Capacity Operations (CapOps) guide translates business plans into versioned technical demand that decision makers can act on. A forecast is a demand signal, not a provider commitment or guarantee. Its usefulness depends on explicit dimensions, uncertainty, ownership, and a decision deadline.

## Prerequisites

- Business milestones, demand drivers, product plans, and confirmed retirements.
- Measured usage and performance evidence for a stated observation period.
- Workload owners, architects, and platform contacts able to validate assumptions.
- Separate normal, peak, and recovery profiles, or an action to establish missing profiles.

Use the [demand template](../templates/capacity-demand-template.md) for submissions. Protect sensitive business assumptions in an approved system; public examples should remain fictional.

## Steps and evidence

1. **Set scope and horizons.** Define near-term execution, medium-term acquisition and design, and long-term portfolio horizons according to business planning cycles and actual lead times. Document the chosen windows rather than assuming fixed month counts.
2. **Establish a measured baseline.** Identify service, resource family, quantity and unit, location, observation time, utilization context, and technical limits. Distinguish allocated from consumed capacity.
3. **Translate business drivers.** Link transactions, users, data volume, migration waves, or service objectives to a sizing model. Record test conditions, performance requirements, efficiency assumptions, ramp, and duration. Do not assume demand scales linearly without evidence.
4. **Add changes and subtract justified retirements.** Include launches, growth, migrations, temporary coexistence, seasonal peaks, and rebuild work. Subtract decommissioning only with an owner, date, and dependency check; uncertain retirement belongs in a scenario.
5. **Model distinct scenarios.** Keep normal, peak, and recovery profiles separate. For each, state whether quantities are total or incremental. Identify which events can overlap and which are mutually exclusive.
6. **Aggregate compatible demand.** Combine only equivalent units in compatible family, service, location, and time slices. Model shared platform limits and concurrent portfolio recovery; do not count the same shared allocation as available to every workload.
7. **Express uncertainty and flexibility.** Use owner-supported ranges or named scenarios with assumptions. Record alternate family, location, service pattern, schedule, and demand-reduction options with validation status.
8. **Compare demand with evidence.** Check quota permission, relevant capacity-mechanism conditions, existing allocations, deployment observations, and remaining gaps separately. Record evidence dates and refresh triggers. Service-catalog availability and a financial discount are not proof of deployability.
9. **Connect to decisions and version.** For each material gap, document acquisition or change lead time, validation time, uncertainty allowance, and the last responsible decision deadline. Obtain business and technical validation, publish a version, and preserve the previous assumptions.

## Worked fictional example

A fictional service uses compatible compute units in one approved location. All figures below are illustrative and apply to the same tested resource family and launch window.

| Component | Units | Evidence and interpretation |
|---|---:|---|
| Measured normal baseline | 40 | Current workload profile and representative performance observation |
| Approved growth | +10 | Business owner validates the transaction scenario |
| Promotion uplift | +25 | Incremental peak demand from a sizing test |
| Confirmed retirement | -5 | Decommissioning completes before the promotion; no remaining dependency |
| Peak scenario total | **70** | 40 + 10 + 25 - 5; not 70 additional units |

The post-retirement normal scenario is 45 units. A downside scenario without the retirement needs 75 units at peak and exposes the dependency explicitly. Recovery is modeled separately at the destination; it is not automatically added to peak or assumed equal to normal. If the failure scenario overlaps the promotion, model that combined situation explicitly, including destination resident demand.

If current deployment evidence covers only 40 units and quota permits 90, the forecast still needs an option for the required increase. The quota number is not a statement that 90 units can be deployed.

## Exit and review criteria

A usable forecast has a business and technical owner, version, horizon definitions, dimension-specific quantities, scenario overlap rules, assumption references, evidence freshness, and decisions for material gaps. An unknown remains labeled unknown with a collection action.

Review after business or architecture changes, missed retirements, capacity-related deployment failures, invalidated evidence, and the normal decision cadence. Compare actual demand with the matching previous scenario and record why it differed. Any forecast-error measure and target must be locally defined, including how zero demand, unit changes, and shifted dates are handled.

## Common mistakes

- Treating current utilization as the entire future demand signal.
- Adding mutually exclusive peaks or double-counting a migration's source and destination after retirement.
- Subtracting an unfunded or unapproved retirement.
- Combining different families as equivalent without performance evidence.
- Hiding uncertain dates and quantities inside a single precise-looking total.

## Related content

- [Capacity forecasting capability](../capabilities/capacity-forecasting.md)
- [Demand template](../templates/capacity-demand-template.md)
- [Workload profile](../templates/workload-capacity-profile.md)
- [Create a capacity-risk register](create-a-capacity-risk-register.md)
