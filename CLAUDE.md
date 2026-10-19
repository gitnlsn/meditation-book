# CLAUDE.md

Production repo for a **nonfiction book** by Íris Gradim about meditation,
Buddhism, neuroscience and neuroplasticity, for a reader starting from zero who
wants to understand **why** the practices benefit health and life. The book
lives in `books/a-mente-treinavel/`, its planning docs in `docs/a-mente-treinavel/`. The Markdown
manuscript builds to a KDP-ready EPUB and a print-ready PDF, with the same
toolchain as *Quarenta dias úteis*, *Manual da Vida*, *What Remains* and the
series in `../new-series`.

The title is ***A mente treinável*** (`a-mente-treinavel`), chosen by the author on
2026-10-11; the English edition is ***The Trainable Mind*** (`the-trainable-mind`).
If the book is ever retitled, rename `books/<slug>/`, `docs/<slug>/`,
`slug:` in its `book.yaml`, the `source:` paths in the English edition, and
`BOOK ?=`, `SERIES` and `TRANSLATIONS` in the Makefile. Do it all at once.

## How the author works

- Open questions are settled as **multiple-choice with a recommended option**.
- Once the plan (`docs/a-mente-treinavel/outline.md`) and a sample chapter are approved,
  **the whole book is drafted in one go** for a single review pass.
- When the author delegates a decision, take it, record the reasoning in the
  outline, and say what was decided.

## Voice — the author's standing instructions

These are the author's own and **outrank any default** about how a book should
sound.

**The reader is the author: a beginner.** Assume zero background in Buddhism,
neuroscience, statistics or meditation. Define every term the first time it is
used, in plain words, and only once (`terms:` in front matter; `make digest
--termos` shows where each one is defined). Pali and Sanskrit terms come with
their plain meaning: *dukkha* (insatisfação, o desconforto de fundo da vida),
not *dukkha* alone.

**The voice is AI-native.** The author dislikes how typical human authors write
and likes how AI writes. Write the way a very good explanation in a
conversation sounds: clear, structured, direct, explanatory.

- **Lead with the point.** The first paragraph of a chapter says what the
  chapter will establish. No slow scene-setting openings, no anecdote before
  the idea.
- **No padding.** No anecdote that does not carry an argument. No "imagine
  que…" warm-ups.
- **No guru tone, no motivational-poster lines, no exclamation marks.** No
  promises of transformation. The book explains; it does not exhort.
- **Structure is welcome.** `##` section heads, short paragraphs, and lists or
  tables when they clarify (a comparison, a sequence of steps, what a study
  did). Not when prose would do.
- **Each chapter ends with a short summary** of what it established (a `##`
  head, a few lines or a short list). Not a teaser for the next chapter.

