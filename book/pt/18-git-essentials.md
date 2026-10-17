# 18. Git essencial

Depois deste capítulo você consegue manter cada entrega a um passo de ser desfeita, um commit no trunk ou um merge nos outros casos, e desfazê-la com `git revert`.
Você também consegue dizer o que um controle de versão guarda e quem criou o git, ler um histórico de commits, branches e merges, fazer o merge de um branch de cada uma das quatro formas que o git oferece, e escolher entre o trunk, um branch por entrega, um worktree por entrega e o git-flow para um projeto.

## O problema

Um projeto muda todo dia, e cedo ou tarde alguém pergunta como ele estava na semana passada, quem mudou uma linha, ou como desfazer a mudança de ontem sem perder a de hoje.
Sem um registro de cada versão, a resposta é a memória de alguém.
Com agentes escrevendo boa parte da mudança, o registro importa mais: cada entrega precisa ser uma peça que você consegue ler, e uma peça que você consegue desfazer.

## Uma entrega, um passo para desfazer

O kit pede uma coisa ao git: uma entrega, um passo para desfazer.
No trunk uma entrega é um commit, e `git revert <commit>` a desfaz; em um branch, a entrega pode ter vários commits, e a forma do merge decide se um passo ainda a desfaz.
O git faz o merge de um branch de quatro formas, e isto é o que cada uma deixa e o que desfazer uma entrega de vários commits exige depois:

| Forma | O que chega ao branch que recebe | Desfazer uma entrega de vários commits |
|---|---|---|
| Fast-forward | Os commits, como eram | Um `git revert` por commit |
| Commit de merge | Os commits, e um commit com dois pais | `git revert -m 1 <merge>` |
| Squash merge | Um commit novo | `git revert <commit>` |
| Rebase, depois fast-forward | Os commits, reescritos | Um `git revert` por commit |

Com um branch por entrega, faça o merge por commit de merge ou por squash, para que a entrega continue uma unidade de trabalho que um `git revert` desfaz.
Um fast-forward ou um rebase só mantém isso quando o branch tinha um commit.
As seções abaixo definem cada termo da tabela: as quatro formas, e depois o `git revert`.

## Commits e o histórico

Um controle de versão é um sistema que registra as mudanças em um conjunto de arquivos ao longo do tempo, para que você possa trazer de volta qualquer versão anterior.[^pro-git-about]
Ele guarda cada versão, cada uma com quem a mudou, quando e por quê, então você consegue comparar duas versões, descobrir quem introduziu um problema e quando, e deixar um arquivo ou o projeto inteiro como estava.[^pro-git-about]
Onde os primeiros sistemas guardavam o histórico em um servidor, o git é distribuído: cada cópia do projeto guarda o histórico inteiro, e qualquer cópia consegue restaurar o servidor se ele se perder.[^pro-git-about]
Linus Torvalds, que criou o Linux, e a comunidade do kernel escreveram o git em 2005 para guardar o histórico do kernel, quando a ferramenta que usavam deixou de ser gratuita para eles, e o escreveram para ser rápido e para muitas linhas de trabalho ao mesmo tempo.[^pro-git-history]

Um repositório é um projeto sob o git: os seus arquivos e, em uma pasta oculta `.git`, o seu histórico inteiro.
Um commit é uma foto salva do projeto inteiro, com o seu autor, a sua mensagem e o commit ou os commits de onde ele veio, os seus pais.
Ele tem como nome um hash, uma longa sequência hexadecimal calculada a partir de tudo isso, que o git imprime encurtada nos primeiros caracteres.
O histórico é a cadeia de pais, do último commit de volta ao primeiro.

`git log --oneline` o imprime com um commit por linha, o mais novo primeiro.
Para a biblioteca de empréstimos da Parte I ele poderia ficar assim; a saída é uma ilustração, escrita para este capítulo:

