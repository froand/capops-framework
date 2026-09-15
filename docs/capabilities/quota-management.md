# Quota management

This page describes how Capacity Operations (CapOps) manages administrative resource limits before deployment, scaling, and recovery. It explicitly separates request permission from underlying supply.

## Definition

Quota management identifies applicable administrative limits, compares them with planned use, requests supported changes, and verifies that approved limits apply to the intended deployment scope.

## Purpose

Address limit-related blockers while preserving a separate evaluation of physical capacity and other deployment conditions.

## Why it matters

Several limits can apply to one workload: organization or account totals, family limits, service-specific limits, or location-specific limits. A change to one does not necessarily change the others. The same limits may constrain expansion or recovery even if steady production fits.

Quota approval does not prove physical capacity exists. It also does not establish that configuration, policy, networking, or dependency requirements are satisfied.

## Desired outcomes

- Every material demand line is mapped to its applicable limits.
- Needed adjustments are requested and verified before their decision deadlines.
- Concurrent projects and recovery demand are considered in shared scopes.
- Limit failures are distinguishable from other deployment failures.

## Inputs

- Current limits and measured use, with unit, scope, observation time, and adjustment rules.
- Forecast production, peak, migration overlap, and recovery demand.
- Technical profiles mapping resource configurations to their consumption of each limit.
- Pending adjustment requests, approval evidence, and deployment error details.
- Authorized requesters and the organization's resource-governance constraints.

## Activities

1. Enumerate all applicable limits for the planned resource and its dependencies. Identify fixed limits separately from adjustable ones using current provider guidance.
2. Map each forecast line to the relevant administrative scope, location, and resource unit. Include existing use and concurrent planned consumers.
3. Calculate **quota headroom = approved limit − measured usage** for each scope at a stated timestamp. Keep this distinct from forecast headroom and from physical capacity.
4. Model peak and recovery scenarios against those limits, including temporary coexistence and destination baseline use.
5. Submit supported adjustment requests with required dimensions and dates. Set follow-up and alternative-decision deadlines; do not invent universal approval lead times.
6. Verify the effective limit after approval through supported interfaces, then separately validate deployment conditions.
7. Monitor consumption and failed attempts. Reopen the forecast or placement decision if a limit cannot be adjusted in time.

## Outputs

- A limit register with scope, current use, freshness, owner, and planned scenario demand.
- Adjustment requests with status, requested and effective values, and decision deadlines.
- Verified approval evidence tied to the correct deployment target.
- Escalated risks and alternatives for fixed, denied, or late adjustments.

## Roles involved

Platform engineering owns scope mapping and authorized requests. Operations monitors consumption and classifies failures. Workload owners confirm timing and concurrency. Architects evaluate alternatives when a limit is binding. The CapOps practitioner coordinates shared-scope planning; business owners retain acceptance of delivery or recovery exposure.

## Dependencies on other capabilities

- [Capacity forecasting](capacity-forecasting.md) supplies future and concurrent demand.
- [Capacity visibility](capacity-visibility.md) supplies measured usage and scope mappings.
- [Capacity resilience](capacity-resilience.md) identifies destination and rebuild limits.
- [Capacity acquisition](capacity-acquisition.md) separately evaluates supported capacity mechanisms.

## Suggested measurements

Targets and alert thresholds are **organization-defined** for each limit scope.

| Measure | Definition | Limitation |
|---|---|---|
| Limit-plan coverage | Due material demand lines checked against every identified applicable limit / all material demand lines due in the period × 100 | Incomplete limit discovery can overstate coverage; unknown dependencies must be disclosed |
| Verified adjustment timeliness | Required adjustments verified effective before their decision deadline / all required adjustments due in the period × 100 | Exclude unchanged limits explicitly; show denied and pending requests, not just completed ones |
| Limit-related failure rate | Deployment operations confirmed blocked by administrative limits / all deployment operations attempted in the same scope and period × 100 | Define operation grouping to avoid retry distortion; unclassified failures remain separate |

## Maturity indicators

- **Reactive:** A deployment error initiates the first limit investigation.
- **Aware:** Important limits and request contacts are documented, but checks depend on individual projects.
- **Managed:** Owned limit records, scenario comparisons, adjustment deadlines, and post-approval verification are routine.
- **Optimized:** Monitoring and forecast changes trigger targeted checks, with evidence that duplicate requests and scope mismatches are corrected.
- **Strategic:** Portfolio sequencing and platform standards account for shared administrative boundaries and fixed-limit alternatives.

## Practical example

In a fictional account, an illustrative family limit is 200 units and current use is 140. Two projects each request 40 additional units for the same window. Both fit individually, but the combined 220 exceeds the limit. Engineering coordinates one adjustment or stages the demand. After any approval, the team verifies the effective value and still evaluates physical deployment capacity separately.

## Risks and common mistakes

- Checking an account total while missing a family or service dependency limit.
- Reporting unused quota as reserved or available physical supply.
- Overlooking destination limits because only the primary environment is monitored.
- Requesting arbitrary maximums without demand justification or governance review.
- Recording an approval message without verifying the effective target scope.

## Related content

- [Secure and allocate capacity domain](../domains/secure-and-allocate-capacity.md)
- [Workload placement](workload-placement.md)
- [Automation](automation.md)
- [Glossary](../glossary.md)
