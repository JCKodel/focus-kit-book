# Worktrees e agentes em paralelo

Depois deste capítulo você consegue construir duas entregas ao mesmo tempo em dois worktrees, fazer o merge delas com `--no-ff`, resolver o conflito onde elas se encontram e pegar um marcador de conflito antes que ele entre num commit.
Você também consegue dizer onde agentes em paralelo deixam de compensar: arquivos compartilhados, recursos compartilhados, disco, e a única pessoa que revisa e faz os merges.

## O que é um worktree

Todo comando git deste capítulo é um que você roda: o agente não roda nenhum além do `git worktree add`, que o `/propose` da clínica roda, e de `git add`, `git status` e `git diff`, como no [capítulo 17](17-git-essentials.md#commits-e-o-historico).
Todo trecho vem do projeto guiado na tag do capítulo [`book-v1/worktrees`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/worktrees), commit `699ab40`, ou do registro da execução que a construiu.[^clinic-worktrees-run]

O seu clone está em `book-v1/four-pieces`.
Entre ele e `book-v1/worktrees` estão a atualização do kit, as sete correções da clínica que as revisões deste livro puseram na fila do marco 1.1 da clínica (o [docs/06](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/worktrees/docs/06-Queue.md) da tag as lista), depois três entregas, `git-worktrees`, `route-errors` e `minutes-of`, e dois merges.
Para este capítulo, rode `git fetch --tags` e depois `git switch -c mine18 book-v1/worktrees`, um branch seu na tag.
Construir essas linhas você mesmo com `/propose` e `/apply` é opcional; a tag é com o que comparar, como no [capítulo 15](15-four-pieces.md#as-quatro-pecas).

Um worktree é uma pasta de trabalho a mais do mesmo repositório git, no seu próprio branch.
A documentação do git diz assim: "*Um repositório git pode ter várias árvores de trabalho, o que permite fazer checkout de mais de um branch ao mesmo tempo.*"[^git-worktree]
A pasta que você clonou é o worktree principal; cada um que você acrescenta fica ligado a ele e compartilha tudo, menos os seus próprios arquivos em checkout, o seu `HEAD` e a sua área de staging.[^git-worktree]

Quatro comandos cobrem a vida dele:

```
git worktree add ../<folder> -b <branch> main
git worktree list
git worktree remove ../<folder>
git branch -d <branch>
```

O `add` cria a pasta, cria o branch no `main` e faz o checkout dele ali; o `list` mostra cada worktree com o seu commit e o seu branch; o `remove` apaga a pasta, e recusa uma com arquivos mudados ou não rastreados, que é como o git guarda o trabalho que você ainda não pôs num commit.[^git-worktree]
O branch sobrevive à pasta: o `git branch -d` o apaga, e só depois que ele passou por merge.
O git também se recusa a fazer checkout de um branch em dois worktrees, então dois agentes nunca escrevem num mesmo branch.[^git-worktree]

Contra um segundo clone, um worktree compartilha um histórico só: um commit feito no worktree está na pasta principal na hora, então você faz o merge dele dali, sem push e sem fetch.
Um clone tem a sua própria cópia do histórico, e os dois só se encontram por um remoto.
Contra trocar de branch numa pasta só, cada agente tem a sua pasta: uma pasta tem um branch por vez, dois agentes escrevendo nela escrevem um por cima do outro, e trocar de branch com trabalho fora de commit exige um `git stash` antes.

A clínica escolheu essa forma na sua entrega `git-worktrees`, que emendou o seu [ADR-0003](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/worktrees/docs/adr/ADR-0003-git-strategy.md): a decisão do trunk fica acima como histórico, e a Decision da emenda diz, no original em inglês e aqui traduzido:

```markdown
Um worktree por entrega. `/propose <slug>` o cria a partir da pasta principal
com `git worktree add ../focus-kit-clinic-<slug> -b <slug> main`, e
escreve ali a página e a marca do docs/06. `/apply <slug>` roda numa sessão
nova aberta nessa pasta. A pessoa faz o commit da entrega no branch
`<slug>`, depois, da pasta principal, roda `git merge --no-ff <slug>` para o
`main`: um merge por entrega. A pessoa resolve qualquer conflito, depois roda
`git worktree remove ../focus-kit-clinic-<slug>` e `git branch -d <slug>`.

O agente faz o stage e sugere a mensagem de commit. Ele nunca faz commit, merge,
resolve um conflito de merge ou remove um worktree. O docs/05 §5 guarda os
comandos.
```

Uma pasta por entrega, ao lado da pasta da clínica, num branch com o nome do slug; um merge `--no-ff` por entrega, para que ela seja revertida num passo só, como o [capítulo 17](17-git-essentials.md#as-quatro-lado-a-lado) mostrou.
Todo passo que muda o histórico é da pessoa: o agente nunca faz commit, merge, resolve um conflito ou remove um worktree.

## Duas entregas ao mesmo tempo

Duas linhas do marco 1.1 da clínica foram primeiro.
A `route-errors` pedia uma cópia compartilhada de cada resposta de erro que as rotas do servidor repetem; o `/propose` dela achou cinco respostas assim onde a linha nomeava duas, e alargou a linha.
A `minutes-of` pedia um só parser compartilhado de horários "HH:MM", cujas duas cópias estavam em `weeklyHours/rules.ts` e `appointments/rules.ts`.

Iniciei as duas sessões de `/propose` no mesmo segundo, as duas da raiz da clínica, sem interface, com `Your call. Diga o que escolheu e por quê.` como resposta às perguntas delas, o briefing do [capítulo 10](10-propose.md).
Cada uma rodou `git worktree add ../focus-kit-clinic-<slug> -b <slug> main` e escreveu a sua página e a sua marca na fila no seu worktree.
Sem interface, uma sessão não consegue escrever numa pasta de `--add-dir` (uma segunda pasta onde a sessão pode trabalhar) que não existia quando ela começou, então criei as duas pastas vazias antes de iniciar as sessões, e o `git worktree add` aceita uma pasta vazia.
Depois, duas sessões de `/apply`, de novo no mesmo segundo, cada uma iniciada da raiz do seu worktree.
Um worktree não tem `node_modules`, já que o git não o rastreia, então cada `/apply` rodou `npm ci` primeiro.
Revisei as duas páginas e as duas mudanças em stage e não mandei nenhum pedido, depois fiz o commit de cada entrega no seu branch, no seu worktree: [`af3269a`](https://github.com/JCKodel/focus-kit-clinic/commit/af3269aecc1d2408012ad0d5c839f49decd5d8e9) com 12 arquivos e [`948b94d`](https://github.com/JCKodel/focus-kit-clinic/commit/948b94de50e941f6f3b816889bcd604319834e4e) com 7.[^clinic-worktrees-run]

O tempo dos agentes se sobrepôs.
As duas sessões de `/propose` levaram 128 segundos do primeiro início ao último fim, contra 177,8 segundos dos seus quatro turnos somados; as duas sessões de `/apply` levaram 155 segundos, contra 277,2 segundos somados.[^clinic-worktrees-run]

Numa sessão interativa, abra um terminal por sessão: um na raiz da clínica para cada `/propose`, um em cada worktree para o seu `/apply`.
O `/propose` escreve na pasta vizinha, fora daquela em que a sua sessão começou, então o host pede que você aprove essa escrita, como o [capítulo 8](08-analyze.md#confira-contra-o-codigo) diz de uma permissão que o modo não concede.
Essa última parte decorre do modo de permissão; a execução foi sem interface e não a mostrou.

## O merge, e o conflito

As saídas de merge deste capítulo vêm do registro da execução: `git worktree list`, o primeiro merge e o `bdb0609` abaixo foram copiados do meu terminal, o resto byte a byte, com os caminhos relativos à raiz da clínica.[^clinic-worktrees-run]
Da raiz da clínica, no `main`, os dois worktrees ao lado da pasta principal:

```
git worktree list
```

```text
.                               0993b68 [main]
../focus-kit-clinic-minutes-of   948b94d [minutes-of]
../focus-kit-clinic-route-errors af3269a [route-errors]
```

O primeiro merge não achou nada no caminho (as linhas de cada arquivo mudado ficaram de fora aqui):

```
git merge --no-ff route-errors
```

```text
Merge made by the 'ort' strategy.
 12 files changed, 304 insertions(+), 67 deletions(-)
```

O segundo parou:

```
git merge --no-ff minutes-of
```

```text
Auto-merging docs/01-Architecture.md
Auto-merging docs/06-Queue.md
CONFLICT (content): Merge conflict in docs/06-Queue.md
Automatic merge failed; fix conflicts and then commit the result.
```

Um conflito é o que o git informa quando os dois branches mudaram as mesmas linhas, ou linhas vizinhas: o git faz o merge de todas as outras mudanças, para antes do commit de merge e deixa o arquivo para você.[^git-merge]
No arquivo, o git escreve as duas versões entre marcadores de conflito: `<<<<<<<` abre a versão do branch em que você está, `=======` a separa da versão do branch que entra, e `>>>>>>>` fecha esta.[^git-merge]
O `git diff` os mostra; durante um merge ele imprime um diff combinado, com duas colunas de `+` e `-`, a primeira contra o branch em que você está e a segunda contra o branch que entra:

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

Acima do `=======` está o `main`, que já tem a `route-errors`: a linha dela marcada `[x]` com o texto mais largo, e a `minutes-of` ainda `[ ]`.
Abaixo está a `minutes-of`: a sua própria linha `[x]`, e a `route-errors` com o texto que tinha antes.
Cada branch marcou a sua própria linha na fila, e as duas linhas são vizinhas, então o git não tinha como ficar com uma mudança sem a versão do outro lado para a linha ao lado.
O docs/01 também mudou nos dois branches, a `route-errors` na listagem de `server/` e a `minutes-of` na de `lib/`, linhas distantes: o git imprimiu "Auto-merging" e fez o merge sozinho.

A resolução fica com o que os dois lados fizeram: as duas linhas, as duas `[x]`, e a `route-errors` com o seu texto novo; os marcadores saem.
Com o arquivo editado assim, o `git diff` mostra a resolução contra cada lado:

```
git diff
```

```text
diff --cc docs/06-Queue.md
index ac17a76,60ea2d3..0000000
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@@ -40,8 -40,8 +40,8 @@@ git-worktrees is built in its own workt
  [ ] time-zone-names      setup accepts every IANA name the runtime knows, such as US/Eastern and Etc/UTC, as docs/03 says
  [ ] slot-taken-retry     after a refused booking whose slot reload fails, "Try again" keeps the "no longer free" message and the chosen date
  [ ] routes-table         the Routes table of docs/02 renders whole, with the slots and appointments routes as rows
 -[ ] route-errors         one shared databaseFailed and one shared notFound answer; the first copies are in session.server.ts and weeklyHours/route.server.ts
 +[x] route-errors         one shared copy of each error answer routes repeat (DatabaseFailed, BadRequest, NotSignedIn, ProfessionalNotFound, ClinicNotSetUp 500); the first copies are in session.server.ts and weeklyHours/route.server.ts
- [ ] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
+ [x] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
  [x] booking-submit       useBooking's submit publishes its in-flight state as an update and books with the state the hook read, not a ref written during render
  [x] hours-save           useWeeklyHours' save publishes its in-flight state as an update, so a time typed just before Save survives
  [x] hours-report         the hours editor's reports reach the professionals section as one WeeklyHoursReport and one tested event; finishes what orchestrator-tests left
```

Nenhum marcador sobrou: na segunda coluna a linha da `route-errors` está como o `main` a tinha, na primeira a linha da `minutes-of` está como o seu branch a tinha.
O `git add` marca o arquivo como resolvido, e o `git commit --no-edit` faz o commit de merge com a mensagem que o git preparou:

```
git add docs/06-Queue.md
git commit --no-edit
```

```text
[main 699ab40] Merge branch 'minutes-of'
```

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

Os dois branches começam no `0993b68`, a `git-worktrees`.
O [`045c744`](https://github.com/JCKodel/focus-kit-clinic/commit/045c744d27acdbaee7e269e848c5de6ee696d21d) junta o único commit da `route-errors` ao `main`, e o [`699ab40`](https://github.com/JCKodel/focus-kit-clinic/commit/699ab4008f78853810c28561110666abd2d0b823) junta o da `minutes-of`; as linhas cruzadas no meio são só o jeito como o `--graph` desenha `af3269a` e `0993b68` em linhas separadas.
Cada entrega é um commit de merge, revertido com `git revert -m 1 <merge>`.
O `npm run verify` no `699ab40` passou os seus 336 testes de Vitest e 144 de Playwright.[^clinic-worktrees-run]

Quando você prefere não resolver agora, o `git merge --abort` sai do merge e põe o branch de volta como estava antes dele.[^git-merge]

## Quando o git faz commit dos marcadores

Na primeira vez, colei os comandos do merge inteiro como um bloco só, então estes dois rodaram logo depois do conflito, antes que eu tivesse tocado no arquivo:

```
git add docs/06-Queue.md
git commit --no-edit
```

```text
[main bdb0609] Merge branch 'minutes-of'
```

O git fez o commit de merge `bdb0609` com os marcadores no docs/06, linhas 43 a 49, e não disse nada.[^clinic-worktrees-run]
Para o git, um marcador é texto como qualquer outro: o `git add` é como você diz a ele que um arquivo está resolvido, e ele acredita.

A proteção é um comando antes do commit do merge:

```
git diff --cached --check
```

Ele lê o que está em stage, informa cada marcador de conflito como `<file>:<line>: leftover conflict marker`, e sai com status diferente de zero quando acha um.[^git-diff]
A execução não o usou; o exercício 18.2 faz você rodá-lo.

O `bdb0609` nunca foi para o remoto, então o desfazer foi levar o `main` de volta ao commit anterior a ele, e jogá-lo fora:

```
git reset --hard 045c744
```

```text
HEAD is now at 045c744 Merge branch 'route-errors'
```

Depois, o mesmo merge de novo, o mesmo conflito, e a resolução da seção anterior.
O `bdb0609` não está em nenhum branch agora, e o histórico da clínica não o tem.
O reset reescreve o histórico, então é para commits que ninguém mais tem; depois que um commit foi para o remoto, desfaça-o com `git revert`, que é a [regra do capítulo 17 para o rebase](17-git-essentials.md#fast-forward-e-rebase).
No registro, pedi ao agente do livro que rodasse essa segunda parte, contra a regra de que a pessoa faz o merge; o capítulo mostra a saída do git, e a regra continua valendo (capítulo 19).

## Onde o paralelismo para

Dois agentes em dois worktrees fizeram duas entregas em menos tempo do que uma depois da outra; a execução também mostrou onde isso para.[^clinic-worktrees-run]

**A fila.** Toda entrega marca a sua linha no docs/06, então duas entregas em andamento sempre mexem nesse arquivo, e as linhas delas muitas vezes são vizinhas.
O ADR-0003 da clínica diz isso nas suas consequências: "*O `docs/06` é editado por toda entrega, então duas entregas em andamento podem entrar em conflito em linhas vizinhas da fila. A pessoa resolve mantendo as duas marcas.*"
É o conflito da execução, e ele sempre se resolve do mesmo jeito.

**Os mesmos arquivos.** A `route-errors` mudou 12 arquivos e a `minutes-of` 7; só o docs/01 e o docs/06 estavam nas duas, e o docs/01 passou pelo merge sozinho porque as mudanças estavam em linhas distantes.
Duas entregas que mudam as mesmas linhas de um arquivo de código entram em conflito ali, e essa resolução é uma decisão sobre o código, não mais uma questão de manter as duas marcas.
ADR-0003: "*Antes de construir duas entregas ao mesmo tempo, a pessoa confere que elas não mexem nos mesmos arquivos.*"

**Recursos compartilhados.** Os worktrees compartilham a máquina: os testes ponta a ponta da clínica sobem um servidor na porta 3100 em todo worktree.
O primeiro `npm run verify` da `route-errors` parou antes do Playwright com `Error: http://localhost:3100/api/health is already used`, já que a execução do outro worktree ocupava a porta; rodado de novo sem mudança nenhuma, passou.
ADR-0003: "*As portas de e2e (3100 e 5174, no `playwright.config.ts`) e o banco de e2e (`e2eDatabasePath`, na pasta temporária do sistema) são compartilhados por todo worktree hoje.*"
O banco não fez nada visível nesta execução.
Uma porta ou um banco por worktree é uma escolha do projeto, com a sua própria entrega; a clínica não a fez.

**Disco.** Cada worktree precisa das suas próprias dependências: o `node_modules` ocupou 155M em cada um, o mesmo que a pasta principal da clínica.
ADR-0003: "*Cada worktree custa uma pasta e o seu próprio `node_modules`.*"

**A pessoa.** O tempo dos agentes se sobrepôs: 155 segundos de relógio para 277,2 segundos de trabalho de `/apply`.
O da revisão, não: uma pessoa lê cada página, cada mudança em stage, faz o commit e o merge, uma por vez.
A execução não mediu esse tempo, então este capítulo não dá número para ele.

Este livro está no trunk pelos dois últimos motivos, arquivos compartilhados e um revisor só, como diz o seu ADR-0010 no [capítulo 6](06-the-documents.md#adrs).

Então você decide quais entregas rodam em paralelo antes de iniciá-las, pelos arquivos em que cada uma vai mexer: leia a linha, o docs/01 e o código que ele nomeia, e junte entregas cujos arquivos não se encontram, fora a fila.
Depois da execução da clínica, o marco 1.1 ainda tem três linhas abertas para construir, e o exercício 18.3 faz você juntar duas.

## Pontos-chave

* Um worktree é uma pasta de trabalho a mais do mesmo repositório, no seu próprio branch: `git worktree add ../<folder> -b <branch> main`, `list`, `remove`, depois `git branch -d`; ele compartilha um histórico só, e cada agente escreve na sua própria pasta.
* Dois agentes em dois worktrees sobrepõem o seu tempo; a pessoa faz o merge de cada entrega com `--no-ff`, um commit de merge cada, revertido com `git revert -m 1`.
* Um conflito são dois branches mudando as mesmas linhas ou linhas vizinhas: o git para, faz o merge do resto e deixa as duas versões entre marcadores; fique com o que os dois fizeram, `git add`, depois o commit, ou saia com `git merge --abort`.
* O git faz commit de marcadores sem dizer nada se você põe o arquivo em stage sem resolver; rode `git diff --cached --check` antes de fazer o commit de um merge, e desfaça um merge ruim que não foi para o remoto com `git reset --hard`, um que foi com `git revert`.
* O paralelismo para na fila (sempre conflita, mantenha as duas marcas), nos arquivos que as duas entregas mudam, em portas e bancos compartilhados, num `node_modules` por worktree, e na única pessoa que revisa e faz os merges.

## Exercícios

Estes exercícios usam o seu clone da clínica em `book-v1/worktrees`, no seu branch `mine18`.
São comandos git que você mesmo roda; nada aqui muda a clínica.

### Exercício 18.1

Crie dois worktrees a partir do seu branch, `../try-a` em `try-a` e `../try-b` em `try-b`.
Em cada um, marque como `[x]` uma diferente das linhas `[ ]` vizinhas `time-zone-names` e `slot-taken-retry` do docs/06, e faça o commit.
Faça o merge das duas no `mine18` com `--no-ff`, resolva o conflito e leia o `git log --oneline --graph`.

### Exercício 18.2

Volte para antes do segundo merge com `git reset --hard`, repita-o, ponha o arquivo em stage com os marcadores, rode `git diff --cached --check`, e diga o que ele imprime e por que nada entrou num commit ainda.
Depois rode `git merge --abort`, remova os dois worktrees e apague os dois branches: diga por que o `git branch -d` recusa um deles, e o que o apaga.

### Exercício 18.3

Do docs/06 da tag, escolha duas linhas abertas do marco 1.1 que dois agentes poderiam construir ao mesmo tempo, nomeie os arquivos em que cada uma mexeria, a partir do docs/01 e do código, e diga que conflitos você ainda esperaria.

[^git-worktree]: Git, "git-worktree", a documentação, acesso em 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^clinic-worktrees-run]: A execução deste livro das entregas em paralelo do projeto guiado, 2026-09-30, com o Claude Code 2.1.286 e o modelo `claude-opus-5-5`: todo turno de `git-worktrees`, `route-errors` e `minutes-of`, os tempos, os merges em `merges.txt`, e a saída do `npm run verify` no commit `699ab40` da clínica em `verify.txt`. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/clinic-worktrees-run/README.md>
[^git-merge]: Git, "git-merge", a documentação, seção "How conflicts are presented" e opção `--abort`, acesso em 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", a documentação, opção `--check`, acesso em 2026-09-30. <https://git-scm.com/docs/git-diff>
