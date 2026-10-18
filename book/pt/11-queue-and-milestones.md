# 11. A fila e os marcos

Depois deste capítulo você consegue ler uma fila e escrever um parágrafo de marco que uma pessoa consegue conferir.
Você também consegue escrever uma linha como uma frase com os seus sufixos, ordenar um marco de modo que a ordem seja a prioridade, escrever em uma linha qual linha precisa estar feita antes dela, `· after <slug>`, acrescentar uma linha no marco cujo parágrafo precisa dela ou sob o seguinte, mover ou mudar uma linha conversando, e transformar uma mudança de código pedida fora do `/apply` em uma linha e no rascunho da página dela.
E consegue dizer quanto custa a menor entrega, da linha dela até o commit.

## O problema

Um time que guarda o plano em um gerenciador de tarefas, as decisões em um chat e o andamento na cabeça de alguém não consegue responder "o que falta, e o que foi feito?" sem uma reunião.
Um agente não consegue responder de jeito nenhum: ele não sabe nada no começo de uma sessão, então o que não está escrito onde ele lê não existe para ele.
A fila é um arquivo, o docs/06, que diz o que vem a seguir, o que está em andamento e o que foi entregue, em uma ordem que uma pessoa e um agente leem igual.

## A linha

O docs/06 guarda os marcos do projeto, cada um com um parágrafo que diz o que é verdade quando ele fecha, e sob cada um uma linha por entrega, em ordem.
Uma linha é a marca, o slug, uma frase do que a entrega dá, e os seus sufixos, como `· after <slug>`, que nomeia uma linha que precisa estar feita antes dela:

```
[ ] <slug>  <o que ela entrega, uma frase> · after <slug>
```

O `· after`, como o `· blocked:` do [capítulo 14](14-queue-states.md), fica em inglês, como o kit o escreve.

O slug é o nome da entrega, em palavras minúsculas unidas por hífens ([capítulo 12](12-propose.md)).
Ele dá nome à página da entrega, `work/<slug>.md`, e é o argumento dos comandos, `/propose <slug>` e `/apply <slug>`, então a linha, a página e os comandos apontam todos para a mesma entrega.

O kit pede uma frase, e o que aconteceu vai para a página, porque o `/propose` lê a fila inteira antes de definir uma entrega: cada palavra de uma linha é lida por toda definição.
No Ninjobs eu deixei as linhas crescerem: a fila dele tinha 102 entregas em 1.711 linhas, 1.052 delas continuações de uma linha, decisões que pertenciam às páginas.
Uma linha que cresce até virar um parágrafo é uma decisão no lugar errado, já que a página é onde a próxima sessão a procura.

## As marcas

Uma linha tem uma de seis marcas, que diz onde a entrega dela está.
Este capítulo precisa de duas: `[ ]`, ainda não definida, a entrega tem uma linha e nenhuma página completa, embora um rascunho dela possa esperar em `work/` (abaixo); e `[x]`, feita, foi construída e a página dela foi para `work/done/` ([capítulo 13](13-apply.md)).
As outras quatro, `[~]`, `[>]`, `[*]` e `[?]`, são do [capítulo 14](14-queue-states.md): o que cada uma significa, quem a põe e em que momento, quando uma linha está livre para começar, e como uma linha espera e sai de `[?]`.

Uma linha nunca sai da fila; ela muda de marca e mantém a sua frase.
Então a fila é também o histórico do que foi entregue, na ordem em que foi planejado, e o que aconteceu está na página em `work/done/` por trás de cada `[x]`, nunca acrescentado à linha.
No trunk (direto na linha principal do histórico) a página espera sem commit (sem ser registrada no histórico) entre os dois comandos, e o `/apply` a lê da árvore de trabalho, então uma sessão nova a encontra tendo ou não havido commit ([capítulo 18](18-git-essentials.md)).

Este é o primeiro marco da biblioteca alguns dias depois do começo do trabalho, escrito para este capítulo:

````markdown
## Marco 1: um bibliotecário empresta e recebe de volta

Quando ele fecha, um bibliotecário consegue cadastrar livros, seus
exemplares e membros, emprestar um exemplar a um membro por 21 dias e
registrar a devolução; um membro com um livro atrasado ou com a inscrição
suspensa é recusado.

```
[x] esqueleto        app e servidor vazios, npm run verify, 1º screenshot
[x] catalogo         o bibliotecário cadastra livros e seus exemplares
[x] membros          o bibliotecário cadastra, suspende e reativa membros
[>] emprestar-livro  o bibliotecário empresta, e as regras podem recusar
[ ] devolver-livro   registra a devolução · after emprestar-livro
[ ] m1-review        o marco conferido contra o parágrafo dele
```
````

