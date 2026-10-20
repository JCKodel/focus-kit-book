# 19. Worktrees e agentes em paralelo

Depois deste capítulo você consegue rodar dois agentes ao mesmo tempo em uma pasta, no trunk, em linhas livres cujos arquivos não se encontram, dizer o que é e o que não é um conflito ali, e fazer o commit de cada entrega sozinha.
Você também consegue dizer quando ainda compensa dar a cada entrega um worktree (uma árvore de trabalho), uma segunda pasta de trabalho do mesmo repositório no seu próprio branch, organizá-lo como o kit lhe dá forma, uma pasta contêiner com `main/` e uma pasta oculta, construir em worktrees, resolver o conflito quando dois branches mexeram nas mesmas linhas, pegar um marcador de conflito antes que ele entre em um commit, e dizer quando trabalhar em paralelo deixa de compensar.
E consegue rodar vários `/propose` ao mesmo tempo nas respostas recomendadas do agente, ler em cada página o que ele decidiu sem você antes de qualquer `/apply`, e dizer por que todo commit continua sendo decisão sua.

## O problema: uma pasta, dois trabalhos

Um agente leva minutos para construir uma entrega, e enquanto ele trabalha você espera.
O movimento natural é começar um segundo agente na próxima entrega, em uma segunda sessão, na mesma pasta.
Muitas vezes isso funciona: os dois agentes escrevem arquivos diferentes, e cada entrega ainda chega como o seu próprio commit.
Dá errado em dois casos.

Se as duas entregas mudam as mesmas linhas de um arquivo, ou uma precisa de um arquivo que a outra está mudando, cada agente constrói em cima do trabalho pela metade do outro, e nenhuma das entregas pode ser revisada ou desfeita sozinha.

Se um commit leva as duas entregas, uma delas talvez pela metade, nenhum `git revert` sozinho consegue desfazê-las separadamente.
A unidade de trabalho do [capítulo 18](18-git-essentials.md), uma entrega que se desfaz em um passo, se perdeu, e separar as duas depois significa escolher mudanças arquivo por arquivo, linha por linha, à mão.

O primeiro caso se evita escolhendo quais entregas rodam juntas; o segundo, pelo jeito de fazer o commit.

## Duas sessões em uma pasta

Duas sessões podem dividir uma pasta quando constroem linhas livres que mexem em arquivos diferentes.
Uma linha livre é uma linha da fila que não está feita, não está esperando, e não precisa de outra linha feita antes ([o capítulo 14](14-queue-states.md) ensina as marcas da fila).

Digamos que a biblioteca de empréstimos tem duas linhas livres: `devolver-livro`, que mexe em `src/features/emprestimos/`, e `lista-de-atrasos`, que mexe em `src/features/relatorios/`; os slugs e os caminhos são uma ilustração, escrita para este capítulo.
Os arquivos de código delas não se encontram.
As duas marcam o docs/06, a fila, mas cada uma marca só a sua própria linha.
O `git add -p` oferece um arquivo para o stage em hunks, pedaços separados de uma mudança: duas linhas distantes são dois hunks, duas linhas vizinhas são um, e cada sessão ainda coloca em stage só a sua própria linha (a seção do lote mostra como).
Então as duas podem rodar em uma pasta ao mesmo tempo.

Cada sessão se atém à sua entrega:

* ela muda a marca da sua própria linha na fila, e de nenhuma outra;
* ela coloca em stage só os seus próprios caminhos, e só a sua própria linha do docs/06;
* ela não mexe em nada que a outra sessão mudou ou colocou em stage.

O commit continua sendo decisão sua, uma entrega por vez, por padrão depois que você a usou e leu o que ela colocou em stage.
Antes de fazer o commit de `devolver-livro`, veja o que está em stage:

```
git diff --cached --stat
```

Ele lista cada arquivo em stage e quantas das suas linhas mudam: ele nomeia arquivos, e não diz nada de quem são as linhas que um arquivo compartilhado guarda.
Então uma lista com só `src/features/emprestimos/`, a página de `devolver-livro` e o docs/06 não resolve o docs/06, que as duas sessões mudam; `git diff --cached docs/06-Queue.md` resolve, e quando ele mostra só a linha de `devolver-livro`, um `git commit` simples leva aquela entrega e nada mais.
Se a lista também guarda `src/features/relatorios/` ou a página de `lista-de-atrasos`, ou o diff em stage da fila guarda a linha de `lista-de-atrasos`, a outra sessão também colocou o seu trabalho em stage, e um commit simples leva as duas.

