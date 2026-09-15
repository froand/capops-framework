# Glossary

This glossary defines the working language of the proposed Capacity Operations (CapOps) community framework. Use it when writing demand, risk, mechanism, and decision records so identical terms do not conceal different assumptions.

## Framework definition

CapOps, or Capacity Operations, is an operational framework and cultural practice for forecasting, securing, allocating, governing, monitoring, optimizing, and validating cloud and infrastructure capacity so workloads can be deployed, scaled, and recovered where and when the business needs them.

CapOps is a proposed, independent community framework and cultural practice, not an established industry standard or a capacity guarantee. It complements FinOps and does not imply provider or foundation endorsement.

## Capacity and demand

| Term | Working meaning |
|---|---|
| **Artificial intelligence (AI)** | Computing methods and systems used for tasks such as prediction, generation, or classification. Capacity demand depends on the actual workload, model, concurrency, and resource requirements, not the label alone. |
| **Baseline demand** | The reference demand under a defined normal operating condition and observation period. It is not necessarily an average or minimum. |
| **Capacity** | The practical ability to provide a specified resource quantity under defined technical, location, time, and operating conditions. |
| **Demand dimensions** | Service, resource family, quantity and unit, region, zone, required date, ramp, duration, priority, and flexibility, linked to a business driver and owner. |
| **Demand forecast** | A versioned estimate of future requirements with assumptions and uncertainty. It is not a provider commitment. |
| **Decommissioning** | Retirement of workload resources and related assignments. Commercial obligations may continue after technical resources are removed. |
| **Duration** | The period for which a demand or allocation is required, including temporary overlap where applicable. |
| **Graphics processing unit (GPU)** | A processor used for parallel computation, among other uses. Capacity matching may depend on model, memory, interconnect, software compatibility, and supporting resources. |
| **Headroom** | The difference between usage or demand and an explicitly named limit or planning envelope. Quota headroom, allocated headroom, and operational headroom are not interchangeable. |
| **Peak profile** | The quantity, shape, duration, and scaling behavior required for an elevated-demand scenario, distinguishing total demand from incremental demand. |
| **Physical capacity** | Underlying deployable supply. Customers may observe deployment outcomes without directly observing provider physical inventory. |
| **Production profile** | The resources and dependencies needed for the agreed normal service level, with location and performance conditions. |
| **Ramp** | How quantity changes over time as resources are introduced, scaled, or removed. |
| **Resource family** | A grouping of resource configurations with related characteristics. Similar names or resource counts do not establish performance equivalence. |
| **Scenario** | A defined combination of events and assumptions used to evaluate demand and response, such as migration overlap with a seasonal peak. |
| **Strategic, medium-term, and near-term horizons** | Locally defined planning ranges supporting architectural options, program and acquisition planning, and imminent execution respectively. Their boundaries depend on decision lead times. |

## Permissions, mechanisms, and allocation

| Term | Working meaning |
|---|---|
| **Allocation** | A time-bound assignment of consumer rights to a defined capacity pool. An internal assignment does not create external supply. |
| **Capacity acquisition** | Evaluation and authorized use of supported mechanisms or sourcing options for specific demand, with their conditions and residual risk recorded. |
| **Capacity path** | The planned combination of placement, administrative permissions, resources or supported mechanisms, dependencies, and fallback actions intended to meet a requirement. Its existence is not a guarantee. |
| **Capacity reservation** | A provider- or infrastructure-specific mechanism concerning deployable capacity under defined conditions. Exact support, eligibility, scope, and terms must be verified. |
| **Commitment** | An obligation or arrangement with explicit parties, scope, dates, and terms. State whether it is financial, capacity-related, or both. |
| **Financial reservation or commitment** | A commercial arrangement that may provide a discount. It does not reserve deployment capacity unless the documented product terms explicitly include that function. |
| **Quota** | An administrative permission or service limit controlling what can be requested or used. Quota approval does not prove physical supply. |
| **Reclaim** | Removal of an assignment or release of resources after review and authorization. Reclaim does not necessarily terminate a financial obligation. |
| **Reservation** | An ambiguous provider-specific term. Always qualify it as financial, capacity-related, or both after checking its actual definition. |
| **Secure capacity** | Take appropriate planning, quota, supported reservation, architecture, allocation, and provider-engagement actions. The phrase does not mean unconditional availability. |
| **Service availability** | A service is offered in a location. This does not establish fulfillment of a particular resource type, quantity, zone, or deployment date. |