Qualquer pessoa lê o estado nele: três entregas feitas, `emprestar-livro` está completamente definida e espera o `/apply`, e duas linhas ainda não estão definidas, das quais `devolver-livro` vem depois de `emprestar-livro`, já que um exemplar só é devolvido depois de ter sido emprestado.

## Marcos

### O parágrafo é um teste

O parágrafo de um marco diz o que é verdade quando o marco fecha, em frases que uma pessoa consegue conferir no produto rodando.
Ele é um teste, nunca um tema e nunca uma lista das linhas sob ele: "um bibliotecário consegue emprestar um exemplar a um membro por 21 dias" pode ser conferido, "empréstimos" não.
Toda frase do parágrafo deveria ter uma linha que a torna verdade, e toda linha deveria servir a uma frase; uma frase sem linha, ou uma linha sem frase, é uma fila para corrigir antes de o trabalho começar.

### Tamanho e ordem

Um marco começa com as linhas de que o seu parágrafo precisa, e depois a revisão dele; para o primeiro marco o kit pede de três a oito entregas.
As primeiras são o esqueleto em que as outras se apoiam: o `esqueleto` da biblioteca cria o `npm run verify`, que toda entrega seguinte roda.
Depois cada linha vem após as linhas de que precisa: um bibliotecário não consegue emprestar um exemplar antes de o catálogo ter exemplares e de os membros existirem.

Linhas são acrescentadas enquanto um marco anda: uma correção que uma entrega encontra fora da sua página, os achados da revisão, um problema que você encontra testando o produto.
Assim um marco fecha maior do que começou, e a fila muda com o trabalho.
A fila deste próprio livro mostra isso: o marco M15 fechou com 42 linhas; a revisão dele foi a 14ª, com 28 sob ela.[^m15-queue]
Um agente a quem você pergunta sobre um problema tende a responder com linhas, cada uma razoável, então, sem uma pessoa julgando, um marco cresce sem fim.
O parágrafo decide onde uma linha vai, seja quem for que a acrescente, você ou o agente: uma linha de que uma cláusula do parágrafo do marco atual precisa vai nesse marco, e qualquer outra vai sob o marco seguinte, que o agente cria quando não há nenhum, com um parágrafo que a linha atende e a sua revisão por último.
Na biblioteca, depois de `devolver-livro` construída, você testa o produto e descobre que um exemplar cujo empréstimo está atrasado não consegue ser recebido de volta; a correção, uma linha escrita para este capítulo, `corrigir-devolucao-atrasada`, fica no marco 1, acima de `m1-review`, porque o parágrafo promete registrar a devolução.
Um achado da revisão do próprio marco também fica no seu marco, sob a revisão, mesmo quando o marco seguinte já está na fila (abaixo).
O que você decide é o parágrafo: uma linha só entra no marco atual por uma cláusula, então para trazer uma você amplia o parágrafo conversando antes, e a linha passa a atender a cláusula nova.

A ordem é a prioridade.
Perguntado qual entrega importa mais, você responde pela fila: a que está mais acima nela; a próxima entrega é a primeira livre para começar ([capítulo 14](14-queue-states.md)).
Não há campo de prioridade nem etiqueta para manter em dia com a ordem.

Quando você acrescenta uma linha e já sabe que ela precisa de outra feita antes, você escreve isso junto, no fim: uma devolução precisa de um empréstimo, então `devolver-livro` termina com `· after emprestar-livro`.
Isso é uma ordem, não uma espera: a linha mantém a sua marca, `[ ]`, e fica livre para começar quando `emprestar-livro` estiver `[x]`.
`emprestar-livro` não leva `after`: as linhas de que ela precisa, `catalogo` e `membros`, já estão `[x]`.

### A revisão, e os seus achados

Um marco é planejado com a sua revisão como a última linha, `<milestone>-review` (em inglês, como o kit a escreve: `m1-review` para o primeiro marco), uma entrega como as outras, que pega o parágrafo cláusula por cláusula ([capítulo 15](15-closing-a-milestone.md)).
Ela não corrige nada: uma pessoa testa cada cláusula à mão e, com a palavra da pessoa, a sessão faz ler o código alterado desde a base do marco pelas áreas que o docs/05 do projeto cita, quando cita áreas, um agente somente leitura em cada uma, e um conferente marca cada candidato antes que a pessoa o veja.
Cada achado vira uma linha `[ ]` no mesmo marco, sob a linha da revisão, mesmo quando o marco seguinte já tem linhas, e essas linhas não têm segunda revisão.

## Mudando a fila

