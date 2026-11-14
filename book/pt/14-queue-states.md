# 14. A fila enquanto acontece

Depois deste capítulo você consegue ler o estado de qualquer linha da fila entre as seis marcas do focus-kit, dizer quem põe cada uma, em que momento, e como, um byte pelo script de marca do kit enquanto toda outra edição da fila muda só as próprias linhas, já que um programa que escreve a fila inteira pode esvaziá-la, e por que o script recusa um segundo começo de uma mesma linha, dizer qual é a próxima entrega, dizer quais linhas podem rodar ao mesmo tempo pela árvore da fila que o script do kit desenha, e dizer por que uma construção para em arquivos que outra construção está mudando.
Você também consegue distinguir uma ordem escrita com a linha, `· after`, lida para cada comando, de uma espera descoberta no caminho, `[?]`, marcar uma linha que espera com o seu motivo e a fase de retomada, e tirá-la de lá de novo; reconhecer uma linha vinda de um achado pelo seu `· from <slug>`, dizer onde ela fica no seu marco e por que todo outro achado é uma nota e não uma linha, e ler a linha `findings:` que o script de fila imprime; e dispor a fila como um quadro kanban que mostra o trabalho enquanto ele acontece, e dizer onde cada marca é vista.
E você consegue retomar uma linha cuja sessão terminou, e registrar uma entrega que a pessoa cancela de modo que ela nunca pareça construída nem faça a revisão do marco esperar.

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
A página está completa quando toda seção está preenchida ou diz que não se aplica e nenhuma questão de escopo está aberta; só então o `/propose` marca a linha `[>]`, e o `/apply` a constrói quando toda linha que o `after` dela nomeia está integrada (abaixo).
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
[ ] m1-review         o marco contra o parágrafo dele · after all
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
Então quem lê a fila, um quadro ou uma sessão que escolhe linhas livres ou resolve um `after`, roda `git fetch` e pega a linha de cada slug no branch dele no origin, que guarda a cópia atual até o merge, a do branch principal depois dele, e acrescenta as linhas que só um branch tem, nunca o arquivo inteiro de um branch.
As marcas mudam na hora pelo mesmo motivo nos dois casos, um quadro de onde as pessoas puxam trabalho: no trunk o quadro lê a fila única, e com um branch ou um worktree por entrega lê a linha de cada slug onde ela mora.
Onde a linha mora decide em quanto tempo quem lê vê a marca: quem lê vê a marca quando o commit dela é enviado ao branch no origin e trazido por um `git fetch`.
Um espelho do próprio projeto numa só direção, atualizado pelos comandos quando uma marca muda, mostra a marca na hora no trunk; com um branch ou um worktree por entrega envia a fila lida do mesmo jeito, então mostra uma marca na primeira atualização depois que a marca é enviada ao branch da entrega, e a atualização de cada entrega leva as marcas já enviadas de cada outra entrega, nunca a cópia do arquivo de um só branch.

## Como uma marca muda

A fila é um arquivo que toda sessão edita, cada uma a sua própria linha, muitas vezes ao mesmo tempo, enquanto um quadro a lê.
Um agente que muda a sua marca com um pequeno programa próprio, um que lê o docs/06, troca a marca e escreve o arquivo de volta, pode perder a fila inteira: um programa que abre o arquivo para escrita antes de lê-lo esvazia o arquivo primeiro.
Em 2026-10-18 num projeto e em 2026-10-26 em outro, um subagente marcando a sua linha rodou um programa assim, de uma linha: a escrita esvaziou o docs/06 antes da leitura, e a fila ficou com zero bytes.
Os dois subagentes estavam colocando em stage o próprio hunk de uma fila que outras sessões também editam, um hunk sendo o pedaço de um arquivo que o git coloca em stage como uma mudança só.

Então uma marca muda de um jeito só: o agente roda o script de marca do kit, `propose/scripts/mark.sh`, pelo próprio shell do git, como o script de reivindicação do capítulo 13 é rodado, `git -c "alias.fm=!sh .agents/skills/propose/scripts/mark.sh" fm <slug> "<marca>"`.
As seis marcas só diferem no caractere entre os colchetes, então uma marca é um byte.
O script acha a única linha do slug, muda esse byte, escreve o resultado num arquivo ao lado da fila e o renomeia por cima da fila, então a própria fila nunca é aberta para escrita; e ele recusa antes de escrever a fila a menos que o resultado mantenha o tamanho da fila e difira dela em no máximo esse byte.
Com `stage` no fim, ele muda a mesma linha no índice e nada mais ali, então as linhas que outra sessão já colocou em stage ficam como estavam: é assim que o `/apply` coloca em stage o seu `[x]`, mesmo quando outra sessão mudou a linha ao lado da sua.

