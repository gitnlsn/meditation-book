# Translation contract — the English edition

The English edition of this book. Carried over from the earlier books: **US
English**; the pen name **Íris Gradim**, pronoun **she**. The title is open:

| Portuguese | English | Slug |
|---|---|---|
| [[?autor: título]] | [[?autor: English title]] | `book-1` (provisório) |

The English edition is a **separate book** in `books/<english-slug>/`, not a
variant. **The Portuguese manuscript stays canon.** The outline and references
describe the book and are not translated. When the English and the Portuguese
disagree about what the book claims, the Portuguese wins. When they disagree
about how to *say* it in English, the book's own
`docs/<source-slug>/translation-en.md` wins, then this file.

Every rule in `CLAUDE.md` binds the translation exactly as it binds the
Portuguese: the voice, the evidence labels, the caveats, the health warnings.
A translation that is fluent and drops a caveat is a worse book.

## How a chapter is translated

- **Same filename as the source.** `books/<english-slug>/chapters/` mirrors the
  Portuguese `chapters/` file for file.
- **Front matter** comes from `scripts/translation-header.py`:

      python3 scripts/translation-header.py <english-slug> \
          books/<source-slug>/chapters/<file>.md "<English title>" > books/<english-slug>/chapters/<file>.md

  It copies the source front matter **verbatim, in Portuguese** (`question`,
  `premise`, `terms`, `evidence`, `caveats`, `practice`, `sources`), so `make
  digest` works on the English book; it replaces `title:` and `part:`, and adds
  `source:`, `source_sha:` and `status: draft`. Then append the English body.
- **`make traducao`** lists every English chapter whose Portuguese source body
  changed since it was translated. Re-translate the changed passage, then
  `python3 scripts/check-translation.py <english-slug> --stamp <file>`.
- **Front, back and part files** carry `source:` too (no hash needed).
- **Translate the chapter, not the sentence.** Keep the register: clear,
  direct, explanatory. Keep the section heads, lists and tables where they are.
- **Nothing added, nothing softened.** No new claim, no new example, no new
  source. An evidence label (*forte* → **strong**, *moderada* → **moderate**,
  *preliminar* → **preliminary**, *contestada* → **contested**) is translated
  exactly, never upgraded or downgraded.
- **Recurring sentences are fixed.** A sentence the book returns to must be the
  same English every time. The book's contract lists them; when you meet a new
  one, add it there before using it.

## Terms and quotations

- **Pali and Sanskrit terms** keep the spelling and diacritics the Portuguese
  uses. The plain-language gloss is translated.
- **Scientific terms** take the standard English form (*default mode network*,
  not a back-translation of *rede de modo padrão*).
- **A quotation whose original is English** is quoted from the original,
  checked against `sources/`, never back-translated from the Portuguese.
- **A quotation from a Pali, Sanskrit, Chinese, Japanese or Tibetan source**
  uses the same published translation the Portuguese relied on, if one exists
  in English; otherwise the translator's note says whose rendering it is.
- **Titles of works** cited by name keep the published English title.

## Form and typography

- **Italics stay italics; bold stays bold.**
- **`##` heads, lists, tables and every `::: {.relatorio}` block stay where they
  are.** `{{cap:slug}}` cross-references are copied unchanged.
- **Numbers.** Decimals take a point: `2,9` → `2.9`. Metric stays metric.
  Percentages, sample sizes and effect sizes are copied, never rounded.
- **Brazilian context** (the SUS, a Brazilian study, a price in reais) stays
  Brazilian. Do not swap in a US equivalent.

## Front and back matter

- *Antes de começar* → **Before You Begin**; *Sobre a autora* → **About the
  Author**. Translate them closely. "About the Author" keeps *She works under
  human direction*, and **never** mentions the person who directed the book.
- Earlier book titles: *Quarenta dias úteis* → *Forty Working Days*; any other
  takes the title of its own English edition.
- **`book.yaml`:** translate `kdp.description`; replace `keywords` with seven
  English ones and `categories` with English BISAC-style paths. Everything else
  is set.

## What the translator does not do

- **Never edit the Portuguese.** A translation finds things: a claim without a
  label, a number that disagrees with references.md, a sentence that only
  works in Portuguese. List them in the book's contract under *Found in the
  Portuguese*, and leave the Portuguese for the author.
- **Never translate the docs** (outline, references).
