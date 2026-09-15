import { mkdir, readdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const output = path.join(root, "test-results", "diagrams");
await mkdir(output, { recursive: true });

async function markdownFiles(directory) {
  const result = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const filename = path.join(directory, entry.name);
    if (entry.isDirectory()) result.push(...await markdownFiles(filename));
    else if (entry.name.endsWith(".md")) result.push(filename);
  }
  return result;
}

const browser = await chromium.launch();
let count = 0;
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  await page.setContent("<!doctype html><html><body><main></main></body></html>");
  await page.addScriptTag({ path: path.join(root, "node_modules", "mermaid", "dist", "mermaid.min.js") });
  await page.evaluate(() => window.mermaid.initialize({ startOnLoad: false, securityLevel: "strict" }));
  for (const filename of await markdownFiles(path.join(root, "docs"))) {
    const text = await readFile(filename, "utf8");
    for (const match of text.matchAll(/^```mermaid\s*\n([\s\S]*?)^```\s*$/gm)) {
      count += 1;
      const svg = await page.evaluate(async ({ source, id }) => {
        await window.mermaid.parse(source);
        const result = await window.mermaid.render(id, source);
        document.querySelector("main").innerHTML = result.svg;
        const diagram = document.querySelector("main svg");
        if (!diagram || diagram.getBoundingClientRect().height === 0) {
          throw new Error("Diagram rendered without visible SVG content");
        }
        return result.svg;
      }, { source: match[1], id: `diagram-${count}` });
      await writeFile(path.join(output, `${count}.svg`), svg);
      await page.locator("main").screenshot({ path: path.join(output, `${count}.png`) });
      console.log(`PASS diagram ${count}: ${path.relative(root, filename)}`);
    }
  }
  if (count < 7) throw new Error(`Expected at least seven diagrams, found ${count}`);
  console.log(`PASS: ${count} Mermaid diagrams parsed and rendered in Chromium.`);
} finally {
  await browser.close();
}
