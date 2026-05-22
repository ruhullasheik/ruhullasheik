"""Convert pages/Ruhulla_Sheik_Resume.md to pages/Ruhulla_Sheik_Resume.pdf."""

from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

MD_PATH = Path("pages/Ruhulla_Sheik_Resume.md")
PDF_PATH = Path("pages/Ruhulla_Sheik_Resume.pdf")

CSS_STYLES = """
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 9.5pt;
    line-height: 1.45;
    color: #1a1a1a;
    max-width: 900px;
    margin: 0 auto;
    padding: 0 4px;
}

h1 {
    font-size: 18pt;
    font-weight: 700;
    margin: 0 0 4px 0;
    color: #0f172a;
}

h2 {
    font-size: 10.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #1e40af;
    border-bottom: 1.5px solid #bfdbfe;
    padding-bottom: 2px;
    margin: 14px 0 6px 0;
}

h3 {
    font-size: 10pt;
    font-weight: 700;
    color: #0f172a;
    margin: 10px 0 1px 0;
}

h4 {
    font-size: 9.5pt;
    font-weight: 600;
    color: #334155;
    margin: 7px 0 2px 0;
}

p { margin: 3px 0 5px 0; }

ul {
    margin: 3px 0 5px 0;
    padding-left: 16px;
}

li { margin-bottom: 2px; }

code {
    font-family: "Consolas", "Courier New", monospace;
    font-size: 8.5pt;
    background: #f1f5f9;
    border: 0.5px solid #cbd5e1;
    border-radius: 3px;
    padding: 0 3px;
    color: #0f172a;
}

table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8.8pt;
    margin: 4px 0 8px 0;
}

th {
    text-align: left;
    font-weight: 700;
    background: #f8fafc;
    border: 0.5px solid #e2e8f0;
    padding: 4px 7px;
    color: #334155;
    white-space: nowrap;
}

td {
    border: 0.5px solid #e2e8f0;
    padding: 4px 7px;
    vertical-align: top;
}

hr {
    border: none;
    border-top: 0.5px solid #e2e8f0;
    margin: 8px 0;
}

blockquote {
    border-left: 3px solid #bfdbfe;
    margin: 6px 0;
    padding: 5px 10px;
    background: #f8fafc;
    font-style: italic;
    color: #334155;
    font-size: 9pt;
}

a { color: #1e40af; text-decoration: none; }
"""


def build_pdf() -> None:
    md_text = MD_PATH.read_text(encoding="utf-8")
    html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Ruhulla Sheik — Resume</title>
  <style>{CSS_STYLES}</style>
</head>
<body>{html_body}</body>
</html>"""

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html, wait_until="domcontentloaded")
        page.pdf(
            path=str(PDF_PATH),
            format="A4",
            margin={"top": "18mm", "bottom": "16mm", "left": "16mm", "right": "16mm"},
            print_background=True,
        )
        browser.close()

    print(f"Generated: {PDF_PATH}")


if __name__ == "__main__":
    build_pdf()