Uma pasta tem um só índice, no qual as duas sessões colocam em stage, então um commit leva o que qualquer uma delas colocou em stage ([capítulo 18](18-git-essentials.md)).
Então não faça o commit ainda: ele espera até o índice guardar só a entrega que você revisou.
A sessão que encontrou as entradas da outra já em stage avisou você e as deixou como estavam; nenhuma sessão tira as entradas da outra.
O caminho comum para um índice de uma entrega só é a ordem: faça o commit de cada entrega quando a sua sessão termina, antes que a outra coloque qualquer coisa em stage.
Se as duas já estão em stage, arrumar o índice é com você: `git restore --staged <os caminhos dela>` tira os arquivos da outra do índice e os deixa na pasta.
A fila não se divide com `s` quando as duas linhas são vizinhas, já que `git restore --staged -p` divide um hunk como o `git add -p` divide;[^git-restore] então `git restore --staged docs/06-Queue.md` tira o arquivo inteiro, você pede à sessão desta entrega que coloque a sua própria linha em stage de novo, e faz o commit.
Depois a outra sessão coloca as suas entradas em stage de novo, quando você pedir.

A armadilha é nomear caminhos.
`git commit -- docs/06-Queue.md src/features/emprestimos/` parece o jeito de fazer o commit de uma entrega, e nunca é um jeito de escolher uma.
Um `git commit` simples pega o índice: uma linha que a outra sessão mudou e não colocou em stage está na pasta, não no índice, então fica fora do commit.
Um commit com caminhos pega a pasta: a documentação do git diz que ele é feito "*pegando o conteúdo atualizado da árvore de trabalho dos caminhos dados na linha de comando, ignorando qualquer conteúdo que tenha sido colocado em stage para outros caminhos.*"[^git-commit]
Então o git pega o docs/06 inteiro da pasta, com a marca da outra linha, em stage ou não, e essa marca entra neste commit.
Você escolhe uma entrega pelo índice e confere com `git diff --cached`, nunca com caminhos no `git commit`.

## O que é e o que não é um conflito ali

Em uma pasta, cada sessão vê o trabalho da outra enquanto ele acontece, e quase nada dele é motivo para parar:

* a marca de outra linha muda no docs/06, de `[~]` para `[*]`, por exemplo;
* a página de outra entrega aparece em `work/`, ou os arquivos dela na árvore;
* as entradas de outra entrega já estão em stage;
* duas linhas vizinhas do docs/06, uma de cada entrega, que o git põe em um hunk: cada sessão coloca em stage a sua própria linha, e compartilhar um hunk não é compartilhar nenhuma linha.

Cada um é trabalho da outra sessão: a sessão segue, e não mexe em nada disso.
Isso está escrito porque, sem isso, uma segunda sessão em outro módulo para quando a primeira muda o docs/06, embora tenha tudo de que precisa para seguir.

Duas coisas são um conflito:

* as duas entregas editam a mesma linha, de `src/features/emprestimos/regras.ts`, por exemplo, ou da fila;
* esta página precisa de um arquivo que a outra entrega está mudando, como quando `devolver-livro` precisa de `src/features/emprestimos/` enquanto outra entrega o reorganiza.

Então a sessão para e relata, e a decisão é sua: ordenar as duas linhas, escrevendo `· after <slug>` na que precisa esperar a outra, ou dar a uma delas um worktree.

## O que é um worktree e quando ele compensa

Um worktree é uma pasta de trabalho extra do mesmo repositório git, com o seu próprio branch.
Nas palavras da documentação do git: "*Um repositório git pode ter várias árvores de trabalho, o que permite fazer checkout de mais de um branch ao mesmo tempo.*"[^git-worktree]
A pasta que você clonou é o worktree principal, aquele cuja pasta `.git` guarda o histórico: os commits, os branches e as tags.
`git worktree add` cria outra pasta, faz checkout de um branch nela, e deixa lá um pequeno arquivo `.git` que aponta de volta para onde o histórico mora.
Todos os worktrees compartilham o histórico; cada um tem os seus próprios arquivos, o seu próprio `HEAD` (o commit em que ele está) e o seu próprio índice, aquele em que toda sessão aberta naquela pasta coloca em stage.[^git-worktree]
Então um commit feito em um worktree aparece na hora em todos os outros, sem push e sem pull, enquanto o que você muda ou coloca em stage em um nunca aparece em outro.
O git também se recusa a fazer checkout de um branch em dois worktrees, então duas pastas nunca escrevem no mesmo branch.[^git-worktree]

