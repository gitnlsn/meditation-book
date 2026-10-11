# Plano — Livro 1

Não ficção sobre meditação, budismo, neurociência e neuroplasticidade, para um
leitor que parte do zero e quer entender **por que** as práticas fazem bem à
saúde e à vida. Título de trabalho: `livro-1`.

Este arquivo é a **fonte única** dos títulos e da numeração dos capítulos:
`make outline` cria ou atualiza os arquivos em `books/livro-1/chapters/`, sem
nunca tocar no corpo já escrito.

**Não rodar `make outline` enquanto as vagas tiverem títulos provisórios** — o
scaffolder cria um arquivo por vaga.

---

## A tese — a decidir

[[?autor: a tese do livro, em duas frases]]

## A decidir pelo autor

- [[?autor: título e subtítulo]]
- [[?autor: tamanho — número de capítulos e palavras por capítulo]]
- [[?autor: quantas práticas guiadas, e em que parte]]

---

## Formato de cada capítulo

Copiar o bloco abaixo por capítulo. `make outline` lê:

- `## PARTE <numeral> — <TÍTULO>` abre uma parte. O texto depois de `PARTE`
  tem de ser **idêntico** ao `part:` do arquivo em `books/livro-1/parts/`.
- `### <n>. <Título>` abre um capítulo. O número dá a ordem e o nome do arquivo.
- `*(English Title)*`, na linha seguinte, vira `title_en:` (opcional).
- `- **Campo** — valor`, com travessão (ou hífen), vira um campo do front
  matter. Só os campos abaixo são lidos; qualquer outro é ignorado.
  `Termos` é uma lista separada por vírgula.

      ### 1. Título do capítulo
      *(Chapter Title)*
      - **A pergunta** — a dúvida do leitor que este capítulo responde
      - **A ideia** — a resposta, em uma frase
      - **Termos** — termo-um, termo-dois (definidos aqui pela primeira vez)
      - **Evidência** — em que se apoia, e a força: forte / moderada / preliminar / contestada
      - **Ressalvas** — o exagero, o limite ou o risco que o capítulo tem de nomear
      - **A prática** — a prática ensinada, se houver
      - **Fontes** — duas a quatro entradas de references.md

---

## PARTE I — O QUE O BUDISMO DIZ

[[?autor: o que esta parte estabelece]]

### 1. Parte I, capítulo 1 — título a decidir
- **A ideia** — [[?autor]]

## PARTE II — COMO O CÉREBRO MUDA

[[?autor: o que esta parte estabelece]]

### 2. Parte II, capítulo 1 — título a decidir
- **A ideia** — [[?autor]]

## PARTE III — A PRÁTICA

[[?autor: o que esta parte estabelece]]

### 3. Parte III, capítulo 1 — título a decidir
- **A ideia** — [[?autor]]
