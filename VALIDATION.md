# Validation report

This report records checks performed for the initial CapOps publication and their limits. It is not a certification of legal originality, security, or provider capacity.

## Review date and scope

Review date: **2026-09-15**. The original 73-file baseline and all 15 presentation slides and associated speaker notes were inspected before changes. The publication candidate contains **102 source files, 82 Markdown files, and 71 documentation pages** under `docs`, expanded from 57 baseline documentation pages. Nine generated project-policy pages reuse root sources; the built site contains 80 content pages plus its 404 page.

## Baseline defects reproduced

The baseline command `python -m mkdocs build --strict` failed with **25 missing navigation targets**. Navigation incorrectly prefixed page paths with `docs/` under the default documentation directory. Most pages were omitted, and the default exclusion of the `templates` directory prevented template links from resolving in the site.

Capability pages repeated generic text and lacked required sections; scenario and provider pages were brief placeholders. Five implementation guides, five templates, and four scenarios were missing. Provider references and review dates were absent. The inherited validation counts were not treated as evidence.

## Source handling and editorial decisions

Original archives and the presentation remain unmodified outside the repository. The complete source-to-page mapping is private and is not distributed. No raw presentation text dump, notes, XML, artwork, or source archive is part of the public project.

The strongest accurate concepts were independently rewritten: demand specificity, business-to-technical forecasting, customer-side visibility, supported capacity mechanisms, architecture flexibility, lifecycle ownership, decision deadlines, and distinct production, peak, and recovery profiles.

The requested canonical definition, five domains, nine-stage lifecycle, and thirteen maturity dimensions take precedence over the presentation's shorter organization. Source pillars become concepts within the requested domains and capabilities. Accountability is decision-specific rather than assigned universally to the practice lead.

Unsupported prevalence, causal, efficacy, staffing, adoption-speed, savings, and delivery-assurance claims were excluded. Provider engagement is not presented as a commitment or an assurance ladder. Multi-region architecture is an evaluated option, not a universal requirement or capacity guarantee. Examples are newly written and fictional.

## License and attribution

The baseline MIT license and existing collective contributor notice are retained unchanged. Provider documentation is referenced, not reproduced. No new named author, employer approval, ownership attestation, or legal clearance is asserted. The editorial review can describe original drafting and checks performed; it cannot prove legal originality or every source right.

## Check status

The local publication gate passed. The commands below were actually executed, and attributable failures were corrected before publication.

| Check | Command or method | Result |
| --- | --- | --- |
| Checker regression tests | `python -m unittest discover -s scripts -p "test_*.py"` | Seven tests passed, including empty sections, YAML keys, file/anchor failures, project-prefixed site links, and diagram wrappers |
| Source structure and links | `python scripts/validate_docs.py` | 102 files, 82 Markdown files, 71 documentation pages, eight YAML files, 476 local links, and seven diagrams checked; no failures |
| Required content shapes | Source contracts and targeted table/heading assertions | Twelve capabilities with fourteen sections each; five complete domains; ten principles and personas; thirteen maturity dimensions with five populated evidence columns; ten guides, templates, and scenarios; four provider pages |
| Markdown lint | `npm run lint` | All 82 Markdown files passed |
| Strict documentation build | `python -m mkdocs build --strict` | Passed; all templates and navigation pages included |
| Generated site | `python scripts/validate_docs.py --site site` | All 81 HTML files, local links, fragments, assets, search index, and navigation destinations passed |
| Mermaid | `npm run diagrams` | All seven diagrams parsed and rendered in Chromium; generated images inspected |
| Browser behavior | Local Playwright Chromium checks at 1440px and 390px viewport widths | Search returned recovery-capacity results; actual code-copy placed the expected command on the clipboard; template tables rendered; home and template avoided page overflow; all seven diagrams rendered and supported keyboard horizontal scrolling |
| Diagram readability | Rendered label-size measurement within the 688px desktop article | Representative node labels ranged from approximately 13.7px to 16px after layout corrections; equivalent surrounding prose retained |
| Dependency advisory check | `npm ci` and `npm audit --audit-level=moderate` | Clean install and zero reported npm vulnerabilities at review time |
| Staged publication artifacts | `git diff --cached --check`, file inventory, extension/path checks, and editorial review | No whitespace errors after LF normalization; no source archive, presentation, XML, private analysis, credential-container file, dependencies, or generated test/build output staged |
| Source integrity and license | Original-file SHA-256 comparison and byte comparison of inherited license | Both originals unchanged; inherited MIT license unchanged |
| Provider references | Dated direct reads and claim-to-source reconciliation | 22 final authoritative references successfully accessed: Azure four, AWS eight, Google Cloud six, hybrid/private four |

