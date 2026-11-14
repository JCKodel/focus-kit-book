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
Uma linha livre é uma linha da fila que não está feita, não está esperando e cujo `· after` deixa o próximo comando dela começar ([o capítulo 14](14-queue-states.md) ensina as marcas da fila).

Digamos que a biblioteca de empréstimos tem duas linhas livres: `devolver-livro`, que mexe em `src/features/emprestimos/`, e `lista-de-atrasos`, que mexe em `src/features/relatorios/`; os slugs e os caminhos são uma ilustração, escrita para este capítulo.
Os arquivos de código delas não se encontram.
As duas marcam o docs/06, a fila, mas cada uma marca só a sua própria linha.
O `git add -p` oferece um arquivo para o stage em hunks, pedaços separados de uma mudança: duas linhas distantes são dois hunks, duas linhas vizinhas são um, e cada sessão ainda coloca em stage só a sua própria linha, com o `stage` do script de marca do kit, que muda essa linha no índice e nada mais ali ([capítulo 14](14-queue-states.md)).
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
A fila não se divide com `s` quando as duas linhas são vizinhas, já que `git restore --staged -p` divide um hunk como o `git add -p` divide;[^git-restore] então `git restore --staged docs/06-Queue.md` tira o arquivo inteiro, você pede à sessão desta entrega que coloque a sua própria linha em stage de novo, com o `stage` do script de marca, e faz o commit.
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

Então a sessão para e relata, e a decisão é sua: ordenar as duas linhas, escrevendo `· after <slug>` na que precisa esperar a outra; um worktree não o desfaz, já que o `/apply` faz a mesma verificação em um worktree.

## O que é um worktree e quando ele compensa

Um worktree é uma pasta de trabalho extra do mesmo repositório git, com o seu próprio branch.
Nas palavras da documentação do git: "*Um repositório git pode ter várias árvores de trabalho, o que permite fazer checkout de mais de um branch ao mesmo tempo.*"[^git-worktree]
A pasta que você clonou é o worktree principal, aquele cuja pasta `.git` guarda o histórico: os commits, os branches e as tags.
`git worktree add` cria outra pasta, faz checkout de um branch nela, e deixa lá um pequeno arquivo `.git` que aponta de volta para onde o histórico mora.
Todos os worktrees compartilham o histórico; cada um tem os seus próprios arquivos, o seu próprio `HEAD` (o commit em que ele está) e o seu próprio índice, aquele em que toda sessão aberta naquela pasta coloca em stage.[^git-worktree]
Então um commit feito em um worktree aparece na hora em todos os outros, sem push e sem pull, enquanto o que você muda ou coloca em stage em um nunca aparece em outro.
O git também se recusa a fazer checkout de um branch em dois worktrees, então duas pastas nunca escrevem no mesmo branch.[^git-worktree]

Um worktree por entrega compensa em dois casos: várias pessoas trabalhando ao mesmo tempo, já que um commit em um branch compartilhado levaria o trabalho pela metade de outra pessoa; e uma pessoa cujas entregas mexem nos mesmos arquivos, para que cada uma seja definida e construída no seu próprio branch e as suas mudanças só se encontrem no merge, uma construção depois da outra, já que o `/apply` não começa em arquivos que outra construção está mudando, em um worktree como em uma pasta ([capítulo 14](14-queue-states.md)).
Um branch por entrega em uma pasta não basta: a pasta guarda um branch por vez, e trocar de branch enquanto um agente tem trabalho ainda sem commit leva esse trabalho junto ou para até o `git stash` guardá-lo de lado.
Um segundo clone dá a cada agente a sua própria pasta, mas com a sua própria cópia do histórico inteiro no disco, que só encontra a do outro por um push e um pull.

Digamos que `devolver-livro` e `lista-de-atrasos` precisam as duas de `src/features/emprestimos/`, na pasta da biblioteca de empréstimos, `biblioteca/`, cujo `main/` guarda o branch `main` (a próxima seção a monta):

