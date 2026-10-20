# 14. A fila enquanto acontece

Depois deste capítulo você consegue ler o estado de qualquer linha da fila entre as seis marcas do focus-kit, dizer quem põe cada uma e em que momento, dizer qual é a próxima entrega, e quais linhas podem rodar ao mesmo tempo.
Você também consegue distinguir uma ordem escrita com a linha, `· after`, de uma espera descoberta no caminho, `[?]`, marcar uma linha que espera com o seu motivo e a fase de retomada, e tirá-la de lá de novo; e dispor a fila como um quadro kanban que mostra o trabalho enquanto ele acontece, e dizer onde cada marca é vista.
E você consegue retomar uma linha cuja sessão terminou, e registrar uma entrega que a pessoa cancela de modo que ela nunca pareça construída.

## O problema

No Caso A, um projeto para um cliente em uma plataforma low-code, o gerente de projeto acompanhava o trabalho em um quadro kanban do Azure DevOps que um script preenchia a partir da fila, numa só direção: `[ ]` ia para To Do, `[>]` para Doing, `[x]` para Done.
Cada marca mudava quando um comando terminava.
Então uma entrega ficava em To Do enquanto o autor e o agente conversavam a página dela, e só chegava a Doing depois de o `/propose` tê-la escrito; e um cartão em Doing podia ser uma página que ninguém estava construindo ainda.
As linhas travadas nas respostas do cliente não tinham marca própria: cinco delas ficavam em Doing e pareciam trabalho que ninguém tinha começado.
O projeto acrescentou uma quarta marca à mão, `[?]`, para uma linha esperando por uma pessoa.

Dois erros, então: o Doing chegava tarde, e a espera parecia parada.
O focus-kit responde aos dois com seis marcas, cada uma posta no momento em que o trabalho muda.

## Seis marcas

| Marca | Significa | Quem põe |
|---|---|---|
| `[ ]` | não definida | a conversa que acrescenta a linha |
| `[~]` | sendo definida | o `/propose`, quando começa |
| `[>]` | completamente definida: a página está pronta para o `/apply` | o `/propose`, quando a página está completa |
| `[*]` | sendo construída | o `/apply`, quando começa |
| `[x]` | feita: a página está em `work/done/`; com `· dropped:`, cancelada | o `/apply`, com a verificação verde; a pessoa, ao cancelar |
| `[?]` | esperando | qualquer sessão, nos quatro casos abaixo |

`· dropped:` é um sufixo do `[x]`, não uma sétima marca: uma entrega cancelada é encerrada como uma construída, e o sufixo diz que nada foi entregue (abaixo).

Uma página que existe ainda não é `[>]`: um rascunho guardado para uma linha `[ ]` também é um arquivo em `work/` ([capítulo 11](11-queue-and-milestones.md)).
A página está completa quando toda seção está preenchida ou diz que não se aplica e nenhuma questão de escopo está aberta; só então o `/propose` marca a linha `[>]`, e o `/apply` a constrói quando toda linha que o `after` dela nomeia está `[x]`.
Enquanto uma questão de escopo ainda está sendo conversada, a linha fica `[~]`; uma pergunta feita a alguém que não respondeu a faz esperar, `[?]` (abaixo).

Este é o primeiro marco da biblioteca em uma tarde, escrito para este capítulo, com todas as marcas em uso.
Os sufixos `· after`, `· resume:`, `· blocked:` e `· dropped:` ficam em inglês, como o kit os escreve:

```
[x] catalogo          o bibliotecário cadastra livros e exemplares
[x] membros           o bibliotecário cadastra e suspende membros
[*] emprestar-livro   o bibliotecário empresta um exemplar ou a regra nega
[ ] devolver-livro    registra a devolução · after emprestar-livro
[>] buscar-catalogo   um membro busca no catálogo
[~] reservas          um membro reserva um exemplar emprestado
[ ] meus-emprestimos  o membro vê seus empréstimos · after emprestar-livro
[?] aviso-prazo       um aviso · resume: propose · blocked: qual provedor?
[ ] m1-review         o marco conferido contra o parágrafo dele
```