Duas sessões que começam uma mesma linha a leem livre até uma delas marcá-la, então uma sessão que lê a linha `[>]` e depois a marca não tem como saber se outra a leu `[>]` um instante antes.
Em 2026-10-26, num projeto, o `/apply` de um mesmo slug foi digitado em duas sessões com seis segundos de diferença, numa mesma pasta, no trunk; a segunda leu a linha `[>]`, marcou-a como `[*]` e a construiu também.
Então o script confere a linha onde põe a marca, contra o que a linha tem naquele momento: ele põe um `[~]` só numa linha `[ ]` e um `[*]` só numa `[>]`, e em qualquer outra linha recusa antes de escrever qualquer coisa, dizendo que um `[~]` ou `[*]` é de outra sessão, retomado só com a palavra da pessoa.
As outras quatro marcas são postas sem essa conferência.

Toda outra edição do docs/06 é a edição de arquivo do próprio host, a ferramenta com que o agente muda as linhas de um arquivo, nas linhas que ela muda, nunca um programa que escreve o arquivo inteiro: uma linha acrescentada, um sufixo como `· blocked:` ou `· dropped:`, uma linha movida para mudar a sua prioridade.
Então pôr uma linha em espera, abaixo, são duas edições: `[?]` pelo script, o seu motivo e a sua fase de retomada pela edição de arquivo.

## A próxima linha, e quais rodam juntas

Uma linha está livre para um comando quando não está `[x]` nem `[?]` e o `after` que ela leva deixa esse comando começar, e o `after` é lido para cada comando.
O `/propose` começa quando toda linha que o `after` de uma linha nomeia está `[>]` ou além, porque a definição precisa das páginas delas; o `/apply` começa quando todas estão integradas, porque a construção precisa do código delas.
Integrada é `[x]` no trunk; com um branch ou um worktree por entrega é a entrega com merge no branch principal, e um `[x]` em um branch ainda sem merge está construído, esperando a integração (um `[x]` que foi cancelado pede a pessoa antes, abaixo).
A linha da revisão de um marco é escrita `· after all`: toda linha acima dela no seu marco menos as canceladas, então o `/propose` dela começa quando todas estão definidas e o `/apply` dela quando todas estão integradas.

No marco acima, `devolver-livro` e `meus-emprestimos` estão livres para o `/propose` com `emprestar-livro` em `[*]`: as páginas delas podem tirar o que a página de `emprestar-livro` diz.
O `/apply` delas espera até `emprestar-livro` estar integrada, já que uma devolução precisa do código do empréstimo.
`buscar-catalogo` está livre para o `/apply`; `m1-review` espera, com quatro linhas acima dela ainda não definidas, e `aviso-prazo` espera o seu motivo.
A próxima entrega é a primeira linha livre que nenhuma sessão pegou, descendo a fila, seja qual for o comando que ela pede: uma sessão está construindo `emprestar-livro` e outra está definindo `reservas`, e a primeira linha livre descendo a fila que nenhuma delas pegou é `devolver-livro`, livre para o `/propose`, então a próxima entrega de uma sessão nova é `/propose devolver-livro`.
Com um branch ou um worktree por entrega, a sessão roda `git fetch` antes, toma como ocupada uma linha cujo branch existe, e julga as linhas livres e o `after` pela linha de cada slug lida como diz a seção acima, então o `after` de `devolver-livro` lê a marca de `emprestar-livro` no branch de `emprestar-livro`, e a construção de `devolver-livro` espera o merge de `emprestar-livro`, não o `[x]` no branch dela.
Só pela cópia do branch principal, `emprestar-livro` leria `[ ]`, livre e sem nenhuma sessão que a tenha pegado, e a resposta nomearia uma entrega que outra sessão está construindo; o branch de `emprestar-livro` no remoto diz que ela está ocupada antes mesmo de qualquer marca dela ser enviada.
Quando `emprestar-livro` fica integrada, as construções de `devolver-livro` e `meus-emprestimos` ficam livres nesse momento, sem nada para tirar e sem marca para mudar; o `· after` fica na linha como o registro da ordem.
Uma linha com duas ordens, `· after emprestar-livro, membros`, só fica livre para um comando quando as duas o deixam começar.