**Plain language** (the author's rule, 2026-10-19). The evidence must be
easy to follow for a beginner, without becoming less true.

- **Verdict first.** Each evidence section opens with the plain answer and
  its label; the studies come after, as the explanation. The same holds for
  paragraphs: the point, then who found it.
- **One or two studies tell the story.** Not a study-by-study tour. The others
  go to the chapter's list in Fontes.
- **Names only when they matter.** Describe a study by what it did ("um
  ensaio de 18 meses com idosos"). A researcher's name stays for a famous
  study or one the book returns to. No journals or universities in the prose.
- **One number per finding, in everyday terms** ("cerca de 1 em cada 10",
  "a vantagem caiu pela metade"). Effect sizes, sample sizes and p-values
  live in the `relatorio` boxes.
- **One new idea per paragraph.** A technical term only if the book uses it
  again; otherwise, a plain description.
- **Caveats in plain words**, and only those that change how far to trust the
  claim ("um único ensaio, feito pelos criadores do método"). The `[care]`
  caveat rule still applies.
- **Short sentences**, about 25 words or fewer; lists where the text
  enumerates.
- **Diagrams are welcome** where a comparison, a sequence or a mechanism is
  easier to see than to read (SVG in `illustrations/figures/`, one per
  language).

## Truth is non-negotiable

- **Every empirical claim** is traceable to a real source recorded in
  `docs/a-mente-treinavel/references.md`, or it is marked `[[?fato: …]]` in the prose.
  `make marcadores` will not let that chapter reach `revised` or `final` while
  the marker stands.
- **Quotations and exact figures** (effect sizes, sample sizes, percentages,
  the wording of a sutta) only after checking against a primary source in
  `sources/` and recording it in `sources/VERIFIED.md`. Otherwise
  `[[?citação: …]]` or `[[?fato: …]]`. Never reconstruct a number or a
  quotation from memory.
- **Label the strength of the evidence** for every finding the book leans on:
  **forte**, **moderada**, **preliminar** or **contestada**. The same label goes
  in the chapter's `evidence:` field.
- **Name the hype where it exists.** Meditation and neuroplasticity research is
  full of small samples, weak controls, failed replications, publication bias,
  and reverse inference from brain scans ("a região X acendeu, então a pessoa
  sentiu Y"). Say so in the body of the text, at the point where the claim is
  made, not in a footnote.
- **Never cite a `[care]` work without its caveat**, in the same paragraph.
- **Keep three things apart**, and say which one a sentence is: what Buddhist
  texts claim, what practitioners report, and what experiments show. A claim
  can be true in one register and unsupported in another.
- **Buddhism is a living, diverse tradition**, presented accurately and with
  respect: Theravada, Mahayana, Vajrayana, Zen, and their disagreements. Never
  flattened into a wellness technique, never reduced to "basically
  neuroscience". When a practice is lifted out of its tradition (mindfulness
  in MBSR, for example), say so.

## Health safety

- **Meditation is not a substitute for treatment.** Where a chapter touches
  depression, anxiety, trauma, pain or any diagnosis, it says so.
- **Adverse effects are real and documented** (e.g. the work of Willoughby
  Britton and Jared Lindahl on difficult meditation experiences). Mention them
  wherever the book recommends a practice, especially intensive or retreat
  practice, with sources from references.md.

## Evidence boxes — `::: {.relatorio}`

Where the book stops explaining and states what a specific study did and found,
it can set that apart:

    ::: {.relatorio}
    **O estudo.** Quem, quando, quantas pessoas, que controle.

    **O que encontrou.** O resultado, com o número conferido.

    **Força da evidência:** preliminar. Por quê.
    :::

It prints with hairline rules and a sans face, in the EPUB and in print. Use it
for evidence that deserves to be inspected, not for every citation.
`make digest --evidencia` and `make stats` count them.

## Cross-references

**Never write a chapter number into this file, into a skill, or into prose.**
Refer to chapters by title here, and by `{{cap:slug}}` in the manuscript, where
`slug` is the chapter filename without its number (`03-o-que-e-dukkha.md` →
`{{cap:o-que-e-dukkha}}`). The build resolves it to the printed number and
fails on an unknown slug.

## Front and back matter

- **Antes de começar** (front) says plainly that Íris Gradim is an AI and
  describes the human's role in choosing and directing the book, following the
  pattern of *Quarenta dias úteis*. It also says how to read the evidence labels
  and that the book is not a substitute for treatment.
- **Sobre a autora** (back) keeps "Trabalha sob direção humana." and **three
  debts**, all to real works or real research the book draws on. It **never
  mentions or credits the person who directed the book**.

## Language: the English edition

Portuguese (pt-BR) is the primary edition. Printed labels come from `labels:`
in `book.yaml`. The **English edition is a separate book** (US English),
`books/the-trainable-mind/`.

- **The Portuguese is canon.** Docs are never translated. Each English chapter
  has the same filename as its source, Portuguese planning notes in its front
  matter, and `source:` + `source_sha:`. **`make traducao`** lists English
  chapters whose source changed, and `make release` stops on a stale one.
- Rules: `docs/translation-en.md` (general) and `docs/a-mente-treinavel/translation-en.md`
  (titles, glossary, fixed sentences, *Found in the Portuguese*).
- Start a chapter with `scripts/translation-header.py`. **Revise the Portuguese
  first, then carry the change into the English** and restamp:
  `python3 scripts/check-translation.py the-trainable-mind --stamp <file>`.
- The English book shares the Portuguese art through an `illustrations` symlink.

## Structure and conventions

- `docs/a-mente-treinavel/outline.md` is the single source for chapter titles and
  numbering. `make outline` creates missing chapter files and refreshes
  planning notes; it never touches a written body. **Don't run it while the
  slots still carry placeholder titles**, because it would create one file per
  placeholder. The chapter block format is documented in the outline itself.
- `docs/a-mente-treinavel/references.md` is what is real, with `[core]` / `[care]`.
- Planning notes (`question`, `premise`, `terms`, `evidence`, `caveats`,
  `practice`, `sources`, `status`) live in chapter front matter; the build
  strips them. `status:` goes `outline` → `draft` → `revised` → `final`, by hand.
- Part openers live in `books/a-mente-treinavel/parts/`. Their `part:` string must match
  the `## PARTE …` heading in the outline exactly (`I — O QUE O BUDISMO DIZ`).
  Rename both together. The part titles are provisional.
- Chapter bodies: `##` for section heads, never an `#` heading. Markdown lists
  and tables are fine.
- Illustrations: one master per part opener in `illustrations/masters/`,
  matched by the part's `illustration:` field (a placeholder is generated
  until the art exists). In-text diagrams are grayscale SVG line art in
  `illustrations/figures/`, `fig-<name>-pt.svg` and `fig-<name>-en.svg`,
  referenced from the chapter with a caption; the build rasterizes them. Any
  note belongs in the caption, not inside the drawing.
- Covers are typographic, from `shared/print/cover.typ`, with a palette under
  `cover:` in `book.yaml` (`bg`, `ink`, `accent`, hex). The current palette is a
  neutral placeholder.
- `dist/` is never committed. Research material goes in `sources/` (untracked);
  only `.md` records of it are committed (`sources/README.md`).

## Commands

Every target takes `BOOK=<slug>`; the default is `a-mente-treinavel`.

    make                 # build the book (epub + interior + cover)
    make books           # build both editions
    make release         # build + check both, list the upload files (BOOK=… for one)
    make release-en      # the same, English edition only
    make check           # KDP preflight + the marker gate
    make marcadores      # unresolved [[?...]] markers (the book + docs/<slug>/ + docs/*.md)
    make traducao        # English chapters behind their Portuguese source
    make digest          # whole-book map: question, idea, terms, evidence
    make stats           # word counts, pacing, evidence boxes
    make outline         # docs/<slug>/outline.md -> chapter files
    make watch           # rebuild the print PDF on every save

**`vale` is not a gate** (English linters, Portuguese manuscript; see
`.vale.ini`). Never report it as passing or failing.

## Template gotchas, already solved: do not "fix" them

Inherited from *Quarenta dias úteis*; the comments in
`shared/print/template.typ` explain each:

1. Recto breaks use `pagebreak(to: "odd")`. Do not reintroduce hand-computed
   page parity from `here().page()`.
2. Running heads and blank-page detection query elements; chapter numbers are
   passed as arguments. Do not convert either to `state`.
3. In the EPUB, a part opener's figure comes *after* the `<h1>`.
4. Only the vendored Libertinus faces are guaranteed to embed; KDP rejects a
   PDF with an unembedded font.