Quem a lê sabe, sem perguntar, que uma sessão está construindo `emprestar-livro`, que `buscar-catalogo` está completamente definida e pronta para o `/apply`, que alguém está conversando `reservas` agora mesmo, que `devolver-livro` e `meus-emprestimos` vêm depois de `emprestar-livro`, e o que `aviso-prazo` espera e qual comando a retoma.

## No momento em que o trabalho muda

Uma marca posta quando um comando termina está errada enquanto o comando roda.
O `/propose` pode conversar por uma hora antes de escrever uma página; uma marca posta só quando a página é escrita lê essa hora como "não definida", e a entrega só aparece como começada depois de a definição dela ter acabado.
Então cada marca é posta quando o trabalho começa ou para: `[~]` quando a conversa começa, `[>]` quando a página está completa, `[*]` quando a construção começa, `[x]` quando ela termina verde.
A fila passa a dizer o que está acontecendo agora, não o que terminou por último.

Onde uma marca é vista depende de onde a sessão trabalha (capítulo 18).
No trunk, a marca muda na fila da pasta onde a sessão roda, um quadro que lê essa fila a vê na hora, e ela chega ao histórico com o commit da pessoa.
Com um branch ou um worktree por entrega, a marca mora no branch da entrega, enviado quando o `/propose` o cria, e o branch principal mostra a linha como ela estava até o merge.
Depois de um `git fetch`, uma linha cujo branch existe está ocupada, mostre o que mostrar o branch principal: o branch é a reivindicação da linha, no remoto desde o momento em que o trabalho começa, antes de qualquer marca nele ser enviada, então a fila do branch principal só muda por merges.
Então quem lê a fila, um quadro ou uma sessão que escolhe linhas livres ou resolve um `after`, pega a linha de cada slug no branch dele, local ou remoto, acrescenta as linhas que só um branch tem, e as reconcilia pelo slug, com cada linha no seu estado mais recente, nunca o arquivo inteiro de um branch.
As marcas mudam na hora pelo mesmo motivo nos dois casos, um quadro de onde as pessoas puxam trabalho: no trunk o quadro lê a fila única, e com um branch ou um worktree por entrega lê a linha de cada slug onde ela mora.
Onde a linha mora decide em quanto tempo quem lê vê a marca: o arquivo de um worktree mostra a marca no momento em que ela muda, um branch quando a marca entra em um commit nele, um branch remoto quando esse commit é enviado.
Um espelho do próprio projeto numa só direção, atualizado pelos comandos quando uma marca muda, mostra a marca na hora, e com um branch ou um worktree por entrega envia a fila lida do mesmo jeito, então cada atualização leva a marca de cada entrega até onde consegue vê-la, não a cópia do próprio branch.

## A próxima linha, e quais rodam juntas

Uma linha está livre quando não está `[x]` nem `[?]`, e toda linha que o `after` dela nomeia está `[x]` (um `[x]` que foi cancelado pede a pessoa antes, abaixo).
No marco acima, `emprestar-livro`, `buscar-catalogo` e `reservas` estão livres; `devolver-livro` e `meus-emprestimos` não, já que `emprestar-livro` ainda não está `[x]`, e `aviso-prazo` espera.
A próxima entrega é a primeira linha livre que nenhuma sessão pegou: uma sessão está construindo `emprestar-livro` e outra está definindo `reservas`, então a próxima entrega de uma sessão nova é `buscar-catalogo`.
Com um branch ou um worktree por entrega, a sessão roda `git fetch` antes, toma como ocupada uma linha cujo branch existe, e julga as linhas livres e o `after` pela linha de cada slug lida como diz a seção acima, então o `after` de `devolver-livro` lê a marca de `emprestar-livro` no branch de `emprestar-livro`.
Só pela cópia do branch principal, `emprestar-livro` leria `[ ]`, livre e sem nenhuma sessão que a tenha pegado, e a resposta nomearia uma entrega que outra sessão está construindo; o branch de `emprestar-livro` no remoto diz que ela está ocupada antes mesmo de qualquer marca dela ser enviada.
Quando `emprestar-livro` vira `[x]`, `devolver-livro` e `meus-emprestimos` ficam livres nesse momento, sem nada para tirar e sem marca para mudar; o `· after` fica na linha como o registro da ordem.
Uma linha com duas ordens, `· after emprestar-livro, membros`, só fica livre quando as duas estão `[x]`.

