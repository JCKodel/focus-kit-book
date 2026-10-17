# 19. Worktrees e agentes em paralelo

Depois deste capítulo você consegue rodar dois agentes ao mesmo tempo em uma pasta, no trunk, em linhas livres cujos arquivos não se encontram, dizer o que é e o que não é um conflito ali, e fazer o commit de cada entrega sozinha.
Você também consegue dizer quando ainda compensa dar a cada entrega um worktree (uma árvore de trabalho), uma segunda pasta de trabalho do mesmo repositório no seu próprio branch, organizá-lo como o kit lhe dá forma, uma pasta contêiner com `main/` e uma pasta oculta, construir em worktrees, resolver o conflito quando dois branches mexeram nas mesmas linhas, pegar um marcador de conflito antes que ele entre em um commit, e dizer quando trabalhar em paralelo deixa de compensar.

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
As duas marcam o docs/06, a fila, mas cada uma marca a sua própria linha, e duas linhas distantes em um arquivo são dois hunks, pedaços separados de uma mudança que o git coloca em stage separadamente.
Então as duas podem rodar em uma pasta ao mesmo tempo.

Cada sessão se atém à sua entrega:

* ela muda a marca da sua própria linha na fila, e de nenhuma outra;
* ela coloca em stage só os seus próprios caminhos, e só o seu próprio hunk do docs/06 (`git add -p` coloca um arquivo em stage hunk por hunk);
* ela não mexe em nada que a outra sessão mudou ou colocou em stage.

O commit continua seu, uma entrega por vez.
Antes de fazer o commit de `devolver-livro`, veja o que está em stage:

```
git diff --cached --stat
```

Ele lista cada arquivo em stage e quantas das suas linhas mudam.
Se a lista guarda só `src/features/emprestimos/`, a página de `devolver-livro` e o docs/06, e `git diff --cached docs/06-Queue.md` mostra só o hunk daquela linha, um `git commit` simples leva aquela entrega e nada mais.
Se ela também guarda `src/features/relatorios/` ou a página de `lista-de-atrasos`, a outra sessão também colocou o seu trabalho em stage, e um commit simples leva as duas.

A armadilha é nomear caminhos.
`git commit -- docs/06-Queue.md src/features/emprestimos/` parece o jeito seguro de fazer o commit de uma entrega, e para arquivos que só aquela entrega mudou, é.
Para um arquivo que as duas mudaram, ele leva demais: a documentação do git diz que um commit com caminhos é feito "*pegando o conteúdo atualizado da árvore de trabalho dos caminhos dados na linha de comando, ignorando qualquer conteúdo que tenha sido colocado em stage para outros caminhos.*"[^git-commit]
Então o git pega o docs/06 inteiro da pasta, com a marca da outra linha, em stage ou não, e essa marca entra neste commit.

A saída é a ordem.
Faça o commit de cada entrega quando a sua sessão termina, antes que a outra coloque qualquer coisa em stage.
Se a outra já colocou, tire as entradas dela do stage você mesmo, `git restore --staged <os caminhos dela>` e `git restore --staged -p docs/06-Queue.md` para o hunk dela na fila, faça o commit, e deixe a sessão dela colocá-las em stage de novo; uma sessão nunca mexe nas entradas da outra.

## O que é e o que não é um conflito ali

Em uma pasta, cada sessão vê o trabalho da outra enquanto ele acontece, e quase nada dele é motivo para parar:

* a marca de outra linha muda no docs/06, de `[~]` para `[*]`, por exemplo;
* a página de outra entrega aparece em `work/`, ou os arquivos dela na árvore;
* as entradas de outra entrega já estão em stage.

Cada um é trabalho da outra sessão: a sessão segue, e não mexe em nada disso.
Isso está escrito porque, sem isso, uma segunda sessão em outro módulo para quando a primeira muda o docs/06, embora tenha tudo de que precisa para seguir.

Duas coisas são um conflito:

* as duas entregas editam o mesmo hunk, as mesmas linhas de `src/features/emprestimos/regras.ts`, por exemplo;
* esta página precisa de um arquivo que a outra entrega está mudando, como quando `devolver-livro` precisa de `src/features/emprestimos/` enquanto outra entrega o reorganiza.

Então a sessão para e relata, e a decisão é sua: ordenar as duas linhas, escrevendo `· after <slug>` na que precisa esperar a outra, ou dar a uma delas um worktree.

## O que é um worktree e quando ele compensa

