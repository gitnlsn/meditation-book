# sources/

Source texts, for verification.

**The works are not committed; the records are.** `.gitignore` keeps every file
here out of the repo *except* `.md` files, because a record is `.md` and a work
never is. So the PDFs, papers and full texts stay local — they are
copyrighted, or simply large — while `VERIFIED.md` and any `verificacao-*.md`
records travel with the repo. Those records are the book's citation audit
trail: without them, every check would have to be redone from scratch.

A fresh clone therefore has no works in it. When a work is obtained, record
where it came from (a direct link, or "comprado", or "biblioteca") so it can be
fetched again.

## Naming

    surname-year-short-title-lang.ext

- **surname** — the first author's family name, lowercase, no accents.
- **year** — the year of *this file's* edition. Where it differs from the
  original, `VERIFIED.md` records both.
- **short-title** — three or four words, no articles.
- **lang** — the two-letter language of the file, always present. This book
  quotes across Portuguese, English and translations from Pali and Sanskrit,
  and the language of the file decides whether a quotation needs translating.

One file per work. No derived `.txt` extracts: regenerate them with
`pdftotext` when needed.

## Why this exists

Claude has detailed knowledge *about* these works but does not have the works.
That distinction decides what can be written:

| What Claude can do without the file | What requires the file |
|---|---|
| The shape of an argument, and who made it | Any direct quotation, in any language |
| That a finding exists and roughly what it shows | Effect sizes, sample sizes, p-values, percentages |
| What a tradition teaches, in outline | The wording of a sutta or sutra, and whose translation it is |
| That a study or edition exists | Its year, journal, authors, pagination |

Anything in the right column that has no file gets a `[[?fato: …]]` or
`[[?citação: …]]` marker in the draft, and `make marcadores` refuses to let
that chapter reach `revised` or `final`. A fabricated quotation or a misremembered
effect size is unfixable once the book is printed.

**Try to obtain the source before marking anything.** Open-access papers (PMC,
journal open access, preprints) and public-domain translations can be
downloaded straight into this directory and checked.