O fim de um marco define a prioridade, não se uma linha está livre.
A `formato-devolucao` do capítulo 11 fica sob o marco 2, abaixo de `m1-review`, e não nomeia nenhum `after`: ela está livre, e não espera `m1-review`.
Mas a próxima entrega é a primeira linha livre descendo a fila, então uma sessão a quem se pede a próxima só chega a ela quando o marco 1 não tem mais nenhuma linha livre.
Uma linha acrescentada depois vai no marco cujo parágrafo precisa dela, nunca mais acima na fila por ser nova: o lugar dela é a sua prioridade, e as linhas que já estavam lá mantêm a ordem e o `after` delas.

O `/propose` e o `/apply` não começam uma linha que não está livre para eles: quando a página de `meus-emprestimos` estiver completa e a linha dela em `[>]`, rode `/apply meus-emprestimos` com `emprestar-livro` em `[*]`, e ele diz o que a linha espera, deixa a marca como está, e para.

Linhas livres podem rodar ao mesmo tempo quando mexem em arquivos diferentes, julgadas pelas páginas delas e pelo docs/01, que diz onde mora cada parte do código.
`buscar-catalogo` e `reservas`, em `src/features/catalogo/` e `src/features/reservas/`, podem.
Duas linhas que mudam ambas `src/features/emprestimos/`, como fariam `emprestar-livro` e uma linha para renovar um empréstimo, não podem rodar juntas em uma pasta: a segunda construção editaria arquivos que a primeira ainda está mudando.

Em quais arquivos uma construção mexe só se sabe quando a página dela existe, então a fila não diz isso, e a verificação é do `/apply`.
Antes da primeira edição, o `/apply` compara os arquivos em que a página dele mexe com os das construções em andamento, `[*]`, e das construções feitas e ainda não integradas; um arquivo em que as duas mexem é um conflito, e ele para antes de marcar a sua linha `[*]`, nomeia a outra linha e os arquivos que elas dividem, e deixa a marca como está.
A mesma biblioteca, em quatro linhas escritas para este capítulo:

```
[x] membros             o bibliotecário cadastra e suspende membros
[*] emprestar-livro     o bibliotecário empresta um exemplar
[>] buscar-catalogo     um membro busca no catálogo
[>] renovar-emprestimo  um membro renova um empréstimo uma vez
```

Nem `buscar-catalogo` nem `renovar-emprestimo` nomeia um `after`, então as duas estão livres para o `/apply`.
A construção de `buscar-catalogo` mora em `src/features/catalogo/`, em que `emprestar-livro` não mexe, então ela é construída agora.
A página de `renovar-emprestimo` muda `src/features/emprestimos/`, como a de `emprestar-livro`, então `/apply renovar-emprestimo` para antes da primeira edição, diz que divide essa pasta com `emprestar-livro`, e deixa a linha em `[>]`; ela é construída quando `emprestar-livro` estiver integrada.
Um comando digitado com vários slugs faz a mesma verificação para cada linha: `/apply buscar-catalogo renovar-emprestimo` constrói `buscar-catalogo` e relata que `renovar-emprestimo` para nos arquivos de `emprestar-livro`, sem esperar por ela ([capítulo 12](12-propose.md)).

O [capítulo 19](19-worktrees.md) mostra como duas sessões rodam em uma pasta, e quando elas precisam de duas.

## O que pode rodar agora

Perguntado o que pode rodar agora, o agente não lê o fim de cada linha atrás do `after` dela: ele roda o script de fila do kit, `propose/scripts/queue.sh`, em uma linha só, `git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq <estratégia>`, o mesmo truque de alias e a mesma palavra de estratégia do script de reivindicação do [capítulo 13](13-apply.md).
O script lê o docs/06 e não edita nada: no trunk a fila da pasta onde a sessão roda, e com um branch ou um worktree por entrega, depois de um `git fetch`, a linha de cada entrega no branch dela no origin, como diz a seção acima.
Ele desenha o marco atual, o primeiro com uma linha que não está `[x]`, como uma árvore, a árvore da fila: cada linha que ainda não está `[x]`, sob a última linha que ela espera, a que está mais abaixo na fila entre as linhas pendentes que o `after` dela nomeia, com as outras nomeadas depois de `+ after`, e o seu estado.
As palavras do script ficam em inglês, como o kit as imprime, assim como os sufixos.
No trunk, um estado é um destes: em andamento, pelo comando que a marca nomeia, `in flight`; `propose now` ou `apply now`, livre para aquele comando; `waits:`, com o que ela espera; ou `blocked:`, com o seu motivo e o comando que a retoma.
Quando o marco tem uma linha vinda de um achado, mais duas linhas podem vir entre o título e a árvore, `findings:` e um aviso, lidas na seção sobre achados abaixo.
Depois vêm as linhas livres para o `/apply` e para o `/propose`, cada lista na ordem da fila, e por último `next:`, o comando da primeira linha livre descendo a fila.
O marco 1 em seis linhas, escritas para este capítulo como as quatro acima, com `devolver-livro` já definida:

```
[x] catalogo          o bibliotecário cadastra livros e exemplares
[x] membros           o bibliotecário cadastra e suspende membros
[*] emprestar-livro   o bibliotecário empresta um exemplar ou a regra nega
[>] devolver-livro    registra a devolução · after emprestar-livro
[>] buscar-catalogo   um membro busca no catálogo
[ ] m1-review         o marco contra o parágrafo dele · after all
```

Nelas o script imprime isto, o título do marco primeiro:

```
milestone: Marco 1: um bibliotecário empresta e recebe de volta
[*] emprestar-livro · in flight: apply
 └[>] devolver-livro · waits: after emprestar-livro
[>] buscar-catalogo · apply now
 └[ ] m1-review + after emprestar-livro, devolver-livro · propose now

free for /apply, in order: buscar-catalogo
free for /propose, in order: m1-review
next: /apply buscar-catalogo
```

O `└` desenha uma linha sob aquela que ela espera.
A página de `devolver-livro` está completa embora `emprestar-livro` ainda esteja sendo construída, já que a definição dela só precisava da página de `emprestar-livro`; a construção dela espera até `emprestar-livro` estar integrada.
`buscar-catalogo` pode ser construída agora, e `m1-review` fica sob ela, a última linha que o seu `after all` nomeia, com as outras duas depois de `+ after`: toda linha acima dela está definida, então ela pode ser definida agora, e a construção dela espera até todas estarem integradas.
A próxima entrega é `/apply buscar-catalogo`, a primeira linha livre descendo a fila.
Quando uma lista tem mais de uma linha, como nas nove linhas acima, em que o script imprime `free for /propose, in order: devolver-livro meus-emprestimos`, o agente as oferece como um comando, `/propose devolver-livro meus-emprestimos`, dizendo que cada slug é um agente a mais e custa tanto quanto uma sessão ([capítulo 12](12-propose.md)).
O `/propose` e o `/apply` digitados sem slug mostram a mesma árvore e perguntam qual linha pegar, e o `/apply` termina com ela.

## Esperando: `[?]`

Uma linha espera em quatro casos:

* **A pessoa diz que ela está travada.** A biblioteca ainda não comprou os leitores de código de barras, então o bibliotecário pede para segurar `escanear-exemplar`: `· resume: propose · blocked: sem leitores ainda`.
* **Uma resposta foi pedida e não veio.** `aviso-prazo` precisa de um provedor de SMS, a pergunta foi para a diretora da biblioteca, e ninguém respondeu: `· resume: propose · blocked: qual provedor?`.
* **Outra linha precisa ser feita antes, descoberto depois de o trabalho começar.** No meio de `/apply meus-emprestimos`, a construção descobre que `emprestar-livro` põe a data de devolução um dia antes no fim de um mês; a correção vira uma linha `[ ]` acima dela, `corrigir-devolucao`, terminada em `· from meus-emprestimos`, e `meus-emprestimos` espera: `· resume: apply · blocked: after corrigir-devolucao`.
* **A leitura do código de uma revisão de marco não cobriu parte do seu intervalo.** A revisão que fecha um marco lê, com a palavra da pessoa, toda mudança desde a base do marco, dividida em áreas com um leitor cada que lista os caminhos que leu ([capítulo 15](15-closing-a-milestone.md)), e um leitor que leu parte da sua área aponta do mesmo jeito que um que a leu inteira, então quando, no meio de `/apply m1-review`, os leitores da revisão não listam nenhum caminho de `src/features/catalogo/`, a linha espera com o que foi lido como motivo: `· resume: apply · blocked: lidos todos menos catalogo/`.

O motivo vai no fim da linha, em palavras, `· blocked: <motivo>`, ou como as linhas que precisam estar `[x]` antes, `· blocked: after <slug>, <slug>`.
Antes dele vai a fase de retomada, `· resume: propose` para uma linha que estava `[ ]` ou `[~]`, `· resume: apply` para uma que estava `[>]` ou `[*]`, para que a sessão que retoma a linha saiba de qual comando ela precisa.
Qualquer marca antes de `[x]` pode virar `[?]`: uma linha pode esperar antes de alguém defini-la, enquanto a página dela está sendo escrita, ou no meio da construção.

