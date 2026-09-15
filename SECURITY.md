# Security policy

Use this policy to report sensitive repository material or a vulnerability in documentation tooling without creating a public disclosure.

## Scope

This project contains documentation, templates, build scripts, and a static documentation site. It is not a production capacity service. Maintainers review the default branch; there is no separate supported-release matrix or promised response time.

Report exposed secrets, confidential data, unsafe workflow behavior, or an exploitable tooling issue privately. Ordinary documentation inaccuracies can use the provider-correction or documentation issue form after removing sensitive details.

## Private reporting

Use the repository's **Security > Advisories > Report a vulnerability** control when private vulnerability reporting is enabled. Provide the affected path, impact, and minimal safe reproduction. Do not include live credentials, account identifiers, customer architectures, or nonpublic provider data.

If the private control is unavailable, do not open a public issue containing the details. Request a private contact without disclosing the incident, or use GitHub platform reporting for exposed sensitive content. Do not assume any public issue, pull request, or discussion is private.

## If information was exposed

Credential owners should revoke or rotate exposed credentials promptly through their established process. Removing a line from the current branch does not remove it from history, caches, or forks. Maintainers should coordinate containment and consult GitHub's sensitive-data removal guidance; do not silently rewrite shared history.

Maintainers assess the report, contain the exposure, correct attributable defects, and publish only a sanitized explanation when appropriate. Private reports are reviewed with minimum necessary access.

## Contributor precautions

Source archives, presentations, extraction files, private notes, account identifiers, and secrets do not belong in commits or build artifacts. Check staged files as well as the working tree. Automated pattern scans are incomplete and must be paired with human review.

## Related content

- [Contributing](CONTRIBUTING.md)
- [Validation report](VALIDATION.md)
- [Disclaimer](DISCLAIMER.md)
