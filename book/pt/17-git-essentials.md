# O essencial de git: trunk, branches, git-flow

Depois deste capítulo você consegue dizer o que um controle de versão guarda e por que o git foi criado, ler o histórico de um projeto como commits, branches e merges, fazer o merge de um branch de cada uma das quatro formas que o git oferece, e dizer quais delas deixam uma entrega que se desfaz em um passo.
Você também consegue desfazer uma entrega com `git revert`, e dizer quando o trunk, um branch por entrega ou o git-flow servem a um projeto.

## Controle de versão, e por que git

Controle de versão é um sistema que registra as mudanças em um conjunto de arquivos ao longo do tempo, para que você possa trazer de volta qualquer versão anterior.[^pro-git-about]
Ele guarda todas as versões, não só a última, cada uma com quem mudou, quando e por quê, então você consegue comparar duas versões, achar quem introduziu um problema e quando, e voltar um arquivo ou o projeto inteiro ao que era.[^pro-git-about]
Um dev muitas vezes conhece o repositório git como o lugar onde o código fica; ele é também cada estado que o código já teve, e o histórico da clínica abaixo é 13 deles, qualquer um dos quais você pode abrir.

Ele funciona com qualquer tipo de arquivo, e o *Pro Git* põe entre os primeiros a ganhar com ele o designer que quer guardar cada versão de uma imagem ou de um layout.[^pro-git-about]
Sem ele, as versões moram no nome dos arquivos, `logo versão final.psd`, `logo versão final 2.psd`, `logo versão final mesmo.psd`, onde só quem deu os nomes sabe qual é a última e nada diz o que mudou de uma para a outra.
O *Pro Git* chama copiar arquivos para outra pasta de a forma mais comum de guardar versões, por ser simples, e uma que convida a erros: é fácil esquecer em que pasta você está, gravar no arquivo errado ou copiar por cima de um que você queria manter.[^pro-git-about]
Com controle de versão existe um `logo.psd`, e as versões anteriores dele estão no histórico, cada uma com o autor, a data e a mensagem.
Um limite para imagens: o git faz merge de texto linha a linha, mas duas versões de um arquivo binário, como um `.psd`, ele não consegue combinar, então fica com a sua e marca o arquivo como conflito, e as duas pessoas que o editaram escolhem que versão fica.[^gitattributes]

Os primeiros sistemas guardavam o histórico em um servidor só, de onde cada pessoa tirava os arquivos; o git é distribuído: cada clone tem o histórico inteiro, então o seu clone da clínica tem todos os commits dela, e qualquer clone pode restaurar o servidor se ele se perder.[^pro-git-about]

O git foi feito para o kernel do Linux.
De 1991 a 2002, as mudanças no kernel passavam entre os desenvolvedores como patches e arquivos compactados; a partir de 2002 o projeto usou o BitKeeper, um sistema distribuído proprietário.[^pro-git-history]
Em 2005 a relação entre a comunidade do kernel e a empresa por trás do BitKeeper se rompeu, e a ferramenta deixou de ser gratuita para eles.[^pro-git-history]
Isso levou a comunidade, e em particular Linus Torvalds, o criador do Linux, a escrever a sua própria ferramenta, com o que tinham aprendido usando o BitKeeper e com estes objetivos: velocidade, um design simples, suporte forte a desenvolvimento não linear, "*milhares de branches paralelos*", ser totalmente distribuído, e dar conta de um projeto do tamanho do kernel.[^pro-git-history]
Esses objetivos são o motivo de um branch quase não custar nada no git: ele é só um nome, como as próximas seções mostram.

## Commits e o histórico