O fim de um marco define a prioridade, não se uma linha está livre.
A `formato-devolucao` do capítulo 11 fica sob o marco 2, abaixo de `m1-review`, e não nomeia nenhum `after`: ela está livre, e não espera `m1-review`.
Mas a próxima entrega é a primeira linha livre descendo a fila, então uma sessão a quem se pede a próxima só chega a ela quando o marco 1 não tem mais nenhuma linha livre.
Uma linha acrescentada depois vai no marco cujo parágrafo precisa dela, nunca mais acima na fila por ser nova: o lugar dela é a sua prioridade, e as linhas que já estavam lá mantêm a ordem e o `after` delas.

O `/propose` e o `/apply` não começam uma linha que não está livre: rode `/propose meus-emprestimos` com `emprestar-livro` em `[*]`, e ele diz o que a linha espera e para.

Perguntado o que pode rodar ao mesmo tempo, você responde pela fila: as linhas livres, e entre elas as que mexem em arquivos diferentes, julgadas pelas páginas delas e pelo docs/01, que diz onde mora cada parte do código.
`buscar-catalogo` e `reservas`, em `src/features/catalogo/` e `src/features/reservas/`, podem.
Duas linhas que mudam ambas `src/features/emprestimos/`, como fariam `emprestar-livro` e uma linha para renovar um empréstimo, não podem rodar juntas em uma pasta.
O [capítulo 19](19-worktrees.md) mostra como duas sessões rodam em uma pasta, e quando elas precisam de duas.

## Esperando: `[?]`

Uma linha espera em quatro casos:

* **A pessoa diz que ela está travada.** A biblioteca ainda não comprou os leitores de código de barras, então o bibliotecário pede para segurar `escanear-exemplar`: `· resume: propose · blocked: sem leitores ainda`.
* **Uma resposta foi pedida e não veio.** `aviso-prazo` precisa de um provedor de SMS, a pergunta foi para a diretora da biblioteca, e ninguém respondeu: `· resume: propose · blocked: qual provedor?`.
* **Outra linha precisa ser feita antes, descoberto depois de o trabalho começar.** No meio de `/apply meus-emprestimos`, a construção descobre que `emprestar-livro` põe a data de devolução um dia antes no fim de um mês; a correção vira uma linha `[ ]` acima dela, `corrigir-devolucao`, e `meus-emprestimos` espera: `· resume: apply · blocked: after corrigir-devolucao`.
* **A leitura do código de uma revisão de marco não cobriu parte do seu intervalo.** A revisão que fecha um marco lê, com a palavra da pessoa, toda mudança desde a base do marco, dividida em áreas com um leitor cada que lista os caminhos que leu ([capítulo 15](15-closing-a-milestone.md)), e um leitor que leu parte da sua área aponta do mesmo jeito que um que a leu inteira, então quando, no meio de `/apply m1-review`, os leitores da revisão não listam nenhum caminho de `src/features/catalogo/`, a linha espera com o que foi lido como motivo: `· resume: apply · blocked: lidos todos menos catalogo/`.

