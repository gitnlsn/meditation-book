# Plano — A mente treinável

Não ficção sobre meditação, budismo, neurociência e neuroplasticidade, para um
leitor que parte do zero e quer entender **por que** as práticas fazem bem à
saúde e à vida. Título de trabalho: `a-mente-treinavel`.

Este arquivo é a **fonte única** dos títulos e da numeração dos capítulos:
`make outline` cria ou atualiza os arquivos em `books/a-mente-treinavel/chapters/`, sem
nunca tocar no corpo já escrito.

**Não rodar `make outline` enquanto as vagas tiverem títulos provisórios** — o
scaffolder cria um arquivo por vaga.

---

## A tese

A meditação é treino de atenção e da relação com a própria experiência. O
budismo descreveu esse treino há 2.500 anos com notável precisão; a
neurociência começou a medir parte dele há uns 25. Onde os dois concordam, a
evidência basta para justificar a prática. Onde não concordam, ou onde a
ciência é fraca, o livro diz isso no corpo do texto.

**A distinção que nunca se embaça:** o que os textos budistas *afirmam*, o que
praticantes *relatam* e o que experimentos *mostram* são três coisas
diferentes, e cada afirmação do livro diz em qual das três está.

## Decisões (2026-10-11)

- **Leitor:** o próprio autor, no nível zero — nunca leu um sutta, nunca
  meditou com método, não sabe o que é córtex pré-frontal. Quer o *porquê*.
- **Voz:** a de uma boa explicação de IA — direta, estruturada, sem enchimento.
- **Estrutura:** fundamentos antes da prática. Parte I, o que o budismo diz;
  Parte II, como saber se algo funciona e como o cérebro e o corpo mudam;
  Parte III, uma prática por capítulo, cada uma com o que a tradição diz e o
  que a ciência diz.
- **Tamanho:** dezesseis capítulos de ~2.500 palavras, ~40 mil no total.
- **Escopo:** moderadamente amplo — meditação no centro, mais atenção, hábito,
  estresse, sono, emoção e o senso de eu.
- **Idiomas:** português primeiro; edição em inglês traduzida depois.
- **Decidido por mim (proposta):** o "como ler a evidência" (ensaio
  randomizado, controle ativo, meta-análise, inferência reversa) virou o
  primeiro capítulo da Parte II, e não uma abertura solta: o leitor precisa
  dele exatamente antes da ciência, e o "Antes de começar" já explica os
  quatro rótulos de evidência.

## Título (decidido em 2026-10-11)

***A mente treinável*** — Budismo, meditação e o cérebro que muda. Em inglês,
***The Trainable Mind*** — Buddhism, Meditation and the Brain That Changes.
Escolhido pelo autor entre três propostas; as outras eram *A segunda flecha* e
*Sentar e ver*.

---

## Formato de cada capítulo

Copiar o bloco abaixo por capítulo. `make outline` lê:

- `## PARTE <numeral> — <TÍTULO>` abre uma parte. O texto depois de `PARTE`
  tem de ser **idêntico** ao `part:` do arquivo em `books/a-mente-treinavel/parts/`.
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

---

## PARTE I — O QUE O BUDISMO DIZ

Antes de medir qualquer coisa, saber o que a tradição de fato ensina — e
separar isso da versão "científica" que chegou ao Ocidente.

