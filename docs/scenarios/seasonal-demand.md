# Seasonal demand

Use this scenario to translate a time-bounded commercial event into a tested capacity and demand-shaping plan. The decision includes how much demand to admit when the preferred scale-out path is unavailable.

## Business context

A fictional ticketing business plans a festival sale. Admission fairness and successful purchase completion matter more than letting every visitor browse without waiting. The product owner can stagger sales by event and provide a visible waiting room.

Quantities, dates, and time windows below are illustrative, not traffic statistics or provider-capacity predictions.

## Capacity challenge

A short event may need several times the normal serving footprint, but payment processing, inventory locks, and connection handling can constrain throughput before compute does. A delayed scale-out during the peak can be less useful than a smaller tested service that controls admission.

## Demand dimensions

| Dimension | Example demand |
| --- | --- |
| Baseline | 24 general-purpose serving workers outside the event |
| Ramp and peak | 48 workers during a two-hour ramp; 72 total serving workers for a six-hour peak |
| Background work | 12 reporting workers, deferrable until after the sale; these are not included in the serving totals |
| Date and duration | Sale on 2027-08-20; ramp begins before public admission; release after reconciliation and stability checks |
| Placement | Approved primary region and failure domains; separately defined recovery destination and capacity profile |
| Dependencies | Payment throughput, inventory update rate, database connections, cache warm-up, routing, and support staffing |
| Flexibility | Staggered sale windows, controlled admission, reduced browsing features, and tested worker-family substitutes |

## Important assumptions

- The load test represents purchase behavior and retries, not just page reads.
- Deferred reporting can catch up without conflicting with settlement or recovery work.
- Quota can permit 72 workers without proving that physical supply is available at the event time.
- A financial discount is not a capacity arrangement unless the product explicitly includes that benefit.
- A forecast shared with a provider remains a forecast; the business must retain a fallback.

## Relevant CapOps capabilities

- **Capacity forecasting:** model ramp, peak, decay, retries, and catch-up.
- **Capacity optimization:** remove avoidable work and warm dependencies before admission.
- **Capacity allocation:** prioritize checkout over background reporting.
- **Capacity acquisition:** evaluate supported arrangements for the short peak window.
- **Capacity risk management:** define admission triggers and event-readiness decisions.

## Recommended actions

1. Convert ticket-release timing into demand ranges and a maximum admitted request rate. State the conversion assumptions and confidence.
2. Test the end-to-end purchase path under steady load, bursts, retries, and slow dependency responses.
3. Qualify worker substitutions and pre-event warm-up. Confirm quota, deployment configuration, and any supported capacity-arrangement state separately.
4. Agree a transparent admission policy, including accessibility needs, waiting-time communication, and how customers recover an interrupted purchase.
5. Run a go/no-go review with product, reliability, finance, and partner-dependency owners. If the desired envelope is unsupported, reduce admission or split the event rather than claim the peak is secured.
6. Monitor useful completed purchases and dependency saturation. Release peak resources only after payment reconciliation and deferred-work scheduling are safe.

## Potential alternatives

Spread ticket releases across several windows, reduce expensive page features, or use a waiting room with a bounded checkout rate. Moving the sale date has commercial costs; adding raw compute may not address payment or inventory limits. Compare alternatives against fairness and completed sales, not only request throughput.

## FinOps considerations

Compare short-term peak expense with lost sales, refunds, and customer-support work. Include prewarming, held but unused resources, load testing, and post-sale processing. Do not purchase a long financial commitment solely to cover one short peak without a credible later use. CapOps does not promise either savings or an uninterrupted event.

## Residual risks

Marketing reach, automated traffic, retry storms, or partner outages can exceed assumptions. A capacity test does not certify future event-day supply. Admission control can preserve throughput while still disappointing customers who cannot purchase.

## Common mistakes

- Using daily average traffic for a synchronized opening minute.
- Scaling serving workers while ignoring payment or inventory bottlenecks.
- Releasing resources immediately after admission closes.
- Treating a waiting room as fair without reviewing who can enter and retry.
- Describing forecast acknowledgement as a protected sales date.

## Example decision record

| Field | Illustrative record |
| --- | --- |
| Decision | Open sales only within the tested checkout rate; use staged admission and pause reporting during the peak |
| Accountable owner | Ticketing product owner; reliability lead controls operational admission changes within approved limits |
| Decision deadline | 2027-08-13, before final event communications |
| Evidence required | Purchase-path load test, dependency confirmations, deployment and quota checks, capacity-arrangement state where used, admission-policy rehearsal |
| Trade-off | Accept a visible queue and delayed reporting instead of unrestricted admission with uncertain completion |
| Residual risk accepted | Unexpected demand or partner failures may still delay or interrupt sales |
| Revisit | At the event-readiness review, after the ramp test, and immediately on dependency saturation |
| Release condition | Finance confirms reconciliation and operations approves the deferred-work plan |

## Related content

- [Build a demand forecast](../implementation/build-a-demand-forecast.md)
- [Capacity optimization](../capabilities/capacity-optimization.md)
- [Capacity demand submission](../templates/capacity-demand-template.md)
- [Rapid business growth](rapid-business-growth.md)