* O agente que constrói `devolver-livro` trabalha em `biblioteca/.focus-kit/worktrees/devolver-livro`, no branch `focus-kit/devolver-livro`; ele vê só as mudanças dessa entrega, e o commit que você faz ali guarda essa entrega e nada mais.
* A `lista-de-atrasos` é definida enquanto isso em `biblioteca/.focus-kit/worktrees/lista-de-atrasos`, no `focus-kit/lista-de-atrasos`, e o `/apply` dela ali para antes da primeira edição enquanto a construção de `devolver-livro` está em andamento ou ainda sem merge, já que as duas tocam `src/features/emprestimos/`; ela é construída quando `devolver-livro` passa pelo merge em `main`.
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
O próprio contêiner não é um checkout: ele guarda `main/` e `.focus-kit/`, mas nenhum `AGENTS.md`, nenhum documento e nenhum comando, então uma sessão aberta ali não tem nada do que o kit lê; toda sessão abre em `main/` ou em um worktree.

Um projeto que escolhe isso escreve esses passos em um manual de `docs/manuals/` ([capítulo 7](07-the-documents.md)), para que quem o clonar depois monte o mesmo contêiner.

O mesmo manual diz como o seu host deixa uma sessão em `main/` editar os worktrees, já que o `/propose` roda ali e escreve a página no worktree da entrega; no Claude Code é uma configuração no `.claude/settings.json` de `main/`, onde `../.focus-kit/worktrees` é a pasta dos worktrees vista de `main/`:

```json
{
  "permissions": {
    "additionalDirectories": ["../.focus-kit/worktrees"]
  }
}
```

Ela soma os worktrees às pastas que a sessão lê e edita, sob as mesmas regras de `main/`, e não carrega nenhum dos comandos que cada worktree guarda, que uma sessão em `main/` já tem: pastas listadas ali "*concedem só acesso a arquivos*".[^claude-code-permissions]

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
O `/propose <slug>` faz fetch do origin e procura ali `<prefixo><slug>`, o prefixo e o slug juntos, `focus-kit/devolver-livro` com o prefixo padrão `focus-kit/`; quando o origin não tem esse branch, ele cria o worktree em `<oculta>/worktrees/<slug>/` nele, a partir do branch principal do origin como acabou de buscar, então um clone que não fez pull parte mesmo assim do que está integrado, e dá push no branch na hora, então a linha fica ocupada em todo clone; ele reabre um worktree que este clone já tem, e escreve a página ali.
O `[~]` da linha e cada marca seguinte são escritos no worktree, no seu branch, então a fila de `main/` mostra a linha como estava e a fila de cada worktree mostra o estado do seu próprio branch; o merge traz as marcas, e é por isso que a fila se encontra em todo merge, como a próxima seção, sobre conflitos, mostra.
O [capítulo 14](14-queue-states.md) diz onde um quadro as vê.

Então nenhuma fila de pasta mostra todas as entregas de uma vez, e perguntar a uma delas quais linhas estão ocupadas dá uma resposta errada: em `main/`, uma linha em andamento no seu branch ainda aparece `[ ]`.
O script de fila do kit (capítulo 14) lê a linha de cada entrega de uma vez, de `main/` ou de qualquer worktree, quando recebe a palavra do slot Git: `git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq worktree .focus-kit focus-kit/`, ou a pasta oculta e o prefixo que o slot nomeia.
Ele faz fetch do origin, lê cada linha da cópia do branch principal, a própria fila de `main/` quando roda em `main/` e o branch padrão no origin quando roda em um worktree, e a linha de cada entrega de `origin/<prefixo><slug>`, e não edita nada.
Um branch no origin é a reivindicação: uma linha cujo branch existe está ocupada, e enquanto a cópia do branch ainda diz `[ ]`, já que o `[~]` nunca precisa ter commit, a árvore a mostra `claimed, progress unknown: propose in flight`.
A cópia que o branch tem da linha do seu slug é a atual até o merge do branch no branch principal do origin, e a cópia do branch principal depois dele, então em `main/` faça pull depois de um merge; um `[?]` em qualquer cópia, a do branch principal ou a de um branch, mostra a linha travada até ela estar `[x]`.
Um `[x]` em um branch ainda sem merge aparece `built, awaiting integration`, e uma linha cujo `after` o nomeia espera com `devolver-livro built, not integrated`, por exemplo, já que a construção dela precisa desse código no branch principal.
Na biblioteca, com `devolver-livro` sendo construída no seu worktree em `[*]`, `lista-de-atrasos` definida no dela em `[>]`, cada marca com commit no branch da linha e push feitos por você, e a fila de `main/` ainda mostrando as duas linhas `[ ]`, o script rodado em `main/` imprime isto; a fila e a execução foram escritas para este capítulo:

