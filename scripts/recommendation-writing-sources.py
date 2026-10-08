#!/usr/bin/env python3
"""Cache the outline's primary sources and metadata; never infer missing fields."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "build/recommendation-writing/sources"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.metadata = {}
        self.text = []
        self.links = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.hidden += 1
        if tag == "meta":
            name = attrs.get("name", attrs.get("property", "")).lower()
            if name and "content" in attrs:
                self.metadata.setdefault(name, []).append(attrs["content"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag in ("p", "h1", "h2", "h3", "div", "li", "tr"):
            self.text.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden:
            self.text.append(data)


def catalog():
    text = (ROOT / "plans/recommendation-and-search-literature.md").read_text()
    items = {}
    for line in text.splitlines():
        match = re.match(r"\| ([RSEAHM]\d+) \| \[([^\]]+)\]\(([^)]+)\) \|", line)
        if match:
            key, title, url = match.groups()
            columns = line.split("|")
            items[key.lower()] = {
                "key": "rs-" + key.lower(), "title_in_map": title,
                "url": url, "publication_in_map": columns[3].strip(),
                "outline_positions": columns[-2].strip(),
            }
    return items


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "MLNotesSourceCheck/1.0"})
    with urllib.request.urlopen(request, timeout=25) as response:
        return response.read(), response.headers.get("Content-Type", "")


def fetch(key, item, fulltext=False):
    CACHE.mkdir(parents=True, exist_ok=True)
    record_path = CACHE / (key + ".json")
    if record_path.exists():
        record = json.loads(record_path.read_text())
    else:
        record = dict(item)
    if "metadata" not in record and "pdf_sha256" not in record:
        try:
            data, kind = get(item["url"])
            record["retrieved_url"] = item["url"]
            if data.startswith(b"%PDF"):
                save_pdf(key, data, record)
            else:
                html = data.decode("utf-8", errors="replace")
                (CACHE / (key + ".html")).write_text(html)
                parser = Page()
                parser.feed(html)
                record["metadata"] = parser.metadata
                record["links"] = parser.links
                (CACHE / (key + ".txt")).write_text("".join(parser.text))
            record.pop("error", None)
        except Exception as error:
            record["error"] = str(error)
    if fulltext and "pdf_sha256" not in record:
        pdf_url = None
        if "/abs/" in item["url"] and "arxiv.org" in item["url"]:
            pdf_url = item["url"].replace("/abs/", "/pdf/")
        else:
            pdf_url = next(iter(record.get("metadata", {}).get("citation_pdf_url", [])), None)
        if pdf_url:
            try:
                data, _ = get(pdf_url)
                if not data.startswith(b"%PDF"):
                    raise ValueError("The linked full text did not return a PDF")
                save_pdf(key, data, record)
                record["fulltext_url"] = pdf_url
                record.pop("fulltext_error", None)
            except Exception as error:
                record["fulltext_error"] = str(error)
    record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(key, "ERROR" if record.get("error") else "cached",
          "fulltext" if record.get("pdf_sha256") else "metadata", flush=True)


def save_pdf(key, data, record):
    path = CACHE / (key + ".pdf")
    path.write_bytes(data)
    record["pdf_sha256"] = hashlib.sha256(data).hexdigest()
    converter = shutil.which("pdftotext")
    if converter:
        subprocess.run([converter, "-layout", str(path), str(CACHE / (key + "-full.txt"))],
                       check=True, capture_output=True)
    else:
        import fitz
        with fitz.open(path) as document:
            (CACHE / (key + "-full.txt")).write_text(
                "\n".join(page.get_text(sort=True) for page in document))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("keys", nargs="*")
    parser.add_argument("--fulltext", action="store_true")
    parser.add_argument("--catalog", action="store_true")
    args = parser.parse_args()
    items = catalog()
    if args.catalog:
        CACHE.mkdir(parents=True, exist_ok=True)
        (CACHE.parent / "source-catalog.json").write_text(
            json.dumps(items, ensure_ascii=False, indent=2) + "\n")
        print(len(items), "sources")
    for key in args.keys:
        fetch(key.lower(), items[key.lower()], args.fulltext)


if __name__ == "__main__":
    main()
