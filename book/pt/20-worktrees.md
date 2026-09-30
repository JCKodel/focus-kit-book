# Worktrees e agentes em paralelo

Depois deste capítulo você consegue pôr dois agentes para construir duas entregas ao mesmo tempo, cada um na sua própria pasta, para que cada merge guarde uma entrega e nada mais.
Você também consegue resolver o conflito quando os dois mexeram nas mesmas linhas, pegar um marcador de conflito antes que ele entre em um commit, e dizer quando trabalhar em paralelo deixa de compensar.

## O problema: uma pasta, dois trabalhos

Um agente leva minutos para construir uma entrega, e enquanto ele trabalha você espera.
O movimento natural é começar um segundo agente na próxima entrega, e em uma pasta isso dá errado de um de dois jeitos.

Se os dois agentes trabalham no mesmo branch, as mudanças deles caem na mesma pasta, misturadas.
Um commit leva as duas: um commit com duas entregas, uma delas talvez pela metade, que nenhum `git revert` sozinho consegue desfazer separadamente.
A unidade de trabalho do [capítulo 19](19-git-essentials.md), uma entrega que se desfaz em um passo, se perdeu, e separar as duas depois significa escolher mudanças arquivo por arquivo, linha por linha, à mão.

Se você dá a cada entrega o seu próprio branch, a pasta ainda guarda só um branch por vez.
Trocar de branch enquanto um agente tem trabalho ainda sem commit ou leva esse trabalho para o outro branch ou faz o git recusar até você guardá-lo de lado com `git stash`; e dois agentes não conseguem estar em dois branches de uma pasta no mesmo momento.

Um segundo clone do repositório dá a cada agente a sua própria pasta, mas cada clone tem a sua própria cópia do histórico: os dois só se encontram dando push para um remoto e pull dele, e cada clone repete o histórico inteiro no disco.

O que você quer são várias pastas, cada uma no seu próprio branch, compartilhando um histórico.
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
Digamos que a biblioteca de empréstimos tem duas entregas prontas para construir, `return-book` e `overdue-list`:

* O agente que constrói `return-book` trabalha em `../library-return-book`, no branch `return-book`; ele vê só as mudanças dessa entrega, e o commit que você faz ali guarda essa entrega e nada mais.
* O agente que constrói `overdue-list` faz o mesmo em `../library-overdue-list`, ao mesmo tempo.
* Ninguém troca de branch, então nada precisa de stash, e nenhum agente vê os arquivos pela metade do outro.

Quando uma entrega está pronta, você a traz para o `main` a partir da pasta principal com um commit de merge, `git merge --no-ff`, para que ela continue uma unidade de trabalho, desfeita em um passo com `git revert -m 1 <merge>` (capítulo 19).

## A vida de um worktree

Seis passos, rodados na pasta principal, exceto onde o texto diz outra coisa.

```
git worktree add ../library-return-book -b return-book main
```

Cria a pasta `../library-return-book`, cria o branch `return-book` no `main`, e faz checkout dele na pasta.

Depois você trabalha dentro da pasta como em qualquer outra: o agente constrói, você revisa e faz o commit ali.
Só o que o git acompanha está na pasta nova: dependências como `node_modules` não estão, então você as instala em cada worktree (`npm ci` em um projeto Node).

```
git worktree list
```

Imprime cada worktree, o commit em que ele está e o seu branch.

```
git merge --no-ff return-book
```

No `main`, na pasta principal, traz a entrega como um commit de merge; os commits do branch já aparecem ali, já que o histórico é compartilhado.

```
git worktree remove ../library-return-book
```

Apaga a pasta.
Ele se recusa a apagar uma pasta com arquivos mudados ou não acompanhados, então trabalho sem commit nunca se perde por acidente.[^git-worktree]

```
git branch -d return-book
```

Apaga o branch, que sobrevive à sua pasta.
`-d` apaga só um branch que já passou por merge; `-D` o apaga mesmo assim.

## Worktrees no kit

Um worktree por entrega é uma das estratégias de git que um projeto pode escrever no slot Git do seu docs/05 (capítulo 19), e no kit são os passos acima com o `/propose` e o `/apply` no meio.
O `/propose <slug>` cria o worktree com o nome do slug, `../<project>-<slug>` em um branch `<slug>` a partir do `main`, e escreve a página ali ([capítulo 14](14-propose.md)).
O `/apply <slug>` roda em uma sessão nova aberta naquela pasta, constrói a página, e coloca a mudança em stage ([capítulo 15](15-apply.md)).
Você revisa e faz o commit no branch, faz o merge no `main` com `--no-ff`, remove o worktree e apaga o branch.

O agente nunca faz commit, merge, resolve um conflito ou remove um worktree: cada passo que muda o histórico é seu, como em toda estratégia de git.
Para rodar duas entregas ao mesmo tempo, abra uma sessão por pasta: uma na pasta principal para cada `/propose`, uma em cada worktree para o seu `/apply`.

## Quando os branches se encontram: o conflito

Os worktrees mantêm as entregas separadas enquanto são construídas; o merge as junta, e o git combina os dois lados linha por linha.
Se os dois branches mudaram as mesmas linhas, ou linhas vizinhas, o git não tem como saber qual manter: ele faz o merge de todas as outras mudanças, para antes do commit de merge, e deixa o arquivo para você.
Isso é um conflito.[^git-merge]
Um conflito é sobre linhas, não sobre arquivos: dois branches que mudam o mesmo arquivo em pontos distantes entram por merge sozinhos.

