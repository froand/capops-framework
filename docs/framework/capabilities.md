# CapOps capabilities

This catalog identifies the twelve capabilities in the proposed Capacity Operations (CapOps) Framework. Use it to select the work and evidence required for a business decision, not as a checklist of tools to buy.

| Capability | Operational question | Example output |
|---|---|---|
| [Capacity visibility](../capabilities/capacity-visibility.md) | What do we know, and what remains unobserved? | Scoped inventory and evidence-quality gaps |
| [Capacity forecasting](../capabilities/capacity-forecasting.md) | What demand is expected, where, and when? | Versioned demand ranges and assumptions |
| [Quota management](../capabilities/quota-management.md) | Do applicable administrative limits permit the planned request? | Verified limit register and request actions |
| [Capacity acquisition](../capabilities/capacity-acquisition.md) | Which supported mechanism or alternative matches the requirement? | Approved capacity path with terms and residual risk |
| [Capacity allocation](../capabilities/capacity-allocation.md) | Which consumers may use a defined pool during a defined period? | Time-bound assignments and priority decisions |
| [Workload placement](../capabilities/workload-placement.md) | Which configurations are technically and operationally acceptable? | Qualified primary and alternative placements |
| [Capacity governance](../capabilities/capacity-governance.md) | Who can decide, using which evidence and guardrails? | Decision rights, checkpoints, and expiring exceptions |
| [Capacity optimization](../capabilities/capacity-optimization.md) | What can be reclaimed or changed without breaking obligations? | Verified efficiency changes and release decisions |
| [Capacity resilience](../capabilities/capacity-resilience.md) | Can the planned service be recovered under the stated scenario? | Recovery profile, exercise evidence, and gaps |
| [Capacity risk management](../capabilities/capacity-risk-management.md) | What business exposure requires a decision before options expire? | Owned risk and treatment records |
| [Reporting and key performance indicators](../capabilities/reporting-and-kpis.md) | What evidence will change an operational or executive decision? | Scoped scorecard with definitions and actions |
| [Automation](../capabilities/automation.md) | Which repeatable tasks can execute safely within approved bounds? | Controlled workflows and auditable execution evidence |

## How to use a capability page

Each page defines purpose, outcomes, inputs, activities, outputs, roles, dependencies, suggested measurements, maturity indicators, an example, and risks. Adapt the work to local scale and criticality. Keep the evidence and authorized decisions even if several capabilities share one workflow.

For each selected capability:

1. Identify the next decision it must support and its deadline.
2. Name the accountable decision owner and contributors.
3. Check whether its input evidence is available, current, and dimensionally compatible.
4. Agree on a useful output and acceptance criteria.
5. Choose a measurement only if someone will act on it.
6. Review actual outcomes and update the practice.

## Measure evidence, not labels

Key performance indicator (KPI) targets are **organization-defined**, not universal benchmarks. Specify numerator, denominator or unit, population, time window, freshness, exclusions, and owner. Do not combine incompatible resource quantities into a percentage of “secured capacity.” A forecast, quota approval, and capacity reservation are different evidence types.

Maturity uses **Reactive, Aware, Managed, Optimized, and Strategic** indicators. Assess each capability and business unit separately using records and observed behavior. A high level in automation does not compensate for an untested recovery capacity assumption.

## Risks and common mistakes

- Implementing capability names without decisions, outputs, or accountable owners.
- Treating every capability as an independent system of record.
- Assuming a measurement target proves capacity will be available.
- Choosing a maturity label from aspiration rather than recent evidence.

## Related content

- [Domains and capability mapping](domains.md)
- [Personas](personas.md)
- [Maturity model](../maturity/maturity-model.md)
- [Conduct a CapOps iteration](../implementation/conduct-a-capops-iteration.md)
