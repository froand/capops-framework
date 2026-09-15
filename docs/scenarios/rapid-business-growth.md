# Rapid business growth

Use this scenario when demand uncertainty comes from onboarding and product adoption, rather than a single predictable peak. The aim is a rolling capacity decision process that can expand, slow, or redirect intake as evidence changes.

## Business context

A fictional business-analytics company wins several distribution partners. Signed customers, prospective customers, and promotional trials have different probabilities and start dates. Sales wants immediate activation, while operations must preserve service for existing customers and finance wants to avoid paying for an unmaterialized upper forecast.

All counts, dates, and decision thresholds below are illustrative. They are not growth statistics, recommended industry targets, or statements about provider supply.

## Capacity challenge

User growth does not translate directly into compute demand. Large customer datasets, simultaneous onboarding imports, feature adoption, and retention can change memory, processing, and storage needs independently. New demand may also consume headroom intended for recovery.

## Demand dimensions

| Dimension | Example demand |
| --- | --- |
| Business signal | Signed activations, partner launch plans, and trial conversion, tracked separately to avoid double counting |
| Serving footprint | 40 general-purpose workers today; next-quarter lower, central, and upper scenarios of 64, 96, and 144 total workers |
| Data tier | Memory-intensive processing and storage throughput sized from dataset and query mix, not the serving-worker ratio |
| Temporary onboarding | Up to 12 import workers, scheduled separately from steady service and recovery |
| Placement | Two approved regions with independently tested families and data-location boundaries |
| Timing | Cohorts activate weekly from 2027-02-01; each cohort has an evidence checkpoint before customer confirmation |
| Flexibility | Staggered imports, smaller cohorts, delayed trial features, and validated alternative worker shapes |

## Important assumptions

- A signed customer still has an uncertain activation date and workload shape.
- The forecast shows ranges and confidence; even the central forecast is not a capacity guarantee.
- Existing quota does not prove physical capacity for a larger cohort.
- Recovery allocations are separately owned; sales growth cannot silently consume them.
- An alternative region counts as an option only after its data path and user experience have been validated.

## Relevant CapOps capabilities

- **Capacity visibility:** link customer cohorts to measured service demand.
- **Capacity forecasting:** revise scenarios using actual activation and retention.
- **Capacity allocation:** set fair intake and import limits.
- **Workload placement and capacity acquisition:** maintain tested configurations and scoped capacity options.
- **Reporting and key performance indicators:** show demand uncertainty, evidence freshness, and decisions required before the next cohort.

## Recommended actions

1. Reconcile the sales pipeline with signed activation plans. Distinguish firm demand, likely demand, and exploratory demand rather than adding every opportunity at full size.
2. Measure demand by customer segment and feature. Include onboarding, data growth, and background maintenance.
3. Maintain rolling forecasts and compare the time to obtain or qualify additional capacity with the next customer decision deadline.
4. Define evidence gates for activation: permission checks, deployment evidence, dependency throughput, operating readiness, and any applicable capacity-arrangement conditions.
5. Publish an intake rule that treats comparable customers consistently. Reserve explicit space for contracted obligations; explain trial deferrals rather than allowing informal queue jumping.
6. Compare expansion with import scheduling, feature efficiency, and architecture changes. Feed realized demand back into the forecast and release unused provisional allocations.

## Potential alternatives

Activate smaller cohorts, separate import processing from interactive service, batch low-urgency analytics, or introduce an approved degraded feature set. Moving more work to another region can create options but adds data and operating constraints; it is not proof of supply. Deferring trials may reduce immediate revenue opportunity while preserving existing service.

## FinOps considerations

Separate the steady installed customer base from uncertain future demand before purchasing financial commitments. Evaluate revenue timing, idle capacity, import costs, data retention, and the engineering cost of efficient features. Do not justify an upper-forecast commitment with optimistic customer counts that have no activation evidence.

## Residual risks

A small number of unusually demanding customers can invalidate average-based estimates. Growth can coincide with recovery or maintenance. Cohort gates make decisions explicit but do not guarantee a customer activation date or a lower unit cost.

## Common mistakes

- Using revenue growth as a direct multiplier for every technical resource.
- Counting a customer in both the signed backlog and partner pipeline.
- Repeatedly admitting new work into continuity headroom.
- Treating quota headroom or two-region design as proof that growth can be absorbed.
- Keeping speculative allocations indefinitely after customer plans change.

## Example decision record

| Field | Illustrative record |
| --- | --- |
| Decision | Admit the first signed cohort against the validated 64-worker envelope; gate later cohorts on measured demand and refreshed capacity evidence |
| Accountable owner | Analytics product owner; sales operations supplies activation evidence and platform lead validates technical readiness |
| Decision deadline | 2027-01-25 for the first cohort; five business days before each subsequent activation |
| Evidence required | Deduplicated cohort forecast, representative query and import tests, current quota and deployment records, destination recovery-allocation check |
| Trade-off | Accept slower trial onboarding rather than fund and promise the full 144-worker upper scenario immediately |
| Residual risk accepted | Unexpected query mix can require further admission limits; future dates remain conditional |
| Revisit | Weekly, after each cohort, or when demand per customer exceeds the tested range |
| Release condition | Remove provisional import allocations when a cohort completes or cancels |

## Related content

- [Capacity forecasting](../capabilities/capacity-forecasting.md)
- [Build a demand forecast](../implementation/build-a-demand-forecast.md)
- [Capacity demand submission](../templates/capacity-demand-template.md)
- [Seasonal demand](seasonal-demand.md)