O motivo vai no fim da linha, em palavras, `· blocked: <motivo>`, ou como as linhas que precisam estar `[x]` antes, `· blocked: after <slug>, <slug>`.
Antes dele vai a fase de retomada, `· resume: propose` para uma linha que estava `[ ]` ou `[~]`, `· resume: apply` para uma que estava `[>]` ou `[*]`, para que a sessão que retoma a linha saiba de qual comando ela precisa.
Qualquer marca antes de `[x]` pode virar `[?]`: uma linha pode esperar antes de alguém defini-la, enquanto a página dela está sendo escrita, ou no meio da construção.

`· after` e `· blocked: after` se parecem e dizem coisas diferentes.
`· after` é uma ordem conhecida quando a linha é escrita: `meus-emprestimos` precisa de empréstimos para mostrar, então foi acrescentada como `[ ] meus-emprestimos ... · after emprestar-livro`, e mantém `[ ]`.
`· blocked: after` é uma espera descoberta depois de o trabalho começar, como foi `corrigir-devolucao`.
Escrever `[?] meus-emprestimos ... · blocked: after emprestar-livro` quando a linha é acrescentada está errado: a linha está na fila, não travada, e em um quadro levaria uma etiqueta de travada que diz a um gerente que algo deu errado quando nada deu.

Uma linha sai de `[?]` quando o motivo se resolve.
A pessoa diz isso; ou a sessão que registra a resposta a tira, como quando a diretora diz o provedor e o nome vira uma linha do docs/00; ou o `/apply` a tira quando marca `[x]` a última linha que um `after` nomeia.
Os dois sufixos saem, `resume` e `blocked`, e a fase de retomada diz para onde a linha volta.
`aviso-prazo`, com `resume: propose`, volta para `[ ]`, e qualquer rascunho da página dela fica para o `/propose` terminar: um rascunho é uma página começada, não uma definição completa.
Uma linha com `resume: apply` volta para `[>]`.

O `/propose` e o `/apply` param os dois em uma linha `[?]`: dizem o que ela espera, e só seguem depois que o motivo se resolve, por um desses três caminhos.
Um comando que passasse por cima do motivo construiria sobre uma resposta que ninguém deu.

## Uma sessão que terminou, uma entrega cancelada

Uma sessão pode terminar sem que ninguém trave a linha dela: o host fecha, a conexão cai, o limite do plano chega.
A linha mantém a sua marca.
`reservas` continua `[~]` depois que a conversa que a definia termina; nada espera por ninguém, então ela não vira `[?]`.
A marca sozinha não diz que a sessão terminou: uma linha `[~]` ou `[*]` está com uma sessão, e essa sessão pode estar conversando agora mesmo em outra pasta ou em outra máquina.
Então uma sessão nova não toma a linha só porque vê a marca; a pessoa, que sabe que a sessão terminou, diz isso e roda `/propose reservas` de novo.
O comando então inspeciona a página, a pasta de trabalho e o índice antes de editar, e segue do que a conversa anterior escreveu.
`emprestar-livro`, em `[*]` quando a construção dela perdeu a conexão, é retomada do mesmo jeito com `/apply emprestar-livro`: os arquivos já construídos e o que já está no índice continuam da entrega, e a linha continua `[*]`, nunca devolvida a `[>]` ou `[ ]` como se nada tivesse sido feito.

Uma entrega que a pessoa cancela, porque o trabalho provou que é impossível, porque foi recusada, ou porque ninguém a quer mais, também fica na fila.
Ela termina `[x]` com o motivo no fim da linha, `· dropped: <motivo>`, e a página dela vai para `work/done/` como qualquer outra, dizendo o que foi construído e o que foi desfeito, ou que nada foi construído.
A biblioteca queria que o bibliotecário imprimisse o cartão de um membro pelo navegador, e a impressora de cartões se mostrou sem um driver que o navegador alcançasse; o bibliotecário cancela a linha, e `reimprimir-cartao`, acrescentada depois dela, espera por ela, em duas linhas escritas para este capítulo:

```
[x] imprimir-cartao    imprime o cartão de membro · dropped: sem driver
[ ] reimprimir-cartao  reimprime um cartão perdido · after imprimir-cartao
```

