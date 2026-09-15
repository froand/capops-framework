# Contributing to the CapOps Framework

Use this guide to propose clear, evidence-based improvements to the independent CapOps community proposal.

## Before opening an issue

Search existing issues and choose the relevant form: documentation, framework feedback, capability proposal, scenario proposal, or provider-guidance correction. Describe the decision a reader cannot make today and the change that would help. A small, concrete correction is as useful as a new capability.

Use fictional or fully public examples. Never submit customer information, credentials, account identifiers, private provider communications, regional inventory observations, or internal processes. See [SECURITY.md](SECURITY.md) if material is sensitive.

## Editorial contract

Write your own prose; link to authoritative sources rather than copying their text or diagrams. Keep the exact canonical definition in [What is CapOps?](docs/overview/what-is-capops.md). Describe CapOps as a proposed community framework and cultural practice, not an official provider method, a FinOps Foundation extension, an established standard, or a capacity guarantee.

Core pages remain provider-neutral. Product names and mechanism details belong in provider guidance. Distinguish quota from physical capacity, forecasts from commitments, financial discounts from capacity reservations, service catalogs from fulfillable quantities, and resilience designs from available recovery capacity.

Start pages with their purpose. Define acronyms on first use, use descriptive headings, provide actionable examples and relevant mistakes, and link related material. Capability pages retain all fourteen sections. Scenario pages retain the eleven scenario sections and mark examples as fictional. Measurement targets are organization-defined; show the scope, denominator, evidence date, and limitations.

Provider corrections need a direct authoritative public reference, the claim it supports, a review date, and applicable restrictions. Microsoft references must use Microsoft Learn's public global site. Never extrapolate a virtual-machine feature to an unrelated managed service. State that capabilities and commercial terms can change.

## Change workflow

1. Fork the repository and use a focused branch.
2. Edit the existing page where possible. For new pages, add a descriptive filename and navigation entry.
3. Update [README.md](README.md) and [WHATS_NEW.md](WHATS_NEW.md) for material additions or behavior changes. Keep template links and related pages consistent.
4. Install the pinned dependencies and run the checks below.
5. Open a pull request explaining the reader problem, evidence, proposed change, and checks actually performed.

```shell
python -m pip install -r requirements.txt
npm ci
npx playwright install chromium
python scripts/validate_docs.py
npm run lint
python -m mkdocs build --strict
python scripts/validate_docs.py --site site
npm run diagrams
```

On Linux, Playwright may need `npx playwright install --with-deps chromium`. Use `python -m mkdocs serve` for a local preview. Check a narrow viewport, the tables, links, code-copy controls, search, and Mermaid diagrams. Review equivalent diagram prose even if rendering succeeds.

Repository policies are single-sourced at the root and exposed to the site by `scripts/community_pages.py`. Do not maintain a second copy under `docs`. The same hook wraps Mermaid diagrams in keyboard-focusable scroll regions, so narrow screens retain readable labels. The `templates` directory is explicitly included in the build and checked against generated navigation targets.

Validation dependencies are pinned. The linter's `smol-toml` dependency is overridden to version 1.8.0 to avoid the vulnerable 1.7.0 parser pinned by the current linter release. Re-evaluate this override when upgrading the linter; do not remove it without rerunning the dependency audit and Markdown checks. Run checker regression tests with `python -m unittest discover -s scripts -p "test_*.py"`.

Keep the browser Mermaid version in `mkdocs.yml` aligned with the version in `package.json`. The site uses a versioned public script rather than the theme's floating major-version default; browser rendering still requires access to that external asset.

## Review and attribution

Maintainers review factual accuracy, practical usefulness, confidentiality, accessibility, and consistency before merging. Foundational changes may need wider discussion; an open proposal is not an accepted standard. Do not claim benchmarks, certification, endorsement, or legal originality without supporting evidence.

Keep the existing MIT notice. Submit only material you have the right to contribute under the repository license; do not add someone else's authorship or employer approval. The initial editorial review is not a legal clearance process. Contributors retain responsibility for the material they submit.

For a disagreement, explain the alternative and its trade-offs in the pull request. Maintainers record the decision under [GOVERNANCE.md](GOVERNANCE.md). Follow the [code of conduct](CODE_OF_CONDUCT.md).
