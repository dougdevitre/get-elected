#!/usr/bin/env python3
"""Convert a branded Markdown file to a campaign PDF via WeasyPrint.

Each source .md may begin with an HTML metadata comment:

    <!--META
    doctype: STRATEGIC PLAN
    title: Campaign Plan
    subtitle: Matt Grant for Congress (MO-02)
    -->

If present, a navy cover page is rendered before the body. The body is
standard Markdown (tables, lists, blockquotes supported).

Usage: python3 md2pdf.py src/<name>.md ../documents/<name>.pdf
"""
import sys, re, datetime, pathlib
import markdown

BUILD = pathlib.Path(__file__).resolve().parent
CSS = (BUILD / "brand.css").read_text()

META_RE = re.compile(r"^<!--META\s*(.*?)-->\s*", re.DOTALL)

def parse(src: str):
    meta = {}
    m = META_RE.match(src)
    if m:
        for line in m.group(1).strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip().lower()] = v.strip()
        src = src[m.end():]
    return meta, src

def cover_html(meta):
    if not meta.get("title"):
        return ""
    today = datetime.date.today().strftime("%B %-d, %Y")
    return f"""
    <section class="cover">
      <div class="wordmark">GRANT <span class="red">for</span> CONGRESS</div>
      <div class="doctype">{meta.get('doctype','Campaign Document')}</div>
      <h1>{meta.get('title','')}</h1>
      <div class="subtitle">{meta.get('subtitle','')}</div>
      <div class="meta">Missouri's 2nd Congressional District &nbsp;·&nbsp; Prepared {today} &nbsp;·&nbsp; Internal campaign use</div>
    </section>
    """

def main():
    inp, outp = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    meta, body_md = parse(inp.read_text())
    body = markdown.markdown(body_md, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
    <style>{CSS}</style></head><body>{cover_html(meta)}{body}</body></html>"""
    from weasyprint import HTML
    HTML(string=html, base_url=str(BUILD)).write_pdf(str(outp))
    print(f"  ✓ {outp.name}")

if __name__ == "__main__":
    main()