```text
a41c9e2 Permite devolver um exemplar (devolver-livro)
7d03b18 Empresta um exemplar, e recusa pelas regras (emprestar-livro)
2f6e5a1 Início: documentos e primeiro marco
```

Cada linha é uma entrega, e a sua mensagem diz o que um usuário agora consegue fazer, com o slug da entrega no fim.
`git show <hash>` abre uma delas: a mensagem, e cada linha que ela acrescentou e removeu.

A página de uma entrega e a sua construção são uma mudança.
O código, os testes, os documentos que a entrega atualizou e a sua página em `work/done/` entram no mesmo commit, então o histórico guarda a decisão e a mudança que ela fez lado a lado, e desfazer a entrega desfaz tudo de uma vez.
O agente coloca essa mudança em stage e sugere a mensagem; você a lê e faz o commit, e esse commit é a sua revisão.

Um remoto é outra cópia do repositório que a sua conhece por um nome, em geral em um servidor como o GitHub, chamado `origin` por convenção: `git clone <url>` o copia para a sua máquina com o histórico inteiro, `git push` envia para ele os commits novos do seu branch, e `git pull` traz os commits novos dele para o seu branch.
Um time compartilha o seu trabalho assim, e o pull request do capítulo 20, que pede que um branch enviado seja revisado e passe por merge, parte daqui.

## Branches e tags

Um branch é um nome que aponta para um commit e anda para cada commit novo feito nele.
O git foi feito para "*milhares de branches em paralelo*", e um branch é só um nome, e por isso não custa nada.[^pro-git-history]
`main` é um branch; `git switch -c <name>` cria outro no commit em que você está e muda para ele, e `git branch` lista os branches, com um `*` antes do seu.
Dois branches que começam no mesmo commit e ganham commits cada um têm dois históricos que compartilham o começo: um merge os junta de novo.

Uma tag é um nome fixo em um commit, que nunca anda.
Um projeto põe tags nas suas versões lançadas, `v1.0`, `v1.1`, para que "o que lançamos na v1.0" esteja a um comando de distância, enquanto o `main` segue em frente.

`HEAD` é o commit em que você está: em geral o último commit do seu branch, que anda com ele.

## Quatro formas de fazer merge

Um merge traz os commits de um branch para outro.
Digamos que você criou um branch `try` a partir do `main`, fez commits nele, e agora o traz para o `main`, o branch que recebe.
O git oferece quatro formas, e cada uma deixa um histórico diferente.[^pro-git-branching]

### Fast-forward

Se o `main` não tem nenhum commit próprio desde que o `try` saiu dele, o git pode simplesmente mover o nome `main` para a frente, até o último commit do `try`.
Isso é um fast-forward (avanço direto), e ele não faz nenhum commit:

```
git switch main
git merge --ff-only try
```

`--ff-only` se recusa a fazer o merge quando um fast-forward não é possível, então você sabe qual forma obteve.
O histórico continua uma linha, e o `main` agora guarda os commits do `try` exatamente como eram.

### Rebase, depois fast-forward

Se o `main` seguiu em frente, um fast-forward é impossível.
Um rebase reescreve os commits do `try` em cima do último commit do `main`, como commits novos com hashes novos, e então um fast-forward volta a ser possível:

```
git switch try
git rebase main
git switch main
git merge --ff-only try
```

O histórico volta a ser uma linha.
O rebase tem uma regra, do *Pro Git*: "*Não faça rebase de commits que existem fora do seu repositório e sobre os quais outras pessoas podem ter baseado trabalho.*"[^pro-git-rebasing]
Um rebase abandona os commits antigos, então quem construiu em cima deles precisa fazer o merge do seu trabalho de novo.
Só faça rebase de commits que ninguém mais tem.

### Commit de merge

Um commit de merge é um commit com dois pais, o último commit do branch que recebe e o do branch que entra, que traz o branch inteiro:

```
git switch main
git merge --no-ff try
```