```
milestone: M2. Devoluções
[*] devolver-livro · in flight: apply
[>] lista-de-atrasos · apply now
 └[ ] m2-review + after devolver-livro · propose now
[ ] exemplar-danificado (only on branch devolver-livro) · propose now

free for /apply, in order: lista-de-atrasos
free for /propose, in order: m2-review exemplar-danificado
next: /apply lista-de-atrasos
```

A linha de cada entrega vem do seu branch: `devolver-livro` está em andamento, e `lista-de-atrasos` está definida e livre para o `/apply`, a primeira linha livre, então o `next:` a nomeia.
O script lê marcas e `after`, não arquivos: o `/apply lista-de-atrasos`, aberto no worktree dela, compara os arquivos da sua página com a construção de `devolver-livro`, encontra `src/features/emprestimos/` nas duas, e para antes da primeira edição, deixando a linha `[>]`; ela é construída quando `devolver-livro` passa pelo merge, como em uma pasta (capítulo 14).
`m2-review`, a revisão do marco, fica sob `lista-de-atrasos` com `+ after devolver-livro`, livre para o `/propose`, já que toda linha que o seu `after all` nomeia está definida.
`exemplar-danificado` é uma linha que a sessão de `devolver-livro` acrescentou no seu branch, ainda em nenhuma fila de `main/`: o script a mostra no fim do seu marco, nomeando entre parênteses um branch que a tem, e a oferece como qualquer outra linha.

A cópia atual conta nos worktrees também.
Depois que `devolver-livro` passa pelo merge em `main` e pelo push, a fila no worktree de `lista-de-atrasos`, cujo branch começou antes do merge, ainda mostra `devolver-livro` como `[ ]`; o script lê a cópia do branch principal no origin, agora a atual, a encontra `[x]` e deixa a linha fora da árvore.
Digitado com `trunk` nesse worktree, o script não faz fetch de nada e lê só a cópia da própria pasta, então oferece `devolver-livro`, já com merge, como `propose now`: em um layout de worktrees, a palavra tem de ser a do slot Git.

O script lê os branches no origin, como no último fetch.
Uma marca com commit em um worktree e sem push, ou um branch que nunca teve push, não são vistos de outra pasta; quando o `git fetch` falha, o script imprime `note: git fetch origin failed; branches as last fetched` e desenha a árvore com o que buscou antes.
E por padrão nenhuma marca chega ao origin antes de você fazer o commit no branch da entrega e o push dele: o `/propose` e o `/apply` escrevem cada marca no worktree e não fazem commit de nada por conta própria, e depois da reivindicação só você faz push, ou pede um.
As marcas do exemplo chegaram lá por esse passo, seu e fora do padrão; sem ele, da reivindicação até o seu commit e push, a árvore lê só o branch e imprime `[ ] lista-de-atrasos · claimed, progress unknown: propose in flight`, livre para nenhum comando.
Uma linha cujo branch está no origin nunca está livre para o `/propose`, digam o que disserem as marcas dela; o que o script de reivindicação responde para ela vem adiante.