`· after` e `· blocked: after` se parecem e dizem coisas diferentes.
`· after` é uma ordem conhecida quando a linha é escrita: `meus-emprestimos` precisa de empréstimos para mostrar, então foi acrescentada como `[ ] meus-emprestimos ... · after emprestar-livro`, e mantém `[ ]`.
`· blocked: after` é uma espera descoberta depois de o trabalho começar, como foi `corrigir-devolucao`.
Escrever `[?] meus-emprestimos ... · blocked: after emprestar-livro` quando a linha é acrescentada está errado: a linha está na fila, não travada, e em um quadro levaria uma etiqueta de travada que diz a um gerente que algo deu errado quando nada deu.

Uma linha sai de `[?]` quando o motivo se resolve.
A pessoa diz isso; ou a sessão que registra a resposta a tira, como quando a diretora diz o provedor e o nome vira uma linha do docs/00; ou ela sai quando a última linha que o `after` dela nomeia fica integrada, o que no trunk é quando o `/apply` marca essa linha `[x]`.
Os dois sufixos saem, `resume` e `blocked`, e a fase de retomada diz para onde a linha volta.
`aviso-prazo`, com `resume: propose`, volta para `[ ]`, e qualquer rascunho da página dela fica para o `/propose` terminar: um rascunho é uma página começada, não uma definição completa.
Uma linha com `resume: apply` volta para `[>]`.

O `/propose` e o `/apply` param os dois em uma linha `[?]`: dizem o que ela espera, e só seguem depois que o motivo se resolve, por um desses três caminhos.
Um comando que passasse por cima do motivo construiria sobre uma resposta que ninguém deu.

## Uma linha de um achado

Uma entrega lê código que não escreveu, e às vezes acha uma falha ali: o `/propose devolver-livro`, lendo o código de `emprestar-livro`, descobre que um membro suspenso pela tela de membros ainda consegue pegar um livro emprestado: `emprestar` recusa um membro cujo `suspenso` é verdadeiro, como os testes dele provam com um membro construído assim, mas suspender um membro por essa tela registra isso em outro campo, que `buscarMembro` não lê.
Uma falha que uma entrega acha no que ela mesma construiu é corrigida nessa entrega; um achado é uma falha que ela acha em qualquer outro lugar, o `/propose` enquanto define incluído.
Cada achado transformado em linha parece razoável sozinho, e linhas vindas de achados, acrescentadas uma a uma, podem ficar à frente do trabalho que o parágrafo do marco pede, e o marco se enche de reparos enquanto as suas features esperam (o capítulo 13 conta onde isso deu errado).

Então um achado só vira uma linha quando é grave: quebra uma cláusula do parágrafo do marco para uma pessoa no seu caminho de costume, perde ou expõe dados, ou deixa a verificação vermelha; uma correção sem a qual uma entrega em andamento não consegue seguir também é grave, como `corrigir-devolucao` é para `meus-emprestimos`.
Um achado grave vira uma linha `[ ]` terminada em `· from <slug>`, a entrega que o achou, como `corrigir-devolucao` termina em `· from meus-emprestimos` acima; o sufixo `· from` fica em inglês, como os outros.
Um empréstimo a um membro suspenso é um que uma regra deveria negar, passando no caminho de costume do bibliotecário, então `corrigir-suspenso` é grave, e a linha dela termina em `· from devolver-livro`.

O lugar de um achado é a sua prioridade, como o de qualquer linha acrescentada depois, e o trabalho que o parágrafo pediu vem primeiro.
Uma linha planejada é uma linha do marco que não vem de um achado e não é a sua revisão: as linhas que as cláusulas do parágrafo pediram.
Um achado grave vai acima das linhas planejadas abertas só quando a verificação está vermelha ou uma delas precisa dele, como `corrigir-devolucao` fica acima de `meus-emprestimos`, que a nomeia no seu `blocked: after`.
Senão ele vai abaixo delas, acima da revisão, ou sob a revisão depois que ela rodou.
A verificação está verde e nem `devolver-livro` nem `buscar-catalogo` precisam de `corrigir-suspenso`, então ela vai abaixo de `buscar-catalogo`, acima de `m1-review`.

Todo outro achado é uma nota na página da entrega que o achou, sob o título `## For the review` (para a revisão, em inglês como o kit o escreve), acima do bloco `commit` da página, uma linha cada: o arquivo e a linha, e o que uma pessoa veria.
Uma nota escrita para este capítulo, na biblioteca:

```
## For the review

* `src/features/catalogo/busca.ts:41`: um título com acento nunca aparece
```

Uma nota não é uma linha: ela espera a próxima revisão de marco, que a copia para a sua página (o capítulo 15 a classifica).
Um achado que ninguém sabe dizer se é grave é uma nota.