## Placement and recovery

| Term | Working meaning |
|---|---|
| **Architecture flexibility** | The ability to use qualified alternative configurations, locations, schedules, or operating patterns within agreed constraints. |
| **Concentration risk** | Exposure from dependence on a narrow set of locations, resource families, services, or shared dependencies. |
| **Minimum viable service** | The business-approved service level that must be restored or maintained under a stated disruption scenario. |
| **Multi-region architecture** | A design using more than one region. It can create options but does not automatically establish capacity or independent failure conditions. |
| **Qualified alternative** | An alternative tested or evaluated against stated technical, operational, data, commercial, and timing criteria, with scope and freshness recorded. |
| **Recovery capacity** | Resources needed to restore, fail over, sustain minimum service, or rebuild a workload. Include destination baseline use and competing recovery demand. |
| **Recovery point objective (RPO)** | The acceptable data-loss window for a specified service and scenario. Its replication or restoration requirements affect capacity planning. |
| **Recovery profile** | Stage-by-stage resource and dependency requirements for a defined recovery scenario, distinct from normal production and peak profiles. |
| **Recovery time objective (RTO)** | The target elapsed time to restore the agreed service level after disruption. A target is not evidence that it has been achieved. |
| **Simultaneous portfolio recovery** | A scenario in which several workloads recover together and may compete for shared destination resources or dependencies. |
| **Workload placement** | Selection of acceptable infrastructure environments, services, families, regions, and zones for a workload and its dependencies. |

## Decisions, evidence, and practice

| Term | Working meaning |
|---|---|
| **Capability** | Repeatable work with defined inputs, activities, outputs, roles, and evidence that supports an operational outcome. |
| **Central stewardship** | Maintenance of common definitions, records, review quality, and cross-portfolio visibility without absorbing every workload decision. |
| **Decision deadline** | The last useful point for an authorized choice while a viable response can still be prepared and executed. It may be earlier than the required deployment date. |
| **Domain** | A grouping of related business outcomes and capabilities, not necessarily a team or sequential project phase. |
| **Evidence freshness** | Whether a record is current enough for its intended decision under an explicit, source-specific rule. Fresh evidence can still be incomplete or incorrect. |
| **Exception** | An authorized, time-bound departure from a rule with rationale, owner, compensating measures, and review conditions. |
| **Federated accountability** | Workload and functional owners retain responsibility for decisions within their authority while participating in a common practice. |
| **FinOps** | A practice connecting technology use, financial accountability, collaboration, and business value. The affordability comparison is introductory shorthand, not a complete definition of FinOps. |
| **Key performance indicator (KPI)** | A selected measure tied to an intended outcome and decision, with a defined population, formula, owner, and organization-defined target. |
| **Maturity** | Evidence of repeatable capability behavior and decision quality, assessed as Reactive, Aware, Managed, Optimized, or Strategic. Different capabilities and business units may have different levels. |
| **Residual risk** | Exposure remaining after a response is chosen or implemented, including uncertainty that a completed action does not remove. |
| **Risk owner** | The person authorized to accept or direct treatment of the relevant exposure. This may differ from the person implementing the action or coordinating the record. |

## Use terms precisely

In a decision record, replace “capacity is available” with the actual evidence: for example, “the scoped quota was verified on the review date; the deployment quantity is not yet validated.” Replace “reservation covers the workload” with the mechanism, dimensions, conditions, matching demand version, and uncovered dependencies.

## Risks and common mistakes

- Using quota, forecast, financial commitment, and capacity reservation as synonyms.
- Describing regional service availability as proof of quantity or date fulfillment.
- Treating a recovery design or multi-region topology as recovery capacity evidence.
- Using “capacity assurance” or “capacity guarantee” without a specific mechanism supported by current public documentation.
- Allowing an average maturity score or metric to conceal a critical unresolved weakness.

## Related content

- [What is CapOps?](overview/what-is-capops.md)
- [Principles](overview/principles.md)
- [Capability catalog](framework/capabilities.md)
- [Capacity acquisition](capabilities/capacity-acquisition.md)
- [Capacity resilience](capabilities/capacity-resilience.md)
- [Reporting and key performance indicators](capabilities/reporting-and-kpis.md)