Um worktree é uma pasta de trabalho extra do mesmo repositório git, com o seu próprio branch.
Nas palavras da documentação do git: "*Um repositório git pode ter várias árvores de trabalho, o que permite fazer checkout de mais de um branch ao mesmo tempo.*"[^git-worktree]
A pasta que você clonou é o worktree principal, aquele cuja pasta `.git` guarda o histórico: os commits, os branches e as tags.
`git worktree add` cria outra pasta, faz checkout de um branch nela, e deixa lá um pequeno arquivo `.git` que aponta de volta para onde o histórico mora.
Todos os worktrees compartilham o histórico; cada um tem os seus próprios arquivos, o seu próprio `HEAD` (o commit em que ele está) e a sua própria área de stage.[^git-worktree]
Então um commit feito em um worktree aparece na hora em todos os outros, sem push e sem pull, enquanto o que você muda ou coloca em stage em um nunca aparece em outro.
O git também se recusa a fazer checkout de um branch em dois worktrees, então duas pastas nunca escrevem no mesmo branch.[^git-worktree]

Um worktree por entrega compensa em dois casos: várias pessoas trabalhando ao mesmo tempo, já que um commit em um branch compartilhado levaria o trabalho pela metade de outra pessoa; e uma pessoa cujas entregas mexem nos mesmos arquivos, para que cada uma seja construída à parte e as suas mudanças só se encontrem no merge.
Um branch por entrega em uma pasta não basta: a pasta guarda um branch por vez, e trocar de branch enquanto um agente tem trabalho ainda sem commit leva esse trabalho junto ou para até o `git stash` guardá-lo de lado.
Um segundo clone dá a cada agente a sua própria pasta, mas com a sua própria cópia do histórico inteiro no disco, que só encontra a do outro por um push e um pull.

Digamos que `devolver-livro` e `lista-de-atrasos` precisam as duas de `src/features/emprestimos/`, na pasta da biblioteca de empréstimos, `biblioteca/`, cujo `main/` guarda o branch `main` (a próxima seção a monta):

* O agente que constrói `devolver-livro` trabalha em `biblioteca/.focus-kit/worktrees/devolver-livro`, no branch `focus-kit/devolver-livro`; ele vê só as mudanças dessa entrega, e o commit que você faz ali guarda essa entrega e nada mais.
* O agente que constrói `lista-de-atrasos` faz o mesmo em `biblioteca/.focus-kit/worktrees/lista-de-atrasos`, no `focus-kit/lista-de-atrasos`, ao mesmo tempo.
* Ninguém troca de branch, então nada precisa de stash, e nenhum agente vê os arquivos pela metade do outro.

Quando uma entrega está pronta, você a traz para o `main` a partir de `main/` com um commit de merge, `git merge --no-ff`, para que ela continue uma unidade de trabalho, desfeita em um passo com `git revert -m 1 <merge>`.

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

Depois você trabalha dentro da pasta como em qualquer outra: o agente constrói, você revisa e faz o commit ali.
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
O `/propose <slug>` cria o worktree em `<oculta>/worktrees/<slug>/` no branch `<prefixo>/<slug>`, a partir do `HEAD` do branch principal, ou reaproveita o que existe, e escreve a página ali.
Um branch `<slug>` sem o prefixo não é o da entrega: é de outra pessoa.
Você monta o contêiner uma vez; o kit cria cada worktree.
O `/apply <slug>` roda em uma sessão nova aberta naquela pasta, constrói a página, e coloca a mudança em stage.
Você revisa e faz o commit no branch, faz o merge no `main` com `--no-ff`, remove o worktree e apaga o branch.

O agente nunca faz commit, merge, resolve um conflito ou remove um worktree: cada passo que muda o histórico é seu, como em toda estratégia de git.
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
[x] devolver-livro     a bibliotecária registra que um exemplar voltou
[ ] lista-de-atrasos   a bibliotecária vê os empréstimos vencidos
=======
[ ] devolver-livro     a bibliotecária registra que um exemplar voltou
[x] lista-de-atrasos   a bibliotecária vê os empréstimos vencidos
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

## Quando o paralelo deixa de compensar

Em uma pasta ou em worktrees, duas entregas ao mesmo tempo ainda compartilham tudo o que não está nos seus próprios arquivos.
Antes de começar duas, confira cinco coisas.

**A fila.** Em uma pasta ela não dá conflito: cada sessão marca a sua própria linha e coloca em stage o seu próprio hunk.
Entre worktrees ela sempre dá conflito no merge, já que cada entrega marca a sua linha, e se resolve do mesmo jeito toda vez: guarde as duas marcas.