Uma linha que entrega um teste, uma ferramenta de prova ou uma mudança no processo, e não é um achado grave, só entra na fila com a palavra da pessoa; sem ela, é uma nota.
Linhas assim parecem progresso e não entregam nada do que o parágrafo pede: num projeto, em 2026-11-12, uma prova rodada em paralelo, uma prova dividida por estado e auxiliares de teste entraram na fila enquanto as features do projeto esperavam.

O script de fila conta as linhas vindas de achados e avisa quando uma fica à frente do trabalho planejado.
O marco 1 da biblioteca em cinco linhas, escritas para este capítulo, com `corrigir-suspenso` posta acima das linhas planejadas:

```
[x] emprestar-livro   o bibliotecário empresta um exemplar ou a regra nega
[ ] corrigir-suspenso membro suspenso pega livro · from devolver-livro
[>] devolver-livro    registra a devolução · after emprestar-livro
[ ] buscar-catalogo   um membro busca no catálogo
[ ] m1-review         o marco contra o parágrafo dele · after all
```

Estas são as três primeiras linhas que o script imprime nelas; a árvore vem depois, lida como na seção sobre o que pode rodar agora:

```
milestone: Marco 1: um bibliotecário empresta e recebe de volta
findings: 1 open of 1 from a finding · 2 planned open
⚠️ ahead of planned lines: corrigir-suspenso
```

O `findings:` conta as linhas do marco terminadas em `· from <slug>`, depois quantas delas estão abertas, uma linha de achado já `[x]` ficando só no primeiro número, depois as linhas planejadas abertas; a revisão e uma linha cancelada não entram na conta.
O aviso nomeia `corrigir-suspenso`, uma linha de achado aberta à frente de `devolver-livro` e de `buscar-catalogo`, embora nenhuma das duas precise dela, e a árvore termina com `next: /propose corrigir-suspenso`: o reparo vem antes do trabalho planejado.
Movida para baixo de `buscar-catalogo`, acima de `m1-review`, a linha não fica mais à frente e o aviso some, o `findings:` fica como está, e o `next:` é `/apply devolver-livro`.
Uma linha de achado que uma linha aberta nomeia no seu `after` ou `blocked: after` fica fora do aviso: `corrigir-devolucao`, que `meus-emprestimos` nomeia, fica acima porque uma linha planejada precisa dela.
O aviso é um olhar, não um veredito: um achado que deixa a verificação vermelha fica à frente e também avisa, e a pessoa lê qual dos dois ele é, um de que a verificação precisa ou um que deveria descer.
Como o `/apply` termina com a árvore, o desvio aparece no fim de toda construção sem ninguém pedir.

## Uma sessão que terminou, uma entrega cancelada

Uma sessão pode terminar sem que ninguém trave a linha dela: o host fecha, a conexão cai, o limite do plano chega.
A linha mantém a sua marca.
`reservas` continua `[~]` depois que a conversa que a definia termina; nada espera por ninguém, então ela não vira `[?]`.
A marca sozinha não diz que a sessão terminou: uma linha `[~]` ou `[*]` está com uma sessão, e essa sessão pode estar conversando agora mesmo em outra pasta ou em outra máquina.
Então uma sessão nova não toma a linha só porque vê a marca; a pessoa, que sabe que a sessão terminou, diz isso e roda `/propose reservas` de novo.
O comando então inspeciona a página, a pasta de trabalho e o índice antes de editar, e segue do que a conversa anterior escreveu.
`emprestar-livro`, em `[*]` quando a construção dela perdeu a conexão, é retomada do mesmo jeito com `/apply emprestar-livro`: os arquivos já construídos e o que já está no índice continuam da entrega, e a linha continua `[*]`, nunca devolvida a `[>]` ou `[ ]` como se nada tivesse sido feito; nenhum dos dois comandos retomados marca a sua linha de novo, e o script de marca recusaria um segundo `[~]` ou `[*]` nela.

Uma entrega que a pessoa cancela, porque o trabalho provou que é impossível, porque foi recusada, ou porque ninguém a quer mais, também fica na fila.
Ela termina `[x]` com o motivo no fim da linha, `· dropped: <motivo>`, e a página dela vai para `work/done/` como qualquer outra, dizendo o que foi construído e o que foi desfeito, ou que nada foi construído.
A biblioteca queria que o bibliotecário imprimisse o cartão de um membro pelo navegador, e a impressora de cartões se mostrou sem um driver que o navegador alcançasse; o bibliotecário cancela a linha, e `reimprimir-cartao`, acrescentada depois dela, espera por ela, em duas linhas escritas para este capítulo:

```
[x] imprimir-cartao    imprime o cartão de membro · dropped: sem driver
[ ] reimprimir-cartao  reimprime um cartão perdido · after imprimir-cartao
```

`[x]` sozinho diz que a promessa da entrega vale, com a verificação verde; `[x]` com `· dropped:` diz que a decisão foi tomada e que a promessa não existe.
Quem o põe é a pessoa, não o `/apply`, porque cancelar é uma decisão de escopo, e a linha fica para que ninguém pergunte depois se `imprimir-cartao` foi esquecida.
Só pela regra de linha livre, a construção de `reimprimir-cartao` fica livre quando `imprimir-cartao` está `[x]`, e essa é a armadilha: o `[x]` que ela nomeia é uma decisão, não uma impressora de cartões que funciona.
Então uma linha cujo `after` nomeia uma entrega cancelada cabe à pessoa redecidir: cancelá-la também, como seria `reimprimir-cartao`, ou reescrevê-la sobre o que existe.

A revisão de um marco não teria uma boa saída.
Uma revisão que nomeasse toda linha acima dela nomearia também a cancelada e esperaria, como `reimprimir-cartao` espera, por uma linha que só a decisão da pessoa libera; e das saídas da pessoa, cancelar a revisão perde o teste do parágrafo do marco, e reescrevê-la sobre o que existe troca o `after all` dela por uma lista de todas as outras linhas acima dela.
Em 2026-10-26, num projeto, a revisão de um Marco 1 esperou uma linha que a pessoa tinha cancelado: o script de fila respondia `after <slug>, dropped: re-decide`, e o `after all` da revisão foi trocado por uma lista dos outros 27 slugs.
Então o `after all` não nomeia nenhuma linha cancelada: ele é toda linha acima da revisão no seu marco menos as canceladas, e as deixa de fora.
Suponha que as duas linhas acima, escritas para este capítulo, fiquem no marco 1 da biblioteca, acima de `m1-review`.
O `after all` deixa `imprimir-cartao` de fora, então a linha cancelada nunca faz a revisão esperar.
`reimprimir-cartao` não está cancelada, então o `after all` a conta: a árvore da fila a imprime com `waits: after imprimir-cartao, dropped: re-decide`, e a revisão espera com ela até a pessoa redecidir `reimprimir-cartao`.
Cancelada também, ela sai do `after all` da revisão; reescrita sobre o que existe, a revisão espera por ela como por qualquer outra linha.

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
Ele lê o docs/06 e as páginas em `work/` pelo slug, no trunk nos arquivos da própria pasta e com um branch ou um worktree por entrega no branch de cada slug no origin, depois de um `git fetch`, com as linhas que só um branch tem, e move os cartões conforme cada marca fica visível para ele enquanto o agente trabalha.

## O que o time ganha

Um gerente lê onde cada entrega está, e o que cada uma em espera espera, sem perguntar a ninguém e sem reunião de status.
No Caso A, cinco linhas travadas no cliente pareciam trabalho parado, e cada entrega só chegava a Doing depois de a definição dela ter acabado, contado pelo autor na fila e no quadro do projeto; uma marca posta quando o trabalho muda, e uma para a espera, respondem aos dois.
Um pedido que se provou impossível ali foi encerrado na fila com o seu motivo em vez de deixado em silêncio ([capítulo 23](23-adoption.md)), e o kit escreve um encerramento assim como `[x]` com `· dropped:`, e uma linha encerrada assim não faz nenhuma revisão esperar.

A fila também diz quais linhas podem rodar juntas: sem isso, uma pessoa que quer duas sessões tem de descobrir sozinha antes de abrir a segunda; a árvore da fila desenha isso pela fila, sem reunião, cada linha sob o que ela espera, e termina com o comando a rodar em seguida, e o `/apply` verifica os arquivos antes da primeira edição, então duas construções nunca mudam o mesmo arquivo ao mesmo tempo.
A árvore também diz quanto do marco veio de achados e nomeia uma linha de achado à frente do trabalho planejado, então o desvio aparece no dia em que começa; e um achado que não é grave espera na página da sua entrega pela revisão em vez de entrar na fila.
E nenhuma sessão marcando a sua linha consegue deixar a fila vazia sob o quadro e as outras sessões, nem duas sessões que começam uma mesma linha conseguem ambas construí-la: uma marca é um byte, mudado inteiro ou não mudado, e um começo numa linha já ocupada é recusado.

## Pontos-chave