No arquivo em conflito, o git escreve as duas versões entre marcadores de conflito: `<<<<<<<` abre a versão do branch em que você está, `=======` a separa da versão do branch que está entrando, e `>>>>>>>` fecha essa.[^git-merge]
Cada entrega marca a sua própria linha na fila ([capítulo 13](13-queue-and-milestones.md)), então duas entregas cujas linhas são vizinhas sempre se encontram ali.
Aqui o merge de `return-book` foi feito primeiro, e `overdue-list` entra em segundo; o bloco é uma ilustração, escrita para este capítulo:

```text
<<<<<<< HEAD
[x] return-book     a librarian records that a copy came back
[ ] overdue-list    a librarian sees every loan past its due date
=======
[ ] return-book     a librarian records that a copy came back
[x] overdue-list    a librarian sees every loan past its due date
>>>>>>> overdue-list
```

Acima de `=======` está o `main`, onde `return-book` está pronta; abaixo está `overdue-list`, onde a sua própria linha está pronta.
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
Com push: `git revert`, já que um reset reescreve um histórico que outros já têm, o que é a regra do rebase do capítulo 19.

## Quando o paralelo deixa de compensar

Os worktrees acabam com a mistura; eles deixam no lugar tudo o que duas entregas compartilham.
Antes de começar duas ao mesmo tempo, confira cinco coisas.

**A fila.** Ela sempre dá conflito, já que cada entrega marca a sua linha, e se resolve do mesmo jeito toda vez: guarde as duas marcas.

**Arquivos que as duas mudam.** Um arquivo de código que duas entregas mudam é diferente: resolvê-lo é uma decisão sobre o código, e quem a toma precisa entender as duas mudanças.
Então junte entregas cujos arquivos não se encontram: leia cada linha da fila, o docs/01 e o código que ela nomeia, e liste os arquivos que cada uma vai tocar.

**Portas e bancos de dados compartilhados.** Os worktrees compartilham a máquina: as suas portas, um banco de dados de teste em uma pasta comum.
Duas execuções de teste que sobem um servidor na mesma porta colidem, e uma falha por um motivo que não tem nada a ver com o seu código.
Uma porta ou um banco de dados por worktree é uma escolha que o projeto pode fazer, em uma entrega própria.

**Dependências.** Cada worktree instala as suas, então cada um custa tanto disco quanto a pasta principal, e a instalação leva o seu tempo de novo.

**Você.** Os agentes trabalham em paralelo; a sua revisão não.
Você lê cada página e cada mudança em stage, faz o commit e o merge, uma entrega por vez, então rode ao mesmo tempo só tantas entregas quantas você consegue revisar.
Este livro, escrito e revisado por uma pessoa em arquivos compartilhados, fica no trunk por esses dois motivos.

## O que o time ganha

Dois agentes constroem ao mesmo tempo, e cada entrega ainda chega como um merge que se desfaz sozinho.
Eu medi isso uma vez, em um pequeno projeto meu em TypeScript: duas entregas construídas ao mesmo tempo por dois agentes levaram 155 segundos do primeiro início ao último fim, contra 277,2 segundos de trabalho dos agentes somados, pouco mais da metade da espera.[^parallel-run]
A mesma execução pagou os custos da seção acima: o `node_modules` de cada worktree ocupou 155 MB de disco, e as duas execuções de teste colidiram uma vez em uma porta compartilhada e passaram quando rodadas de novo; a fila deu conflito, como sempre dá.[^parallel-run]
Uma execução é um sinal, não uma taxa: o ganho vale enquanto os arquivos das entregas não se encontram, e termina na velocidade da pessoa que as revisa e faz o merge delas.

## Pontos-chave

* Dois agentes em uma pasta misturam as suas entregas em um commit, ou brigam pelo único branch que a pasta guarda; um worktree dá a cada entrega a sua própria pasta e o seu próprio branch, compartilhando um histórico.
* `git worktree add ../<folder> -b <branch> main`, trabalhe e faça o commit ali, `git merge --no-ff <branch>` na pasta principal, depois `git worktree remove` e `git branch -d`; no kit, o `/propose` cria o worktree e o `/apply` constrói nele, e a pessoa faz o merge.
* Um conflito são dois branches mudando as mesmas linhas ou linhas vizinhas: o git faz o merge do resto e deixa as duas versões entre marcadores; guarde o que os dois fizeram, `git add`, faça o commit, ou saia com `git merge --abort`.
* O git faz commit dos marcadores sem dizer nada se você coloca o arquivo em stage sem resolver: rode `git diff --cached --check` antes de fazer o commit de um merge.
* O paralelo compensa enquanto os arquivos das entregas não se encontram, as portas e os bancos de dados da máquina não colidem, o disco comporta as dependências de cada worktree, e uma pessoa ainda consegue revisar cada entrega.

[^git-worktree]: Git, "git-worktree", a documentação, acesso em 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^git-merge]: Git, "git-merge", a documentação, seção "How conflicts are presented" e opção `--abort`, acesso em 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", a documentação, opção `--check`, acesso em 2026-09-30. <https://git-scm.com/docs/git-diff>
[^parallel-run]: J.C. Ködel, "One Page at a Time", o registro de duas entregas construídas em paralelo em dois worktrees, 2026-09-30, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-worktrees-run>