`[x]` sozinho diz que a promessa da entrega vale, com a verificação verde; `[x]` com `· dropped:` diz que a decisão foi tomada e que a promessa não existe.
Quem o põe é a pessoa, não o `/apply`, porque cancelar é uma decisão de escopo, e a linha fica para que ninguém pergunte depois se `imprimir-cartao` foi esquecida.
Só pela regra de linha livre, `reimprimir-cartao` fica livre quando `imprimir-cartao` está `[x]`, e essa é a armadilha: o `[x]` que ela nomeia é uma decisão, não uma impressora de cartões que funciona.
Então uma linha cujo `after` nomeia uma entrega cancelada cabe à pessoa redecidir: cancelá-la também, como seria `reimprimir-cartao`, ou reescrevê-la sobre o que existe.

## A fila como quadro kanban

Um quadro kanban mostra o trabalho como cartões em colunas, uma coluna por estado, e um cartão passa de coluna em coluna conforme o estado dele muda.
As fábricas da Toyota usavam kanban, cartões que diziam que peças eram necessárias, onde e quando, e os adotaram em todas as fábricas em 1963.[^toyota-kanban]
Times de software levaram a ideia para um quadro em que, nas palavras da Microsoft sobre o Azure DevOps, "*os membros do time arrastam cartões entre colunas para atualizar o status*".[^azure-kanban]

Lida como um quadro, a fila tem uma coluna por marca, seis delas, e cada mudança de marca move um cartão.
Um cartão `[?]` fica em Esperando com o seu motivo, e quando o motivo se resolve ele passa para a coluna da marca a que volta, `[ ]` ou `[>]`.
Um time cujo quadro tem três colunas as dobra: `[ ]` para A fazer; `[~]`, `[>]` e `[*]` para Fazendo; `[x]` para Feito.
No quadro de três colunas deste capítulo, uma ilustração e não uma regra do kit nem um recurso de algum quadro, um cartão `[?]` vai pela sua fase de retomada, etiquetado como travado com o seu motivo, então a espera nunca parece parada: `resume: propose` em A fazer, `resume: apply` em Fazendo.
A linha diz para onde o cartão vai, então o quadro não guarda memória da coluna em que um cartão estava.
O marco acima, em um quadro de três colunas:

```
A FAZER              FAZENDO                    FEITO
aviso-prazo TRAVADA  reservas                   catalogo
devolver-livro       buscar-catalogo            membros
meus-emprestimos     emprestar-livro
m1-review
```

`devolver-livro` e `meus-emprestimos` ficam em A fazer sem etiqueta: esperam a sua vez, não por alguém, e só `aviso-prazo` é etiquetada como travada, em A fazer porque a sua linha diz `resume: propose`.

`reservas` está em Fazendo desde o primeiro minuto da conversa dela, que era o erro do quadro do Caso A.

Se `reservas` travasse no meio da definição, o seu `resume: propose` a levaria de Fazendo para A fazer, etiquetada como travada; resolvida, ela fica em A fazer como `[ ]`, com o rascunho mantido e sem etiqueta.
`meus-emprestimos`, esperando `corrigir-devolucao` no meio da construção, ficaria em Fazendo pelo seu `resume: apply`, etiquetada como travada; resolvida, ela fica em Fazendo como `[>]`, não como um `[*]` que nenhuma sessão está construindo.
Nos dois casos, resolver o motivo tira os dois sufixos e, com eles, a etiqueta.

O capítulo 20 mostra como um script espelha a fila no quadro do próprio time, numa só direção.

Um quadro também pode ler a própria fila, sem nada a espelhar.
Ele lê o docs/06 e as páginas em `work/` pelo slug, no trunk nos arquivos da própria pasta e com um branch ou um worktree por entrega no branch de cada slug, local ou remoto, e move os cartões conforme cada marca fica visível para ele enquanto o agente trabalha.

## O que o time ganha

