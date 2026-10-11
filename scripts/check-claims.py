#!/usr/bin/env python3
"""Find unresolved markers left in the manuscript.

    scripts/check-claims.py <book-slug>

Markers look like `[[?fato: tamanho da amostra em Lazar et al. 2005]]` and are
written by whoever drafts a chapter whenever something could not be settled at
the time: an empirical claim not yet checked against docs/<livro>/references.md,
a quotation not yet checked against a source in sources/, or a decision that
belongs to the author and not to the draft.

A chapter whose status is `revised` or `final` may not contain any. That is the
gate. In a book about evidence it is the whole point: a claim about what
meditation does to a brain or a body is either traceable to a real source, or
it is visibly marked as not yet traced, and a marked claim cannot reach print.

Kinds, by convention -- the prefix is free text, these are just the ones the
drafts write:

    [[?fato: ...]]       an empirical claim not yet checked against a source
    [[?citação: ...]]    a quotation or translation not yet in sources/VERIFIED.md
    [[?autor: ...]]      a decision only the author can make
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
MARKER = re.compile(r"\[\[\?(.+?)\]\]", re.S)
SEALED = {"revised", "final"}
# `[[?fato: …]]` written in docs/ to *document* the syntax is not an open
# marker, and counting it as one taught everyone to ignore the docs/ line. The
# pattern is deliberately narrow -- a type, a colon, and nothing but an
# ellipsis. A real marker always says what has to be settled.
DOCUMENTATION = re.compile(r"^\w+:\s*(?:…|\.\.\.)$")


def open_markers(text: str) -> list[str]:
    found = [" ".join(m.group(1).split()) for m in MARKER.finditer(text)]
    return [f[:96] for f in found if not DOCUMENTATION.match(f)]


def lint_front_matter(book: Path) -> None:
    """Every front matter must be valid YAML before any other gate runs.

    This exists because the same mistake happened twice: a colon inside an
    unquoted multi-line value -- `premise: a atenção muda o cérebro, mas: só
    um pouco` -- makes the second line parse as a new key, and the file stops
    being readable. build.py then died with a traceback instead of a sentence,
    which is a gate nobody reads. Prose fields are prose: they will keep
    acquiring colons, so the check belongs here rather than in a rule nobody
    remembers.
    """
    broken = []
    for path in sorted(book.rglob("*.md")):
        if m := FM.match(path.read_text(encoding="utf-8")):
            try:
                yaml.safe_load(m.group(1))
            except yaml.YAMLError as exc:
                line = next((l.strip() for l in str(exc).splitlines()
                             if l.strip() and not l.strip().startswith("^")), "")
                broken.append((path, line))
    if not broken:
        return
    for path, line in broken:
        print(f"[FAIL] {path.relative_to(ROOT)}: front matter não é YAML válido")
        print(f"       {line}")
    print("\nQuase sempre é dois-pontos dentro de um valor de prosa. Use um\n"
          "travessão no lugar, ou passe o campo para bloco:\n\n"
          "    premise: >-\n      texto com : dentro, em quantas linhas quiser\n")
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    book = ROOT / "books" / sys.argv[1]
    if not book.is_dir():
        sys.exit(f"!! no such book: {sys.argv[1]}")

    lint_front_matter(book)

    total = blocking = 0
    kinds: Counter[str] = Counter()
    # docs/ is scanned too: the outline and the references carry the author's own
    # open decisions, and those are exactly the ones that get forgotten.
    targets = [(book / f, f) for f in ("front", "parts", "chapters", "back")]
    for folder, _ in targets:
        for path in sorted(folder.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            status = "outline"
            if m := FM.match(text):
                status = (yaml.safe_load(m.group(1)) or {}).get("status", "outline")
                text = text[m.end():]
            found = open_markers(text)
            if not found:
                continue
            for f in found:
                kinds[f.split(":", 1)[0].strip().lower() if ":" in f else "sem tipo"] += 1
            total += len(found)
            sealed = status in SEALED
            blocking += len(found) if sealed else 0
            print(f"\n[{'FAIL' if sealed else 'todo'}] "
                  f"{path.relative_to(ROOT)}  (status: {status})")
            for f in found:
                print(f"       [[?{f}]]")

    open_docs = 0
    # Series-level docs, then this book's own folder -- never another book's,
    # so one book's open decisions do not show up in the next book's report.
    doc_files = sorted((ROOT / "docs").glob("*.md")) + \
        sorted((ROOT / "docs" / sys.argv[1]).glob("*.md"))
    for path in doc_files:
        found = open_markers(path.read_text(encoding="utf-8"))
        if found:
            open_docs += len(found)
            print(f"\n[docs] {path.relative_to(ROOT)}: {len(found)} em aberto")

    if not total and not open_docs:
        print("nenhum marcador em aberto.")
        return
    if kinds:
        print("\npor tipo: " + ", ".join(f"{k} ×{n}" for k, n in kinds.most_common()))
    print(f"\n{total} marcador(es) no manuscrito, {blocking} em capítulos "
          f"marcados {' ou '.join(sorted(SEALED))}"
          + (f"; {open_docs} em docs/" if open_docs else ""))
    if blocking:
        print("\nUm capítulo não pode ser `revised` ou `final` com um marcador\n"
              "em aberto. Resolva o marcador -- conferindo o fato numa fonte\n"
              "registrada em docs/<livro>/references.md, conferindo a citação\n"
              "em sources/VERIFIED.md, ou perguntando ao autor -- ou volte o\n"
              "status para `draft`.")
        sys.exit(1)


if __name__ == "__main__":
    main()
