"""Validate publication structure and local links; never certify confidentiality."""

import argparse
from collections import Counter, defaultdict
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import markdown
import yaml

from community_pages import POLICIES


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".venv", "node_modules", "site", "__pycache__", "test-results", "playwright-report"}
CANONICAL = (
    "CapOps, or Capacity Operations, is an operational framework and cultural practice "
    "for forecasting, securing, allocating, governing, monitoring, optimizing, and "
    "validating cloud and infrastructure capacity so workloads can be deployed, "
    "scaled, and recovered where and when the business needs them."
)
CAPABILITY_SECTIONS = (
    "Definition", "Purpose", "Why it matters", "Desired outcomes", "Inputs", "Activities",
    "Outputs", "Roles involved", "Dependencies on other capabilities",
    "Suggested measurements", "Maturity indicators", "Practical example",
    "Risks and common mistakes", "Related content",
)
SCENARIO_SECTIONS = (
    "Business context", "Capacity challenge", "Demand dimensions", "Important assumptions",
    "Relevant CapOps capabilities", "Recommended actions", "Potential alternatives",
    "FinOps considerations", "Residual risks", "Common mistakes", "Example decision record",
)
DOMAIN_SECTIONS = (
    "Objective", "Business outcome", "Included capabilities", "Main activities",
    "Primary inputs", "Expected outputs", "Participating personas", "Example decisions",
)


class DocumentationLoader(yaml.SafeLoader):
    # YAML 1.1 treats the GitHub Actions key "on" as a boolean.
    yaml_implicit_resolvers = {
        key: [item for item in values if item[0] != "tag:yaml.org,2002:bool"]
        for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
    }

    def construct_mapping(self, node, deep=False):
        keys = [self.construct_object(key, deep=deep) for key, _ in node.value]
        if len(keys) != len(set(keys)):
            raise ValueError("Duplicate YAML mapping key")
        return super().construct_mapping(node, deep=deep)


DocumentationLoader.add_constructor(
    "tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format",
    lambda loader, node: loader.construct_scalar(node),
)


class Document(HTMLParser):
    def __init__(self, content):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.headings = []
        self.heading = None
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        if tag in {"a", "img", "script", "link"}:
            target = values.get("href") or values.get("src")
            if target:
                self.links.append(target)
        if re.fullmatch(r"h[1-6]", tag):
            self.heading = [int(tag[1]), ""]

    def handle_data(self, data):
        if self.heading is not None:
            self.heading[1] += data

    def handle_endtag(self, tag):
        if re.fullmatch(r"h[1-6]", tag) and self.heading is not None:
            self.headings.append(tuple(self.heading))
            self.heading = None


def source_files():
    for directory, dirs, names in os.walk(ROOT):
        dirs[:] = sorted(name for name in dirs if name not in IGNORED)
        for name in sorted(names):
            yield Path(directory) / name


def parse_markdown(text):
    return Document(markdown.markdown(text, extensions=["tables", "fenced_code", "toc"]))


def nav_paths(node):
    if isinstance(node, list):
        for item in node:
            yield from nav_paths(item)
    elif isinstance(node, dict):
        for value in node.values():
            yield from nav_paths(value)
    elif isinstance(node, str):
        yield node


def missing_sections(text, sections):
    missing = []
    for section in sections:
        match = re.search(rf"^## {re.escape(section)}[ \t]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        if not match or not match[1].strip():
            missing.append(section)
    return missing


def check_links(documents, boundary, errors, site=False, site_url=""):
    count = 0
    site_parts = urlsplit(site_url)
    prefix = site_parts.path.rstrip("/") + "/"
    for path, document in documents.items():
        for link in document.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                if not site or not site_parts.netloc or parts.netloc != site_parts.netloc:
                    continue
            count += 1
            if parts.path.startswith("/"):
                if not site:
                    errors.append(f"{path.relative_to(boundary)}: root-relative link {link}")
                    continue
                if not parts.path.startswith(prefix):
                    errors.append(f"{path.relative_to(boundary)}: link outside site URL prefix: {link}")
                    continue
                target = (boundary / unquote(parts.path[len(prefix):])).resolve()
            else:
                target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if not target.is_relative_to(boundary):
                errors.append(f"{path.relative_to(boundary)}: link escapes publication root: {link}")
                continue
            if site and target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"{path.relative_to(boundary)}: missing link {link}")
            elif parts.fragment and target in documents:
                anchor = unquote(parts.fragment)
                if anchor not in documents[target].ids:
                    errors.append(f"{path.relative_to(boundary)}: missing anchor {link}")
    return count