Nenhum comando é dono da fila.
Uma ideia nova vira uma linha conversando, em qualquer sessão: você conta ao agente, e ele escreve a linha, com um slug novo e `[ ]`, no marco cujo parágrafo precisa dela, ou sob o seguinte.

O código tem um dono, o `/apply`, o comando que constrói uma entrega (capítulo 13).
Uma mudança nele pedida em qualquer outra sessão, por menor que seja, vira uma linha `[ ]`: o agente escreve a linha, escreve num rascunho da página o que você disse e a linha não comporta, diz isso, e a resposta para ali, sem nenhum arquivo do app alterado.
Pedido numa sessão comum para mostrar a data de devolução na tela do empréstimo como dia/mês/ano, e informado de como ela deve aparecer numa tela estreita e de que o catálogo mantém a forma ISO, ano-mês-dia, o agente escreve uma linha, `formato-devolucao`, e procura onde ela vai.
Nenhuma cláusula do parágrafo do marco 1 precisa dela: o parágrafo promete um empréstimo de 21 dias e uma devolução registrada, não como uma data se lê.
Então a linha não vai acima de `m1-review`, como se chegar agora a tornasse parte do marco; ela vai sob o marco seguinte, e sem nenhum na fila o agente cria um, com um parágrafo que a linha atende e a sua revisão por último, escrito para este capítulo:

````markdown
## Marco 2: datas de empréstimo lidas de relance

Quando ele fecha, um membro lê a data de devolução na tela do empréstimo
como dia/mês/ano, numa tela estreita também.

```
[ ] formato-devolucao   a tela mostra a data de devolução em dia/mês/ano
[ ] m2-review           o marco conferido contra o parágrafo dele
```
````

O marco 1 mantém as suas linhas, a ordem delas e o `· after emprestar-livro` de `devolver-livro`; o marco 2 vem depois dele, então a sua linha vem depois de todas elas em prioridade, e o parágrafo que o agente escreveu é seu para ler e corrigir, como toda mudança na fila.

A regra da tela estreita e a exceção do catálogo não cabem na frase única da linha, então vão para um rascunho `work/formato-devolucao.md`, e a resposta para ali, nomeando `/propose formato-devolucao` para uma sessão nova, escrito como o seu host chama os comandos; um pedido que a linha comporta inteiro não ganha rascunho.
O rascunho é onde o detalhe espera: o `/propose formato-devolucao`, numa sessão nova, parte dele e escreve a página (o capítulo 12 mostra o `/propose`), então nada do que você disse na primeira sessão é dito duas vezes.
A linha fica `[ ]` com o rascunho ao lado: um rascunho em `work/` não é uma definição, e o `/apply` só constrói uma linha que o `/propose` marcou `[>]` ([capítulo 14](14-queue-states.md)).
Dizer "defina agora" recebe a mesma resposta: a regra do kit é o `/propose` numa sessão nova, cuja janela contém o arquivo de regras, os documentos e o rascunho, e nada desta conversa, então a página guarda só o que ficou por escrito, que é tudo o que o `/apply` terá.
Um host pode mesmo assim rodar o comando aqui quando você o nomeia na sua mensagem, e alguns se oferecem para isso; a página seria escrita com tudo o que foi dito nesta sessão ainda na janela, então abra uma sessão nova.

Uma mudança tão pequena passa mesmo assim pelo método inteiro, e isto é o que ela custa.
O `/propose formato-devolucao` lê os documentos do projeto e o rascunho e escreve esta página, escrita para este capítulo:

```markdown
# formato-devolucao

**Objetivo.** Um membro vê a data de devolução de um empréstimo como
dia/mês/ano na tela do empréstimo.

**Comportamento.**
* Um empréstimo com data de devolução 2026-03-05 mostra 05/03/2026, numa
  tela estreita também.
* Um empréstimo sem data de devolução não mostra nada onde a data estaria.

**Contrato.** Nenhum.

**Estados.** Os padrões.

**Referência visual.** Nenhuma.

**Fora do escopo.** As datas do catálogo, que mantêm ano-mês-dia; as datas
da lista de atrasos, uma linha própria.

**Pronto quando.** As duas linhas de Comportamento passam como testes; a
verificação está verde.
```

Todas as seções estão lá, e três delas só dizem que não se aplicam; os dois detalhes do rascunho são uma linha de Comportamento e um item de Fora do escopo.
Você lê a página e a corrige, e numa outra sessão nova o `/apply formato-devolucao` a constrói: ele muda a função que formata a data na tela do empréstimo e escreve um teste com as duas linhas de Comportamento, umas cinco linhas entre os dois, roda o verify até ficar verde, move a página para `work/done/`, coloca em stage os dois arquivos com a página e a linha da fila, e sugere a mensagem, também escrita para este capítulo (o capítulo 13 explica o formato dela):