Todo comando de git deste capítulo é um que você roda: o agente não roda nenhum deles além de `git add`, `git status` e `git diff`, como no [capítulo 11](11-apply.md#revise-antes-do-commit).
Os históricos mostrados são o do projeto guiado na tag do capítulo [`book-v1/four-pieces`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/four-pieces), commit `e6653b5`, e o do CLAHub, o projeto brownfield do capítulo 8, no fork `JCKodel/clahub` na tag [`book-v1`](https://github.com/JCKodel/clahub/tree/book-v1); cada saída é citada como rodou.

Um commit é um retrato salvo do projeto inteiro, com o autor, a mensagem e o commit ou commits de onde veio, os pais dele.
Ele é nomeado por um hash, uma sequência hexadecimal longa calculada a partir de tudo isso, que o git imprime encurtada nos primeiros caracteres.
O histórico é a cadeia de pais, do último commit de volta ao primeiro.
O `git log --oneline` o imprime com um commit por linha, o mais novo primeiro:

```
git log --oneline book-v1/four-pieces
```

```text
e6653b5 Move each client hook's events into tested plain functions
c54d011 Queue the confirmed findings of the milestone 1 review (docs/06)
f16f83b Let a client cancel an appointment up to 24 hours before it starts
442f88a Let a client book a free slot and keep the booking code
afc833a Wait for SQLite locks instead of failing with SQLITE_BUSY
064d7a9 Let the owner set each professional's weekly hours
4cceb3a Let the owner add, rename and remove professionals
75a8a25 Set up the clinic and let the owner sign in and out
d5b5c03 Build the skeleton: health page, Hono server, migrations, verify
3f0b47c Update focus-kit to e7607c5
23f67bb Brainstorm: documents and first milestone
a5ac6fd Install focus-kit
31d9503 Start: README and licenses
```

Esses são os 13 commits da clínica: um por entrega, cada um com a página e a construção dela, feitos pelo `git commit` do [capítulo 11](11-apply.md#revise-antes-do-commit).
O `git log --merges book-v1/four-pieces` lista só os commits com dois pais, e não imprime nada: não há merge neste histórico.

Um commit guarda uma entrega.
Este é o [`f16f83b`](https://github.com/JCKodel/focus-kit-clinic/commit/f16f83bdfadf7bf5919545aa390c92e6c01d5e3c), a entrega `cancel-appointment`, com os arquivos que ela mudou e quantas linhas cada um ganhou e perdeu (o `--format=` deixa de fora o autor e a mensagem):

```
git show --stat --format= f16f83b
```

```text
 docs/01-Architecture.md                            |   4 +-
 docs/02-Backend.md                                 |  15 +
 docs/03-Domain.md                                  |   4 +-
 docs/06-Queue.md                                   |   2 +-
 src/app/main.tsx                                   |   2 +
 src/features/appointments/BookingView.e2e.ts       |  99 +----
 src/features/appointments/BookingView.tsx          |  14 +-
 src/features/appointments/CancelView.e2e.ts        | 432 +++++++++++++++++++++
 src/features/appointments/CancelView.tsx           |  99 +++++
 src/features/appointments/RememberedView.tsx       | 118 +++++-
 src/features/appointments/api.ts                   |  67 +++-
 src/features/appointments/e2e.server.ts            |  92 +++++
 src/features/appointments/remembered.test.ts       |  36 ++
 src/features/appointments/remembered.ts            |  32 +-
 .../appointments/repository.server.test.ts         |  69 +++-
 src/features/appointments/repository.server.ts     |  45 +++
 src/features/appointments/route.server.test.ts     | 212 ++++++++++
 src/features/appointments/route.server.ts          |  63 ++-
 src/features/appointments/rules.test.ts            |  64 +++
 src/features/appointments/rules.ts                 |  23 ++
 src/features/appointments/strings.ts               |  23 ++
 src/features/appointments/styles.ts                |  16 +
 src/features/appointments/useCancel.ts             |  60 +++
 src/features/appointments/useRemembered.ts         |  82 +++-
 work/done/cancel-appointment-cancelled-390x844.png | Bin 0 -> 32270 bytes
 work/done/cancel-appointment-confirm-390x844.png   | Bin 0 -> 36094 bytes
 work/done/cancel-appointment-form-390x844.png      | Bin 0 -> 41477 bytes
 work/done/cancel-appointment-list-390x844.png      | Bin 0 -> 32483 bytes
 work/done/cancel-appointment-no-match-390x844.png  | Bin 0 -> 45783 bytes
 .../cancel-appointment-typed-cancelled-390x844.png | Bin 0 -> 39982 bytes
 work/done/cancel-appointment.md                    | 316 +++++++++++++++
 31 files changed, 1854 insertions(+), 135 deletions(-)
```

A página, `work/done/cancel-appointment.md`, está no mesmo commit que o código, os testes, os documentos e as capturas de tela que ela provou: 31 arquivos, uma unidade de trabalho.
Isso é o trunk, a primeira resposta do kit à escolha de git do [capítulo 6](06-the-documents.md#as-duas-escolhas): uma pessoa no `main`, um commit por entrega.

## Branches e tags

Um branch é um nome que aponta para um commit e anda para cada commit novo feito nele.
O `main` é um branch; `git switch -c <nome>` cria outro no commit em que você está e muda para ele, e `git branch` lista os branches, com um `*` antes do seu.
Dois branches que começam no mesmo commit e ganham commits cada um têm dois históricos que dividem o começo: é isso que um merge junta de novo.

Uma tag é um nome fixo em um commit, que nunca anda.
As tags de capítulo em que você fez checkout desde o [capítulo 5](05-install-and-hosts.md#exercicios), de `book-v1/start` a `book-v1/four-pieces`, são tags: `book-v1/four-pieces` nomeia o `e6653b5` hoje e sempre, enquanto o `main` da clínica segue em frente.

O `HEAD` é o commit em que você está: em geral o último commit do seu branch, que anda com ele.

## Quatro formas de merge

Um merge traz os commits de um branch para outro.
Digamos que você criou um branch `try` a partir do `main`, fez commits nele, e agora o traz para o `main`, o branch que recebe.
O git oferece quatro formas, e cada uma deixa um histórico diferente.[^pro-git-branching]

### Fast-forward e rebase

Se o `main` não tem nenhum commit próprio desde que o `try` saiu dele, o git pode só mover o nome `main` para o último commit do `try`.
Isso é um fast-forward, e não faz commit:

```
git switch main
git merge --ff-only try
```

O `--ff-only` recusa o merge quando um fast-forward não é possível, então você sabe que forma obteve.
O histórico continua uma linha, e o `main` agora tem os commits do `try` exatamente como eram.
O histórico da clínica acima é o que uma linha de fast-forwards deixaria: nenhum commit de merge em lugar nenhum.

Se o `main` andou, um fast-forward é impossível.
Um rebase reescreve os commits do `try` em cima do último commit do `main`, como commits novos com hashes novos, e aí um fast-forward volta a ser possível:

```
git switch try
git rebase main
git switch main
git merge --ff-only try
```

O histórico é de novo uma linha.
O rebase tem uma regra, do *Pro Git*: "*Não faça rebase de commits que existem fora do seu repositório e sobre os quais outras pessoas podem ter baseado trabalho.*"[^pro-git-rebasing]
Um rebase abandona os commits antigos, então quem construiu em cima deles precisa fazer o merge do seu trabalho de novo.

### Commit de merge

Um commit de merge é um commit com dois pais, o último commit do branch que recebe e o do branch que entra, que traz o branch inteiro:

```
git switch main
git merge --no-ff try
```

O `--no-ff` faz o commit de merge mesmo quando um fast-forward era possível.
O CLAHub faz merge assim, por pull requests: um pull request, que o [capítulo 6](06-the-documents.md#as-duas-escolhas) definiu e o capítulo 20 ensina, pede que um branch entre depois que alguém o revisa.
O `--graph` desenha os pais como linhas, com um commit de merge onde duas linhas se juntam:

```
git log --oneline --graph book-v1 | head -20
```

```text
* 9d1e666 chore(deps): bump hono to 4.12.12 and prisma to 7.7.0 (#308)
* 7681b69 chore(deps): bump next from 16.1.7 to 16.2.3 (#307)
* 67c7328 chore(deps): bump vite from 7.3.1 to 7.3.2 (#304)
* e610454 chore(deps): bump defu from 6.1.4 to 6.1.6 (#303)
* d416f52 chore(deps): bump brace-expansion (#302)
* 47d957f chore(deps): bump picomatch (#301)
* 0876294 chore(deps-dev): bump flatted from 3.3.3 to 3.4.2 (#300)
*   9e9bdfe Merge pull request #291 from DamageLabs/dependabot/npm_and_yarn/multi-0d13b2d87f
|\  
| * f359190 chore(deps): bump serialize-javascript and terser-webpack-plugin
* |   59dbf66 Merge pull request #299 from DamageLabs/feat/about-page
|\ \  
| * | c849395 feat: add About page with project history and DamageLabs links
|/ /  
* |   26c9049 Merge pull request #298 from DamageLabs/feat/umami-analytics
|\ \  
| * | a3683be feat: add Umami analytics tracking
|/ /  
* |   cde3de9 Merge pull request #297 from DamageLabs/fix/docs-styling
|\ \  
```

`9e9bdfe`, `59dbf66`, `26c9049` e `cde3de9` são commits de merge, um por pull request, cada um com os commits do branch na linha à direita.
Os commits acima deles têm um pai cada e um número de pull request no assunto: squash merges, a próxima forma.

Um commit de merge mantém os commits do branch no histórico.
O pull request #246, [`846e337`](https://github.com/JCKodel/clahub/commit/846e337fab0c7c89f42101de0ab42241c2f0fa57), trouxe um branch de sete commits.
`<commit>^1` é o primeiro pai de um commit e `<commit>^2` o segundo, então isto lista o que o lado do segundo pai tinha e o primeiro não:

```
git log --oneline 846e337^1..846e337^2
```

```text
42ccb59 fix(test): update webhook E2E test for structured error response
2efdc4e test(lib): add tests for result, logger, and api-error utilities
5f3d099 feat(exclusions): add toast notifications for error feedback
acee866 feat(ui): add error boundaries and not-found page
99c45a2 refactor: replace console.* with structured logger
a10bfdb refactor(actions): use shared result utilities and add error codes
bae1f35 feat(lib): add shared action result, logger, and API error helpers
```

O trabalho do branch continua legível, commit a commit, no histórico.
E o próprio commit de merge, com o hash, os dois pais e o assunto:

```
git show --no-patch --format='%h %p %s' 846e337
```

```text
846e337 2779b05 42ccb59 Merge pull request #246 from clahub/feat/214-structured-error-handling
```

O `2779b05` é onde o `main` estava; o `42ccb59` é o último commit do branch, a primeira linha da lista acima.

### Squash merge

Um squash merge escreve a mudança inteira do branch como um commit novo com um pai:

```
git switch main
git merge --squash try
git commit
```

O `--squash` põe a mudança no stage e não faz commit; o seu `git commit` o faz.
O [`9d1e666`](https://github.com/JCKodel/clahub/commit/9d1e666e1d30f271aea9640393229a7cbfbd1b62) do CLAHub, a primeira linha do grafo, é um:

```
git show --no-patch --format='%h %p %s' 9d1e666
```

```text
9d1e666 7681b69 chore(deps): bump hono to 4.12.12 and prisma to 7.7.0 (#308)
```

Um pai, e o número do pull request, #308, no assunto, que é como um squash merge feito no GitHub diz de onde veio.
Os commits do próprio branch não estão no histórico do `book-v1`: só este commit está.

### As quatro lado a lado

Uma entrega de vários commits, com merge feito em cada forma, e o que desfazê-la exige, com o `git revert` da próxima seção:

| Forma | O que chega ao branch que recebe | Desfazer uma entrega de vários commits |
|---|---|---|
| Fast-forward | Os commits, como eram | Um revert por commit |
| Commit de merge | Os commits, e um commit com dois pais | `git revert -m 1 <merge>` |
| Squash merge | Um commit novo | `git revert <commit>` |
| Rebase, depois fast-forward | Os commits, reescritos | Um revert por commit |

Com um branch por entrega, faça o merge por commit de merge ou por squash, para que a entrega continue uma unidade de trabalho: a regra do [capítulo 6](06-the-documents.md#as-duas-escolhas), um merge do branch, que o [`[>]` do capítulo 9](09-queue-and-milestones.md#as-marcas) já supõe.
Um fast-forward ou um rebase só mantém isso quando o branch tinha um commit.

Quando os dois branches mudaram as mesmas linhas, o git não consegue escolher e para com um conflito, que você resolve antes de o merge terminar; o [capítulo 18](18-worktrees.md#o-merge-e-o-conflito) o ensina, onde entregas paralelas se encontram.

## Desfazendo uma entrega

O `git revert <commit>` faz um commit novo que desfaz um anterior, e mantém o histórico: a entrega e o desfazer dela ficam os dois ali para ler.[^git-revert]

No trunk, logo depois do `f16f83b`, `git revert f16f83b` desfaria o `cancel-appointment` inteiro, a página incluída, já que são um commit só.
Commits posteriores que mudam as mesmas linhas fazem o revert parar com um conflito, o mesmo de um merge ([capítulo 18](18-worktrees.md#o-merge-e-o-conflito)).

Um commit de merge tem dois pais, então é preciso dizer ao git que lado manter.
`git revert -m 1 846e337` mantém o pai 1, o `main` como estava, e desfaz tudo o que o segundo pai trouxe: os sete commits do #246, em um commit novo.
O que ele desfaria é a diferença entre o pai 1 e o merge:

```
git diff --stat 846e337^1 846e337 | tail -1
```

```text
 19 files changed, 533 insertions(+), 94 deletions(-)
```

A documentação do git faz um alerta: depois que um merge é desfeito, um merge posterior do mesmo branch traz só os commits feitos nele depois daquele merge.[^git-revert]

Nada aqui rodou na clínica nem no fork: você mesmo roda no exercício 17.2.

## Trunk, e trunk-based development

O trunk do kit é uma pessoa fazendo commit no `main`, uma entrega de cada vez.
Trunk-based development é uma prática de equipe com o mesmo nome: todos fazem merge de mudanças pequenas no branch principal "*pelo menos uma vez a cada 24 horas*", muitas vezes por branches de vida curta revisados como pull requests,[^tbd] o que nos termos do kit é um branch por entrega com entregas pequenas.

## git-flow

O git-flow é o modelo de branches que Vincent Driessen publicou em 2010.[^git-flow]
Ele tem dois branches que vivem para sempre e três tipos que vêm e vão:

* `master` (hoje `main`) guarda só versões lançadas, cada merge nele um lançamento, com tag.
* `develop` guarda a próxima versão enquanto é construída.
* `feature/<nome>` começa do `develop` e volta para ele com `--no-ff`, pela razão dele: "*Desfazer uma feature inteira (isto é, um grupo de commits) é uma verdadeira dor de cabeça no segundo caso, enquanto é fácil se a flag `--no-ff` foi usada.*"[^git-flow] É a razão da tabela: um commit de merge, um revert.
* `release/<versão>` começa do `develop` para preparar um lançamento e entra tanto no `master` quanto no `develop`.
* `hotfix/<versão>` começa do `master` para corrigir uma versão lançada e entra nos dois.

Em 2020 ele acrescentou uma nota no topo do post: para software entregue continuamente, como um app web, que não volta atrás e não mantém várias versões em uso, um fluxo mais simples serve melhor; o git-flow ainda serve a software que lança versões explícitas ou mantém várias em uso.[^git-flow]

No kit, o git-flow é um branch por entrega cujo branch começa do `develop` e se chama `feature/<slug>`, e o slot Git do docs/05 diz isso.
Os branches de release e de hotfix são o trabalho de lançamento da equipe, que o kit não modela.
Este livro, uma pessoa, está no trunk; a clínica também estava até `book-v1/four-pieces`, e desde a sua entrega `git-worktrees` ela constrói um worktree por entrega ([capítulo 18](18-worktrees.md)); o CLAHub, uma equipe que faz merge de pull requests no `main`, é um branch por entrega.

## Pontos-chave

* Um controle de versão guarda todas as versões dos arquivos de um projeto, de qualquer tipo, com quem mudou o quê e quando; o git, feito em 2005 para o kernel do Linux, é distribuído, então cada clone tem o histórico inteiro.
* Um commit é um retrato com autor, mensagem e pais, nomeado por um hash; um branch é um nome que anda com cada commit feito nele; uma tag é um nome que nunca anda.
* Um fast-forward e um rebase deixam uma linha com os commits do branch; um commit de merge acrescenta um commit com dois pais; um squash merge deixa um commit novo com um pai.
* O `git revert` desfaz um commit com um commit novo e mantém o histórico; com um branch por entrega, faça o merge por commit de merge ou por squash, para que um revert desfaça a entrega (`git revert -m 1 <merge>` ou `git revert <commit>`), como um commit faz no trunk.
* O trunk do kit é uma pessoa no `main`; trunk-based development é uma equipe fazendo merge de mudanças pequenas todo dia; o git-flow serve a software que lança versões explícitas, e no kit é um branch por entrega a partir do `develop`.

## Exercícios

Estes exercícios usam o seu clone da clínica em `book-v1/four-pieces`, em um branch seu (`git switch -c mine book-v1/four-pieces`).
São comandos de git que você mesmo roda, já que o agente nunca faz commit nem merge.

### Exercício 17.1

Crie um branch `try-merge` a partir do `mine`, faça dois commits pequenos nele, e volte para o `mine`.
Traga o `try-merge` para o `mine` quatro vezes, voltando com `git reset --hard book-v1/four-pieces` entre as tentativas: `git merge --ff-only`, `git merge --no-ff`, `git merge --squash` e um `git commit`, e `git rebase mine` no `try-merge` seguido de `git merge --ff-only` no `mine`.
Depois de cada uma, leia o `git log --oneline --graph` e escreva quantos reverts desfazem as duas mudanças.

### Exercício 17.2

Refaça a tentativa com `--no-ff`, rode `git revert -m 1 HEAD`, depois `git diff book-v1/four-pieces`, e diga por que ele não imprime nada.
Depois `git switch -c undo-cancel f16f83b`, `git revert HEAD`, e diga por que `git diff 442f88a` não imprime nada.

### Exercício 17.3

No fork em `book-v1`, encontre um pull request que entrou como commit de merge e um que entrou com squash, e escreva o comando que desfaz cada um.
Nada é rodado.

[^pro-git-about]: Scott Chacon e Ben Straub, "About Version Control", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control>
[^pro-git-history]: Scott Chacon e Ben Straub, "A Short History of Git", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git>
[^gitattributes]: Git, "gitattributes", a documentação, o atributo `merge`, acesso em 2026-09-30. <https://git-scm.com/docs/gitattributes>
[^pro-git-branching]: Scott Chacon e Ben Straub, "Basic Branching and Merging", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>
[^pro-git-rebasing]: Scott Chacon e Ben Straub, "Rebasing", seção "The Perils of Rebasing", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Rebasing>
[^git-revert]: Git, "git-revert", a documentação, opção `-m`, acesso em 2026-09-30. <https://git-scm.com/docs/git-revert>
[^tbd]: Paul Hammant, "Trunk Based Development", seção "Elaboration, Claims and Caveats", acesso em 2026-09-30. <https://trunkbaseddevelopment.com/>
[^git-flow]: Vincent Driessen, "A successful Git branching model", 2010, com a sua "Note of reflection" de 2020. <https://nvie.com/posts/a-successful-git-branching-model/>
