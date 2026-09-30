# Worktrees e agentes em paralelo

Depois deste capítulo você consegue pôr dois agentes para construir duas entregas ao mesmo tempo, cada um na sua pasta, de modo que cada commit tenha uma entrega e nada mais.
Você também consegue fazer o merge das duas de volta, resolver o conflito quando elas mexeram nas mesmas linhas, pegar um marcador de conflito antes que ele entre num commit, e dizer quando trabalhar em paralelo deixa de compensar.

## O problema: uma pasta, dois trabalhos

Um agente leva minutos para construir uma entrega, e enquanto ele trabalha você espera.
O passo natural é iniciar um segundo agente na próxima entrega, e numa pasta só isso dá errado de um de dois jeitos.

Se os dois agentes trabalham no mesmo branch, as mudanças deles caem na mesma pasta.
O `git status` mostra as duas entregas misturadas, e um commit leva as duas: um commit com duas entregas, uma delas talvez pela metade, que nenhum `git revert` sozinho desfaz em separado.
A unidade de trabalho do [capítulo 17](17-git-essentials.md#as-quatro-lado-a-lado), uma entrega que se reverte num passo só, se perde, e separar as duas depois significa escolher as mudanças arquivo por arquivo, linha por linha, à mão.

Se você dá a cada entrega o seu próprio branch, a pasta continua tendo um branch só por vez.
Trocar de branch enquanto um agente tem trabalho ainda fora de commit ou leva esse trabalho para o outro branch ou faz o git recusar até você guardá-lo com `git stash`; e dois agentes não podem estar em dois branches de uma pasta no mesmo momento.

Um segundo clone do repositório dá a cada agente a sua pasta, mas cada clone tem a sua própria cópia do histórico: os dois só se encontram fazendo push para um remoto e fetch dele, e cada clone repete o histórico inteiro no disco.

O que você quer são várias pastas, cada uma no seu branch, compartilhando um histórico só.
Isso é um worktree.

## O que é um worktree

Um worktree é uma pasta de trabalho a mais do mesmo repositório git, com o checkout de um branch próprio.
Nas palavras da documentação do git: "*Um repositório git pode ter várias árvores de trabalho, o que permite fazer checkout de mais de um branch ao mesmo tempo.*"[^git-worktree]

A pasta que você clonou é o worktree principal.
Ela guarda a pasta `.git`, onde mora o histórico: os commits, os branches e as tags.
O `git worktree add` cria outra pasta, faz o checkout de um branch nela e deixa ali um pequeno arquivo `.git` que aponta de volta para o principal.
Todos os worktrees compartilham o histórico; cada um tem os seus arquivos, o seu `HEAD` (o commit em que está) e a sua área de staging.[^git-worktree]
Então um commit feito num worktree fica visível na hora em todos os outros, sem push e sem fetch, enquanto o que você muda ou põe em stage num nunca aparece em outro.
O git também se recusa a fazer checkout de um branch em dois worktrees, então duas pastas nunca escrevem no mesmo branch.[^git-worktree]

Este é o projeto guiado com duas entregas em andamento, `route-errors` e `minutes-of`, como o `git worktree list` o mostrou da pasta principal:[^clinic-worktrees-run]

```text
.                               0993b68 [main]
../focus-kit-clinic-minutes-of   948b94d [minutes-of]
../focus-kit-clinic-route-errors af3269a [route-errors]
```

Três pastas, um repositório: a pasta principal no `main`, e ao lado dela uma pasta por entrega, cada uma num branch com o nome da entrega, cada linha com o commit em que o seu branch está.

## Como isso resolve o problema

Dê a cada entrega o seu worktree, e a cada agente a sua pasta:

* O agente que constrói a `route-errors` trabalha em `../focus-kit-clinic-route-errors`, no branch `route-errors`; o `git status` dele mostra só as mudanças dessa entrega, e o commit que você faz ali tem essa entrega e nada mais.
* O agente que constrói a `minutes-of` faz o mesmo na sua pasta, ao mesmo tempo.
* Ninguém troca de branch, então nada precisa de stash, e nenhum agente vê os arquivos pela metade do outro.

Quando uma entrega fica pronta, você a traz para o `main` da pasta principal com um commit de merge, `git merge --no-ff`, para que ela continue uma unidade de trabalho, revertida num passo só com `git revert -m 1 <merge>` ([capítulo 17](17-git-essentials.md#commit-de-merge)).

Também economiza tempo: no projeto guiado, os dois agentes que construíram essas duas entregas ao mesmo tempo levaram 155 segundos do primeiro início ao último fim, para 277,2 segundos de trabalho somados.[^clinic-worktrees-run]

## A vida de um worktree

Cinco comandos, rodados da pasta principal, menos onde o texto diz outra coisa.

```
git worktree add ../app-x -b x main
```

Cria a pasta `../app-x`, cria o branch `x` no `main` e faz o checkout dele na pasta.
Depois você constrói e faz commit dentro de `../app-x` como em qualquer pasta.
Só o que o git rastreia está ali: dependências como o `node_modules` não, então você as instala em cada worktree (`npm ci` no projeto guiado).

```
git worktree list
```

Mostra cada worktree, o seu commit e o seu branch, como acima.

```
git merge --no-ff x
```

No `main`, na pasta principal, traz a entrega como um commit de merge; o commit do branch já está visível ali, já que o histórico é compartilhado.

```
git worktree remove ../app-x
```

Apaga a pasta.
Ele recusa uma pasta com arquivos mudados ou não rastreados, então trabalho que você não pôs num commit nunca se perde por acidente.[^git-worktree]

```
git branch -d x
```

Apaga o branch, que sobrevive à sua pasta.
O `-d` só apaga um branch que já passou por merge; o `-D` apaga assim mesmo.

## Worktrees no kit

Um worktree por entrega é uma das três estratégias de git do [capítulo 6](06-the-documents.md#as-duas-escolhas), e no kit são esses cinco comandos com o `/propose` e o `/apply` no meio.
O `/propose <slug>` roda `git worktree add ../<projeto>-<slug> -b <slug> main` e escreve a página na pasta nova; o `/apply <slug>` roda numa sessão nova aberta nessa pasta; você revisa, faz o commit no branch, o merge com `--no-ff`, remove o worktree e apaga o branch.
O agente nunca faz commit, merge, resolve um conflito ou remove um worktree: todo passo que muda o histórico é seu, como em toda estratégia de git.
O projeto guiado adotou essa estratégia no seu [ADR-0003](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/worktrees/docs/adr/ADR-0003-git-strategy.md), que registra os mesmos passos.

Para rodar duas entregas ao mesmo tempo numa sessão interativa, abra um terminal por sessão: um na pasta principal para cada `/propose`, um em cada worktree para o seu `/apply`.
O `/propose` escreve numa pasta fora daquela em que a sua sessão começou, então o host pede que você aprove essa escrita, como o [capítulo 8](08-analyze.md#confira-contra-o-codigo) diz de uma permissão que o modo não concede.
Sem interface, uma sessão só consegue escrever numa pasta de `--add-dir` (uma segunda pasta onde ela pode trabalhar) que já existia quando ela começou, então crie a pasta vazia antes; o `git worktree add` aceita uma pasta vazia.[^clinic-worktrees-run]

## Quando os branches se encontram: o conflito

Os worktrees mantêm as entregas separadas enquanto elas são construídas; o merge as junta, e o git combina os dois lados linha a linha.
Se os dois branches mudaram as mesmas linhas, ou linhas vizinhas, o git não tem como saber qual manter: ele faz o merge de todas as outras mudanças, para antes do commit de merge e deixa o arquivo para você.
Isso é um conflito.[^git-merge]

No projeto guiado, cada entrega marcou a sua própria linha no docs/06, a fila, e as duas linhas são vizinhas.
O primeiro merge, `route-errors`, entrou limpo; o segundo parou:

```
git merge --no-ff minutes-of
```

```text
Auto-merging docs/01-Architecture.md
Auto-merging docs/06-Queue.md
CONFLICT (content): Merge conflict in docs/06-Queue.md
Automatic merge failed; fix conflicts and then commit the result.
```

O docs/01 também tinha mudado nos dois branches, mas em linhas distantes, então o git fez o merge dele sozinho ("Auto-merging"): um conflito é questão de linhas, não de arquivos.

No arquivo em conflito, o git escreve as duas versões entre marcadores de conflito: `<<<<<<<` abre a versão do branch em que você está, `=======` a separa da versão do branch que entra, e `>>>>>>>` fecha esta.[^git-merge]
O `git diff` os mostra.
Durante um merge ele imprime duas colunas de `+` e `-` antes de cada linha, a primeira comparando com o branch em que você está e a segunda com o branch que entra; o que importa aqui são as linhas entre os marcadores:

```
git diff
```

```text
diff --cc docs/06-Queue.md
index ac17a76,60ea2d3..0000000
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@@ -40,8 -40,8 +40,13 @@@ git-worktrees is built in its own workt
  [ ] time-zone-names      setup accepts every IANA name the runtime knows, such as US/Eastern and Etc/UTC, as docs/03 says
  [ ] slot-taken-retry     after a refused booking whose slot reload fails, "Try again" keeps the "no longer free" message and the chosen date
  [ ] routes-table         the Routes table of docs/02 renders whole, with the slots and appointments routes as rows
++<<<<<<< HEAD
 +[x] route-errors         one shared copy of each error answer routes repeat (DatabaseFailed, BadRequest, NotSignedIn, ProfessionalNotFound, ClinicNotSetUp 500); the first copies are in session.server.ts and weeklyHours/route.server.ts
 +[ ] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
++=======
+ [ ] route-errors         one shared databaseFailed and one shared notFound answer; the first copies are in session.server.ts and weeklyHours/route.server.ts
+ [x] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
++>>>>>>> minutes-of
  [x] booking-submit       useBooking's submit publishes its in-flight state as an update and books with the state the hook read, not a ref written during render
  [x] hours-save           useWeeklyHours' save publishes its in-flight state as an update, so a time typed just before Save survives
  [x] hours-report         the hours editor's reports reach the professionals section as one WeeklyHoursReport and one tested event; finishes what orchestrator-tests left
```

Acima do `=======` está o `main`, que já tem a `route-errors`: a linha dela `[x]`, com o texto que essa entrega reescreveu, e a `minutes-of` ainda `[ ]`.
Abaixo está a `minutes-of`: a sua própria linha `[x]`, e a `route-errors` como era antes.
Nenhum lado está certo sozinho; a versão certa fica com o que os dois fizeram: as duas linhas `[x]`, e a `route-errors` com o seu texto novo.

Para resolver, edite o arquivo até essa versão e apague as três linhas de marcador; depois o `git add` diz ao git que o arquivo está resolvido, e o `git commit --no-edit` faz o commit de merge com a mensagem que o git preparou:

```
git add docs/06-Queue.md
git commit --no-edit
```

Se você prefere não resolver agora, o `git merge --abort` sai do merge e põe o branch de volta como estava antes.[^git-merge]

O histórico depois, no gráfico do [capítulo 17](17-git-essentials.md#commit-de-merge):

```
git log --oneline --graph -5
```

```text
*   699ab40 Merge branch 'minutes-of'
|\  
| * 948b94d Declare minutesOf once in lib/time.ts (minutes-of)
* |   045c744 Merge branch 'route-errors'
|\ \  
| |/  
|/|   
| * af3269a Share the error answers routes repeat (route-errors)
|/  
* 0993b68 Build every delivery in its own worktree (git-worktrees)
```

Os dois branches começam no `0993b68`, cada um tem um commit, e cada um entra no `main` pelo seu próprio commit de merge, `045c744` e `699ab40`: duas entregas, cada uma revertida sozinha.

## A armadilha: fazer commit dos marcadores

O `git add` é como você diz ao git que um conflito está resolvido, e o git acredita.
Ponha o arquivo em stage com os marcadores ainda dentro, faça o commit, e o commit de merge fica com os marcadores, sem aviso nenhum.
Isso aconteceu no projeto guiado, quando os comandos do merge foram colados como um bloco só e o add e o commit rodaram antes que alguém tocasse no arquivo.[^clinic-worktrees-run]

A proteção é um comando, antes do commit do merge:

```
git diff --cached --check
```

Ele lê o que está em stage, informa cada marcador de conflito como `<file>:<line>: leftover conflict marker`, e sai com status diferente de zero quando acha um, então um script pode parar nele.[^git-diff]

Se os marcadores entraram no commit mesmo assim, o desfazer depende de alguém mais ter o commit.
Sem push: `git reset --hard <o commit anterior ao merge>` joga o merge fora, e você faz o merge de novo.
Com push: `git revert`, já que o reset reescreve um histórico que outros já têm, que é a [regra do capítulo 17 para o rebase](17-git-essentials.md#fast-forward-e-rebase).

## Quando o paralelo deixa de compensar

Os worktrees acabam com a mistura; não acabam com tudo o que duas entregas compartilham.
Antes de iniciar duas ao mesmo tempo, confira quatro coisas.

**Arquivos.** Duas entregas que mudam as mesmas linhas entram em conflito no merge.
A fila é sempre uma delas, já que toda entrega marca a sua linha, e ela se resolve do mesmo jeito toda vez: mantenha as duas marcas.
Um arquivo de código que as duas mudam é diferente: a resolução dele é uma decisão sobre o código.
Então junte entregas cujos arquivos não se encontram: leia cada linha da fila, o docs/01 e o código que ele nomeia, e liste os arquivos em que cada uma vai mexer.

**Recursos compartilhados.** Os worktrees compartilham a máquina: as portas dela, um banco de testes numa pasta comum.
No projeto guiado, as duas entregas rodaram os seus testes ponta a ponta ao mesmo tempo, as duas na porta 3100, e uma parou com `Error: http://localhost:3100/api/health is already used`; rodada de novo, passou.[^clinic-worktrees-run]
Uma porta ou um banco por worktree é uma escolha que o projeto pode fazer, numa entrega própria.

**Disco.** Cada worktree tem as suas dependências: no projeto guiado, 155M de `node_modules` por worktree, o mesmo que a pasta principal.[^clinic-worktrees-run]

**Você.** Os agentes trabalham em paralelo; a sua revisão, não.
Você lê cada página e cada mudança em stage, faz o commit e o merge, uma entrega por vez, então rode ao mesmo tempo só as entregas que você consegue revisar.
Este livro, escrito e revisado por uma pessoa em arquivos compartilhados, fica no trunk por esses dois motivos, como diz o seu ADR-0010 no [capítulo 6](06-the-documents.md#adrs).

## Pontos-chave

* Dois agentes numa pasta misturam as suas entregas num commit, ou disputam o único branch que a pasta tem; um worktree dá a cada entrega a sua pasta e o seu branch, compartilhando um histórico só.
* `git worktree add ../<folder> -b <branch> main`, trabalhe e faça o commit ali, `git merge --no-ff <branch>` da pasta principal, depois `git worktree remove` e `git branch -d`; cada entrega continua um commit de merge, revertido sozinho.
* Um conflito são dois branches mudando as mesmas linhas ou linhas vizinhas: o git faz o merge do resto e deixa as duas versões entre marcadores; fique com o que os dois fizeram, `git add`, commit, ou saia com `git merge --abort`.
* O git faz commit de marcadores sem dizer nada se você põe o arquivo em stage sem resolver: rode `git diff --cached --check` antes de fazer o commit de um merge.
* O paralelo compensa enquanto os arquivos das entregas não se encontram, os recursos compartilhados da máquina não colidem, o disco comporta uma cópia das dependências por worktree, e você ainda consegue revisar cada entrega.

## Exercícios

Estes exercícios usam o projeto guiado na sua tag do capítulo [`book-v1/worktrees`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/worktrees), que tem as duas entregas acima e os seus merges.
O seu clone está em `book-v1/four-pieces`: rode `git fetch --tags`, depois `git switch -c mine18 book-v1/worktrees`.
Entre as duas tags estão a atualização do kit, sete correções que as revisões deste livro puseram no marco 1.1 da clínica, a troca para worktrees e as duas entregas; construí-las você mesmo com `/propose` e `/apply` é opcional, e a tag é com o que comparar.
Os comandos são comandos git que você mesmo roda.

### Exercício 18.1

Crie dois worktrees a partir do seu branch, `../try-a` em `try-a` e `../try-b` em `try-b`.
Em cada um, marque como `[x]` uma diferente das linhas `[ ]` vizinhas `time-zone-names` e `slot-taken-retry` do docs/06, e faça o commit.
Faça o merge das duas no `mine18` com `--no-ff`, resolva o conflito e leia o `git log --oneline --graph`.

### Exercício 18.2

Volte para antes do segundo merge com `git reset --hard`, repita-o, ponha o arquivo em stage com os marcadores, rode `git diff --cached --check`, e diga o que ele imprime e por que nada entrou num commit ainda.
Depois rode `git merge --abort`, remova os dois worktrees e apague os dois branches: diga por que o `git branch -d` recusa um deles, e o que o apaga.

### Exercício 18.3

Do [docs/06](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/worktrees/docs/06-Queue.md) da tag, escolha duas linhas abertas do marco 1.1 que dois agentes poderiam construir ao mesmo tempo, nomeie os arquivos em que cada uma mexeria, a partir do docs/01 e do código, e diga que conflitos você ainda esperaria.

[^git-worktree]: Git, "git-worktree", a documentação, acesso em 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^clinic-worktrees-run]: A execução deste livro de duas entregas do projeto guiado em paralelo, 2026-09-30, com o Claude Code 2.1.286 e o modelo `claude-opus-5-5`: todo turno, os tempos, os merges em `merges.txt` (a saída do `git worktree list` copiada do terminal, o resto byte a byte, caminhos relativos à raiz da clínica), e os testes no commit `699ab40` da clínica em `verify.txt`. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/clinic-worktrees-run/README.md>
[^git-merge]: Git, "git-merge", a documentação, seção "How conflicts are presented" e opção `--abort`, acesso em 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", a documentação, opção `--check`, acesso em 2026-09-30. <https://git-scm.com/docs/git-diff>