Um gerente lê onde cada entrega está, e o que cada uma em espera espera, sem perguntar a ninguém e sem reunião de status.
No Caso A, cinco linhas travadas no cliente pareciam trabalho parado, e cada entrega só chegava a Doing depois de a definição dela ter acabado, contado pelo autor na fila e no quadro do projeto; uma marca posta quando o trabalho muda, e uma para a espera, respondem aos dois.
Um pedido que se provou impossível ali foi encerrado na fila com o seu motivo em vez de deixado em silêncio ([capítulo 23](23-adoption.md)), e o kit escreve um encerramento assim como `[x]` com `· dropped:`.

A fila também diz quais linhas podem rodar juntas: sem isso, uma pessoa que quer duas sessões tem de descobrir sozinha antes de abrir a segunda; as linhas livres e os arquivos em que mexem respondem isso pela fila, sem reunião.

## Pontos-chave

* Seis marcas, `[ ]` não definida, `[~]` sendo definida, `[>]` completamente definida e pronta para o `/apply`, `[*]` sendo construída, `[x]` feita, `[?]` esperando, cada uma mudada quando o trabalho muda, não quando um comando termina: o `/propose` põe `[~]` e `[>]`, o `/apply` põe `[*]` e `[x]`, a pessoa põe `[x]` com `· dropped: <motivo>` ao cancelar, qualquer sessão põe `[?]`.
* Uma linha está livre quando não está `[x]` nem `[?]` e toda linha que o `after` dela nomeia está `[x]`, e quando uma é cancelada a pessoa redecide a linha; com um branch ou um worktree por entrega, uma linha cujo branch existe depois de um `git fetch` está ocupada, mostre o que mostrar o branch principal; a próxima entrega é a primeira linha livre que nenhuma sessão pegou, e linhas livres que mexem em arquivos diferentes podem rodar ao mesmo tempo.
* Uma linha cuja sessão terminou mantém a sua marca, e o seu comando a retoma com a palavra da pessoa, inspecionando antes a página, a pasta e o índice; uma entrega cancelada termina `[x] · dropped: <motivo>`, com a página em `work/done/` dizendo o que foi construído e desfeito.
* `· after` é uma ordem escrita com a linha, que mantém a sua marca; `[?]` com `· blocked: after` é uma espera descoberta depois de o trabalho começar; uma linha espera quando a pessoa diz, quando uma resposta foi pedida e não veio, quando o trabalho já começado descobre que outra linha precisa ser feita antes, ou quando a leitura do código de uma revisão de marco não cobriu parte do seu intervalo, com a fase de retomada e o motivo no fim, `· resume: apply · blocked: after <slug>`; quando o motivo se resolve, os dois sufixos saem e ela volta conforme essa fase, `resume: propose` para `[ ]` com qualquer rascunho mantido, `resume: apply` para `[>]`, e até lá o `/propose` e o `/apply` param nela, como numa linha que não está livre.
* A fila é um quadro kanban, uma coluna por marca, um cartão `[?]` em Esperando até voltar a `[ ]` ou `[>]`; nas três colunas deste capítulo, Fazendo guarda `[~]`, `[>]` e `[*]`, e um cartão `[?]` é etiquetado como travado na coluna que a sua fase de retomada nomeia, A fazer para `propose`, Fazendo para `apply`; um quadro que lê a fila vê uma marca na hora no trunk, e com um branch ou um worktree por entrega pela linha de cada slug no branch dele, local ou remoto, enviado quando o `/propose` o cria, já que o branch principal mostra a linha como ela estava até o merge.

[^toyota-kanban]: Toyota Motor Corporation, "75 Years of Toyota", Part 2, Chapter 1, Section 4, Item 4, "Development and Deployment of the Toyota Production System", acesso em 2026-10-05. <https://www.toyota-global.com/company/history_of_toyota/75years/text/entering_the_automotive_business/chapter1/section4/item4.html>
[^azure-kanban]: Microsoft Learn, "About Kanban boards", Azure Boards, acesso em 2026-09-30. <https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview>