```commit
Mostrar a data de devolução como dia/mês/ano

- Não mostra nada quando um empréstimo não tem data de devolução

work/done/formato-devolucao.md
```

Você revisa um diff de poucas linhas contra uma página que já leu, e faz o commit; a linha agora diz:

```
[x] formato-devolucao   a tela mostra a data de devolução em dia/mês/ano
```

Foi isso o que a regra custou: duas sessões curtas, uma revisão e um commit.
Em troca, a fila diz que a mudança existe, a página diz o que ela faz e o que deixa de fora, e um teste falha se o formato um dia voltar ao que era.
Uma edição feita na hora teria pulado a linha, a página, o teste e a revisão.
A página é do tamanho da mudança: sete seções de uma ou duas linhas, e uma página que precisa de mais para uma mudança deste tamanho está definindo mais de uma entrega.
A regra vale em toda sessão: durante o `/propose` a mudança é uma linha nova, a não ser que você a peça na página que está sendo escrita; durante o `/apply`, uma correção encontrada fora da sua página vira uma linha `[ ]`, e só uma correção de que a entrega precisa antes fica acima dela e a faz esperar (capítulo 14); e uma edição feita mesmo assim, para "só trocar o rótulo", é desfeita antes de qualquer commit.
Os documentos continuam mudando conversando, em qualquer sessão; a regra cobre o código: o fonte do app, os testes, uma migração, a configuração.

O parágrafo de um marco ou a descrição de uma linha também muda conversando, e o slug fica, já que uma página ou um commit pode já usá-lo.
Mover uma linha para cima ou para baixo é mudar a prioridade dela, e acontece do mesmo jeito: você pede ao agente para movê-la.
Uma mudança de lugar mantém o `· after` da linha, e uma linha levada para o marco atual precisa de uma cláusula do parágrafo dele, ou de um parágrafo que você ampliou antes, então mover nunca muda o que um marco promete sem uma palavra.
Linhas também vêm da revisão de um marco e, em um projeto existente, das issues ou do roadmap dele.
Você lê a mudança antes do commit, como com todo documento, e ninguém edita a fila à mão.

## O que o time ganha

A fila é o quadro de status compartilhado do time e o histórico dele em um arquivo: o que vem a seguir, o que está em andamento, o que foi feito e em que ordem, legível por um gerente sem ferramenta nenhuma e por um agente no começo de toda sessão.
No Ninjobs ela guardou 102 entregas, feitas e ainda não feitas, em um arquivo.
No Caso A, um projeto para um cliente em uma plataforma low-code, o Microsoft Power Apps com o Copilot Studio, o relatório de status e a estimativa de risco para o gerente de projeto foram escritos a partir da fila e das páginas, não de memória ([capítulo 17](17-project-as-assistant.md)).

## Pontos-chave

* O docs/06 guarda marcos, cada um com um parágrafo, e uma linha por entrega sob ele: uma marca, um slug, uma frase e os seus sufixos; o que aconteceu vai para a página.
* A marca de uma linha diz onde a entrega dela está, de `[ ]`, não definida, a `[x]`, feita; uma linha nunca sai, então a fila é também o histórico.
* O parágrafo de um marco é um teste que uma pessoa confere no produto, nunca um tema, sobre as entregas que o tornam verdade, de três a oito no primeiro marco: o esqueleto primeiro, cada linha após as linhas de que precisa, e por último a revisão, cujos achados viram linhas sob ela no mesmo marco; linhas são acrescentadas enquanto ele anda, e quem acrescenta uma a põe no marco que tem uma cláusula que precisa dela, ou sob o seguinte, criado quando falta com um parágrafo que a linha atende e a sua revisão por último.
* A ordem é a prioridade: a linha mais acima importa mais, mover uma linha muda a prioridade dela, e uma dependência conhecida quando a linha é acrescentada é escrita junto, `· after <slug>`, uma ordem, não uma espera, então a linha mantém `[ ]`.
* Nenhum comando é dono da fila: linhas e parágrafos mudam conversando, em qualquer sessão, com o slug mantido; o código só muda dentro do `/apply`, até uma mudança de cinco linhas tem sua página, e uma mudança pedida em qualquer outro lugar vira uma linha, com um rascunho da página para o que a linha não comporta, e o `/propose` numa sessão nova.

[^m15-queue]: J.C. Ködel, "One Page at a Time", o docs/06, a fila, marco M15, acesso em 2026-10-18, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/blob/main/docs/06-Queue.md>