`--no-ff` faz o commit de merge mesmo quando um fast-forward era possível.
Os commits do próprio branch ficam no histórico, legíveis um a um, e o commit de merge marca onde o branch inteiro entrou.
`git log --oneline --graph` desenha os pais como linhas, e um commit de merge é onde duas linhas se juntam.

### Squash merge

Um squash merge (merge compactado) escreve a mudança inteira do branch como um commit novo com um pai só:

```
git switch main
git merge --squash try
git commit
```

`--squash` coloca a mudança em stage e não faz nenhum commit; o seu `git commit` o faz.
Os commits do próprio branch não chegam ao `main`: só este commit chega.

Quando os dois branches mudaram as mesmas linhas, o git não consegue escolher e para com um conflito, que você resolve antes de o merge terminar; o [capítulo 19](19-worktrees.md) ensina isso, onde entregas em paralelo se encontram.

## Desfazer uma entrega

`git revert <commit>` faz um commit novo que desfaz um anterior, e mantém o histórico: a entrega e o seu desfazer estão os dois lá para ler.[^git-revert]
No trunk ele desfaz uma entrega inteira, a página incluída.
Commits posteriores que mudaram as mesmas linhas fazem o `git revert` parar com um conflito, resolvido do mesmo jeito que o de um merge.

Um commit de merge tem dois pais, então o git precisa saber qual lado manter.
`git revert -m 1 <merge>` mantém o pai 1, o branch que recebeu como estava, e desfaz tudo o que o segundo pai trouxe, cada commit do branch, em um commit novo.[^git-revert]
A documentação do git acrescenta um cuidado: depois que um merge é desfeito, um merge posterior do mesmo branch traz só os commits feitos nele depois daquele merge.[^git-revert]

O `git revert` é o jeito de desfazer qualquer coisa já compartilhada.
`git reset --hard <commit>` também volta, movendo o branch e descartando os commits depois dele; isso reescreve o histórico, então é a regra do rebase de novo: só em commits que ninguém mais tem.

## Trunk

O trunk do kit é uma pessoa fazendo commits no `main`, um commit por entrega, sozinha ou com vários agentes abertos ao mesmo tempo em entregas que mexem em arquivos diferentes (capítulo 19): uma linha, onde cada commit é uma entrega e cada `git revert` desfaz uma.
Trunk-based development (desenvolvimento baseado no tronco) é uma prática de time com o mesmo nome, descrita por Paul Hammant: todos fazem o merge de mudanças pequenas no branch principal "*pelo menos uma vez a cada 24 horas*", muitas vezes por branches de vida curta revisados como pull requests.[^tbd]
Nos termos do kit, isso é um branch por entrega com entregas pequenas, cada uma com merge por commit de merge ou por squash.

## git-flow

O git-flow é o modelo de branches que Vincent Driessen publicou em 2010: dois branches que vivem para sempre, `master` (hoje `main`) para as versões lançadas e `develop` para a próxima, e três tipos que vêm e vão, branches `feature/` que voltam para o `develop` por commit de merge, para que uma feature inteira seja fácil de desfazer, e branches `release/` e `hotfix/` que preparam e corrigem um lançamento.[^git-flow]
Em 2020 ele acrescentou uma nota no topo do post: para software entregue continuamente, como um app web, que não volta atrás e não mantém várias versões em uso, um fluxo mais simples serve melhor; o git-flow ainda serve a software que lança versões explícitas ou mantém várias em uso.[^git-flow]
No kit, o git-flow é um branch por entrega cujo branch começa do `develop` e se chama `feature/<slug>`, e os seus branches de release e de hotfix são o trabalho de lançamento do time, que o kit não modela.

## Escolher

Um projeto escreve a sua escolha uma vez, no slot Git do seu docs/05, e todo comando a lê.