### 1. Quem foi o Buda — e quem ele não foi
*(Who the Buddha Was, and Wasn't)*
- **A pergunta** — o que é o budismo, afinal: religião, filosofia, técnica?
- **A ideia** — o budismo é uma tradição religiosa viva e diversa, e a versão "científica" que chega ao Ocidente é uma leitura moderna e seletiva dela.
- **Termos** — Buda, Dharma, Sangha, Theravāda, Mahāyāna, Vajrayāna, Zen, modernismo budista, sutta
- **Evidência** — histórica e textual; forte quanto ao contexto geral, contestada quanto às datas e à biografia
- **Ressalvas** — não reduzir o budismo a técnica de bem-estar; não vender "o budismo é ciência"
- **Fontes** — Gethin 1998; Rahula 1959; McMahan 2008; Lopez 2008

### 2. As Quatro Nobres Verdades como diagnóstico
*(The Four Noble Truths as a Diagnosis)*
- **A pergunta** — qual é o problema que o budismo diz resolver?
- **A ideia** — o ensinamento central tem a forma de um diagnóstico médico: sintoma, causa, prognóstico e tratamento.
- **Termos** — dukkha, taṇhā, nirodha, magga, Quatro Nobres Verdades, nirvana, segunda flecha
- **Evidência** — textual; forte quanto ao que os textos dizem
- **Ressalvas** — dukkha não é só "sofrimento"; a analogia médica é antiga, mas é analogia
- **A prática** — notar a segunda flecha num incômodo pequeno do dia
- **Fontes** — Dhammacakkappavattana Sutta (SN 56.11); Sallatha Sutta (SN 36.6); Anālayo 2011; Rainville et al. 1997

### 3. Impermanência e não-eu
*(Impermanence and Not-Self)*
- **A pergunta** — o que significa dizer que "não existe eu"?
- **A ideia** — o budismo afirma que não há um eu fixo por trás da experiência; a ciência cognitiva tem razões independentes para desconfiar do mesmo, mas não prova a doutrina.
- **Termos** — anicca, anattā, cinco agregados, modelo de si, construção do eu
- **Evidência** — textual (forte); convergência com ciência cognitiva (preliminar e filosoficamente contestada)
- **Ressalvas** — não dizer que a neurociência "confirmou" o não-eu
- **Fontes** — Anattalakkhaṇa Sutta; Metzinger 2009; Thompson 2020

### 4. O caminho, e onde a meditação entra nele
*(The Path, and Where Meditation Fits)*
- **A pergunta** — meditar é a mesma coisa que ser budista?
- **A ideia** — na tradição, meditação é uma das três partes do treino (ética, concentração, sabedoria), e tirá-la do conjunto muda o que ela é.
- **Termos** — Nobre Caminho Óctuplo, sīla, samādhi, paññā, samatha, vipassanā, sati, mindfulness, satipaṭṭhāna
- **Evidência** — textual; forte quanto aos textos, contestada quanto à tradução de sati como "mindfulness"
- **Ressalvas** — o Kālāma Sutta não é empirismo moderno; o mindfulness clínico é uma adaptação, e diz isso
- **Fontes** — Satipaṭṭhāna Sutta (MN 10); Anālayo 2003; Kālāma Sutta; Sharf 2015

## PARTE II — COMO O CÉREBRO MUDA

Como saber se algo funciona, e o que se sabe — de verdade — sobre o cérebro
e o corpo que mudam com o treino.

### 5. Como saber se algo funciona
*(How to Know Whether Something Works)*
- **A pergunta** — por que tanta gente diz que meditação "comprovadamente" faz bem, e como checar?
- **A ideia** — saber se uma prática funciona exige comparar com algo ativo, sortear quem pratica e somar muitos estudos; quase todo exagero vem de pular uma dessas etapas.
- **Termos** — ensaio randomizado, grupo controle, controle ativo, placebo, meta-análise, tamanho de efeito, viés de publicação, replicação, inferência reversa, fMRI
- **Evidência** — metodológica; forte
- **Ressalvas** — o salmão morto é piada séria, não prova de que fMRI não presta
- **Fontes** — Van Dam et al. 2018; Goldberg et al. 2018; Open Science Collaboration 2015; Poldrack 2006

### 6. Neuroplasticidade sem exagero
*(Neuroplasticity Without the Hype)*
- **A pergunta** — o cérebro adulto realmente muda?
- **A ideia** — muda com o uso, mas menos, mais devagar e de forma mais difícil de medir do que os livros populares dizem.
- **Termos** — neurônio, sinapse, neuroplasticidade, aprendizagem hebbiana, massa cinzenta, neurogênese, hipocampo
- **Evidência** — plasticidade sináptica (forte); mudança estrutural visível em ressonância (moderada, pequena); neurogênese adulta humana (contestada)
- **Ressalvas** — o mito dos 10%; "religar o cérebro em oito semanas"
- **Fontes** — Hebb 1949; Maguire et al. 2000, 2006; Draganski et al. 2004; Sorrells et al. 2018; Boldrini et al. 2018

### 7. A mente que divaga
*(The Wandering Mind)*
- **A pergunta** — por que é tão difícil ficar no presente?
- **A ideia** — a mente passa boa parte do tempo fora do presente, há redes cerebrais associadas a isso, e parte do que a meditação treina é perceber o desvio.
- **Termos** — rede de modo padrão, divagação mental, ruminação, metaconsciência
- **Evidência** — divagação frequente (moderada); "mente que divaga é mente infeliz" (preliminar, correlacional); papel da rede de modo padrão (moderada, com risco de inferência reversa)
- **Ressalvas** — correlação não é causa; a rede de modo padrão também serve para planejar e imaginar
- **Fontes** — Raichle et al. 2001; Killingsworth & Gilbert 2010; Brewer et al. 2011

### 8. Estresse: o alarme que não desliga
*(Stress: the Alarm That Won't Switch Off)*
- **A pergunta** — como um pensamento faz mal ao corpo?
- **A ideia** — o corpo responde a ameaças imaginadas como a reais, e manter o alarme ligado tem custo físico; aqui a segunda flecha encontra a fisiologia.
- **Termos** — resposta ao estresse, eixo HPA, cortisol, carga alostática, interocepção, sistema nervoso autônomo
- **Evidência** — fisiologia do estresse (forte); efeitos da meditação em marcadores biológicos (preliminar)
- **Ressalvas** — teoria polivagal é popular e contestada; telômeros e inflamação são promessas, não resultados
- **Fontes** — Sapolsky 2004; McEwen 1998; Barrett 2017; Grossman 2023

### 9. Atenção, emoção e hábito
*(Attention, Emotion and Habit)*
- **A pergunta** — o que, exatamente, a meditação treina?
- **A ideia** — atenção, regulação emocional e hábito são capacidades treináveis com mecanismos conhecidos — e são elas, não "o cérebro" em geral, o alvo do treino.
- **Termos** — atenção focada, monitoramento aberto, piscar atencional, regulação emocional, hábito, aprendizagem por reforço
- **Evidência** — melhora de atenção com treino (moderada); hábito leva meses, não 21 dias (moderada)
- **Ressalvas** — o mito dos 21 dias; ganhos de atenção nem sempre se transferem para outras tarefas
- **Fontes** — Lutz et al. 2008; Slagter et al. 2007; MacLean et al. 2010; Lally et al. 2010

### 10. O que a ciência da meditação mostra — e o que não mostra
*(What Meditation Science Shows, and What It Doesn't)*
- **A pergunta** — no balanço, meditação faz bem à saúde?
- **A ideia** — há evidência moderada de benefícios reais em ansiedade, depressão recorrente e estresse, de tamanho parecido ao de outros tratamentos ativos; muito do que se diz sobre o cérebro não se sustenta.
- **Termos** — MBSR, MBCT, recaída, não inferioridade
- **Evidência** — ansiedade, depressão, estresse (moderada); prevenção de recaída com MBCT (moderada a forte); mudança estrutural no cérebro (contestada)
- **Ressalvas** — efeitos pequenos a moderados; não supera tratamentos ativos; não substitui tratamento
- **Fontes** — Goyal et al. 2014; Kuyken et al. 2016; Hoge et al. 2023; Galante et al. 2021; Kral et al. 2022

## PARTE III — A PRÁTICA

Uma prática por capítulo: como fazer, o que a tradição diz que ela faz, o que
a ciência diz que ela faz, e onde os dois se separam.

### 11. Atenção na respiração
*(Attention on the Breath)*
- **A pergunta** — como se começa?
- **A ideia** — a prática básica é voltar: notar que a atenção saiu e trazê-la de volta, e cada volta é a repetição que treina.
- **Termos** — ānāpānasati, âncora, postura, contagem
- **Evidência** — melhora de atenção sustentada (moderada); doses curtas (preliminar)
- **Ressalvas** — "esvaziar a mente" não é o objetivo
- **A prática** — dez minutos por dia durante uma semana, contando respirações
- **Fontes** — Ānāpānasati Sutta; MacLean et al. 2010; Jha et al. 2015

### 12. Observar sem agarrar
*(Watching Without Grabbing)*
- **A pergunta** — o que é "atenção plena" na prática?
- **A ideia** — no sentido de satipaṭṭhāna, é observar sensações, emoções e pensamentos como eventos que passam, sem seguir nem empurrar.
- **Termos** — rotulagem, equanimidade, as quatro bases da atenção
- **Evidência** — rotular emoções reduz reatividade (preliminar); monitoramento aberto e atenção focada diferem (moderada)
- **Ressalvas** — observar não é suprimir; quem tem trauma pode precisar de outra porta de entrada
- **A prática** — rotular por dez minutos ("pensando", "ouvindo", "planejando")
- **Fontes** — Satipaṭṭhāna Sutta; Anālayo 2003; Lutz et al. 2008

### 13. Bondade e compaixão como treino
*(Kindness and Compassion as Training)*
- **A pergunta** — dá para treinar ser mais gentil?
- **A ideia** — mettā e karuṇā são treináveis, e empatia sem compaixão desgasta; a ciência que separa as duas é uma das mais interessantes da área.
- **Termos** — mettā, karuṇā, muditā, upekkhā, brahmavihāras, empatia, compaixão, fadiga por empatia
- **Evidência** — aumento de afeto positivo (moderada); empatia × compaixão (preliminar, poucos laboratórios)
- **Ressalvas** — efeitos no comportamento real são menores que nos questionários
- **A prática** — mettā em quatro círculos
- **Fontes** — Karaṇīya Mettā Sutta; Fredrickson et al. 2008; Klimecki et al. 2014; Singer & Engert 2019

### 14. O corpo, o sono e a dor
*(Body, Sleep and Pain)*
- **A pergunta** — meditação ajuda a dormir e a sentir menos dor?
- **A ideia** — práticas centradas no corpo têm evidência própria em sono e dor, e entender o mecanismo muda a relação com o desconforto.
- **Termos** — escaneamento corporal, insônia, dor crônica, modulação da dor
- **Evidência** — sono (moderada); dor crônica (moderada, efeitos pequenos)
- **Ressalvas** — não substitui tratamento para insônia (TCC-I) nem para dor
- **A prática** — escaneamento corporal antes de dormir
- **Fontes** — Kabat-Zinn 1990; Black et al. 2015; Rusch et al. 2019; Zeidan et al. 2015

### 15. Quando a meditação dá errado
*(When Meditation Goes Wrong)*
- **A pergunta** — meditação pode fazer mal?
- **A ideia** — sim: há efeitos adversos documentados, e saber reconhecê-los faz parte de praticar com segurança.
- **Termos** — efeito adverso, despersonalização, retiro intensivo
- **Evidência** — existência de efeitos adversos (moderada); frequência (preliminar, varia muito entre estudos)
- **Ressalvas** — não alarmar nem minimizar; quando parar e quando procurar ajuda
- **Fontes** — Lindahl et al. 2017; Farias et al. 2020; Britton et al. 2021

### 16. Uma prática para a vida
*(A Practice for a Life)*
- **A pergunta** — como transformar isso em algo que dure?
- **A ideia** — o que sustenta uma prática por anos não é motivação, é estrutura: horário, comunidade, orientação e uma razão que você entende.
- **Termos** — sangha (na prática), retiro, professor
- **Evidência** — formação de hábito (moderada); efeitos de longo prazo em praticantes (preliminar, viés de seleção)
- **Ressalvas** — praticantes de longa data se autosselecionam
- **A prática** — montar o próprio plano de oito semanas
- **Fontes** — Wood 2019; Lally et al. 2010; Goleman & Davidson 2017
