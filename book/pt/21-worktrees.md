# 21. Worktrees e agentes em paralelo

Depois deste capítulo você consegue rodar dois agentes ao mesmo tempo em uma pasta, no trunk, em linhas livres cujos arquivos não se encontram, dizer o que é e o que não é um conflito ali, e fazer o commit de cada entrega sozinha.
Você também consegue dizer quando um worktree por entrega ainda compensa, construir em worktrees, resolver o conflito quando dois branches mexeram nas mesmas linhas, pegar um marcador de conflito antes que ele entre em um commit, e dizer quando trabalhar em paralelo deixa de compensar.

## O problema: uma pasta, dois trabalhos

Um agente leva minutos para construir uma entrega, e enquanto ele trabalha você espera.
O movimento natural é começar um segundo agente na próxima entrega, em uma segunda sessão, na mesma pasta.
Muitas vezes isso funciona: os dois agentes escrevem arquivos diferentes, e cada entrega ainda chega como o seu próprio commit.
Dá errado em dois casos.

Se as duas entregas mudam as mesmas linhas de um arquivo, ou uma precisa de um arquivo que a outra está mudando, cada agente constrói em cima do trabalho pela metade do outro, e nenhuma das entregas pode ser revisada ou desfeita sozinha.

Se um commit leva as duas entregas, uma delas talvez pela metade, nenhum `git revert` sozinho consegue desfazê-las separadamente.
A unidade de trabalho do [capítulo 20](20-git-essentials.md), uma entrega que se desfaz em um passo, se perdeu, e separar as duas depois significa escolher mudanças arquivo por arquivo, linha por linha, à mão.

O primeiro caso se evita escolhendo quais entregas rodam juntas; o segundo, pelo jeito de fazer o commit.

## Duas sessões em uma pasta

Duas sessões podem dividir uma pasta quando constroem linhas livres que mexem em arquivos diferentes.
Uma linha livre é uma linha da fila que não está pronta, não está esperando, e não precisa de outra linha pronta antes ([o capítulo 16](16-queue-states.md) ensina as marcas da fila).

Digamos que a biblioteca de empréstimos tem duas linhas livres: `devolver-livro`, que mexe em `src/emprestimos/`, e `lista-de-atrasos`, que mexe em `src/relatorios/`; os slugs e os caminhos são uma ilustração, escrita para este capítulo.
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
Se a lista guarda só `src/emprestimos/`, a página de `devolver-livro` e o docs/06, e `git diff --cached docs/06-Queue.md` mostra só o hunk daquela linha, um `git commit` simples leva aquela entrega e nada mais.
Se ela também guarda `src/relatorios/` ou a página de `lista-de-atrasos`, a outra sessão também colocou o seu trabalho em stage, e um commit simples leva as duas.

A armadilha é nomear caminhos.
`git commit -- docs/06-Queue.md src/emprestimos/` parece o jeito seguro de fazer o commit de uma entrega, e para arquivos que só aquela entrega mudou, é.
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
O changelog do kit, na entrada 2026.10.08.3, conta por que isso foi escrito: um usuário rodou duas sessões em um repositório, em módulos diferentes, e a segunda parou porque a primeira tinha mudado o docs/06, quando tinha tudo de que precisava para seguir.

Duas coisas são um conflito:

* as duas entregas editam o mesmo hunk, as mesmas linhas de `src/emprestimos/emprestimo.ts`, por exemplo;
* esta página precisa de um arquivo que a outra entrega está mudando, como quando `devolver-livro` precisa de `src/emprestimos/` enquanto outra entrega o reorganiza.

Então a sessão para e relata, e a decisão é sua: ordenar as duas linhas, escrevendo `· after <slug>` na que precisa esperar a outra, ou dar a uma delas um worktree.

## Quando um worktree ainda compensa

Uma pasta guarda um branch por vez, e todos que trabalham nela dividem os seus arquivos.
Então um worktree por entrega compensa em dois casos: várias pessoas trabalhando ao mesmo tempo, já que um commit em um branch compartilhado levaria o trabalho pela metade de outra pessoa; e uma pessoa cujas entregas mexem nos mesmos arquivos, para que cada uma seja construída à parte e as suas mudanças só se encontrem no merge.

