# 16. A fila enquanto acontece

Depois deste capítulo você consegue ler o estado de qualquer linha da fila entre as seis marcas do focus-kit, dizer quem põe cada uma e em que momento, e marcar uma linha que espera com o seu motivo e tirá-la de lá de novo.
Você também consegue dispor a fila como um quadro kanban que mostra o trabalho enquanto ele acontece, e dizer onde cada marca é vista.

## O problema

No Caso A, um projeto para um cliente em uma plataforma low-code, o gerente de projeto acompanhava o trabalho em um quadro kanban do Azure DevOps que um script preenchia a partir da fila, numa só direção: `[ ]` ia para To Do, `[>]` para Doing, `[x]` para Done.
Cada marca mudava quando um comando terminava.
Então uma entrega ficava em To Do enquanto o autor e o agente conversavam a página dela, e só chegava a Doing depois de o `/propose` tê-la escrito; e um cartão em Doing podia ser uma página que ninguém estava construindo ainda.
As linhas travadas nas respostas do cliente não tinham marca própria: cinco delas ficavam em Doing e pareciam trabalho que ninguém tinha começado.
O projeto acrescentou uma quarta marca à mão, `[?]`, para uma linha esperando por uma pessoa.

Dois erros, então: o Doing chegava tarde, e a espera parecia parada.
O focus-kit responde aos dois desde a sua versão 2026.10.05, com seis marcas, cada uma posta no momento em que o trabalho muda.[^setup]

## Seis marcas

| Marca | Significa | Quem põe |
|---|---|---|
| `[ ]` | não definida | a conversa que acrescenta a linha |
| `[~]` | sendo definida | o `/propose`, quando começa |
| `[>]` | definida: a página existe | o `/propose`, quando a página está escrita |
| `[*]` | sendo construída | o `/apply`, quando começa |
| `[x]` | feita: a página está em `work/done/` | o `/apply`, com a verificação verde |
| `[?]` | esperando | qualquer sessão, nos três casos abaixo |

Este é o primeiro marco da biblioteca em uma tarde, escrito para este capítulo, com todas as marcas em uso.
O motivo da espera, `· blocked:`, fica em inglês, como o kit o escreve:

```
[x] catalogo          a bibliotecária cadastra livros e exemplares
[x] membros           a bibliotecária cadastra e suspende membros
[*] emprestar-livro   a bibliotecária empresta, e as regras recusam
[>] devolver-livro    a bibliotecária registra uma devolução
[~] reservas          um membro reserva um exemplar emprestado
[?] meus-emprestimos  o membro vê os dele · blocked: after emprestar-livro
[?] aviso-prazo       SMS antes do prazo · blocked: qual provedor?
[ ] m1-review         o marco conferido contra o parágrafo dele
```

Quem a lê sabe, sem perguntar, que uma sessão está construindo `emprestar-livro`, que `devolver-livro` tem uma página pronta para o `/apply`, que alguém está conversando `reservas` agora mesmo, e o que cada linha em espera espera.

## No momento em que o trabalho muda

Uma marca posta quando um comando termina está errada enquanto o comando roda.
O `/propose` pode conversar por uma hora antes de escrever uma página; com três marcas essa hora se lê como "não definida", e a entrega só aparece como começada depois de a definição dela ter acabado.
Então cada marca é posta quando o trabalho começa ou para: `[~]` quando a conversa começa, `[>]` quando a página está escrita, `[*]` quando a construção começa, `[x]` quando ela termina verde.
A fila passa a dizer o que está acontecendo agora, não o que terminou por último.

Onde uma marca é vista depende de onde a sessão trabalha (capítulo 20).
No trunk, a marca muda na fila da pasta onde a sessão roda, na hora, e chega ao histórico com o commit da pessoa.
Em um branch ou em uma worktree, o `[~]` e o `[*]` moram nesse branch, e o branch principal só os vê quando o merge da entrega chega, então a fila do branch principal guarda o que já chegou.
Um quadro atualizado pelo comando que mudou a marca a mostra na hora, em qualquer branch em que o trabalho esteja.