Um branch `<slug>` sem o prefixo não é o da entrega: é de outra pessoa.
Você monta o contêiner uma vez; o kit cria cada worktree.
O `/propose` termina dando o caminho dessa pasta, e o `/apply <slug>` roda em uma sessão nova aberta nela, constrói a página, e coloca a mudança em stage.
Na biblioteca, depois do `/propose devolver-livro` em `main/`, você abre essa sessão em `biblioteca/.focus-kit/worktrees/devolver-livro`, a pasta que o `git worktree list` também imprime, e digita `/apply devolver-livro` ali.
Ela abre ali porque a página e o `[>]` da linha estão no branch da entrega, enquanto a fila de `main/` mostra a linha como estava até o merge, e o índice em que ela coloca a mudança em stage é o do worktree.
Aberto em qualquer outra pasta, `main/` incluída, o `/apply` para antes de qualquer edição e dá o caminho do worktree ([capítulo 13](13-apply.md)).
Por padrão, você usa a entrega, revisa e faz o commit no branch, faz o merge no `main` com `--no-ff`, remove o worktree e apaga o branch.

A consulta ao remoto, o worktree, o seu branch e o push são um script só, o script de reivindicação do kit, que o `/propose` roda como o [capítulo 13](13-apply.md) mostra, com `worktree .focus-kit focus-kit/`, ou a pasta oculta e o prefixo que o slot nomeia.
Antes de mudar qualquer coisa o script recusa, imprimindo `error:` com o motivo e saindo com 2 em vez de 0: fora de um repositório, com o `HEAD` destacado, para um slug com um caractere que um nome de branch não aceita, sem um remoto `origin`, quando o `git fetch` falha, quando não consegue saber qual é o branch padrão, e em qualquer branch que não seja o padrão.
Ele recusa também no worktree de outro slug ou em um branch de entrega: roda a partir de `main/`, como o `/propose`; rodado no worktree do próprio slug, responde `claim: here` com o caminho dessa pasta e não cria nada.
Sem parar, ele avisa quando o `main` está atrás ou à frente do origin, a entrega partindo do branch principal do origin mesmo assim, então commits do `main` ainda sem push não estão nela, e quando um branch `devolver-livro` sem o prefixo está no remoto, que não é o da entrega.
Quando o worktree existe mas o seu branch nunca chegou ao remoto, ele dá push no branch então, e quando um push falha ele diz que a linha não foi reivindicada.
Um branch no origin do qual este clone não tem branch é a linha de outro clone: o script responde `claim: taken`, sai com 2 e não cria nada, e só a abre quando o comando termina com `resume`, que o `/propose` acrescenta com a sua palavra, como quando você continua, nesta máquina, uma definição começada em outra; então ele imprime `claim: resumed`.
Um clone feito com `git clone --bare` guarda como seus todos os branches que o origin tinha naquele momento, então em um contêiner montado depois da reivindicação de uma linha o script encontra esse branch aqui e responde `existing`.
Ele imprime algumas linhas `chave: valor`, aqui para `devolver-livro`, nova, em um exemplo escrito para este capítulo:

```
claim: new
branch: focus-kit/devolver-livro, on origin
path: /projetos/biblioteca/.focus-kit/worktrees/devolver-livro
draft: none
```

O `claim` é `new`; `existing` quando o worktree ou o branch deste clone já estava lá; `existing, branch pushed now`; `resumed`; ou `here`; o `path` é a pasta em que a sessão do `/apply` abre; e o `draft` é `none` ou nomeia um rascunho da página que `main/` guarda para o slug, que o `/propose` traz para a entrega.

Quando o `/apply devolver-livro` trava no seu worktree esperando uma resposta que ninguém deu, ele para como o capítulo 13 diz: marca a linha `[?]` com `· resume: apply · blocked: e se o exemplar voltar danificado?`, escreve na página o que foi construído, e mostra uma mensagem parcial em um bloco `commit`.
Ali ele também pode colocar o trabalho parcial em stage para você fazer o commit no `focus-kit/devolver-livro` quando quiser, com essa mensagem: ela diz que é parcial, nomeia o que trava, nunca dá a entender que a verificação passou ou que a entrega está pronta, e a sua última linha é `work/devolver-livro.md`, onde a página espera.
Por padrão, esse commit é a única exceção a usar a entrega antes de fazer o commit dela: um commit de trabalho inacabado cuja mensagem diz isso; o commit que completa a entrega continua vindo depois de você usar a entrega inteira e ler o seu diff em stage.
Enquanto a linha está `[?]`, não faça o merge do branch, quem quer que peça: ele fica sem merge até a entrega estar pronta, então um só `git merge --no-ff` ainda leva a entrega inteira ao `main`.
Quando o `/apply` é retomado no mesmo worktree, uma pasta de trabalho limpa não quer dizer que nada foi construído: o trabalho até ali está nesses commits, e a revisão da entrega os lê contra a base do branch (capítulo 13).
No trunk não há commit parcial: um `/apply` travado não coloca nada em stage, e o trabalho fica sem commit até estar inteiro.