The complete desktop/mobile browser evidence and source-to-page mapping remain private. The repository's repeatable CI checks do not depend on private source artifacts or those private test files.

## Defects found and corrected

- Removed 25 invalid `docs/` navigation prefixes and included every documentation page in the learning path.
- Explicitly re-included the ten templates excluded by the default MkDocs configuration. A strict build alone had not detected every exclusion; generated-navigation checks now verify each expected output file.
- Corrected two standalone-emphasis Markdown lint errors and ambiguous adjacent numeric citations in provider pages.
- Replaced two unsuccessful public-reference lookups with successfully read current pages; neither failed URL is cited.
- Reworked wide lifecycle, domain, maturity, operating-model, and risk diagrams after browser measurements exposed unreadably small labels. Added focusable horizontal-scroll regions for narrow screens.
- Aligned browser Mermaid with the tested package version instead of the theme's floating major-version URL.
- Added a scoped dependency override after an actual npm advisory check identified the linter's pinned TOML parser; the clean-install advisory check then passed.
- Normalized staged text to LF through repository attributes rather than changing global Git behavior.

Browser-test assumptions also required correction: the theme renders Mermaid inside closed shadow roots and its current copy control uses a different selector. The checks now inspect the actual native rendering and clipboard behavior rather than treating selector failures as site defects.

## Editorial and confidentiality review

All authored framework, practice, scenario, provider, and project-policy pages received scoped editorial review. Checks covered terminology, acronym expansion, provider neutrality, fictional examples, measurement scope, source distinctions, and unsupported assurance/statistical statements. Automated inventories supplemented that review; no long paragraph appeared in four or more documentation pages.

No confidential customer information, internal provider process, current regional inventory, raw notes, source artwork, private paths, account identifiers, or credentials were identified in the reviewed publication content. Core provider-name references are confined to explicit independence statements. Product names in provider guidance identify documented mechanisms, not endorsements.

The 22 provider references have private claim/access mappings. Relevant claim-bearing sections were read; several long pages were only partially retrieved, and unused examples or tables were not represented as reviewed. Reference access means readable public documentation, not confirmation of account eligibility, fulfillment, or contractual protection.

## Publication status

The validated repository was published to [froand/capops-framework](https://github.com/froand/capops-framework) on **2026-09-15**, with `main` as the default branch.

The [initial Documentation workflow](https://github.com/froand/capops-framework/actions/runs/34965776260) completed successfully for commit `72efea7625db94f08ca41e933ed8e560910691d3`. Both its Ubuntu build and Pages deployment jobs succeeded. This is the observed initial publication run, not a claim about every future revision; see the [workflow history](https://github.com/froand/capops-framework/actions/workflows/docs.yml) for later changes.

The [HTTPS documentation site](https://froand.github.io/capops-framework/) was verified live. The home page, a template, Azure guidance, this policy page, search index, and 404 document returned HTTP 200. The same browser checks then passed on the live site: search results, actual clipboard copying, all seven native diagrams, representative label sizes, mobile layout, and keyboard diagram scrolling.

All nine requested topics and eight requested labels were configured. Private vulnerability reporting is enabled. The remote `main` commit matched the local publication commit. An initial push was rejected because the active credential lacked workflow scope; a process-only switch to the existing, separately verified same-owner credential resolved the push without changing global authentication configuration or rewriting history.

## Known limitations

Pattern scanning cannot establish that text is confidential or original. Citation access does not establish that an entire page is correct; claims must be compared with the referenced scope. Example numbers and locally selected targets are not benchmarks. Rendering and representative label-size checks do not replace comprehensive accessibility testing with assistive technology.

Provider terms and supported features can change after the review date. No cloud-workload deployment, quota request, reservation purchase, or real recovery exercise was performed. The framework is a proposed practice, not evidence that capacity can be obtained.

The browser checks used Chromium, not every supported browser. The site loads Mermaid from a versioned public CDN and theme fonts from external services; it is not an offline distribution. The npm audit is a point-in-time advisory check of Node dependencies, not a full supply-chain or application-security audit.

The successful hosted run reported GitHub annotations that several pinned actions declare Node.js 20 and are being executed on Node.js 24. These did not fail the run; reviewing those action pins is a maintenance item, not evidence of a completed runtime migration.

## Recommended future improvements

Prioritize independent practitioner review, periodic provider-reference review, accessible diagram review, more end-to-end fictional iterations, and explicit maintenance ownership for any future assessment tool.
