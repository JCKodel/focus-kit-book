# Git essencial

Depois deste capítulo você consegue dizer o que um controle de versão guarda e por que o git foi criado, ler um histórico de commits, branches e merges, e fazer o merge de um branch de cada uma das quatro formas que o git oferece.
Você também consegue desfazer uma entrega em um passo com `git revert`, e escolher entre o trunk, um branch por entrega e o git-flow para um projeto.

## O problema

Um projeto muda todo dia, e cedo ou tarde alguém pergunta como ele estava na semana passada, quem mudou uma linha, ou como desfazer a mudança de ontem sem perder a de hoje.
Sem um registro de cada versão, a resposta é a memória de alguém.
Com agentes escrevendo boa parte da mudança, o registro importa mais: cada entrega precisa ser uma peça que você consegue ler, e uma peça que você consegue desfazer.

## Controle de versão, e por que o git

Um controle de versão é um sistema que registra as mudanças em um conjunto de arquivos ao longo do tempo, para que você possa trazer de volta qualquer versão anterior.[^pro-git-about]
Ele guarda cada versão, cada uma com quem a mudou, quando e por quê, então você consegue comparar duas versões, descobrir quem introduziu um problema e quando, e deixar um arquivo ou o projeto inteiro como estava.[^pro-git-about]

Ele funciona com qualquer tipo de arquivo, e o *Pro Git* cita o designer que quer guardar cada versão de uma imagem ou de um layout entre os primeiros a ganhar com ele.[^pro-git-about]
Sem ele, as versões moram nos nomes dos arquivos, `logo final.psd`, `logo final final.psd`, `logo final agora vai.psd`, onde só quem os nomeou sabe qual é o último e nada diz o que mudou de um para o outro.
O *Pro Git* chama copiar arquivos para outra pasta de o jeito mais comum de guardar versões, porque é simples, e um jeito que convida a erros: é fácil esquecer em que pasta você está, escrever no arquivo errado ou copiar por cima de um que você queria guardar.[^pro-git-about]
Com controle de versão existe um `logo.psd`, e as versões anteriores dele estão no histórico, cada uma com o seu autor, a sua data e a sua mensagem.
Um limite para imagens: o git faz o merge de texto linha por linha, mas duas versões de um arquivo binário, como um `.psd`, ele não consegue combinar, então ele fica com a sua e marca o arquivo como um conflito, e as duas pessoas que o editaram escolhem qual versão fica.[^gitattributes]

Os primeiros sistemas guardavam o histórico em um servidor, do qual cada pessoa baixava os arquivos.
O git é distribuído: cada cópia do projeto guarda o histórico inteiro, e qualquer cópia consegue restaurar o servidor se ele se perder.[^pro-git-about]

O git foi criado para o kernel do Linux.
De 1991 a 2002, as mudanças no kernel passavam entre os seus desenvolvedores como patches e arquivos compactados; a partir de 2002 o projeto usou o BitKeeper, um sistema distribuído proprietário.[^pro-git-history]
Em 2005 a relação entre a comunidade do kernel e a empresa por trás do BitKeeper se rompeu, e a ferramenta deixou de ser gratuita para eles.[^pro-git-history]
Isso levou a comunidade, e em especial Linus Torvalds, que criou o Linux, a escrever a sua própria ferramenta, com o que tinham aprendido usando o BitKeeper e com estes objetivos: velocidade, um design simples, bom suporte a desenvolvimento não linear, "*milhares de branches em paralelo*", totalmente distribuída, e capaz de lidar com um projeto do tamanho do kernel.[^pro-git-history]
Esses objetivos são o motivo de um branch custar quase nada no git: ele é só um nome, como as seções abaixo mostram.

## Commits e o histórico

Um repositório é um projeto sob o git: os seus arquivos e, em uma pasta oculta `.git`, o seu histórico inteiro.
Um commit é uma foto salva do projeto inteiro, com o seu autor, a sua mensagem e o commit ou os commits de onde ele veio, os seus pais.
Ele tem como nome um hash, uma longa sequência hexadecimal calculada a partir de tudo isso, que o git imprime encurtada nos primeiros caracteres.
O histórico é a cadeia de pais, do último commit de volta ao primeiro.

`git log --oneline` o imprime com um commit por linha, o mais novo primeiro.
Para a biblioteca de empréstimos da Parte I ele poderia ficar assim; a saída é uma ilustração, escrita para este capítulo:

```text
a41c9e2 Permite que um membro devolva um exemplar (devolver-livro)
7d03b18 Permite que a bibliotecária empreste um exemplar e recusa quando as regras dizem não (emprestar-livro)
2f6e5a1 Início: documentos e primeiro marco
```

Cada linha é uma entrega, e a sua mensagem diz o que um usuário agora consegue fazer, com o slug da entrega no fim (o capítulo 14 dá nome às entregas por slug).
`git show <hash>` abre uma delas: a mensagem, e cada linha que ela acrescentou e removeu.

