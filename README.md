# CapOps Framework

**CapOps, or Capacity Operations, is an operational framework and cultural practice for forecasting, securing, allocating, governing, monitoring, optimizing, and validating cloud and infrastructure capacity so workloads can be deployed, scaled, and recovered where and when the business needs them.**

> **Project status:** Proposed independent community framework and cultural practice. CapOps is not an official Microsoft product or methodology, a FinOps Foundation extension, an established industry standard, or a capacity-guarantee program.

[Documentation site](https://froand.github.io/capops-framework/) | [GitHub repository](https://github.com/froand/capops-framework)

## Why CapOps exists

An approved budget and a supported service do not answer every deployment question. Capacity constraints can depend on service, resource family, region, zone, quantity, date, or a combination of these dimensions. This is not a claim that cloud capacity is generally unavailable. It is a reason to identify the assumptions behind important migrations, growth, artificial intelligence workloads, seasonal peaks, and recovery plans.

FinOps asks, **"Can we afford it?"**

CapOps asks, **"Can we get it where and when we need it?"**

Organizations need both answers. This comparison is a useful introduction, not a complete definition of FinOps, which also addresses business value and shared financial accountability. CapOps complements rather than replaces that practice.

## Framework at a glance

The framework organizes CapOps into five domains:

1. **Understand capacity**: Build visibility into demand, usage, limits, dependencies, constraints, and risk.
2. **Plan capacity**: Convert business roadmaps into time-bound technical demand forecasts.
3. **Secure and allocate capacity**: Use suitable quota, reservation, provider-engagement, and allocation mechanisms.
4. **Operate and optimize capacity**: Monitor, govern, reclaim, modernize, and improve capacity efficiency.
5. **Manage the CapOps practice**: Establish ownership, cadence, measurement, enablement, and continuous improvement.

## Start here

- [What is CapOps?](docs/overview/what-is-capops.md)
- [Why CapOps?](docs/overview/why-capops.md)
- [CapOps principles](docs/overview/principles.md)
- [CapOps and FinOps](docs/overview/capops-and-finops.md)
- [Framework overview](docs/framework/framework-overview.md)
- [Getting started](docs/implementation/getting-started.md)
- [Maturity model](docs/maturity/maturity-model.md)
- [Glossary](docs/glossary.md)

## Repository content

The learning path covers ten principles, five domains, twelve capabilities, ten personas, and a nine-step iterative lifecycle. It connects these concepts to a decision-focused operating model and a five-level maturity model assessed across thirteen dimensions.

Ten implementation guides, ten copyable table templates, and ten fictional scenarios make the framework usable without adopting a new tool or creating a department. Four [provider guidance pages](docs/cloud-guidance/azure.md) map terminology using dated public references; their mechanisms do not apply universally to every service.

## Try one decision

Choose a capacity-sensitive workload. Complete its [capacity profile](docs/templates/workload-capacity-profile.md), separate production, peak, and recovery demand, and name acceptable alternatives. Record one material gap in the [risk register](docs/templates/capacity-risk-register.md), with a business owner and decision deadline. Use the [monthly review](docs/implementation/monthly-capops-review.md) to choose an action, not merely report status.

Quota is not physical capacity. A forecast is not a provider commitment. A financial discount is not necessarily a capacity reservation. Regional service availability does not prove fulfillment of a particular quantity or date. Resilience architecture and multiple regions do not establish available recovery capacity.

Here, "secure capacity" includes planning, quota, supported reservations, architecture flexibility, allocation, and established provider-engagement mechanisms. It never means unconditional availability.

## Build and check locally

Use Python 3.11 or later and Node.js 22 or later. From the repository root:

```shell
python -m pip install -r requirements.txt
npm ci
python scripts/validate_docs.py
npm run lint
python -m mkdocs build --strict
python scripts/validate_docs.py --site site
npm run diagrams
python -m mkdocs serve
```

The local site is served at `http://127.0.0.1:8000`. The diagram check uses Playwright Chromium; install its browser once with `npx playwright install chromium`. On Linux hosts that lack browser libraries, use `npx playwright install --with-deps chromium`.

The source checker validates Markdown links and anchors, page contracts, navigation, YAML, and common publication hazards. The site checker validates generated local links, fragments, and every navigation page, including templates and project policies. Mermaid uses the same version in browser and syntax checks; diagrams can scroll horizontally on narrow screens rather than shrinking their labels. These checks support, but cannot replace, editorial and confidentiality review. See [VALIDATION.md](VALIDATION.md) for actual publication results and limitations.

## Project direction

See [WHATS_NEW.md](WHATS_NEW.md) for documentation changes and [ROADMAP.md](ROADMAP.md) for proposed releases. Roadmap items are review goals, not dated commitments, certification criteria, or evidence of industry adoption.

## Contributing

CapOps is intended to improve through practical, public feedback. Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Contributions must use public information and must not include confidential customer data, nonpublic provider information, or unsupported claims.

## Disclaimer

This project is an independent community proposal. It is not affiliated with or endorsed by Microsoft, the FinOps Foundation, Amazon Web Services, Google Cloud, or any other cloud provider. See [DISCLAIMER.md](DISCLAIMER.md).

## License

Documentation and code in this repository are licensed under the [MIT License](LICENSE), unless stated otherwise.
