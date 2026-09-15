# CapOps documentation

Use this proposed independent community framework to make capacity assumptions, decisions, and ownership explicit.

CapOps, or Capacity Operations, is an operational framework and cultural practice for forecasting, securing, allocating, governing, monitoring, optimizing, and validating cloud and infrastructure capacity so workloads can be deployed, scaled, and recovered where and when the business needs them.

FinOps asks, **"Can we afford it?"** CapOps asks, **"Can we get it where and when we need it?"** Organizations need both answers. The comparison is a shorthand: CapOps complements, rather than replaces, FinOps and its broader business-value practice.

## Choose a starting point

- [What is CapOps?](overview/what-is-capops.md)
- [Framework overview](framework/framework-overview.md)
- [Capabilities](framework/capabilities.md)
- [Operating model](operating-model/operating-model.md)
- [Maturity model](maturity/maturity-model.md)
- [Getting started](implementation/getting-started.md)
- [Demand submission template](templates/capacity-demand-template.md)
- [Fictional migration scenario](scenarios/cloud-migration.md)

Read the overview before selecting a domain. Use capabilities to identify the work, personas to locate decision owners, and the lifecycle to connect evidence to action. Start with a bounded set of workloads rather than a portfolio-wide tool rollout.

## Keep evidence separate from assumptions

Quota grants administrative permission; it is not physical capacity. Forecasts describe expected demand, not provider commitments. Discounts and capacity reservations are different mechanisms unless a documented product explicitly combines them. A region's service catalog does not establish that a requested quantity can deploy on a required date.

A recovery design needs a destination-capacity path, including shared dependencies and concurrent workload demand. Multiple regions create options, not an automatic guarantee.

## What this project is

The framework proposes a shared operating practice, not a certification or an established standard. It is not an official Microsoft product or methodology, a Microsoft capacity-guarantee program, or a FinOps Foundation extension. It is not endorsed by any provider. Provider guidance contains public, dated references; core pages remain provider-neutral.

The practical content includes twelve capability descriptions, ten implementation guides, ten copyable table templates, and ten fictional scenarios. Numerical examples are illustrative and measurement targets are organization-defined.

## Related content

- [Principles](overview/principles.md)
- [CapOps and FinOps](overview/capops-and-finops.md)
- [Framework overview](framework/framework-overview.md)