Um worktree por entrega compensa em dois casos: várias pessoas trabalhando ao mesmo tempo, já que um commit em um branch compartilhado levaria o trabalho pela metade de outra pessoa; e uma pessoa cujas entregas mexem nos mesmos arquivos, para que cada uma seja construída à parte e as suas mudanças só se encontrem no merge.
Um branch por entrega em uma pasta não basta: a pasta guarda um branch por vez, e trocar de branch enquanto um agente tem trabalho ainda sem commit leva esse trabalho junto ou para até o `git stash` guardá-lo de lado.
Um segundo clone dá a cada agente a sua própria pasta, mas com a sua própria cópia do histórico inteiro no disco, que só encontra a do outro por um push e um pull.

Digamos que `devolver-livro` e `lista-de-atrasos` precisam as duas de `src/features/emprestimos/`, na pasta da biblioteca de empréstimos, `biblioteca/`, cujo `main/` guarda o branch `main` (a próxima seção a monta):

* O agente que constrói `devolver-livro` trabalha em `biblioteca/.focus-kit/worktrees/devolver-livro`, no branch `focus-kit/devolver-livro`; ele vê só as mudanças dessa entrega, e o commit que você faz ali guarda essa entrega e nada mais.
* O agente que constrói `lista-de-atrasos` faz o mesmo em `biblioteca/.focus-kit/worktrees/lista-de-atrasos`, no `focus-kit/lista-de-atrasos`, ao mesmo tempo.
* Ninguém troca de branch, então nada precisa de stash, e nenhum agente vê os arquivos pela metade do outro.

Quando uma entrega está pronta, por padrão você a traz para o `main` a partir de `main/`, ou pede ao agente que o faça, com um commit de merge, `git merge --no-ff`, para que ela continue uma unidade de trabalho, desfeita em um passo com `git revert -m 1 <merge>`.

## A vida de um worktree

Primeiro, uma vez por clone, o contêiner: uma pasta que guarda o checkout, `main/`, e uma pasta oculta, `.focus-kit/`, com o histórico e o worktree de cada entrega.
Os comandos, a pasta e os slugs foram escritos para este capítulo, na biblioteca de empréstimos.
A partir de uma pasta vazia `biblioteca/`:

```
git clone --bare <url> .focus-kit/repo.git
```

Copia o histórico do remoto para `.focus-kit/repo.git`, um repositório bare: um repositório sem arquivos próprios, só com o histórico.[^git-clone]
Então nenhuma pasta de trabalho guarda o histórico, e toda pasta de trabalho, `main/` incluída, é um worktree do repositório bare.

```
cd .focus-kit/repo.git
git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
```

Escreve a linha de fetch que um clone bare deixa de fora: sem ela, o `git fetch` em `main/` não traz nenhum `origin/main`, o registro do git de onde está o `main` do remoto.

```
git worktree add ../../main main
```

Rodado dentro de `.focus-kit/repo.git`, cria `biblioteca/main/` no branch `main`: o checkout, um worktree como os outros, cujo `.git` é um arquivo que aponta para `.focus-kit/repo.git`.
`git worktree list` agora imprime duas linhas, uma terminando em `biblioteca/.focus-kit/repo.git` marcada `(bare)`, outra terminando em `biblioteca/main` em `[main]`.

Um projeto que escolhe isso escreve esses passos em um manual de `docs/manuals/` ([capítulo 7](07-the-documents.md)), para que quem o clonar depois monte o mesmo contêiner.

Depois, seis passos, rodados em `main/`, exceto onde o texto diz outra coisa.
Um caminho dado ao `git worktree add` é relativo à pasta em que você está, então o mesmo comando rodado em outro lugar põe a pasta em outro lugar; a partir de `main/`, `../.focus-kit/worktrees/<slug>` cai dentro do contêiner.

```
git worktree add ../.focus-kit/worktrees/devolver-livro \
  -b focus-kit/devolver-livro main
```

Cria a pasta `biblioteca/.focus-kit/worktrees/devolver-livro`, cria o branch `focus-kit/devolver-livro` no `main`, e faz checkout dele na pasta.
A pasta fica na pasta oculta, ao lado de `main/`, então nenhum dos arquivos de `main/` a mostra.

Depois você trabalha dentro da pasta como em qualquer outra: o agente constrói, você usa o que ele construiu, revisa e, por padrão, faz o commit ali, ou pede ao agente que o faça; pela palavra do slot Git o agente faz o commit ali e você revisa o commit.
Só o que o git acompanha está na pasta nova: dependências como `node_modules` não estão, então você as instala em cada worktree (`npm ci` em um projeto Node).

```
git worktree list
```