O agente nunca faz commit, merge ou push, nem resolve um conflito ou remove um worktree por conta própria, fora o branch em que o `/propose` dá push quando o cria ou não o encontra no remoto, a reivindicação da linha: cada passo que muda o histórico é decisão sua, como em toda estratégia de git; para o commit e o merge, o slot Git pode dizer que o agente os faz pela palavra do slot, que vale como o pedido, e você então revisa o commit ou o merge ([capítulo 7](07-the-documents.md)); todo push depois desse, o conflito e o worktree continuam esperando o seu pedido.
Peça, e ele dá qualquer um desses passos por você: escreve a mensagem de commit, resolve o conflito, faz o commit, o merge ou o push, remove o worktree, e conhece os comandos que desfazem um passo, como `git merge --abort` para um merge parado por um conflito ou `git revert` para uma entrega a desfazer.
Por padrão, cada passo vem depois da sua leitura: peça o commit quando você tiver usado a entrega e o diff em stage tiver só ela, o commit de merge quando o arquivo resolvido não tiver nenhum marcador de conflito, e o push quando o `git log` mostrar o que vai sair.
Depois de um merge que ele fez, `git log --oneline --graph -3` em `main/` mostra o commit de merge e o branch que ele trouxe.
Para rodar duas entregas ao mesmo tempo em worktrees, abra uma sessão por pasta: uma em `main/` para cada `/propose`, ou uma para um `/propose a b` que nomeia as duas, cujos subagentes escrevem em cada worktree; uma em cada worktree para o seu `/apply`, ou uma em `main/` para um `/apply a b`, que manda um subagente para o caminho de cada worktree; e nenhuma no contêiner.

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

Isso é um lote: um comando que nomeia cada linha, `/propose devolver-livro lista-de-atrasos`, instruído a decidir sozinho, que abre um subagente por linha, cada um seguindo a sua própria recomendação onde perguntaria ([capítulo 12](12-propose.md)).
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
Antes do primeiro `/apply`, leia cada página, esta lista primeiro, e corrija cada uma na sessão que digitou o comando, que leva a correção a um subagente no slug dela (capítulo 12); um comando que também disse para construir deixa essa leitura para o fim, com os diffs (capítulo 13).

A recomendação cobre só uma pergunta que os documentos deixam em aberto e que você conseguiria responder.
Uma pergunta que pertence a outra pessoa, um cliente ou a diretora da biblioteca, nunca é respondida por uma recomendação: a página vai até onde consegue, e a linha espera como `[?]` com `· resume: propose`, como `aviso-prazo` espera em `· blocked: qual provedor?` no capítulo 14.
O Caso A deu a uma pergunta assim uma linha própria, uma entrega de pergunta, cujo único resultado é uma resposta escrita; ela é uma customização do próprio Caso A, não um passo do kit (capítulo 20).

Páginas escritas ao mesmo tempo não leem umas às outras.
O `/propose` lê as entregas em andamento em `work/` quando começa, e uma página sendo escrita ao mesmo tempo ainda não está lá: duas páginas podem decidir a mesma pergunta de dois jeitos, ou cada uma pedir ao docs/03 o mesmo termo novo.
Você encontra isso lendo as páginas lado a lado, e corrige uma delas na sessão que digitou o comando, como acima.

