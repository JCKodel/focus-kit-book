# Os documentos

Depois deste capítulo você consegue dizer o que guarda cada um dos sete documentos do projeto, os ADRs e o `AGENTS.md`, e decidir a qual deles um fato novo pertence.
Você também consegue explicar por que um agente que os lê em uma sessão nova constrói o que foi decidido.
E consegue nomear as duas escolhas do kit, o FOCUS e a estratégia de git, as três respostas de cada uma e onde os documentos registram a que você escolher.

## Um lugar por fato

Uma sessão nova só sabe o que está escrito em arquivos ([capítulo 2](02-how-agents-see.md)), e uma decisão escrita em vários lugares fica desatualizada em alguns deles ([capítulo 4](04-birth-of-focus-kit.md)).
Então cada fato do projeto mora em um lugar, e o agente o lê lá.
O focus-kit dá a esses lugares uma forma fixa, no seu arquivo `references/documents.md`: sete documentos numerados, de `docs/00` a `docs/06`; uma pasta de decisões, `docs/adr/`; o arquivo de regras, `AGENTS.md`; e `work/`, que guarda uma página por entrega.
Os números são fixos porque os comandos os citam; o nome depois do número fica na língua da documentação, `00-Product.md` neste livro e `00-Produto.md` em um projeto documentado em português.

Este livro é escrito com o focus-kit, então o repositório dele tem o mesmo conjunto, e os trechos abaixo vêm dele, como estava em um commit.[^book-docs]
No repositório eles estão em inglês; aqui vão traduzidos, cada um avisado antes.
O capítulo 7 escreve o conjunto para a clínica.

## Os sete documentos

O `/brainstorm` e o `/analyze` escrevem os sete documentos; o `/propose` e o `/apply` os leem antes de agir.
Nos arquivos deles, o `/propose` lê o docs/00, o docs/03, o docs/05, o docs/06 e as páginas em `work/`, e o docs/01 para ver onde uma mudança cai; o `/apply` lê o `AGENTS.md`, o docs/01, o docs/04 e o docs/05.

### docs/00, o produto

O docs/00 diz o que o produto é e para quem: o propósito em um parágrafo, o público, como funciona nas palavras do usuário, o que ele não é, os valores contra os quais as decisões são medidas, as perguntas do produto e as decisões em aberto.
Nada pode contradizê-lo sem mudá-lo na mesma entrega.
Você o lê quando uma decisão está em dúvida, e o `/propose` o lê antes de escrever uma página.
Estas são as perguntas do produto do docs/00 deste livro, a lista que toda entrega do livro precisa cumprir; o original está em inglês, e aqui vai traduzido:

```markdown
## Perguntas do produto

Toda decisão precisa responder sim a todas estas:

1. O capítulo abre com o que o leitor consegue fazer depois de lê-lo?
2. Toda frase carrega valor, e nada de que o leitor precisa ficou de fora?
3. Todo artefato é real e todo número é rastreável até uma fonte?
4. O texto seria seguro se o caso privado em que se apoia fosse lido pelo concorrente do dono dele?
5. Um leitor que leu só os capítulos anteriores consegue acompanhá-lo?
6. As duas edições foram atualizadas nesta entrega?
```

Cada pergunta se responde com sim ou não sobre um capítulo, então uma página pode ser conferida contra ela: este capítulo foi lido contra a pergunta 2, frase por frase, antes de ficar pronto.

O docs/00 termina com as decisões em aberto: o que ninguém fecha sozinho, para que um agente nunca as resolva por suposição.
A OD-3 deste livro diz que o autor aprova o texto anonimizado de cada trecho tirado de um caso privado antes de o capítulo ficar pronto.
Um agente que escreve um trecho assim lê essa linha e para para perguntar, quando de outro modo teria julgado a própria anonimização boa o bastante.

### docs/03, o domínio

O docs/03 é uma tabela com os termos do projeto, seguida das entidades e das regras que sempre valem para elas.
A tabela também é o vocabulário: toda página, todo identificador e todo teste usam os termos dela, e um conceito novo entra aqui antes de entrar em qualquer outro lugar.
A tabela deste livro tem uma coluna para o termo em português, já que o livro tem duas edições; este é o cabeçalho e a linha de entrega, a unidade de trabalho que cada página descreve, no original em inglês e aqui traduzidos:

```markdown
| Termo | Português | Identificador | Significado |
|---|---|---|---|
| delivery | entrega | `<slug>` | A menor unidade de trabalho com valor; cabe em uma página. |
```

A linha fixa a palavra, o nome que os arquivos usam para ela e o que ela quer dizer, então uma página que diz "entrega" e um arquivo com o nome de um slug querem dizer a mesma coisa.

### docs/01, a arquitetura, e docs/02, o backend

O docs/01 guarda o desenho em uma frase, a stack com o motivo de cada escolha que tinha alternativa, como o código se organiza, como os dados são acessados, como os erros viajam, os ambientes e o que foi tentado e removido de propósito, para que não seja reconstruído.
O `/apply` o lê para saber onde vai cada peça.
O docs/02 só existe quando um servidor guarda regras que o cliente não pode duplicar: o esquema, as regras de acesso, as funções que o cliente pode chamar; senão, é uma linha.
O docs/02 deste livro é essa linha, que, traduzida do inglês, diz: "Não há nenhum. O livro é estático; nenhum servidor guarda regras."
O docs/01 também registra a resposta à primeira das [duas escolhas](#as-duas-escolhas) do kit, a arquitetura.

### docs/04, as convenções

O docs/04 guarda as línguas da documentação e dos identificadores, a nomenclatura, o estilo e a ferramenta que o garante, onde ficam os testes e o formato da mensagem de commit; a seção 6 mostra uma das regras dele.

### docs/05, o processo

O docs/05 é o modelo de processo do kit, o mesmo em todo projeto, com uma seção preenchida pelo projeto: a §5, "This project" (este projeto), cujos itens são os slots, os fatos deste projeto que os comandos leem.
Estes são dois slots da §5 deste livro, o comando que confere uma entrega e a estratégia de git, no original em inglês e aqui traduzidos:

```markdown
* **Verificação:** `make verify`, que roda o build estrito do site, a
  paridade das edições, a verificação de travessão, as regras de prosa, a
  verificação de links e a varredura de divulgação. Verde antes de qualquer
  coisa ser declarada pronta. Criado por `site-skeleton` (build, paridade,
  travessão); `disclosure-scan`, `prose-rules` e `link-check` acrescentam
  as suas verificações a ele; `commit-hooks` acrescenta as mensagens de
  commit e os hooks à varredura de divulgação.
* **Git:** trunk. O agente prepara; ele nunca faz commit nem merge.
```

Os nomes entre crases depois de "Criado por" são entregas deste livro, linhas da fila dele, e o slot registra qual delas acrescentou cada verificação.
O `/apply` lê o comando de verificação aqui, então o arquivo do comando não guarda nenhum: a regra que veio depois no Ninjobs, de que um comando não guarda nenhum fato do projeto.
O docs/05 também guarda o fluxo da fila ao commit, na §2, e a forma de uma página, na §3; os capítulos 10 e 11 os ensinam.

### docs/06, a fila

O docs/06 lista os marcos, cada um com um parágrafo que diz o que é verdade quando ele fecha, e sob cada um uma linha por entrega, em ordem, com uma marca do seu estado.
O capítulo 9 a ensina.

## As duas escolhas

O kit oferece duas escolhas, na seção Choices de `references/documents.md`, e não impõe nenhuma: a arquitetura e a estratégia de git.

O FOCUS, a arquitetura que o kit oferece, são quatro letras, cada uma com o seu próprio valor.[^book-adr-0016]
Feature-oriented (orientado a funcionalidades): o código se organiza em fatias verticais, uma pasta com tudo de que uma funcionalidade precisa, sem pasta por tecnologia.
Clean (limpo): toda regra de negócio fica longe do I/O, em uma função pura, então é testada com dados na entrada e um valor na saída.
Unidirectional (unidirecional): um evento corre em um só sentido até um novo estado, sem nada voltando, então "o que acontece quando este evento chega?" é um teste só.
Scalable (escalável): toda peça é isolada e testável, então o código se sustenta em qualquer tamanho.
Atrás da tela, que dispara eventos e renderiza o estado que recebe, ficam três peças: o orquestrador transforma um evento em um novo estado, um caso de uso guarda uma regra, e o repositório busca e salva; só o orquestrador tem dependências injetadas, e elas são os repositórios.
Só o repositório faz I/O, então só ele captura uma exceção, uma falha esperada como uma conexão perdida, e a devolve como valor, um Result; um erro, um bug, nunca é capturado (o Dart separa as suas classes `Exception` e `Error` do mesmo jeito).[^dart-error-exception]
O livro chama o princípio de "exceções como valores", onde a área diz "erros como valores", porque um bug nunca é um valor.[^book-adr-0016]
Nada existe por cerimônia: KISS (keep it simple, mantenha simples), YAGNI (you aren't gonna need it, você não vai precisar disso) e DRY (don't repeat yourself, não se repita) decidem quando uma peça se paga, e uma funcionalidade sem regra não tem caso de uso.
O kit dá três respostas: o FOCUS inteiro; só os dois princípios, fatias verticais e exceções como valores, na estrutura que a stack favorecer; ou nenhum, as convenções do próprio projeto.
O docs/01 registra a resposta, e um ADR registra o porquê.
A Parte III ensina o FOCUS.

A estratégia de git é uma estratégia, não uma bala de prata: cada uma das suas três respostas serve a um jeito de trabalhar.
Em todas, a página que o `/propose` escreve e a construção que o `/apply` faz são uma unidade de trabalho, que se desfaz em um passo: um commit no trunk, um merge do branch nas outras; e o agente nunca faz commit nem merge.
O trunk põe tudo no branch principal, uma entrega de cada vez, e é só para uma pessoa trabalhando sozinha: com duas, as entregas delas dividem um branch, e um commit leva o trabalho pela metade da outra.
Um branch por entrega faz o `/propose` criar um branch com o nome do slug e escrever a página nele, e o `/apply` construir nele; a pessoa faz o merge por um pull request, um pedido de merge de um branch que alguém revisa antes, então ele serve ao trabalho sequencial revisado desse jeito.
Uma worktree por entrega dá a cada entrega uma segunda pasta de trabalho no seu próprio branch, criada pelo `/propose`, para que vários agentes construam entregas diferentes ao mesmo tempo sem que um branch mexa no outro.
Antes de rodar duas ao mesmo tempo, você decide quais entregas podem rodar em paralelo e quais mexem nos mesmos arquivos, senão os merges delas entram em conflito.
O slot Git do docs/05 registra a resposta, e um ADR registra o porquê; a deste livro é o trunk, no slot Git acima e no ADR-0010 abaixo.
A Parte IV ensina as três.

## ADRs

Um ADR (registro de decisão de arquitetura) é um arquivo por decisão, `docs/adr/ADR-NNNN-<slug>.md`, com o contexto, a decisão, as consequências e a data.
Um ADR é emendado, nunca reescrito: quando a decisão muda, uma emenda abaixo dele diz o que mudou e quando, e o motivo original fica acima, para que a próxima pessoa que queira mudá-la de novo leia por que ela era assim.
Este é o ADR-0010 deste livro, que escolheu a estratégia de git do slot Git acima, no original em inglês e aqui traduzido:

```markdown
# ADR-0010: trunk

**Data:** 2026-09-24

## Contexto

Uma worktree por entrega deixaria agentes escreverem capítulos em paralelo, mas os arquivos compartilhados (navegação, glossário, fila) entrariam em conflito, e o autor revisa cada entrega sozinho.

## Decisão

Tudo acontece em `main`, uma entrega de cada vez.
O agente prepara e sugere a mensagem; o autor revisa e faz o commit.

## Consequências

O histórico mais simples. A Parte IV ainda ensina branches e worktrees, a partir dos outros casos.
```

O contexto guarda por que a alternativa perdeu (a worktree das [duas escolhas](#as-duas-escolhas)): se o livro ganhar um segundo revisor, uma emenda pode responder a esse motivo em vez de adivinhá-lo.

## AGENTS.md

O capítulo 2 mostrou o começo do arquivo de regras deste livro, até a lista de documentos a ler antes de agir.
Este é o resto dele, no original em inglês e aqui traduzido:

```markdown
## Inegociáveis
- Nada privado entra no repositório: casos privados são só o Caso A e o Caso B, sem nome, lugar, data de reunião, caminho ou detalhe de negócio; a varredura de divulgação está verde (docs/03, ADR-0012).
- O Ninjobs aparece só pelos seus artefatos de processo e números publicados, parafraseados; nunca a sua infraestrutura, credenciais, usuários ou planos comerciais (docs/03).
- Uma mudança em uma edição é uma mudança nas duas, na mesma entrega; o inglês é a fonte (ADR-0004).
- Todo capítulo abre com o que o leitor consegue fazer depois dele e é tão longo quanto provar isso exige: sem enchimento, nada útil cortado, sem meta de tamanho (ADR-0015).
- Todo artefato mostrado é real e todo número cita a sua fonte (docs/04).
- O livro não menciona nenhum dos livros anteriores do autor e não copia texto deles (ADR-0005).
- Uma entrega = uma página em work/<slug>.md: /propose para definir, /apply para construir.
- Nenhum travessão em texto que um usuário lê.
- O agente prepara e sugere a mensagem de commit. Ele nunca faz commit.

## Não reconstruir
- Uma wiki do GitHub, escrita ou espelhada (ADR-0001).
- Exemplos de código em várias linguagens (ADR-0008).
- Um encurtador de links ou servidor de playground para trechos de código; as tags do projeto guiado fazem isso (docs/01).
- A marca `[?]` (ADR-0013).

## Como trabalhar
- Capítulos são `book/<edition>/NN-<slug>.md`, o mesmo nome de arquivo nas duas edições; scripts em `scripts/` (docs/01).
- Toda verificação imprime `file:line: rule: message` e sai com código diferente de zero (docs/01).
- `make verify` antes de declarar qualquer coisa pronta.
- Abstração na segunda ocorrência concreta, e a entrega diz qual foi a primeira.
- Ambiguidade → pergunte. Os documentos são vivos: uma entrega que muda comportamento atualiza o documento que é dono dele, na mesma entrega.
```

A maioria das linhas termina com o documento ou o ADR que guarda a regra inteira: a linha lembra o agente no começo de toda sessão, e o dono guarda o motivo.

As regras do kit para esse arquivo, em `references/documents.md`, são três: sessenta linhas no máximo, tudo nele aponta para um documento, e nada nele é o único lugar onde uma regra está escrita.
Ele é carregado inteiro em toda sessão, então fica curto, e uma regra que morasse só nele não teria o seu motivo escrito em lugar nenhum; o Claude Code o lê também pelo `CLAUDE.md` do capítulo 5.

## Documentos vivos

Quando revisei o capítulo 3, os trechos dele mostravam o cenário de cada ferramenta sem o projeto nem o pedido a que respondiam, e um era uma linha solta que dependia da linha de cima.
Corrigi o capítulo e, no mesmo commit, escrevi a correção no docs/04, as convenções, como duas regras para todo capítulo, "Contexto antes de um trecho" e "Ensinar, não só mostrar".
Esta é a primeira, como o docs/04 a guarda, no original em inglês e aqui traduzida:

```markdown
* **Contexto antes de um trecho.** Um leitor que leu só os capítulos anteriores entende todo artefato mostrado sem abrir mais nada (docs/00, pergunta do produto 5).
  Antes dele, o texto diz do que o artefato trata: o projeto, o problema a que responde, de onde vem.
  Um trecho é uma unidade inteira que tem sentido sozinha (uma história de usuário com os seus cenários, um requisito, uma seção de uma página), nunca uma linha solta que depende das linhas ao redor; quando várias ferramentas são comparadas, cada uma mostra a mesma unidade.
```

A regra nomeia a pergunta do produto a que serve, então o motivo viaja com ela.
O capítulo 5 foi escrito depois desse commit: a página dele pôs a clínica e a tag de partida antes do relatório da instalação, e a entrega acrescentou duas frases apresentando o projeto guiado, citando a regra; ninguém repetiu o pedido.
Cada seção deste capítulo segue a mesma regra.

Isso é um documento vivo: uma entrega que muda comportamento atualiza o documento que é dono dele, na mesma entrega.
A próxima sessão lê a mudança junto com todo o resto e a segue sem que ninguém precise dizer de novo.

Você não precisa editar os documentos à mão, e eu recomendo que não edite.
Converse com o agente: aponte uma lacuna, um detalhe errado, algo a acrescentar, mudar ou tirar, e ele encontra o documento que é dono do fato e escreve a mudança lá, mais rápido e com mais precisão do que você faria à mão, já que os documentos dizem a ele onde mora cada fato.
O seu papel é interpretar, guiar e validar: dizer o que a mudança quer dizer, conduzi-la e lê-la antes do commit.
O texto de um agente parece certo mesmo quando está errado, então você o confere com o que sabe e nunca o aceita por confiança; você é o cérebro da operação, e o agente escreve.

## Pontos-chave

* Cada fato de um projeto mora em um lugar: sete documentos numerados, `docs/adr/`, `AGENTS.md` e `work/`, com números fixos porque os comandos os citam.
* O docs/00 é o produto e as suas decisões em aberto, o docs/03 o vocabulário, o docs/01 e o docs/02 como ele é construído, o docs/04 as convenções, o docs/05 o processo com os slots do projeto, o docs/06 a fila.
* Um ADR registra uma decisão com o seu motivo e é emendado, nunca reescrito, para que o motivo sobreviva à próxima mudança; as duas escolhas do kit, o FOCUS (inteiro, os dois princípios, nenhum) e o git (trunk, um branch ou uma worktree por entrega), ficam registradas no docs/01 e no docs/05, cada uma com o seu ADR.
* O `AGENTS.md` é curto e só aponta: nada nele é o único lugar onde uma regra está escrita, e os comandos não guardam nenhum fato do projeto.
* Uma entrega que muda comportamento atualiza o documento que é dono dele, na mesma entrega, e toda sessão seguinte segue a mudança; o agente a escreve, e você a conduz e a confere, nunca por confiança.

## Exercícios

### Exercício 6.1

No seu clone do projeto guiado, faça checkout de `book-v1/install-and-hosts` e abra `.claude/skills/brainstorm/references/documents.md`, a descrição dos documentos feita pelo próprio kit.
Quais documentos da clínica poderiam dizer "não há nenhum", e o que decidiria isso?

### Exercício 6.2

Escreva à mão o parágrafo de Propósito do docs/00 da clínica e três inegociáveis.
Guarde-os, para comparar com o que o `/brainstorm` escreve no capítulo 7.

### Exercício 6.3

No [`AGENTS.md`](https://github.com/JCKodel/focus-kit-book/blob/6c2713b63af7397ee00142497287b8408a5651b1/AGENTS.md) deste livro, encontre o documento para o qual cada linha aponta, e alguma linha que seja o único lugar onde a sua regra está escrita.

### Exercício 6.4

Escolha uma resposta para cada uma das duas escolhas da clínica, com um motivo para cada.
Guarde-as, para comparar com o briefing da clínica para o `/brainstorm` no capítulo 7.

[^book-docs]: J.C. Ködel, "One Page at a Time", o repositório deste livro no commit 6c2713b63af7397ee00142497287b8408a5651b1: os trechos do docs/00, do docs/03, do docs/05, do ADR-0010 e do `AGENTS.md`. <https://github.com/JCKodel/focus-kit-book/tree/6c2713b63af7397ee00142497287b8408a5651b1>
[^dart-error-exception]: Dart, "Error class" e "Exception class", referência da API de `dart:core`, acesso em 2026-09-28: um `Error` é "*uma falha do programa que o programador deveria ter evitado*"; uma `Exception` "*foi feita para ser capturada*". <https://api.dart.dev/dart-core/Error-class.html> e <https://api.dart.dev/dart-core/Exception-class.html>
[^book-adr-0016]: J.C. Ködel, "One Page at a Time", o ADR-0016 deste livro, `docs/adr/ADR-0016-the-books-definition-of-focus.md`, de 2026-09-28, na pasta de ADRs em `main`. <https://github.com/JCKodel/focus-kit-book/tree/main/docs/adr>
