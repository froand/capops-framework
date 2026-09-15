"""Expose root policies and preserve readable diagrams in the generated site."""

from pathlib import Path
import re

from mkdocs.structure.files import File


POLICIES = (
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "DISCLAIMER.md",
    "ROADMAP.md",
    "WHATS_NEW.md",
    "VALIDATION.md",
)


def on_files(files, config):
    root = Path(config.config_file_path).parent
    for name in POLICIES:
        content = (root / name).read_text(encoding="utf-8")
        content = content.replace("](docs/", "](../")
        content = content.replace("](LICENSE)", "](LICENSE.md)")
        content = content.replace("](README.md)", "](../index.md)")
        files.append(File.generated(config, f"project/{name}", content=content))
    license_text = (root / "LICENSE").read_text(encoding="utf-8")
    files.append(
        File.generated(
            config,
            "project/LICENSE.md",
            content="# Project license\n\nThe repository retains the baseline MIT license.\n\n"
            f"```text\n{license_text.rstrip()}\n```\n",
        )
    )
    return files


def on_page_content(html, **kwargs):
    return re.sub(
        r'(<pre class="mermaid">.*?</pre>)',
        r'<p class="capops-diagram-note">Diagram: scroll horizontally on narrow screens. '
        r'An equivalent explanation appears in the surrounding text.</p>'
        r'<div class="capops-diagram" role="region" tabindex="0" '
        r'aria-label="Diagram, horizontally scrollable">\1</div>',
        html,
        flags=re.S,
    )
