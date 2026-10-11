# Meditação (título de trabalho)

Não ficção sobre meditação, budismo, neurociência e neuroplasticidade, para
quem parte do zero. Manuscrito em Markdown; EPUB pronto para a KDP e PDF pronto
para impressão do outro lado. Mesma cadeia de ferramentas dos livros
anteriores de Íris Gradim.

    make deps                  # uma vez, no macOS
    make                       # constrói o livro
    make check                 # preflight contra o que a KDP recusa
    make marcadores            # o que ainda está em aberto
    make release               # constrói e confere tudo (pt + en)
    make traducao              # capítulos em inglês atrás do original

| Livro | `BOOK=` | Edição em inglês | `BOOK=` |
|---|---|---|---|
| *a decidir* | `livro-1` | *to be decided* | `book-1` |

## Layout

    books/<slug>/
      book.yaml              metadados, formato, anúncio na KDP
      front/                 o que vier antes             (fólios romanos)
      chapters/              o livro                      (fólios arábicos)
      parts/                 aberturas das 3 partes
      back/                  o que vier depois
      illustrations/masters/ originais em alta, um por parte
    docs/
      series.md              o que é comum às duas edições
      translation-en.md      as regras da edição em inglês
      kdp-upload.md          o passo a passo do upload
      livro-1/
        outline.md           a tese, as partes, fonte única dos capítulos
        references.md        o que é real, e onde foi conferido
        translation-en.md    títulos, glossário e frases fixas em inglês
    sources/                 obras para conferência (só os registros .md vão ao git)
    shared/                  template de impressão, capa, CSS do EPUB, fontes
    scripts/                 build, gates, digest, stats, scaffolders