Imprime cada worktree, o commit em que ele está e o seu branch.

```
git merge --no-ff focus-kit/devolver-livro
```

No `main`, em `main/`, traz a entrega como um commit de merge; os commits do branch já aparecem ali, já que o histórico é compartilhado.

```
git worktree remove ../.focus-kit/worktrees/devolver-livro
```

Apaga a pasta.
Ele se recusa a apagar uma pasta com arquivos mudados ou não acompanhados, então trabalho sem commit nunca se perde por acidente.[^git-worktree]

```
git branch -d focus-kit/devolver-livro
```

Apaga o branch, que sobrevive à sua pasta.
`-d` apaga só um branch que já passou por merge; `-D` o apaga mesmo assim.

## Worktrees no kit

Um worktree por entrega é uma das estratégias de git que um projeto pode escrever no slot Git do seu docs/05, e no kit são os passos acima com o `/propose` e o `/apply` no meio.
O slot pode nomear a pasta oculta e o prefixo do branch, e um que não nomeia nenhum dos dois vale `.focus-kit/` e `focus-kit/`, os de acima; um slot que nomeia `.wt/` e `wt/` põe `devolver-livro` em `.wt/worktrees/devolver-livro/` no `wt/devolver-livro`.
Os dois nomes do kit dizem o que criou a pasta e o branch, então quem os encontra em um projeto sabe de onde vieram.
O `/propose <slug>` consulta o remoto por `<prefixo>/<slug>`, cria o worktree em `<oculta>/worktrees/<slug>/` nesse branch, a partir do `HEAD` do branch principal, e dá push no branch na hora, então a linha fica ocupada em todo clone, ou, quando a definição é retomada, reaproveita o worktree e o branch que existem, e escreve a página ali.
O `[~]` da linha e cada marca seguinte são escritos no worktree, no seu branch, então a fila de `main/` mostra a linha como estava e a fila de cada worktree mostra o estado do seu próprio branch; o merge traz as marcas, e é por isso que a fila se encontra em todo merge, como a próxima seção, sobre conflitos, mostra.
O [capítulo 14](14-queue-states.md) diz onde um quadro as vê.
Um branch `<slug>` sem o prefixo não é o da entrega: é de outra pessoa.
Você monta o contêiner uma vez; o kit cria cada worktree.
O `/apply <slug>` roda em uma sessão nova aberta naquela pasta, constrói a página, e coloca a mudança em stage.
Por padrão, você usa a entrega, revisa e faz o commit no branch, faz o merge no `main` com `--no-ff`, remove o worktree e apaga o branch.

Quando o `/apply devolver-livro` trava no seu worktree esperando uma resposta que ninguém deu, ele para como o capítulo 13 diz: marca a linha `[?]` com `· resume: apply · blocked: e se o exemplar voltar danificado?`, escreve na página o que foi construído, e mostra uma mensagem parcial em um bloco `commit`.
Ali ele também pode colocar o trabalho parcial em stage para você fazer o commit no `focus-kit/devolver-livro` quando quiser, com essa mensagem: ela diz que é parcial, nomeia o que trava, nunca dá a entender que a verificação passou ou que a entrega está pronta, e a sua última linha é `work/devolver-livro.md`, onde a página espera.
Por padrão, esse commit é a única exceção a usar a entrega antes de fazer o commit dela: um commit de trabalho inacabado cuja mensagem diz isso; o commit que completa a entrega continua vindo depois de você usar a entrega inteira e ler o seu diff em stage.
Enquanto a linha está `[?]`, não faça o merge do branch, quem quer que peça: ele fica sem merge até a entrega estar pronta, então um só `git merge --no-ff` ainda leva a entrega inteira ao `main`.
Quando o `/apply` é retomado no mesmo worktree, uma pasta de trabalho limpa não quer dizer que nada foi construído: o trabalho até ali está nesses commits, e a revisão da entrega os lê contra a base do branch (capítulo 13).
No trunk não há commit parcial: um `/apply` travado não coloca nada em stage, e o trabalho fica sem commit até estar inteiro.

