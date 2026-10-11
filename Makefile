# Book production. `make` on its own builds everything for the default book;
# pass BOOK=<slug> for another one. The books (working slugs, see docs/series.md):
#
#   1  livro-1
#
# Each has an English edition, a separate book translated from it:
#
#   1  book-1
#
#   make BOOK=<slug> all            epub + interior pdf + cover
#   make books                      every book, one after another
#   make release                    build + check the series, list the upload files
#   make release BOOK=<slug>        the same, for one book only
#   make traducao                   English chapters behind their Portuguese source
#   make release-en                 release only the English editions
#   make epub / print / cover       one target at a time
#   make check                      KDP preflight + the marker gate
#   make marcadores                 unresolved [[?...]] markers
#   make watch                      rebuild the print pdf as you write
#   make stats                      word counts, pacing, evidence boxes
#   make digest                     whole-book map: questions, terms, evidence
#   make outline                    docs/$(BOOK)/outline.md -> chapter files
#   make chapter TITLE="..."        add a chapter outside the outline
#   make clean

BOOK  ?= livro-1
BOOKS := $(notdir $(wildcard books/*))
# Series order, for release. Books not listed here are appended.
SERIES := livro-1 book-1
# The English editions. Each chapter names its Portuguese source and its hash.
TRANSLATIONS := book-1
SERIES += $(filter-out $(SERIES),$(BOOKS))
# `make release` does the whole series; `make release BOOK=x` does one book.
RELEASE := $(if $(filter command line environment,$(origin BOOK)),$(BOOK),$(SERIES))
PY   := python3
DIST := dist/$(BOOK)

.DEFAULT_GOAL := all
.PHONY: all books epub print cover check marcadores watch stats digest outline \
        clean new-book chapter open deps release release-en traducao

all:
	@$(PY) scripts/build.py $(BOOK) --all

books:
	@for b in $(BOOKS); do $(PY) scripts/build.py $$b --all || exit 1; done

epub:
	@$(PY) scripts/build.py $(BOOK) --epub

print:
	@$(PY) scripts/build.py $(BOOK) --print

cover:
	@$(PY) scripts/build.py $(BOOK) --cover

check: marcadores
	@$(PY) scripts/check.py $(BOOK)

# Unchecked facts, unverified quotations and open authorial decisions still
# marked in the manuscript. A chapter cannot be `revised` or `final` while one
# stands.
marcadores:
	@$(PY) scripts/check-claims.py $(BOOK)

# Builds and checks every book in RELEASE, stopping at the first failure, then
# lists the files to upload to KDP for each one.
# A stale translation stops the release before anything is built: a release of
# one edition without the other is how they drift apart.
release:
	@for t in $(filter $(TRANSLATIONS),$(RELEASE)); do \
		$(PY) scripts/check-translation.py $$t || exit 1; done
	@for b in $(RELEASE); do \
		echo "\n== $$b =="; \
		$(PY) scripts/build.py $$b --all && \
		$(PY) scripts/check-claims.py $$b && \
		$(PY) scripts/check.py $$b || { echo "\n!! release stopped at $$b"; exit 1; }; \
	done
	@echo "\nReady to upload:"
	@for b in $(RELEASE); do \
		echo "  $$b/"; \
		ls -lh dist/$$b/*.epub dist/$$b/*.pdf 2>/dev/null | awk '{print "    " $$9 "  " $$5}'; \
	done

# Only the English editions.
release-en:
	@$(MAKE) --no-print-directory release RELEASE="$(TRANSLATIONS)"

# Every English chapter whose Portuguese source changed after it was translated.
traducao:
	@for t in $(or $(TRANSLATION),$(TRANSLATIONS)); do \
		echo "== $$t"; $(PY) scripts/check-translation.py $$t || exit 1; done

stats:
	@$(PY) scripts/stats.py $(BOOK)

# The question, idea, terms, evidence and caveats of every chapter, plus where
# each term is first defined. Read this before reviewing a chapter against the
# book.
digest:
	@$(PY) scripts/digest.py $(BOOK)

# docs/$(BOOK)/outline.md is the single source for chapter titles and numbering.
# Never touches a body you have written.
outline:
	@$(PY) scripts/scaffold-outline.py $(BOOK)

# Rebuilds on every save. Needs `brew install fswatch`.
watch:
	@command -v fswatch >/dev/null || { echo "brew install fswatch"; exit 1; }
	@$(PY) scripts/build.py $(BOOK) --print
	@fswatch -o books/$(BOOK) shared | while read _; do \
		$(PY) scripts/build.py $(BOOK) --print; done

open:
	@open $(DIST)/$(BOOK)-interior.pdf

new-book:
	@test -n "$(SLUG)" || { echo "usage: make new-book SLUG=<slug> [TITLE=\"...\"]"; exit 1; }
	@$(PY) scripts/new-book.py "$(SLUG)" $(if $(TITLE),--title "$(TITLE)",)

chapter:
	@test -n "$(TITLE)" || { echo "usage: make chapter TITLE=\"...\" [BOOK=$(BOOK)]"; exit 1; }
	@$(PY) scripts/new-chapter.py $(BOOK) "$(TITLE)"

# Everything the toolchain needs, on macOS.
deps:
	brew install pandoc typst imagemagick qpdf poppler epubcheck fswatch

clean:
	rm -rf dist