Cada `/propose` escreve a sua página e a marca da sua linha e não coloca nada em stage: a proposta fica na pasta, sem commit, e o que o índice já guardava fica como estava.
Nem é preciso um commit para passar a página adiante: o `/apply` que a constrói, na mesma pasta, lê a página e a marca da pasta, como estão.
As linhas de um lote ficam lado a lado na fila, então o git põe as suas marcas em um hunk do docs/06.
Esse hunk não guarda conflito: nenhuma linha dele é mudada por duas sessões, e a mudança de cada sessão é a marca da sua própria linha, que a lista do que não é conflito nomeia.
Nem é motivo para colocar nada em stage enquanto as páginas estão sendo escritas.

Os `/apply` que vêm depois não acrescentam regra própria: rodam ao mesmo tempo só em linhas livres cujos arquivos não se encontram, e cada commit é decisão sua, uma entrega por vez.
Cada `/apply` coloca a sua entrega em stage quando termina: a sua página, o que construiu e a sua linha da fila, e as outras propostas ficam fora do stage, na pasta.
É aí que o hunk compartilhado conta, e quem coloca em stage a marca de uma linha é a sessão dona dela, nunca você.
O `git add -p` não consegue fazer isso aqui: ele divide um hunk com `s` só onde uma linha sem mudança separa duas mudanças, e o `e` dele abre o hunk em um editor, que uma sessão não opera.[^git-add]
Então a sessão coloca em stage o seu `[x]`, a sua última edição, com o `stage` do script de marca: o script muda a marca dessa linha no índice (a cópia em stage de onde o commit é feito), um byte, e deixa as outras linhas ali como estavam.
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

**A fila.** Em uma pasta ela não dá conflito: cada sessão marca a sua própria linha, e cada `/apply` coloca em stage só essa linha com o `stage` do script de marca, esteja ela no mesmo hunk que a da outra ou não.
Entre worktrees ela sempre dá conflito no merge, já que cada entrega marca a sua linha, e se resolve do mesmo jeito toda vez: guarde as duas marcas.

**Arquivos que as duas mudam.** Um arquivo de código que duas entregas mudam é diferente.
Antes da primeira edição, o `/apply` compara os arquivos da sua página com os de toda construção em andamento ou ainda não integrada e para em um arquivo que as duas tocam, em uma pasta ou em worktrees, então a segunda construção espera a primeira ser integrada; onde o branch dela começou antes desse merge, as duas mudanças ainda se encontram no merge dela, e resolvê-lo é uma decisão sobre o código: quem a toma precisa entender as duas mudanças.
Então liste os arquivos que cada entrega vai tocar, a partir da sua linha da fila, do docs/01 e do código que ela nomeia: entregas cujos arquivos não se encontram podem ser construídas ao mesmo tempo, em uma pasta ou em worktrees; entregas cujos arquivos se encontram são construídas uma depois da outra em qualquer dos dois, e um `· after <slug>` na segunda diz isso na fila.

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