O agente nunca faz commit, merge ou push, nem resolve um conflito ou remove um worktree por conta própria, fora o branch em que o `/propose` dá push quando o cria, a reivindicação da linha: cada passo que muda o histórico é decisão sua, como em toda estratégia de git; para o commit e o merge, o slot Git pode dizer que o agente os faz pela palavra do slot, que vale como o pedido, e você então revisa o commit ou o merge ([capítulo 7](07-the-documents.md)); todo push depois desse, o conflito e o worktree continuam esperando o seu pedido.
Peça, e ele dá qualquer um desses passos por você: escreve a mensagem de commit, resolve o conflito, faz o commit, o merge ou o push, remove o worktree, e conhece os comandos que desfazem um passo, como `git merge --abort` para um merge parado por um conflito ou `git revert` para uma entrega a desfazer.
Por padrão, cada passo vem depois da sua leitura: peça o commit quando você tiver usado a entrega e o diff em stage tiver só ela, o commit de merge quando o arquivo resolvido não tiver nenhum marcador de conflito, e o push quando o `git log` mostrar o que vai sair.
Depois de um merge que ele fez, `git log --oneline --graph -3` em `main/` mostra o commit de merge e o branch que ele trouxe.
Para rodar duas entregas ao mesmo tempo em worktrees, abra uma sessão por pasta: uma em `main/` para cada `/propose`, uma em cada worktree para o seu `/apply`.

O kit dá essa forma única a toda ferramenta e toda pessoa por causa de um erro: um `/propose` rodando em um worktree que outra ferramenta criou, numa pasta própria, escreve a página onde o próximo `/apply` não procura.

## Quando os branches se encontram: o conflito

Os worktrees mantêm as entregas separadas enquanto são construídas; o merge as junta, e o git combina os dois lados linha por linha.
Se os dois branches mudaram as mesmas linhas, ou linhas vizinhas, o git não tem como saber qual manter: ele faz o merge de todas as outras mudanças, para antes do commit de merge, e deixa o arquivo para você.
Isso é um conflito.[^git-merge]
Um conflito é sobre linhas, não sobre arquivos: dois branches que mudam o mesmo arquivo em pontos distantes entram por merge sozinhos.

No arquivo em conflito, o git escreve as duas versões entre marcadores de conflito: `<<<<<<<` abre a versão do branch em que você está, `=======` a separa da versão do branch que está entrando, e `>>>>>>>` fecha essa.[^git-merge]
Cada entrega marca a sua própria linha na fila, então duas entregas cujas linhas são vizinhas sempre se encontram ali.
Aqui o merge de `devolver-livro` foi feito primeiro, e `lista-de-atrasos` entra em segundo; o bloco é uma ilustração, escrita para este capítulo:

```text
<<<<<<< HEAD
[x] devolver-livro     o bibliotecário registra que um exemplar voltou
[ ] lista-de-atrasos   o bibliotecário vê os empréstimos vencidos
=======
[ ] devolver-livro     o bibliotecário registra que um exemplar voltou
[x] lista-de-atrasos   o bibliotecário vê os empréstimos vencidos
>>>>>>> focus-kit/lista-de-atrasos
```

Acima de `=======` está o `main`, onde `devolver-livro` está pronta; abaixo está `lista-de-atrasos`, onde a sua própria linha está pronta.
Nenhum dos lados está certo sozinho; a versão certa guarda o que os dois fizeram, as duas linhas em `[x]`.

Para resolver, edite o arquivo até essa versão e apague as três linhas de marcador; então `git add` diz ao git que o arquivo está resolvido, e `git commit --no-edit` faz o commit de merge com a mensagem que o git preparou:

```
git add docs/06-Queue.md
git commit --no-edit
```

Se você prefere não resolver agora, `git merge --abort` sai do merge e deixa o branch como estava antes.[^git-merge]

## A armadilha: fazer commit dos marcadores

`git add` é como você diz ao git que um conflito está resolvido, e o git acredita na sua palavra.
Coloque o arquivo em stage com os marcadores ainda dentro, faça o commit, e o commit de merge guarda os marcadores, sem nenhum aviso.
Isso acontece com mais facilidade quando os comandos do merge rodam como um bloco só, e o add e o commit rodam antes que alguém tenha tocado no arquivo.

A proteção é um comando, antes do commit do merge:

```
git diff --cached --check
```

Ele lê o que está em stage e relata cada marcador de conflito como `<arquivo>:<linha>: leftover conflict marker`, e termina com código diferente de zero quando acha um, então um script consegue parar nele.[^git-diff]

Se os marcadores entraram em um commit mesmo assim, o jeito de desfazer depende de alguém mais ter o commit.
Sem push: `git reset --hard <o commit antes do merge>` joga o merge fora, e você faz o merge de novo.
Com push: `git revert`, já que um reset reescreve um histórico que outros já têm, o que é a regra do rebase do capítulo 18.

## Propor em lote