O kit mantém uma regra aqui: a página de uma entrega e a sua construção são uma mudança.
O código, os testes, os documentos que a entrega atualizou e a sua página em `work/done/` entram no mesmo commit, então o histórico guarda a decisão e a mudança que ela fez lado a lado, e desfazer a entrega desfaz tudo de uma vez.
O agente coloca essa mudança em stage e sugere a mensagem; você a lê e faz o commit, e esse commit é a sua revisão ([capítulo 15](15-apply.md)).

## Branches e tags

Um branch é um nome que aponta para um commit e anda para cada commit novo feito nele.
`main` é um branch; `git switch -c <name>` cria outro no commit em que você está e muda para ele, e `git branch` lista os branches, com um `*` antes do seu.
Dois branches que começam no mesmo commit e ganham commits cada um têm dois históricos que compartilham o começo: um merge os junta de novo.

Uma tag é um nome fixo em um commit, que nunca anda.
Um projeto põe tags nas suas versões lançadas, `v1.0`, `v1.1`, para que "o que lançamos na v1.0" esteja a um comando de distância, enquanto o `main` segue em frente.

`HEAD` é o commit em que você está: em geral o último commit do seu branch, que anda com ele.

## Remotos: clone, push e pull

Um remoto é outra cópia do repositório que a sua conhece por um nome, em geral um servidor como o GitHub, e por convenção chamado `origin`.
`git clone <url>` copia um remoto para a sua máquina, com o histórico inteiro, e o guarda como `origin`.
`git push` envia os commits novos do seu branch para o remoto; `git pull` traz os commits novos do remoto para o seu branch.
Um time compartilha o seu trabalho assim: cada pessoa faz commits na sua própria cópia e dá push, e os outros dão pull.
O capítulo 21 parte daqui, com o pull request que pede que um branch enviado seja revisado e passe por merge.

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

### As quatro lado a lado

Uma entrega de vários commits, com o merge feito de cada forma, e o que desfazê-la exige, com o `git revert` da próxima seção:

| Forma | O que chega ao branch que recebe | Desfazer uma entrega de vários commits |
|---|---|---|
| Fast-forward | Os commits, como eram | Um `git revert` por commit |
| Commit de merge | Os commits, e um commit com dois pais | `git revert -m 1 <merge>` |
| Squash merge | Um commit novo | `git revert <commit>` |
| Rebase, depois fast-forward | Os commits, reescritos | Um `git revert` por commit |

Com um branch por entrega, faça o merge por commit de merge ou por squash, para que a entrega continue uma unidade de trabalho que um `git revert` desfaz.
Um fast-forward ou um rebase só mantém isso quando o branch tinha um commit.

Quando os dois branches mudaram as mesmas linhas, o git não consegue escolher e para com um conflito, que você resolve antes de o merge terminar; o [capítulo 20](20-worktrees.md) ensina isso, onde entregas em paralelo se encontram.

## Desfazer uma entrega

`git revert <commit>` faz um commit novo que desfaz um anterior, e mantém o histórico: a entrega e o seu desfazer estão os dois lá para ler.[^git-revert]
No trunk, uma entrega é um commit, então `git revert <commit>` desfaz a entrega inteira, a página incluída.
Commits posteriores que mudaram as mesmas linhas fazem o `git revert` parar com um conflito, resolvido do mesmo jeito que o de um merge.

Um commit de merge tem dois pais, então o git precisa saber qual lado manter.
`git revert -m 1 <merge>` mantém o pai 1, o branch que recebeu como estava, e desfaz tudo o que o segundo pai trouxe, cada commit do branch, em um commit novo.[^git-revert]
A documentação do git acrescenta um cuidado: depois que um merge é desfeito, um merge posterior do mesmo branch traz só os commits feitos nele depois daquele merge.[^git-revert]

O `git revert` é o jeito de desfazer qualquer coisa já compartilhada.
`git reset --hard <commit>` também volta, movendo o branch e descartando os commits depois dele; isso reescreve o histórico, então é a regra do rebase de novo: só em commits que ninguém mais tem.

## Trunk, e trunk-based development

O trunk do kit é uma pessoa fazendo commits no `main`, uma entrega por vez, um commit por entrega.
É o histórico mais simples que existe: uma linha, onde cada commit é uma entrega e cada `git revert` desfaz uma.

Trunk-based development (desenvolvimento baseado no tronco) é uma prática de time com o mesmo nome, descrita por Paul Hammant: todos fazem o merge de mudanças pequenas no branch principal "*pelo menos uma vez a cada 24 horas*", muitas vezes por branches de vida curta revisados como pull requests.[^tbd]
Nos termos do kit, isso é um branch por entrega com entregas pequenas, cada uma com merge por commit de merge ou por squash.

## git-flow

