# 14. A fila enquanto acontece

Depois deste capítulo você consegue ler o estado de qualquer linha da fila entre as seis marcas do focus-kit, dizer quem põe cada uma e em que momento, dizer qual é a próxima entrega, e quais linhas podem rodar ao mesmo tempo.
Você também consegue distinguir uma ordem escrita com a linha, `· after`, de uma espera descoberta no caminho, `[?]`, marcar uma linha que espera com o seu motivo e a fase de retomada, e tirá-la de lá de novo; e dispor a fila como um quadro kanban que mostra o trabalho enquanto ele acontece, e dizer onde cada marca é vista.

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
| `[>]` | definida: a página existe | o `/propose`, quando a página está completa |
| `[*]` | sendo construída | o `/apply`, quando começa |
| `[x]` | feita: a página está em `work/done/` | o `/apply`, com a verificação verde |
| `[?]` | esperando | qualquer sessão, nos três casos abaixo |

Este é o primeiro marco da biblioteca em uma tarde, escrito para este capítulo, com todas as marcas em uso.
Os sufixos `· after`, `· resume:` e `· blocked:` ficam em inglês, como o kit os escreve:

```
[x] catalogo          a bibliotecária cadastra livros e exemplares
[x] membros           a bibliotecária cadastra e suspende membros
[*] emprestar-livro   a bibliotecária empresta, e as regras recusam
[>] buscar-catalogo   um membro busca no catálogo
[~] reservas          um membro reserva um exemplar emprestado
[ ] meus-emprestimos  o membro vê os dele · after emprestar-livro
[?] aviso-prazo       um aviso · resume: propose · blocked: qual provedor?
[ ] m1-review         o marco conferido contra o parágrafo dele
```

Quem a lê sabe, sem perguntar, que uma sessão está construindo `emprestar-livro`, que `buscar-catalogo` tem uma página pronta para o `/apply`, que alguém está conversando `reservas` agora mesmo, que `meus-emprestimos` vem depois de `emprestar-livro`, e o que `aviso-prazo` espera e qual comando a retoma.

## No momento em que o trabalho muda

Uma marca posta quando um comando termina está errada enquanto o comando roda.
O `/propose` pode conversar por uma hora antes de escrever uma página; uma marca posta só quando a página é escrita lê essa hora como "não definida", e a entrega só aparece como começada depois de a definição dela ter acabado.
Então cada marca é posta quando o trabalho começa ou para: `[~]` quando a conversa começa, `[>]` quando a página está completa, `[*]` quando a construção começa, `[x]` quando ela termina verde.
A fila passa a dizer o que está acontecendo agora, não o que terminou por último.

Onde uma marca é vista depende de onde a sessão trabalha (capítulo 18).
No trunk, a marca muda na fila da pasta onde a sessão roda, na hora, e chega ao histórico com o commit da pessoa.
Em um branch ou em uma worktree, o `[~]` e o `[*]` moram nesse branch, e o branch principal só os vê quando o merge da entrega chega, então a fila do branch principal guarda o que já chegou.
Um quadro atualizado pelo comando que mudou a marca a mostra na hora, em qualquer branch em que o trabalho esteja.

## A próxima linha, e quais rodam juntas

Uma linha está livre quando não está `[x]` nem `[?]`, e toda linha que o `after` dela nomeia está `[x]`.
No marco acima, `emprestar-livro`, `buscar-catalogo` e `reservas` estão livres; `meus-emprestimos` não, já que `emprestar-livro` ainda não está `[x]`, e `aviso-prazo` espera.
A próxima entrega é a primeira linha livre que nenhuma sessão pegou: uma sessão está construindo `emprestar-livro` e outra está definindo `reservas`, então a próxima entrega de uma sessão nova é `buscar-catalogo`.
Quando `emprestar-livro` vira `[x]`, `meus-emprestimos` fica livre nesse momento, sem nada para tirar e sem marca para mudar; o `· after` fica na linha como o registro da ordem.
Uma linha com duas ordens, `· after emprestar-livro, membros`, só fica livre quando as duas estão `[x]`.