* **Trunk** serve a uma pessoa, sozinha ou com várias sessões abertas em linhas livres, linhas da fila prontas para construir, que mexem em arquivos diferentes: um commit por entrega no `main`, cada sessão colocando em stage só a sua entrega, e a pessoa fazendo o commit de uma entrega por vez.
  Não serve a duas pessoas: as entregas delas dividem um branch, e um commit leva o trabalho pela metade da outra.
* **Um branch por entrega** serve a trabalho em sequência revisado por pull request (capítulo 20): cada entrega com merge por commit de merge ou por squash.
* **Um worktree por entrega** serve a várias pessoas trabalhando ao mesmo tempo, ou a uma pessoa cujas entregas mexem nos mesmos arquivos ([capítulo 19](19-worktrees.md)): cada entrega no seu próprio branch, na sua própria pasta, com merge do mesmo jeito.
* **git-flow** serve a software que lança versões numeradas e mantém várias em uso.

Seja qual for, a regra é a mesma: uma entrega, um passo para desfazer, e a pessoa faz o commit e o merge, nunca o agente.
Este livro, escrito e revisado por uma pessoa, está no trunk.

## O que o time ganha

Cada entrega chega como um commit no trunk ou um merge nos outros casos, com a sua página ao lado do seu código, então desfazer uma entrega é um comando, e ler por que uma linha mudou é um commit que guarda tanto a mudança quanto a decisão.
A evidência é o próprio histórico: o log da biblioteca de empréstimos, mostrado antes neste capítulo, se lê como a lista do que os usuários conseguem fazer, uma linha por entrega e um `git revert` por linha, e uma pessoa que nunca abre o código consegue acompanhá-lo.

## Pontos-chave

* Uma entrega, um passo para desfazer: a página e a construção de uma entrega são uma mudança, um commit no trunk ou um merge nos outros casos, desfeita com `git revert <commit>` ou `git revert -m 1 <merge>`.
* Um controle de versão guarda cada versão dos arquivos de um projeto com quem mudou o quê e quando; o git, escrito em 2005 por Linus Torvalds e pela comunidade do kernel do Linux, é distribuído, então cada cópia guarda o histórico inteiro.
* Um commit é uma foto com autor, mensagem e pais, com um hash como nome; um branch é um nome que anda com cada commit feito nele; uma tag nunca anda; um remoto é outra cópia que você clona, para a qual dá push e da qual dá pull.
* Um fast-forward e um rebase deixam uma linha com os commits do branch; um commit de merge acrescenta um commit com dois pais; um squash merge deixa um commit novo; nunca faça rebase de commits que outra pessoa tem.
* O trunk serve a uma pessoa, sozinha ou com várias sessões em linhas livres que mexem em arquivos diferentes; um branch por entrega serve a trabalho em sequência revisado por pull request; um worktree por entrega serve a várias pessoas, ou a entregas que mexem nos mesmos arquivos; o git-flow serve a software que lança versões; o agente coloca em stage, a pessoa faz o commit e o merge.

[^pro-git-about]: Scott Chacon e Ben Straub, "About Version Control", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control>
[^pro-git-history]: Scott Chacon e Ben Straub, "A Short History of Git", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git>
[^pro-git-branching]: Scott Chacon e Ben Straub, "Basic Branching and Merging", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>
[^pro-git-rebasing]: Scott Chacon e Ben Straub, "Rebasing", seção "The Perils of Rebasing", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Rebasing>
[^git-revert]: Git, "git-revert", a documentação, opção `-m`, acesso em 2026-09-30. <https://git-scm.com/docs/git-revert>
[^tbd]: Paul Hammant, "Trunk Based Development", seção "Elaboration, Claims and Caveats", acesso em 2026-09-30. <https://trunkbaseddevelopment.com/>
[^git-flow]: Vincent Driessen, "A successful Git branching model", 2010, com a sua "Note of reflection" de 2020. <https://nvie.com/posts/a-successful-git-branching-model/>
