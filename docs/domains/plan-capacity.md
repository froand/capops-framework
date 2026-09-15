# Plan capacity

This Capacity Operations (CapOps) domain turns business plans into technical demand, placement options, and recovery assumptions. Use it to decide what must be ready before the business's remaining options expire.

## Objective

Develop versioned forecasts and feasible alternatives across near-term, medium-term, and strategic horizons. Define each horizon locally based on delivery, acquisition, and architectural lead times.

## Business outcome

Product and portfolio owners can compare the consequences of timing, scale, placement, architecture, and scope choices. Forecasting improves the basis for those choices but creates no provider commitment.

## Included capabilities

- **Primary:** [Capacity forecasting](../capabilities/capacity-forecasting.md), [workload placement](../capabilities/workload-placement.md), and [capacity resilience](../capabilities/capacity-resilience.md).
- **Supporting:** [Capacity visibility](../capabilities/capacity-visibility.md) supplies the baseline; [capacity risk management](../capabilities/capacity-risk-management.md) connects uncertainty to deadlines.

## Main activities

1. Translate business drivers through measured or explicitly assumed resource conversion factors.
2. Model baseline, growth, migration overlap, launches, seasonal effects, artificial intelligence (AI), peaks, recovery, and decommissioning. Identify overlap to avoid double-counting.
3. Express service, family, quantity and unit, region, zone, date, ramp, duration, priority, and flexibility for each demand line.
4. Keep production, peak, and recovery profiles distinct; evaluate concurrency by scenario.
5. Qualify alternatives against performance, data, security, operational, commercial, and switching-time constraints.
6. Set a decision deadline that leaves enough time to implement the fallback.

## Primary inputs

- Current usage and workload dependency profiles.
- Business roadmaps, migration waves, launch calendars, and retirement plans.
- Performance tests and uncertainty around demand-to-resource conversions.
- Approved location constraints, service objectives, and continuity obligations.
- Cost scenarios and lead-time information for each feasible option.

## Expected outputs

- Versioned low, expected, and high demand scenarios with assumptions and owners.
- A primary placement and qualified alternatives, including why other options were rejected.
- Production, peak, and recovery requirements with explicit concurrency assumptions.
- Acquisition requirements, validation actions, and decision dates.
- Residual risks for unvalidated configurations or unresolved timing.

## Participating personas

Business and product owners own demand intent and priority. Architects own design recommendations and qualification criteria. Engineering and operations supply technical conversion and testing evidence. Continuity teams define recovery scenarios. FinOps and procurement assess economics and terms. The CapOps practitioner reconciles the plan without taking over the business owner's risk acceptance.

## Example decisions

- Whether to split a migration wave to avoid overlap with a seasonal peak.
- Whether a strategic family change warrants qualification before the next growth step.
- Whether minimum viable recovery service can use a smaller configuration.
- Whether to revise a launch date because its only alternative needs more preparation time.

## Risks and common mistakes

- Treating expected demand as a promise or as the only scenario worth evaluating.
- Omitting retirement dates and migration overlap.
- Calling an untested family or location a ready alternative.
- Assuming independent workload recovery plans can all consume the same destination headroom.

## Related content

- [Domain catalog](../framework/domains.md)
- [Secure and allocate capacity](secure-and-allocate-capacity.md)
- [Capacity forecasting](../capabilities/capacity-forecasting.md)
- [Workload placement](../capabilities/workload-placement.md)
- [Capacity resilience](../capabilities/capacity-resilience.md)