O `/propose` e o `/apply` não começam uma linha que não está livre: rode `/propose meus-emprestimos` com `emprestar-livro` em `[*]`, e ele diz o que a linha espera e para.

Perguntado o que pode rodar ao mesmo tempo, você responde pela fila: as linhas livres, e entre elas as que mexem em arquivos diferentes, julgadas pelas páginas delas e pelo docs/01, que diz onde mora cada parte do código.
`buscar-catalogo` e `reservas`, em `src/catalogo/` e `src/reservas/`, podem.
Duas linhas que mudam ambas `src/emprestimos/`, como fariam `emprestar-livro` e uma linha para renovar um empréstimo, não podem rodar juntas em uma pasta.
O [capítulo 19](19-worktrees.md) mostra como duas sessões rodam em uma pasta, e quando elas precisam de duas.

## Esperando: `[?]`

Uma linha espera em três casos:

* **A pessoa diz que ela está travada.** A biblioteca ainda não comprou os leitores de código de barras, então a bibliotecária pede para segurar `escanear-exemplar`: `· resume: propose · blocked: sem leitores ainda`.
* **Uma resposta foi pedida e não veio.** `aviso-prazo` precisa de um provedor de SMS, a pergunta foi para a diretora da biblioteca, e ninguém respondeu: `· resume: propose · blocked: qual provedor?`.
* **Outra linha precisa ser feita antes, descoberto depois de o trabalho começar.** No meio de `/apply meus-emprestimos`, a construção descobre que `emprestar-livro` põe o prazo um dia antes no fim de um mês; a correção vira uma linha `[ ]` acima dela, `corrigir-vencimento`, e `meus-emprestimos` espera: `· resume: apply · blocked: after corrigir-vencimento`.

O motivo vai no fim da linha, em palavras, `· blocked: <reason>`, ou como as linhas que precisam estar `[x]` antes, `· blocked: after <slug>, <slug>`.
Antes dele vai a fase de retomada, `· resume: propose` para uma linha que estava `[ ]` ou `[~]`, `· resume: apply` para uma que estava `[>]` ou `[*]`, para que a sessão que retoma a linha saiba de qual comando ela precisa.
Qualquer marca antes de `[x]` pode virar `[?]`: uma linha pode esperar antes de alguém defini-la, enquanto a página dela está sendo escrita, ou no meio da construção.

`· after` e `· blocked: after` se parecem e dizem coisas diferentes.
`· after` é uma ordem conhecida quando a linha é escrita: `meus-emprestimos` precisa de empréstimos para mostrar, então foi acrescentada como `[ ] meus-emprestimos ... · after emprestar-livro`, e mantém `[ ]`.
`· blocked: after` é uma espera descoberta depois de o trabalho começar, como foi `corrigir-vencimento`.
Escrever `[?] meus-emprestimos ... · blocked: after emprestar-livro` quando a linha é acrescentada está errado: a linha está na fila, não travada, e em um quadro levaria uma etiqueta de travada que diz a um gerente que algo deu errado quando nada deu.

Uma linha sai de `[?]` quando o motivo se resolve.
A pessoa diz isso; ou a sessão que registra a resposta a tira, como quando a diretora diz o provedor e o nome vira uma linha do docs/00; ou o `/apply` a tira quando marca `[x]` a última linha que um `after` nomeia.
Os dois sufixos saem, e a fase de retomada diz para onde a linha volta.
`aviso-prazo`, com `resume: propose`, volta para `[ ]`, e qualquer rascunho da página dela fica para o `/propose` terminar.
Uma linha com `resume: apply` volta para `[>]`; se o escopo ficou indefinido, volta para `[ ]` no lugar, e a sessão diz o que o `/propose` precisa decidir.

O `/propose` e o `/apply` param os dois em uma linha `[?]`: dizem o que ela espera, e só seguem quando a pessoa diz que está resolvido.
Um comando que passasse por cima do motivo construiria sobre uma resposta que ninguém deu.

## A fila como quadro kanban