* Duas sessões dividem uma pasta no trunk quando as suas linhas estão livres e os seus arquivos não se encontram: cada uma marca só a sua linha, coloca em stage só os seus caminhos e a sua linha da fila, a linha com o `stage` do script de marca, e você decide cada commit, uma entrega por vez.
* A marca de outra linha, a página ou os arquivos de outra entrega e as entradas em stage de outra sessão não são conflito; nem duas linhas vizinhas da fila em um hunk; uma linha editada pelas duas, ou um arquivo de que uma página precisa e que a outra está mudando, é: pare, e então ordene as linhas com `· after`, já que o `/apply` faz a mesma verificação em um worktree.
* Uma pasta tem um só índice, então faça o commit a partir dele quando ele guarda só aquela entrega: `git diff --cached --stat` nomeia arquivos, então leia também o diff em stage de um arquivo compartilhado, pelas suas linhas; com outra entrega em stage, espere; e nunca escolha uma entrega com `git commit -- <caminhos>`, que pega cada arquivo nomeado inteiro da pasta, com as linhas da outra entrega em um arquivo compartilhado, em stage ou não.
* Um worktree por entrega compensa para várias pessoas, ou para entregas que mexem nos mesmos arquivos: uma pasta contêiner cujo `main/` é o checkout guarda o worktree de cada entrega em `<oculta>/worktrees/<slug>/` no `<prefixo><slug>`, `.focus-kit/` e `focus-kit/` por padrão; `git worktree add`, trabalhe ali, `git merge --no-ff` em `main/`, `git worktree remove`, `git branch -d`; cada worktree tem o seu próprio índice, o `/propose` reivindica a linha com o script do kit, que roda como um alias do git pelo próprio `sh` do git, o do Git for Windows no Windows, roda a partir de `main/` no branch padrão, respondendo `here` no worktree do próprio slug, cria o worktree a partir do branch principal do origin e o branch no origin só quando o origin não tem nenhum, a reivindicação da linha, responde `taken` para o branch de outro clone a não ser com `resume`, e imprime o caminho do worktree, e as marcas da linha ficam no branch até o merge, e o script de fila, digitado com a palavra do slot em `main/` ou em qualquer worktree, lê um branch no origin como a reivindicação e a linha de cada entrega do seu branch até o merge, a cópia do branch principal depois dele, um `[?]` em qualquer cópia travando, e mostra uma linha que só um branch tem no seu marco, embora não veja marca que ainda não teve push; cada sessão abre onde trabalha, nunca no contêiner: o `/propose` em `main/`, que edita os worktrees pelo manual do contêiner, um comando digitado com vários slugs ali também, os subagentes dele escrevendo em cada worktree, ou mandados para cada um, e o `/apply` em uma sessão nova no worktree cujo caminho o `/propose` dá, parando antes de qualquer edição em qualquer outro lugar; um `/apply` travado ali pode colocar o seu trabalho parcial em stage para você fazer o commit no branch, que fica sem merge até a entrega estar pronta; um conflito deixa as duas versões entre marcadores, e `git diff --cached --check` pega qualquer um que sobrou antes do commit.
* O paralelo compensa enquanto as construções das entregas não tocam os mesmos arquivos, o que o `/apply` verifica em uma pasta e em worktrees do mesmo jeito, as portas e os bancos de dados da máquina não colidem, o disco comporta as dependências de cada worktree, e uma pessoa ainda consegue revisar cada entrega; o `/propose` pode rodar em lote, um comando instruído a decidir sozinho, sem colocar nada em stage, cada página listando o que decidiu sozinha para você ler antes de qualquer `/apply`, cada `/apply` colocando a sua própria entrega em stage, e todo commit continua sendo decisão sua, feito por você ou pedido ao agente depois da sua revisão, ou dada uma vez no slot Git, com cada commit ou merge revisado depois que entra.

[^git-commit]: Git, "git-commit", a documentação, opção `--only`, acesso em 2026-10-13. <https://git-scm.com/docs/git-commit>
[^git-clone]: Git, "git-clone", a documentação, opção `--bare`, acesso em 2026-10-16. <https://git-scm.com/docs/git-clone>
[^git-worktree]: Git, "git-worktree", a documentação, acesso em 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^git-merge]: Git, "git-merge", a documentação, seção "How conflicts are presented" e opção `--abort`, acesso em 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", a documentação, opção `--check`, acesso em 2026-09-30. <https://git-scm.com/docs/git-diff>
[^git-add]: Git, "git-add", a documentação, seção "Interactive mode", acesso em 2026-10-18. <https://git-scm.com/docs/git-add>
[^git-restore]: Git, "git-restore", a documentação, opção `--patch`, acesso em 2026-10-18. <https://git-scm.com/docs/git-restore>
[^parallel-run]: J.C. Ködel, "One Page at a Time", o registro de duas entregas construídas em paralelo em dois worktrees, 2026-09-30, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-worktrees-run>
[^claude-code-permissions]: Anthropic, "Configure permissions", documentação do Claude Code, seção "Additional directories grant file access, not configuration", acesso em 2026-10-21. <https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration>