Só branches não bastam.
Se você dá a cada entrega o seu próprio branch em uma pasta, a pasta ainda guarda só um branch por vez.
Trocar de branch enquanto um agente tem trabalho ainda sem commit ou leva esse trabalho para o outro branch ou faz o git recusar até você guardá-lo de lado com `git stash`; e dois agentes não conseguem estar em dois branches de uma pasta no mesmo momento.

Um segundo clone do repositório dá a cada agente a sua própria pasta, mas cada clone tem a sua própria cópia do histórico: os dois só se encontram dando push para um remoto e pull dele, e cada clone repete o histórico inteiro no disco.

O que você quer então são várias pastas, cada uma no seu próprio branch, compartilhando um histórico.
Isso é um worktree (uma árvore de trabalho).

## O que é um worktree

Um worktree é uma pasta de trabalho extra do mesmo repositório git, com o seu próprio branch.
Nas palavras da documentação do git: "*Um repositório git pode ter várias árvores de trabalho, o que permite fazer checkout de mais de um branch ao mesmo tempo.*"[^git-worktree]

A pasta que você clonou é o worktree principal.
Ela guarda a pasta `.git`, onde o histórico mora: os commits, os branches e as tags.
`git worktree add` cria outra pasta, faz checkout de um branch nela, e deixa lá um pequeno arquivo `.git` que aponta de volta para o principal.
Todos os worktrees compartilham o histórico; cada um tem os seus próprios arquivos, o seu próprio `HEAD` (o commit em que ele está) e a sua própria área de stage.[^git-worktree]
Então um commit feito em um worktree aparece na hora em todos os outros, sem push e sem pull, enquanto o que você muda ou coloca em stage em um nunca aparece em outro.
O git também se recusa a fazer checkout de um branch em dois worktrees, então duas pastas nunca escrevem no mesmo branch.[^git-worktree]

## Como ele resolve o problema

Dê a cada entrega o seu próprio worktree, e a cada agente a sua própria pasta.
Digamos que `devolver-livro` e `lista-de-atrasos` precisam as duas de `src/emprestimos/`:

* O agente que constrói `devolver-livro` trabalha em `../biblioteca-devolver-livro`, no branch `devolver-livro`; ele vê só as mudanças dessa entrega, e o commit que você faz ali guarda essa entrega e nada mais.
* O agente que constrói `lista-de-atrasos` faz o mesmo em `../biblioteca-lista-de-atrasos`, ao mesmo tempo.
* Ninguém troca de branch, então nada precisa de stash, e nenhum agente vê os arquivos pela metade do outro.

Quando uma entrega está pronta, você a traz para o `main` a partir da pasta principal com um commit de merge, `git merge --no-ff`, para que ela continue uma unidade de trabalho, desfeita em um passo com `git revert -m 1 <merge>`.

## A vida de um worktree

Seis passos, rodados na pasta principal, exceto onde o texto diz outra coisa.

```
git worktree add ../biblioteca-devolver-livro -b devolver-livro main
```

Cria a pasta `../biblioteca-devolver-livro`, cria o branch `devolver-livro` no `main`, e faz checkout dele na pasta.

Depois você trabalha dentro da pasta como em qualquer outra: o agente constrói, você revisa e faz o commit ali.
Só o que o git acompanha está na pasta nova: dependências como `node_modules` não estão, então você as instala em cada worktree (`npm ci` em um projeto Node).

```
git worktree list
```

Imprime cada worktree, o commit em que ele está e o seu branch.

```
git merge --no-ff devolver-livro
```

No `main`, na pasta principal, traz a entrega como um commit de merge; os commits do branch já aparecem ali, já que o histórico é compartilhado.

```
git worktree remove ../biblioteca-devolver-livro
```

Apaga a pasta.
Ele se recusa a apagar uma pasta com arquivos mudados ou não acompanhados, então trabalho sem commit nunca se perde por acidente.[^git-worktree]

```
git branch -d devolver-livro
```

Apaga o branch, que sobrevive à sua pasta.
`-d` apaga só um branch que já passou por merge; `-D` o apaga mesmo assim.

## Worktrees no kit

Um worktree por entrega é uma das estratégias de git que um projeto pode escrever no slot Git do seu docs/05, e no kit são os passos acima com o `/propose` e o `/apply` no meio.
O `/propose <slug>` cria o worktree com o nome do slug, `../<project>-<slug>` em um branch `<slug>` a partir do `main`, e escreve a página ali.
O `/apply <slug>` roda em uma sessão nova aberta naquela pasta, constrói a página, e coloca a mudança em stage.
Você revisa e faz o commit no branch, faz o merge no `main` com `--no-ff`, remove o worktree e apaga o branch.