## Esperando: `[?]`

Uma linha espera em três casos:

* **A pessoa diz que ela está travada.** A biblioteca ainda não comprou os leitores de código de barras, então a bibliotecária pede para segurar `escanear-exemplar`: `· blocked: sem leitores ainda`.
* **Uma resposta foi pedida e não veio.** `aviso-prazo` precisa de um provedor de SMS, a pergunta foi para a diretora da biblioteca, e ninguém respondeu: `· blocked: qual provedor?`.
* **Outra linha precisa ser feita antes.** No meio de `/apply meus-emprestimos`, a construção descobre que `emprestar-livro` põe o prazo um dia antes no fim de um mês; a correção vira uma linha `[ ]` acima dela, e `meus-emprestimos` espera: `· blocked: after corrigir-vencimento`.

O motivo vai no fim da linha, em palavras, `· blocked: <reason>`, ou como as linhas que precisam estar `[x]` antes, `· blocked: after <slug>, <slug>`.
Qualquer marca antes de `[x]` pode virar `[?]`: uma linha pode esperar antes de alguém defini-la, enquanto a página dela está sendo escrita, ou no meio da construção.

Uma linha sai de `[?]` quando o motivo se resolve.
A pessoa diz isso; ou a sessão que registra a resposta a tira, como quando o nome do provedor chega e vira uma linha do docs/00; ou o `/apply` a tira quando marca `[x]` a última linha que um `after` nomeia.
Ela volta para `[>]` quando a página dela existe e para `[ ]` quando não tem página, e o próximo comando a marca de novo.

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
m1-review            devolver-livro             membros
                     emprestar-livro
                     meus-emprestimos TRAVADA
```

`reservas` está em Fazendo desde o primeiro minuto da conversa dela, que era o erro do quadro do Caso A.
O capítulo 22 mostra como um script espelha a fila no quadro do próprio time, numa só direção.

## O que o time ganha

Um gerente lê onde cada entrega está, e o que cada uma em espera espera, sem perguntar a ninguém e sem reunião de status.
No Caso A, cinco linhas travadas no cliente pareciam trabalho parado, e cada entrega só chegava a Doing depois de a definição dela ter acabado, contado pelo autor na fila e no quadro do projeto; uma marca posta quando o trabalho muda, e uma para a espera, respondem aos dois.

## Pontos-chave

* Seis marcas: `[ ]` não definida, `[~]` sendo definida, `[>]` definida, `[*]` sendo construída, `[x]` feita, `[?]` esperando.
* Uma marca muda quando o trabalho muda, não quando um comando termina: o `/propose` põe `[~]` e `[>]`, o `/apply` põe `[*]` e `[x]`, qualquer sessão põe `[?]`.
* Uma linha espera quando a pessoa diz, quando uma resposta foi pedida e não veio, ou quando outra linha precisa ser feita antes; o motivo vai no fim, `· blocked: <reason>` ou `· blocked: after <slug>`.
* Uma linha sai de `[?]` quando o motivo se resolve, de volta a `[>]` com página ou a `[ ]` sem; o `/propose` e o `/apply` param em uma linha `[?]` até a pessoa dizer que está resolvido.
* A fila é um quadro kanban, uma coluna por marca; em três colunas, Fazendo guarda `[~]`, `[>]` e `[*]`, e um cartão `[?]` é etiquetado como travado onde estava.

[^setup]: J.C. Ködel, focus-kit, `SETUP.md`, versão 2026.10.05, o §4 do documento de processo. <https://github.com/JCKodel/focus-kit/blob/main/SETUP.md>
[^toyota-kanban]: Toyota Motor Corporation, "75 Years of Toyota", Part 2, Chapter 1, Section 4, Item 4, "Development and Deployment of the Toyota Production System", acesso em 2026-10-05. <https://www.toyota-global.com/company/history_of_toyota/75years/text/entering_the_automotive_business/chapter1/section4/item4.html>
[^azure-kanban]: Microsoft Learn, "About Kanban boards", Azure Boards, acesso em 2026-09-30. <https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview>
