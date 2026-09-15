# Capacity forecasting

This page explains how Capacity Operations (CapOps) translates business intent into versioned technical demand. It is for teams deciding what quantity is needed, where, when, and under which assumptions.

## Definition

Capacity forecasting estimates future requirements by service, resource family, quantity and unit, region, zone, date, ramp, duration, priority, and flexibility. Each estimate includes its business driver, assumptions, uncertainty, and accountable owner.

## Purpose

Give placement, acquisition, allocation, and portfolio decisions enough time and detail to evaluate credible options.

## Why it matters

Business roadmaps describe customers, transactions, migrations, or launches; infrastructure plans require resource quantities. The translation depends on performance, concurrency, architecture, and operating assumptions. A precise-looking number can be misleading when those assumptions are untested. A forecast shared with a provider remains a forecast, not a commitment.

## Desired outcomes

- Demand can be traced to a business event and a technical conversion model.
- Delivery and recovery planners use the same forecast version.
- Scenario ranges and timing changes are visible before alternative paths expire.
- Decommissioning and temporary overlap are included rather than silently accumulated.

## Inputs

- Observed baseline demand, resource use, and performance tests.
- Growth assumptions, migration waves, launch calendars, and seasonal events.
- Artificial intelligence (AI) plans, including job concurrency and graphics processing unit (GPU) compatibility where relevant.
- Peak and recovery profiles, destination baseline load, and portfolio concurrency assumptions.
- Decommissioning dates, resource release conditions, and uncertainty around completion.
- Placement constraints, decision lead times, and business priorities.

## Activities

1. Define three horizons locally. **Near-term** demand supports imminent deployment and limit actions; **medium-term** demand supports program sequencing and acquisition; **strategic** demand informs architecture, location, and investment options. Do not impose universal month boundaries.
2. Establish the baseline and translate business drivers into resources using measured conversion factors where possible. Label estimates and arrange tests for sensitive assumptions.
3. Model baseline, growth, migration, launch, seasonal, AI, peak, recovery, and decommissioning effects. Use event identifiers to prevent the same launch being counted as both growth and peak demand.
4. Separate steady production, additional peak demand, and recovery demand. Construct explicit concurrency scenarios rather than summing every maximum or assuming all peaks are independent.
5. For each demand line, record all dimensions in the definition, including required date, ramp steps, time zone, duration, and acceptable changes.
6. Produce low, expected, and high cases with reasons for the range. Include migration coexistence and subtract decommissioning only when its scenario assumes release actually occurs.
7. Freeze a version for each material decision. Compare it with unconstrained observed demand where available, explain variance, and update future versions without rewriting history.

## Outputs

- A versioned demand ledger by compatible technical and time dimensions.
- Business-to-technical conversion assumptions and validation actions.
- Scenario envelopes for production, peaks, migration overlap, and recovery.
- A change log and decision dates for material uncertainty.

## Roles involved

Business and product owners own demand drivers and timing. Architects and engineering own technical conversion assumptions. Operations provides measured behavior and constrained-demand caveats. Continuity owners define recovery scenarios. FinOps aligns economic forecasts. The CapOps practitioner reconciles versions and portfolio overlaps; it does not become the owner of every demand estimate.

## Dependencies on other capabilities

- [Capacity visibility](capacity-visibility.md) supplies the baseline and evidence quality.
- [Workload placement](workload-placement.md) defines valid configurations and interchangeable alternatives.
- [Capacity resilience](capacity-resilience.md) provides recovery quantities and simultaneous-event assumptions.
- [Capacity acquisition](capacity-acquisition.md) uses the forecast to evaluate mechanisms but does not turn the forecast into a guarantee.

## Suggested measurements

Targets, materiality thresholds, and horizon boundaries are **organization-defined**.

| Measure | Definition | Limitation |
|---|---|---|
| Forecast error | Sum of absolute forecast-minus-observed demand / sum of observed demand × 100, for a fixed version and homogeneous resource/time buckets | Undefined when observed demand totals zero; consumption suppressed by capacity limits is not true demand |
| Forecast bias | Sum of forecast-minus-observed demand / sum of observed demand × 100 for the same population | Positive and negative errors can cancel; show error and scenario context alongside bias |
| Timely demand coverage | Material demand lines submitted before their agreed decision deadline / all material demand lines due in the reporting period × 100 | Thresholds and excluded unplanned events must be explicit; early submission does not mean accuracy |

## Maturity indicators

- **Reactive:** Teams request resources when deployment begins and reconstruct demand after a shortfall.
- **Aware:** Selected projects submit estimates, but technical conversions and forecast versions are inconsistent.
- **Managed:** Owned forecasts cover three defined horizons, scenario ranges, dimensioned demand, and documented changes.
- **Optimized:** Teams compare frozen versions with observed demand and improve conversion models and change triggers.
- **Strategic:** Portfolio sequencing and architecture investments use forecast uncertainty and alternative scenarios, not a single deterministic total.

## Practical example

A fictional retailer's illustrative forecast starts with 80 equivalent workers and adds 20 for growth. A seasonal event requires 40 more, producing 140 in the peak scenario. A migration needs 30 temporary workers during overlap; they are not added to the seasonal scenario unless the dates overlap. Recovery in another location includes that destination's existing load and the retailer's agreed minimum service, not an automatic copy of every production maximum. A delayed retirement creates a new version and allocation review.

## Risks and common mistakes

- Forecasting only currency, resource count, or average utilization.
- Mixing incompatible families without validated performance equivalence.
- Treating a strategic estimate as an approved purchase quantity.
- Erasing forecast errors by revising historical versions.
- Assuming a forecast submission or positive provider discussion establishes supply.

## Related content

- [Plan capacity domain](../domains/plan-capacity.md)
- [Capacity allocation](capacity-allocation.md)
- [Capacity optimization](capacity-optimization.md)
- [The lifecycle](../framework/lifecycle.md)