O agente nunca faz commit, merge, resolve um conflito ou remove um worktree: cada passo que muda o histórico é seu, como em toda estratégia de git.
Para rodar duas entregas ao mesmo tempo em worktrees, abra uma sessão por pasta: uma na pasta principal para cada `/propose`, uma em cada worktree para o seu `/apply`.

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
>>>>>>> lista-de-atrasos
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

Ele lê o que está em stage e relata cada marcador de conflito como `<file>:<line>: leftover conflict marker`, e termina com código diferente de zero quando acha um, então um script consegue parar nele.[^git-diff]

Se os marcadores entraram em um commit mesmo assim, o jeito de desfazer depende de alguém mais ter o commit.
Sem push: `git reset --hard <the commit before the merge>` joga o merge fora, e você faz o merge de novo.
Com push: `git revert`, já que um reset reescreve um histórico que outros já têm, o que é a regra do rebase do capítulo 20.

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
Eu medi isso uma vez, em um pequeno projeto meu em TypeScript: duas entregas construídas ao mesmo tempo por dois agentes levaram 155 segundos do primeiro início ao último fim, contra 277,2 segundos de trabalho dos agentes somados, pouco mais da metade da espera.[^parallel-run]
A mesma execução pagou os custos da seção acima: o `node_modules` de cada worktree ocupou 155 MB de disco, e as duas execuções de teste colidiram uma vez em uma porta compartilhada e passaram quando rodadas de novo; a fila deu conflito, como sempre dá.[^parallel-run]
Essa execução foi em worktrees.
Uma pasta tira a segunda pasta, a segunda instalação de 155 MB, o merge e o conflito da fila; nenhuma execução mediu duas sessões em uma pasta, então esse ganho não tem número próprio.
A regra do que não é conflito tira o erro que o changelog do kit registra: uma segunda sessão que parou numa fila mudada quando tinha tudo de que precisava para seguir.
Uma execução é um sinal, não uma taxa: o ganho vale enquanto os arquivos das entregas não se encontram, e termina na velocidade da pessoa que as revisa e faz o commit delas.

## Pontos-chave

* Duas sessões dividem uma pasta no trunk quando as suas linhas estão livres e os seus arquivos não se encontram: cada uma marca só a sua linha, coloca em stage só os seus caminhos e o seu hunk da fila, e você faz o commit de uma entrega por vez.
* A marca de outra linha, a página ou os arquivos de outra entrega e as entradas em stage de outra sessão não são conflito; o mesmo hunk editado pelas duas, ou um arquivo de que uma página precisa e que a outra está mudando, é: pare, e então ordene as linhas ou dê a uma delas um worktree.
* Faça o commit a partir do stage quando `git diff --cached --stat` guarda só aquela entrega; `git commit -- <paths>` pega cada arquivo nomeado inteiro da pasta, com o hunk da outra entrega em um arquivo compartilhado.
* Um worktree por entrega compensa para várias pessoas, ou para entregas que mexem nos mesmos arquivos: `git worktree add`, trabalhe ali, `git merge --no-ff` na pasta principal, `git worktree remove`, `git branch -d`; um conflito deixa as duas versões entre marcadores, e `git diff --cached --check` pega qualquer um que sobrou antes do commit.
* O paralelo compensa enquanto os arquivos das entregas não se encontram, as portas e os bancos de dados da máquina não colidem, o disco comporta as dependências de cada worktree, e uma pessoa ainda consegue revisar cada entrega.

[^git-commit]: Git, "git-commit", a documentação, opção `--only`, acesso em 2026-10-13. <https://git-scm.com/docs/git-commit>
[^git-worktree]: Git, "git-worktree", a documentação, acesso em 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^git-merge]: Git, "git-merge", a documentação, seção "How conflicts are presented" e opção `--abort`, acesso em 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", a documentação, opção `--check`, acesso em 2026-09-30. <https://git-scm.com/docs/git-diff>
[^parallel-run]: J.C. Ködel, "One Page at a Time", o registro de duas entregas construídas em paralelo em dois worktrees, 2026-09-30, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-worktrees-run>