* Seis marcas, `[ ]` não definida, `[~]` sendo definida, `[>]` completamente definida e pronta para o `/apply`, `[*]` sendo construída, `[x]` feita, `[?]` esperando, cada uma mudada quando o trabalho muda, não quando um comando termina: o `/propose` põe `[~]` e `[>]`, o `/apply` põe `[*]` e `[x]`, a pessoa põe `[x]` com `· dropped: <motivo>` ao cancelar, qualquer sessão põe `[?]`; toda marca muda pelo script de marca do kit, um byte, `[~]` só numa linha `[ ]` e `[*]` só numa `[>]`, o `[x]` do `/apply` colocado em stage só na sua linha com `stage`, e toda outra edição da fila é a edição de arquivo do host nas linhas dela, nunca um programa que escreve o arquivo inteiro; uma linha cuja sessão terminou mantém a sua marca, e o seu comando a retoma com a palavra da pessoa, inspecionando antes a página, a pasta e o índice, e a página de uma entrega cancelada em `work/done/` diz o que foi construído e desfeito.
* Uma linha está livre para um comando quando não está `[x]` nem `[?]` e o `after` dela deixa esse comando começar: o `/propose` quando toda linha que ele nomeia está `[>]` ou além, o `/apply` quando todas estão integradas, `[x]` no trunk, com merge no branch principal com um branch ou um worktree por entrega; o `· after all` da linha da revisão nomeia toda linha acima dela no seu marco menos as canceladas, e uma linha cujo `after` nomeia uma cancelada cabe à pessoa redecidir; com um branch ou um worktree por entrega, uma linha cujo branch existe depois de um `git fetch` está ocupada, mostre o que mostrar o branch principal; a próxima entrega é a primeira linha livre que nenhuma sessão pegou, e antes da primeira edição o `/apply` para em um arquivo que uma construção em andamento ou ainda não integrada está mudando.
* Perguntado o que pode rodar agora, o agente roda o script de fila do kit e mostra a árvore dele: o marco atual, com o `findings:` e o seu aviso `⚠️` sob o título quando o marco tem uma linha vinda de um achado, cada linha que não está `[x]` sob a última linha que ela espera com o seu estado, depois as linhas livres para o `/apply` e para o `/propose`, na ordem, e o `next:`, o comando da primeira; ele oferece as linhas livres como um comando com vários slugs, cada slug um agente a mais que custa tanto quanto uma sessão, e o `/propose` e o `/apply` digitados sem slug mostram a árvore e perguntam.
* `· after` é uma ordem escrita com a linha, que mantém a sua marca; `[?]` com `· blocked: after` é uma espera descoberta depois de o trabalho começar; uma linha espera quando a pessoa diz, quando uma resposta foi pedida e não veio, quando o trabalho já começado descobre que outra linha precisa ser feita antes, ou quando a leitura do código de uma revisão de marco não cobriu parte do seu intervalo, com a fase de retomada e o motivo no fim, `· resume: apply · blocked: after <slug>`; quando o motivo se resolve, os dois sufixos saem e ela volta conforme essa fase, `resume: propose` para `[ ]` com qualquer rascunho mantido, `resume: apply` para `[>]`, e até lá o `/propose` e o `/apply` param nela, como numa linha que não está livre; um achado grave é uma linha `[ ]` terminada em `· from <slug>`, acima das linhas planejadas abertas só quando a verificação está vermelha ou uma delas precisa dele, todo outro achado uma nota sob `## For the review` na página da entrega que o achou, e uma linha que entrega um teste, uma ferramenta de prova ou uma mudança no processo só entra com a palavra da pessoa.
* A fila é um quadro kanban, uma coluna por marca, um cartão `[?]` em Esperando até voltar a `[ ]` ou `[>]`; nas três colunas deste capítulo, Fazendo guarda `[~]`, `[>]` e `[*]`, e um cartão `[?]` é etiquetado como travado na coluna que a sua fase de retomada nomeia, A fazer para `propose`, Fazendo para `apply`; um quadro que lê a fila vê uma marca na hora no trunk, e com um branch ou um worktree por entrega pela linha de cada slug no branch dele no origin, depois de um `git fetch`, enviado quando o `/propose` o cria, já que o branch principal mostra a linha como ela estava até o merge.

[^toyota-kanban]: Toyota Motor Corporation, "75 Years of Toyota", Part 2, Chapter 1, Section 4, Item 4, "Development and Deployment of the Toyota Production System", acesso em 2026-10-05. <https://www.toyota-global.com/company/history_of_toyota/75years/text/entering_the_automotive_business/chapter1/section4/item4.html>
[^azure-kanban]: Microsoft Learn, "About Kanban boards", Azure Boards, acesso em 2026-09-30. <https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview>