def check_source(errors):
    paths = list(source_files())
    texts = {}
    for path in paths:
        if path.suffix.lower() in {".zip", ".pptx", ".ppt", ".pdf", ".xml", ".pem", ".key"}:
            errors.append(f"Prohibited publication artifact: {path.relative_to(ROOT)}")
        if path.name.startswith(".env"):
            errors.append(f"Environment file in publication tree: {path.relative_to(ROOT)}")
        if path.suffix in {".md", ".yml", ".yaml", ".py", ".mjs", ".json", ".jsonc"}:
            text = path.read_text(encoding="utf-8")
            texts[path] = text
            if re.search(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
                         r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b", text):
                errors.append(f"Possible secret: {path.relative_to(ROOT)}")
            if path.suffix == ".md" and re.search(
                r"\b[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}\b|"
                r"[A-Z]:\\Users\\|docs\.azure\.cn", text
            ):
                errors.append(f"Private identifier/path or disallowed source: {path.relative_to(ROOT)}")
    documents = {path: parse_markdown(text) for path, text in texts.items() if path.suffix == ".md"}
    docs = {path: document for path, document in documents.items() if path.is_relative_to(ROOT / "docs")}
    titles = defaultdict(list)
    for path, document in documents.items():
        headings = document.headings
        if path.name != "pull_request_template.md":
            if len([h for h in headings if h[0] == 1]) != 1:
                errors.append(f"{path.relative_to(ROOT)}: expected exactly one H1")
        for previous, current in zip(headings, headings[1:]):
            if current[0] > previous[0] + 1:
                errors.append(f"{path.relative_to(ROOT)}: skipped heading level at {current[1]}")
        if path in docs:
            for level, title in headings:
                if level == 1:
                    titles[title.casefold()].append(path.relative_to(ROOT).as_posix())
            if len(texts[path].split()) < 50:
                errors.append(f"{path.relative_to(ROOT)}: page too short; inspect for a stub")
        if texts[path].count("```") % 2:
            errors.append(f"{path.relative_to(ROOT)}: unbalanced code fences")
    for title, files in titles.items():
        if len(files) > 1:
            errors.append(f"Duplicate documentation title {title!r}: {files}")
    for folder, expected in [("domains", 5), ("capabilities", 12), ("implementation", 10),
                             ("templates", 10), ("scenarios", 10), ("cloud-guidance", 4)]:
        actual = list((ROOT / "docs" / folder).glob("*.md"))
        if len(actual) != expected:
            errors.append(f"{folder}: expected {expected} pages, found {len(actual)}")
    for folder, sections in [("capabilities", CAPABILITY_SECTIONS), ("scenarios", SCENARIO_SECTIONS),
                             ("domains", DOMAIN_SECTIONS)]:
        for path in (ROOT / "docs" / folder).glob("*.md"):
            text = texts[path]
            for section in missing_sections(text, sections):
                errors.append(f"{path.relative_to(ROOT)}: missing/empty section {section}")
    for path in (ROOT / "docs" / "templates").glob("*.md"):
        if not re.search(r"^\|.*\|$", texts[path], re.M):
            errors.append(f"{path.relative_to(ROOT)}: missing copyable table")
    for relative in ["README.md", "docs/index.md", "docs/overview/what-is-capops.md"]:
        if CANONICAL not in texts[ROOT / relative]:
            errors.append(f"{relative}: canonical definition differs")
    config = None
    yaml_count = 0
    for path in paths:
        if path.suffix not in {".yaml", ".yml"}:
            continue
        yaml_count += 1
        data = yaml.load(texts[path], Loader=DocumentationLoader)
        if path.name == "mkdocs.yml":
            config = data
        if path.parent.name == "ISSUE_TEMPLATE" and path.name != "config.yml":
            if not all(key in data for key in ["name", "description", "body"]):
                errors.append(f"{path.relative_to(ROOT)}: incomplete issue form")
            ids = [field.get("id") for field in data["body"] if field["type"] != "markdown"]
            if None in ids or len(ids) != len(set(ids)):
                errors.append(f"{path.relative_to(ROOT)}: missing/duplicate issue field ID")
    if config is None:
        errors.append("Missing MkDocs configuration")
    else:
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        mermaid = package["devDependencies"]["mermaid"]
        if f"https://unpkg.com/mermaid@{mermaid}/dist/mermaid.min.js" not in config.get("extra_javascript", []):
            errors.append("Browser Mermaid version must match the tested package version")
        expected = {path.relative_to(ROOT / "docs").as_posix() for path in docs}
        expected.update(f"project/{name}" for name in POLICIES)
        expected.add("project/LICENSE.md")
        entries = list(nav_paths(config["nav"]))
        actual = {entry for entry in entries if not urlsplit(entry).scheme}
        if expected != actual:
            errors.append(f"Navigation mismatch: missing={sorted(expected - actual)}, extra={sorted(actual - expected)}")
        if len(entries) != len(set(entries)):
            errors.append("Duplicate navigation destinations")
    diagrams = sum(text.count("```mermaid") for path, text in texts.items() if path in docs)
    if diagrams < 7:
        errors.append(f"Expected at least seven Mermaid diagrams, found {diagrams}")
    for path in (ROOT / "docs" / "cloud-guidance").glob("*.md"):
        text = texts[path]
        if ("## References" not in text or not re.search(r"202\d-\d{2}-\d{2}", text)
                or not re.search(r"https://", text)):
            errors.append(f"{path.relative_to(ROOT)}: references or review date missing")
    repeated = Counter(
        paragraph.strip() for path, text in texts.items() if path in docs
        for paragraph in text.split("\n\n")
        if len(paragraph.strip()) >= 160 and not paragraph.startswith(("|", "```"))
    )
    repeated_count = sum(count >= 4 for count in repeated.values())
    links = check_links(documents, ROOT, errors)
    print(f"Source: {len(paths)} files; {len(documents)} Markdown files; {len(docs)} documentation pages; "
          f"{yaml_count} YAML files; {links} local links; {diagrams} Mermaid diagrams.")
    print(f"Editorial attention: {repeated_count} long paragraphs repeated in at least four pages. "
          "Repetition, semantic accuracy, acronym use and confidentiality still require editorial review.")


def check_site(site, errors):
    documents = {path.resolve(): Document(path.read_text(encoding="utf-8")) for path in site.rglob("*.html")}
    if not documents or not (site / "index.html").is_file():
        errors.append("Generated site is missing or empty")
    config = yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=DocumentationLoader)
    links = check_links(documents, site, errors, site=True, site_url=config.get("site_url", ""))
    for entry in nav_paths(config["nav"]):
        if entry.endswith(".md") and not urlsplit(entry).scheme:
            relative = entry[:-8] if entry.endswith("index.md") else entry[:-3]
            if not (site / relative / "index.html").is_file():
                errors.append(f"Navigation page missing from generated site: {entry}")
    if not (site / "search" / "search_index.json").is_file():
        errors.append("Missing search index")
    print(f"Generated site: {len(documents)} HTML files; {links} local links and asset references checked.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, help="Check an existing generated site instead of sources")
    args = parser.parse_args()
    errors = []
    if args.site:
        check_site(args.site.resolve(), errors)
    else:
        check_source(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("PASS: requested structural/link checks. Not a legal or confidentiality certification.")


if __name__ == "__main__":
    main()