Tudo acima roda o `/apply` em paralelo.
Um `/propose` parece mais lento, e o tempo vai para você, respondendo às suas perguntas, as horas de uma pessoa que, como o [capítulo 22](22-cost-and-where.md) mostra, nenhuma contagem de tokens vê.
Quando você mesmo conseguiria responder a cada uma dessas perguntas, dá para levar esse tempo para uma leitura só, em vez de gastá-lo em cada conversa.

Isso é um lote: uma sessão por linha, cada uma rodando `/propose <slug>`, e cada uma instruída, na conversa, a seguir a sua própria recomendação onde perguntaria.
O kit não tem comando para isso e não precisa de um.
O `/propose` já pergunta com a sua recomendação primeiro, e escreve na página cada decisão que toma com o documento de onde ela veio (capítulo 12); o processo do kit pede que toda escolha feita em seu nome fique explícita na página.
O lote apenas responde às suas perguntas de antemão.

Cada página então lista as perguntas que respondeu sozinha: a pergunta, a resposta escolhida e o porquê, e o documento que a deixou em aberto.
Aqui está essa lista na página de `lista-de-atrasos`, escrita para este capítulo:

```
**Decidido sem você.**

1. Ordem da lista: mais dias de atraso primeiro. O docs/00 não
   diz; recomendado, já que o bibliotecário cobra primeiro o
   empréstimo mais antigo.
2. Um exemplar devolvido hoje sai da lista na hora. O docs/00 não
   diz; recomendado, para a lista nunca mostrar um livro já de volta.
```

Cada item dá a pergunta, a resposta e o seu motivo, e nomeia o docs/00 como o documento que a deixou em aberto; o título é do projeto, que o nomeia como quiser, já que o kit fixa as seções da página e não esta.
Uma página que não respondeu nada sozinha diz isso, ou não traz lista.

O lote leva as suas decisões para a leitura e não tira nenhuma delas.
Antes do primeiro `/apply`, leia cada página, esta lista primeiro, e corrija cada uma na sua própria conversa.

A recomendação cobre só uma pergunta que os documentos deixam em aberto e que você conseguiria responder.
Uma pergunta que pertence a outra pessoa, um cliente ou a diretora da biblioteca, nunca é respondida por uma recomendação: a página vai até onde consegue, e a linha espera como `[?]` com `· resume: propose`, como `aviso-prazo` espera em `· blocked: qual provedor?` no capítulo 14.
O Caso A deu a uma pergunta assim uma linha própria, uma entrega de pergunta, cujo único resultado é uma resposta escrita; ela é uma customização do próprio Caso A, não um passo do kit (capítulo 20).

Páginas escritas ao mesmo tempo não leem umas às outras.
O `/propose` lê as entregas em andamento em `work/` quando começa, e uma página sendo escrita ao mesmo tempo ainda não está lá: duas páginas podem decidir a mesma pergunta de dois jeitos, ou cada uma pedir ao docs/03 o mesmo termo novo.
Você encontra isso lendo as páginas lado a lado, e corrige uma delas na sua conversa.

Cada `/propose` escreve a sua página e a marca da sua linha e não coloca nada em stage: a proposta fica na pasta, sem commit, e o que o índice já guardava fica como estava.
Nem é preciso um commit para passar a página adiante: o `/apply` que a constrói, na mesma pasta, lê a página e a marca da pasta, como estão.
As linhas de um lote ficam lado a lado na fila, então o git põe as suas marcas em um hunk do docs/06.
Esse hunk não guarda conflito: nenhuma linha dele é mudada por duas sessões, e a mudança de cada sessão é a marca da sua própria linha, que a lista do que não é conflito nomeia.
Nem é motivo para colocar nada em stage enquanto as páginas estão sendo escritas.

Os `/apply` que vêm depois não acrescentam regra própria: rodam ao mesmo tempo só em linhas livres cujos arquivos não se encontram, e cada commit é decisão sua, uma entrega por vez.
Cada `/apply` coloca a sua entrega em stage quando termina: a sua página, o que construiu e a sua linha da fila, e as outras propostas ficam fora do stage, na pasta.
É aí que o hunk compartilhado conta, e quem coloca em stage a marca de uma linha é a sessão dona dela, nunca você.
O `git add -p` não consegue fazer isso aqui: ele divide um hunk com `s` só onde uma linha sem mudança separa duas mudanças, e o `e` dele abre o hunk em um editor, que uma sessão não opera.[^git-add]
Então a sessão escreve um patch, o texto que o `git diff` imprime para uma mudança, com só o `-` e o `+` da sua própria linha, um ao lado do outro, e as outras linhas como estão no índice (a cópia em stage de onde o commit é feito), sem mudança, em volta deles.
Ela entrega esse patch ao `git apply --cached`, que o aplica só ao índice e deixa os arquivos da pasta como estão.[^git-apply]
Antes de cada commit, `git diff --cached docs/06-Queue.md` mostra só as mudanças desta entrega, o `-` e o `+` da sua linha lado a lado, e nenhuma mudança de outra sessão.
Se o índice já guardava entradas de outra sessão, a sessão avisa você e as deixa como estavam, e o commit espera até o índice guardar só esta entrega, como mais acima neste capítulo.