**Arquivos que as duas mudam.** Um arquivo de código que duas entregas mudam é diferente.
Em uma pasta a sessão para quando encontra a mudança da outra; entre worktrees o merge para, e resolvê-lo é uma decisão sobre o código: quem a toma precisa entender as duas mudanças.
Então junte entregas cujos arquivos não se encontram: leia cada linha da fila, o docs/01 e o código que ela nomeia, e liste os arquivos que cada uma vai tocar.

**Portas e bancos de dados compartilhados.** Duas sessões compartilham a máquina nas duas formas: as suas portas, um banco de dados de teste em uma pasta comum.
Em uma pasta elas também compartilham a própria pasta, o seu banco de dados de teste e a saída do seu build.
Duas execuções de teste que sobem um servidor na mesma porta, ou escrevem no mesmo banco, colidem, e uma falha por um motivo que não tem nada a ver com o seu código.
Uma porta ou um banco de dados por sessão é uma escolha que o projeto pode fazer, em uma entrega própria.

**Dependências.** Uma pasta as instala uma vez.
Cada worktree instala as suas, então cada um custa tanto disco quanto a pasta principal, e a instalação leva o seu tempo de novo.

**Você.** Os agentes trabalham em paralelo; a sua revisão não.
Você lê cada página e cada mudança em stage, faz o commit e o merge, uma entrega por vez, então rode ao mesmo tempo só tantas entregas quantas você consegue revisar.
Este livro, escrito e revisado por uma pessoa em arquivos compartilhados, fica no trunk por esses motivos, e o seu docs/05 deixa duas sessões trabalharem em uma pasta em linhas livres que mexem em arquivos diferentes.

## O que o time ganha

Dois agentes constroem ao mesmo tempo, e cada entrega ainda chega como uma mudança que se desfaz sozinha: um commit em uma pasta, um merge a partir de um worktree.
Eu medi isso uma vez, em worktrees, em um pequeno projeto meu em TypeScript: duas entregas construídas ao mesmo tempo levaram 155 segundos do primeiro início ao último fim, contra 277,2 segundos de trabalho dos agentes somados, ao custo de uma pasta `node_modules` em cada worktree, duas execuções de teste que colidiram uma vez em uma porta compartilhada, e o conflito da fila no merge.[^parallel-run]
O ganho vale enquanto os arquivos das entregas não se encontram, e termina na velocidade da pessoa que as revisa e faz o commit delas.

## Pontos-chave

* Duas sessões dividem uma pasta no trunk quando as suas linhas estão livres e os seus arquivos não se encontram: cada uma marca só a sua linha, coloca em stage só os seus caminhos e o seu hunk da fila, e você faz o commit de uma entrega por vez.
* A marca de outra linha, a página ou os arquivos de outra entrega e as entradas em stage de outra sessão não são conflito; o mesmo hunk editado pelas duas, ou um arquivo de que uma página precisa e que a outra está mudando, é: pare, e então ordene as linhas ou dê a uma delas um worktree.
* Faça o commit a partir do stage quando `git diff --cached --stat` guarda só aquela entrega; `git commit -- <caminhos>` pega cada arquivo nomeado inteiro da pasta, com o hunk da outra entrega em um arquivo compartilhado.
* Um worktree por entrega compensa para várias pessoas, ou para entregas que mexem nos mesmos arquivos: uma pasta contêiner cujo `main/` é o checkout guarda o worktree de cada entrega em `<oculta>/worktrees/<slug>/` no `<prefixo>/<slug>`, `.focus-kit/` e `focus-kit/` por padrão; `git worktree add`, trabalhe ali, `git merge --no-ff` em `main/`, `git worktree remove`, `git branch -d`; um conflito deixa as duas versões entre marcadores, e `git diff --cached --check` pega qualquer um que sobrou antes do commit.
* O paralelo compensa enquanto os arquivos das entregas não se encontram, as portas e os bancos de dados da máquina não colidem, o disco comporta as dependências de cada worktree, e uma pessoa ainda consegue revisar cada entrega.

[^git-commit]: Git, "git-commit", a documentação, opção `--only`, acesso em 2026-10-13. <https://git-scm.com/docs/git-commit>
[^git-clone]: Git, "git-clone", a documentação, opção `--bare`, acesso em 2026-10-16. <https://git-scm.com/docs/git-clone>
[^git-worktree]: Git, "git-worktree", a documentação, acesso em 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^git-merge]: Git, "git-merge", a documentação, seção "How conflicts are presented" e opção `--abort`, acesso em 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", a documentação, opção `--check`, acesso em 2026-09-30. <https://git-scm.com/docs/git-diff>
[^parallel-run]: J.C. Ködel, "One Page at a Time", o registro de duas entregas construídas em paralelo em dois worktrees, 2026-09-30, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-worktrees-run>
