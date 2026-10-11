#!/usr/bin/env python3
"""A compact map of the whole book, for reading one chapter against the rest.

    scripts/digest.py <book-slug>              the map, plus the reports
    scripts/digest.py <book-slug> --termos     where every term is first defined
    scripts/digest.py <book-slug> --evidencia  evidence strength and evidence boxes
    scripts/digest.py <book-slug> --capitulo 09

Reviewing a chapter means holding the rest of the book in mind: which terms the
reader already has, which claims were already made and how strongly, which
chapter this one leans on. The front matter already carries that brief --
question, premise, terms, evidence, caveats, practice, sources -- for every
chapter, so the map is generated from it rather than written by hand, and
cannot drift out of date the way a hand-kept summary would.

Read the map first, then the target chapter in full.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
MARKER = re.compile(r"\[\[\?(.+?)\]\]", re.S)
XREF = re.compile(r"\{\{cap:([a-z0-9-]+)\}\}")
RELATORIO = re.compile(r"^::: *\{\.relatorio\}", re.M)
# The four evidence labels CLAUDE.md asks for, in Portuguese and English.
STRENGTHS = {
    "forte": "forte", "strong": "forte",
    "moderada": "moderada", "moderate": "moderada",
    "preliminar": "preliminar", "preliminary": "preliminar",
    "contestada": "contestada", "contested": "contestada",
}


def one_line(value, width: int = 96) -> str:
    """Front matter wraps across lines; a map is only readable one line deep."""
    if isinstance(value, list):
        value = ", ".join(str(v) for v in value)
    text = " ".join(str(value or "").split())
    return text if len(text) <= width else text[: width - 1] + "…"


def words(body: str) -> int:
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    body = re.sub(r"[#>*_`\[\]()]", " ", body)
    return len(body.split())


class Chapter:
    def __init__(self, path: Path, order: int) -> None:
        text = path.read_text(encoding="utf-8")
        m = FM.match(text)
        self.path = path
        self.order = order
        self.slug = re.sub(r"^\d+-", "", path.stem)
        self.num = path.stem.split("-")[0]
        self.meta = (yaml.safe_load(m.group(1)) if m else {}) or {}
        body = FM.sub("", text)
        self.words = words(body)
        self.refs = [s for s in XREF.findall(body) if s != self.slug]
        self.markers = MARKER.findall(body)
        self.relatorios = len(RELATORIO.findall(body))
        self.incoming: list[str] = []

    def get(self, key: str) -> str:
        return one_line(self.meta.get(key))

    def list_of(self, key: str) -> list[str]:
        value = self.meta.get(key) or []
        if isinstance(value, str):
            value = [v.strip() for v in value.split(",") if v.strip()]
        return [str(v) for v in value]

    @property
    def title(self) -> str:
        return str(self.meta.get("title") or self.slug)

    @property
    def part(self) -> str:
        return str(self.meta.get("part") or "?")

    @property
    def status(self) -> str:
        return str(self.meta.get("status") or "outline")

    @property
    def strengths(self) -> list[str]:
        text = str(self.meta.get("evidence") or "").lower()
        return sorted({v for k, v in STRENGTHS.items() if k in text})


def load(book: Path) -> list[Chapter]:
    chapters = [Chapter(p, i) for i, p
                in enumerate(sorted((book / "chapters").glob("*.md")))]
    by_slug = {c.slug: c for c in chapters}
    for c in chapters:
        for target in c.refs:
            if target in by_slug:
                by_slug[target].incoming.append(c.num)
    return chapters


def print_map(chapters: list[Chapter]) -> None:
    part = None
    for c in chapters:
        if c.part != part:
            part = c.part
            print(f"\n{part}")
        flags = []
        if c.relatorios:
            flags.append(f"relatório×{c.relatorios}")
        if c.markers:
            flags.append(f"marcadores×{len(c.markers)}")
        tail = f"  [{', '.join(flags)}]" if flags else ""
        print(f"\n  {c.num} {c.title}   ({c.status}, {c.words} palavras){tail}")
        print(f"      pergunta.: {c.get('question')}")
        print(f"      ideia....: {c.get('premise')}")
        print(f"      termos...: {c.get('terms') or '—'}")
        print(f"      evidência: {c.get('evidence') or '—'}")
        print(f"      ressalvas: {c.get('caveats') or '—'}")
        print(f"      prática..: {c.get('practice') or '—'}")
        print(f"      remete a.: {', '.join(c.refs) if c.refs else '—'}")
        print(f"      citado em: {', '.join(c.incoming) if c.incoming else '—'}")


def print_termos(chapters: list[Chapter]) -> None:
    """Where each term is defined.

    The reader starts from zero, so a term must be defined the first time it
    is used, and only once. A term declared in two chapters is either defined
    twice (cut one) or declared in the wrong one (fix the outline). A term
    used in a chapter before the one that declares it is the failure this
    report cannot see -- that takes reading.
    """
    print("\n\ntermos, onde cada um é definido")
    where: dict[str, list[Chapter]] = defaultdict(list)
    for c in chapters:
        for term in c.list_of("terms"):
            where[term.lower()].append(c)
    if not where:
        print("  nenhum capítulo declara `terms:` ainda.")
        return
    for term, group in sorted(where.items(), key=lambda x: (x[1][0].order, x[0])):
        caps = ", ".join(g.num for g in group)
        warn = "   definido mais de uma vez" if len(group) > 1 else ""
        print(f"  {term:<32} {caps}{warn}")


def print_evidencia(chapters: list[Chapter]) -> None:
    print("\n\nevidência")
    for c in chapters:
        labels = ", ".join(c.strengths) or "—— sem rótulo de força"
        print(f"  {c.num} {c.title[:40]:<42} {labels}")
    unlabelled = [c for c in chapters if c.meta.get("evidence") and not c.strengths]
    if unlabelled:
        print("\n  `evidence:` sem forte/moderada/preliminar/contestada "
              "(CLAUDE.md pede o rótulo):")
        for c in unlabelled:
            print(f"      {c.num} {c.title}")
    used = sum(1 for c in chapters if c.relatorios)
    print(f"\n  relatórios: {used} de {len(chapters)} capítulos")


def print_chapter(chapters: list[Chapter], key: str) -> None:
    key = key.lower()
    matches = [c for c in chapters if c.num == key.zfill(2) or key in c.slug]
    if not matches:
        sys.exit(f"!! nenhum capítulo casa com {key!r}")
    for c in matches:
        print_map([c])
        print("\n  vizinhos de leitura:")
        for s in chapters[max(0, c.order - 2):c.order + 3]:
            if s is c:
                continue
            print(f"      {s.num} {s.title}")
            print(f"          {s.get('premise')}")
        known = [t for s in chapters[:c.order] for t in s.list_of("terms")]
        print(f"\n  termos que o leitor já tem: {', '.join(known) if known else '—'}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    book = ROOT / "books" / args[0]
    if not book.is_dir():
        sys.exit(f"!! no such book: {args[0]}")
    chapters = load(book)
    if not chapters:
        print("nenhum capítulo ainda.")
        return

    if "--capitulo" in args:
        print_chapter(chapters, args[args.index("--capitulo") + 1])
    elif "--termos" in args:
        print_termos(chapters)
    elif "--evidencia" in args:
        print_evidencia(chapters)
    else:
        print_map(chapters)
        print_termos(chapters)
        print_evidencia(chapters)


if __name__ == "__main__":
    main()