Pedir um passo não é entregar o lote.
Depois que você usou e revisou uma entrega, e o índice guarda só ela, os seus arquivos no `git diff --cached --stat` e só a sua linha no `git diff --cached docs/06-Queue.md`, você pode pedir à sessão dela que faça o commit; a entrega seguinte espera o seu próprio uso, a sua própria revisão e o seu próprio índice.
Quando os agentes fazem o commit de um lote de `/apply` antes que você o tenha lido, isso custa quatro coisas, seja por conta própria, o que sai do método, seja pela palavra do slot Git.
Um commit deixa de dizer que uma pessoa leu a mudança, que é o que ele diz no [capítulo 13](13-apply.md).
Em uma pasta, o commit de um agente leva o que outra sessão colocou em stage, ou, com caminhos, o docs/06 compartilhado inteiro: a armadilha de nomear caminhos, no começo deste capítulo.
Ler muitas mudanças depois que elas entraram em commits é a condição do viés de automação (capítulos 13 e 24).
E uma entrega errada sobre a qual as seguintes construíram se desfaz com um conflito onde quer que elas tenham mudado as suas linhas (capítulo 18).

## Quando o paralelo deixa de compensar

Em uma pasta ou em worktrees, duas entregas ao mesmo tempo ainda compartilham tudo o que não está nos seus próprios arquivos.
Antes de começar duas, confira cinco coisas.

**A fila.** Em uma pasta ela não dá conflito: cada sessão marca a sua própria linha, e cada `/apply` coloca em stage só essa linha, esteja ela no mesmo hunk que a da outra ou não.
Entre worktrees ela sempre dá conflito no merge, já que cada entrega marca a sua linha, e se resolve do mesmo jeito toda vez: guarde as duas marcas.

**Arquivos que as duas mudam.** Um arquivo de código que duas entregas mudam é diferente.
Em uma pasta a sessão para quando encontra a mudança da outra; entre worktrees o merge para, e resolvê-lo é uma decisão sobre o código: quem a toma precisa entender as duas mudanças.
Então liste os arquivos que cada entrega vai tocar, a partir da sua linha da fila, do docs/01 e do código que ela nomeia: entregas cujos arquivos não se encontram podem dividir uma pasta; entregas cujos arquivos se encontram rodam ao mesmo tempo só em worktrees, e só quando você consegue tomar a decisão do merge; senão, ordene-as com `· after <slug>`.

**Portas e bancos de dados compartilhados.** Duas sessões compartilham a máquina nas duas formas: as suas portas, um banco de dados de teste em uma pasta comum.
Em uma pasta elas também compartilham a própria pasta, o seu banco de dados de teste e a saída do seu build.
Duas execuções de teste que sobem um servidor na mesma porta, ou escrevem no mesmo banco, colidem, e uma falha por um motivo que não tem nada a ver com o seu código.
Uma porta ou um banco de dados por sessão é uma escolha que o projeto pode fazer, em uma entrega própria.

**Dependências.** Uma pasta as instala uma vez.
Cada worktree instala as suas, então cada um custa tanto disco quanto a pasta principal, e a instalação leva o seu tempo de novo.

**Você.** Os agentes trabalham em paralelo; a sua revisão não.
Você lê cada página, usa cada entrega, lê a mudança em stage dela e decide cada commit e cada merge, uma entrega por vez, então rode ao mesmo tempo só tantas entregas quantas você consegue revisar; um lote de `/propose` leva essa leitura para uma leitura só e não a encurta.
Este livro, escrito e revisado por uma pessoa em arquivos compartilhados, fica no trunk por esses motivos, e o seu docs/05 deixa duas sessões trabalharem em uma pasta em linhas livres que mexem em arquivos diferentes.

## O que o time ganha