Um quadro kanban mostra o trabalho como cartões em colunas, uma coluna por estado, e um cartão passa de coluna em coluna conforme o estado dele muda.
As fábricas da Toyota usavam kanban, cartões que diziam que peças eram necessárias, onde e quando, e os adotaram em todas as fábricas em 1963.[^toyota-kanban]
Times de software levaram a ideia para um quadro em que, nas palavras da Microsoft sobre o Azure DevOps, "*os membros do time arrastam cartões entre colunas para atualizar o status*".[^azure-kanban]

Lida como um quadro, a fila tem uma coluna por marca, seis delas, e cada mudança de marca move um cartão.
Um time cujo quadro tem três colunas as dobra: `[ ]` para A fazer; `[~]`, `[>]` e `[*]` para Fazendo; `[x]` para Feito.
Um cartão `[?]` fica na coluna em que estava, etiquetado como travado, com o seu motivo, então a espera nunca parece parada.
O marco acima, em um quadro de três colunas:

```
A FAZER              FAZENDO                    FEITO
aviso-prazo TRAVADA  reservas                   catalogo
meus-emprestimos     buscar-catalogo            membros
m1-review            emprestar-livro
```

`meus-emprestimos` fica em A fazer sem etiqueta: espera a sua vez, não por alguém, e só `aviso-prazo` é etiquetada como travada.

`reservas` está em Fazendo desde o primeiro minuto da conversa dela, que era o erro do quadro do Caso A.
O capítulo 20 mostra como um script espelha a fila no quadro do próprio time, numa só direção.

## O que o time ganha

Um gerente lê onde cada entrega está, e o que cada uma em espera espera, sem perguntar a ninguém e sem reunião de status.
No Caso A, cinco linhas travadas no cliente pareciam trabalho parado, e cada entrega só chegava a Doing depois de a definição dela ter acabado, contado pelo autor na fila e no quadro do projeto; uma marca posta quando o trabalho muda, e uma para a espera, respondem aos dois.

A fila também diz quais linhas podem rodar juntas: sem isso, uma pessoa que quer duas sessões tem de descobrir sozinha antes de abrir a segunda; as linhas livres e os arquivos em que mexem respondem isso pela fila, sem reunião.

## Pontos-chave

* Seis marcas: `[ ]` não definida, `[~]` sendo definida, `[>]` definida, `[*]` sendo construída, `[x]` feita, `[?]` esperando.
* Uma marca muda quando o trabalho muda, não quando um comando termina: o `/propose` põe `[~]` e `[>]`, o `/apply` põe `[*]` e `[x]`, qualquer sessão põe `[?]`.
* Uma linha está livre quando não está `[x]` nem `[?]` e toda linha que o `after` dela nomeia está `[x]`; a próxima entrega é a primeira linha livre que nenhuma sessão pegou, e linhas livres que mexem em arquivos diferentes podem rodar ao mesmo tempo.
* `· after` é uma ordem escrita com a linha, que mantém a sua marca; `[?]` com `· blocked: after` é uma espera descoberta depois de o trabalho começar.
* Uma linha espera quando a pessoa diz, quando uma resposta foi pedida e não veio, ou quando o trabalho já começado descobre que outra linha precisa ser feita antes; no fim vão a fase de retomada e o motivo, `· resume: apply · blocked: after <slug>`.
* Uma linha sai de `[?]` quando o motivo se resolve, pela fase de retomada; o `/propose` e o `/apply` param em uma linha `[?]`, ou em uma que não está livre, até que esteja.
* A fila é um quadro kanban, uma coluna por marca; em três colunas, Fazendo guarda `[~]`, `[>]` e `[*]`, e um cartão `[?]` é etiquetado como travado onde estava.

[^toyota-kanban]: Toyota Motor Corporation, "75 Years of Toyota", Part 2, Chapter 1, Section 4, Item 4, "Development and Deployment of the Toyota Production System", acesso em 2026-10-05. <https://www.toyota-global.com/company/history_of_toyota/75years/text/entering_the_automotive_business/chapter1/section4/item4.html>
[^azure-kanban]: Microsoft Learn, "About Kanban boards", Azure Boards, acesso em 2026-09-30. <https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview>
