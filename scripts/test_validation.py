"""Small regression tests for the repository's publication checks."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import yaml

from community_pages import on_page_content
from validate_docs import Document, DocumentationLoader, check_links, missing_sections, parse_markdown


class ValidationTests(unittest.TestCase):
    def test_diagram_wrapper_preserves_code_and_normal_blocks(self):
        diagram = '<pre class="mermaid"><code>flowchart TB\nA --&gt; B</code></pre>'
        result = on_page_content(diagram)
        self.assertIn(diagram, result)
        self.assertIn('tabindex="0"', result)
        self.assertIn('role="region"', result)
        ordinary = "<pre><code>example</code></pre>"
        self.assertEqual(on_page_content(ordinary), ordinary)

    def test_empty_section_does_not_borrow_following_content(self):
        text = "# Page\n\n## Definition\n\n## Purpose\nUseful purpose.\n"
        self.assertEqual(missing_sections(text, ["Definition", "Purpose"]), ["Definition"])
        self.assertEqual(missing_sections(text, ["Activities"]), ["Activities"])

    def test_yaml_preserves_actions_on_and_rejects_duplicates(self):
        self.assertIn("on", yaml.load("on:\n  push:\n", Loader=DocumentationLoader))
        with self.assertRaises(ValueError):
            yaml.load("name: one\nname: two\n", Loader=DocumentationLoader)

    def test_markdown_reference_link_and_anchor(self):
        with TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            first = root / "first.md"
            target = root / "target.md"
            first.write_text("[go][ref]\n\n[ref]: target.md#target-heading\n", encoding="utf-8")
            target.write_text("# Target heading\n", encoding="utf-8")
            documents = {p: parse_markdown(p.read_text(encoding="utf-8")) for p in (first, target)}
            errors = []
            self.assertEqual(check_links(documents, root, errors), 1)
            self.assertEqual(errors, [])
            documents[first] = parse_markdown("[bad](target.md#missing)")
            check_links(documents, root, errors)
            self.assertTrue(any("missing anchor" in error for error in errors))

    def test_missing_file_and_escape_are_errors(self):
        with TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            page = root / "index.md"
            page.write_text("# Page\n", encoding="utf-8")
            errors = []
            check_links({page: parse_markdown("[a](missing.md) [b](../private.md)")}, root, errors)
            self.assertEqual(len(errors), 2)

    def test_site_directory_links_and_asset_references(self):
        with TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "guide").mkdir()
            index = root / "index.html"
            target = root / "guide" / "index.html"
            index.write_text('<a href="guide/#steps">Guide</a><img src="missing.png">', encoding="utf-8")
            target.write_text('<h1 id="steps">Steps</h1>', encoding="utf-8")
            docs = {p: Document(p.read_text(encoding="utf-8")) for p in (index, target)}
            errors = []
            self.assertEqual(check_links(docs, root, errors, site=True), 2)
            self.assertEqual(len(errors), 1)
            self.assertIn("missing.png", errors[0])

    def test_generated_root_links_respect_project_site_prefix(self):
        with TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            index = root / "index.html"
            index.write_text('<h1 id="home">Home</h1>', encoding="utf-8")
            docs = {index: Document('<a href="/project/#home">Home</a><a href="/wrong/">Bad</a>')}
            docs[index].ids.add("home")
            errors = []
            check_links(docs, root, errors, site=True, site_url="https://example.org/project/")
            self.assertEqual(len(errors), 1)
            self.assertIn("outside site URL prefix", errors[0])


if __name__ == "__main__":
    unittest.main()