O git-flow é o modelo de branches que Vincent Driessen publicou em 2010.[^git-flow]
Ele tem dois branches que vivem para sempre e três tipos que vêm e vão:

* `master` (hoje `main`) guarda só versões lançadas, cada merge nele um lançamento, com tag.
* `develop` guarda a próxima versão enquanto ela é construída.
* `feature/<name>` começa do `develop` e volta para ele com `--no-ff`, pela razão dele: "*Desfazer uma feature inteira (isto é, um grupo de commits) é uma verdadeira dor de cabeça no segundo caso, enquanto é fácil se a flag `--no-ff` foi usada.*"[^git-flow] É a razão da tabela: um commit de merge, um `git revert`.
* `release/<version>` começa do `develop` para preparar um lançamento e entra por merge tanto no `master` quanto no `develop`.
* `hotfix/<version>` começa do `master` para corrigir uma versão lançada e entra por merge nos dois.

Em 2020 ele acrescentou uma nota no topo do post: para software entregue continuamente, como um app web, que não volta atrás e não mantém várias versões em uso, um fluxo mais simples serve melhor; o git-flow ainda serve a software que lança versões explícitas ou mantém várias em uso.[^git-flow]

No kit, o git-flow é um branch por entrega cujo branch começa do `develop` e se chama `feature/<slug>`.
Os branches de release e de hotfix são o trabalho de lançamento do time, que o kit não modela.

## Escolher

Um projeto escreve a sua escolha uma vez, no slot Git do seu docs/05 ([capítulo 10](10-the-documents.md)), e todo comando a lê.

* **Trunk** serve a uma pessoa, ou a uma pessoa por vez: um commit por entrega no `main`.
* **Um branch por entrega** serve a um time, ou a uma pessoa rodando agentes em paralelo ([capítulo 20](20-worktrees.md)): cada entrega com merge por commit de merge ou por squash, em geral por um pull request (capítulo 21).
* **git-flow** serve a software que lança versões numeradas e mantém várias em uso.

Seja qual for, a regra é a mesma: uma entrega, um passo para desfazer, e a pessoa faz o commit e o merge, nunca o agente.
Este livro, escrito e revisado por uma pessoa, está no trunk.

## O que o time ganha

Cada entrega chega como um commit no trunk ou um merge nos outros casos, com a sua página ao lado do seu código, então desfazer uma entrega é um comando, e ler por que uma linha mudou é um commit que guarda tanto a mudança quanto a decisão.
O histórico se lê como a lista do que os usuários conseguem fazer, uma linha por entrega, e uma pessoa que nunca abre o código consegue acompanhá-lo.
Não há número para este ganho: ele é uma propriedade da forma do histórico, e nenhuma medição foi feita.

## Pontos-chave

* Um controle de versão guarda cada versão dos arquivos de um projeto, de qualquer tipo, com quem mudou o quê e quando; o git, criado em 2005 para o kernel do Linux, é distribuído, então cada cópia guarda o histórico inteiro.
* Um commit é uma foto com autor, mensagem e pais, com um hash como nome; um branch é um nome que anda com cada commit feito nele; uma tag nunca anda; um remoto é outra cópia que você clona, para a qual dá push e da qual dá pull.
* Um fast-forward e um rebase deixam uma linha com os commits do branch; um commit de merge acrescenta um commit com dois pais; um squash merge deixa um commit novo; nunca faça rebase de commits que outra pessoa tem.
* A página e a construção de uma entrega são uma mudança: um commit no trunk, um merge nos outros casos, desfeita com `git revert <commit>` ou `git revert -m 1 <merge>`.
* O trunk serve a uma pessoa; um branch por entrega serve a um time ou a agentes em paralelo; o git-flow serve a software que lança versões; o agente coloca em stage, a pessoa faz o commit e o merge.

[^pro-git-about]: Scott Chacon e Ben Straub, "About Version Control", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control>
[^pro-git-history]: Scott Chacon e Ben Straub, "A Short History of Git", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git>
[^gitattributes]: Git, "gitattributes", a documentação, o atributo `merge`, acesso em 2026-09-30. <https://git-scm.com/docs/gitattributes>
[^pro-git-branching]: Scott Chacon e Ben Straub, "Basic Branching and Merging", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>
[^pro-git-rebasing]: Scott Chacon e Ben Straub, "Rebasing", seção "The Perils of Rebasing", *Pro Git*, 2ª ed., acesso em 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Rebasing>
[^git-revert]: Git, "git-revert", a documentação, opção `-m`, acesso em 2026-09-30. <https://git-scm.com/docs/git-revert>
[^tbd]: Paul Hammant, "Trunk Based Development", seção "Elaboration, Claims and Caveats", acesso em 2026-09-30. <https://trunkbaseddevelopment.com/>
[^git-flow]: Vincent Driessen, "A successful Git branching model", 2010, com a sua "Note of reflection" de 2020. <https://nvie.com/posts/a-successful-git-branching-model/>