Dois agentes constroem ao mesmo tempo, e cada entrega ainda chega como uma mudança que se desfaz sozinha no git, e o que ela fez fora do git fica por conta da sua página (capítulo 18): um commit em uma pasta, um merge a partir de um worktree.
Eu medi isso uma vez, em worktrees, em um pequeno projeto meu em TypeScript: duas entregas construídas ao mesmo tempo levaram 155 segundos do primeiro início ao último fim, contra 277,2 segundos de trabalho dos agentes somados, ao custo de uma pasta `node_modules` em cada worktree, duas execuções de teste que colidiram uma vez em uma porta compartilhada, e o conflito da fila no merge.[^parallel-run]
A medição é de duas entregas cujos arquivos de código não se encontravam; o ganho termina na velocidade da pessoa que as revisa e decide os commits e os merges delas.
O `/propose` em lote leva o paralelo para a definição: os agentes escrevem as páginas enquanto você está fora, e cada página traz as decisões que tomou sozinha, listadas para a sua única leitura.

## Pontos-chave

* Duas sessões dividem uma pasta no trunk quando as suas linhas estão livres e os seus arquivos não se encontram: cada uma marca só a sua linha, coloca em stage só os seus caminhos e a sua linha da fila, e você decide cada commit, uma entrega por vez.
* A marca de outra linha, a página ou os arquivos de outra entrega e as entradas em stage de outra sessão não são conflito; nem duas linhas vizinhas da fila em um hunk; uma linha editada pelas duas, ou um arquivo de que uma página precisa e que a outra está mudando, é: pare, e então ordene as linhas ou dê a uma delas um worktree.
* Uma pasta tem um só índice, então faça o commit a partir dele quando ele guarda só aquela entrega: `git diff --cached --stat` nomeia arquivos, então leia também o diff em stage de um arquivo compartilhado, pelas suas linhas; com outra entrega em stage, espere; e nunca escolha uma entrega com `git commit -- <caminhos>`, que pega cada arquivo nomeado inteiro da pasta, com as linhas da outra entrega em um arquivo compartilhado, em stage ou não.
* Um worktree por entrega compensa para várias pessoas, ou para entregas que mexem nos mesmos arquivos: uma pasta contêiner cujo `main/` é o checkout guarda o worktree de cada entrega em `<oculta>/worktrees/<slug>/` no `<prefixo>/<slug>`, `.focus-kit/` e `focus-kit/` por padrão; `git worktree add`, trabalhe ali, `git merge --no-ff` em `main/`, `git worktree remove`, `git branch -d`; cada worktree tem o seu próprio índice, o `/propose` dá push no branch quando o cria, a reivindicação da linha, e as marcas da linha ficam no branch até o merge; um `/apply` travado ali pode colocar o seu trabalho parcial em stage para você fazer o commit no branch, que fica sem merge até a entrega estar pronta; um conflito deixa as duas versões entre marcadores, e `git diff --cached --check` pega qualquer um que sobrou antes do commit.
* O paralelo compensa enquanto os arquivos das entregas não se encontram, ou só se encontram entre worktrees cujo merge você consegue decidir, as portas e os bancos de dados da máquina não colidem, o disco comporta as dependências de cada worktree, e uma pessoa ainda consegue revisar cada entrega; o `/propose` pode rodar em lote nas respostas recomendadas, sem colocar nada em stage, cada página listando o que decidiu sozinha para você ler antes de qualquer `/apply`, cada `/apply` colocando a sua própria entrega em stage, e todo commit continua sendo decisão sua, feito por você ou pedido ao agente depois da sua revisão, ou dada uma vez no slot Git, com cada commit ou merge revisado depois que entra.

[^git-commit]: Git, "git-commit", a documentação, opção `--only`, acesso em 2026-10-13. <https://git-scm.com/docs/git-commit>
[^git-clone]: Git, "git-clone", a documentação, opção `--bare`, acesso em 2026-10-16. <https://git-scm.com/docs/git-clone>
[^git-worktree]: Git, "git-worktree", a documentação, acesso em 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^git-merge]: Git, "git-merge", a documentação, seção "How conflicts are presented" e opção `--abort`, acesso em 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", a documentação, opção `--check`, acesso em 2026-09-30. <https://git-scm.com/docs/git-diff>
[^git-add]: Git, "git-add", a documentação, seção "Interactive mode", acesso em 2026-10-18. <https://git-scm.com/docs/git-add>
[^git-restore]: Git, "git-restore", a documentação, opção `--patch`, acesso em 2026-10-18. <https://git-scm.com/docs/git-restore>
[^git-apply]: Git, "git-apply", a documentação, opção `--cached`, acesso em 2026-10-18. <https://git-scm.com/docs/git-apply>
[^parallel-run]: J.C. Ködel, "One Page at a Time", o registro de duas entregas construídas em paralelo em dois worktrees, 2026-09-30, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-worktrees-run>
