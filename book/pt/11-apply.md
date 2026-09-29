# `/apply`: construir, verificar, provar, nunca fazer commit

Depois deste capítulo você consegue rodar o `/apply` em uma página revisada, em uma sessão nova, e acompanhar o que ele faz, da página até uma mudança no stage.
Você consegue revisar essa mudança contra a página antes do commit, e fazer o commit você mesmo.
Depois você consegue construir o resto de um marco do mesmo jeito, uma linha de cada vez.

## O que ele faz

O `/apply <slug>`, cujo arquivo é o `apply/SKILL.md`, constrói a entrega que `work/<slug>.md` descreve, por inteiro, em uma sessão: o código, os testes, a prova e os documentos.
Ele começa em uma sessão nova ([capítulo 2](02-how-agents-see.md)): a página é tudo o que ele leva da conversa que a escreveu, e é por isso que o [capítulo 10](10-propose.md) pede que você leia a página antes de este comando rodar.

### O que ele lê

A página, o `AGENTS.md` e três dos documentos do projeto: o docs/01, a arquitetura, que diz onde cada peça fica e como os erros viajam; o docs/04, as convenções, que dizem quais testes escrever; e o docs/05, o processo.
O docs/05 guarda os slots do projeto, e o `/apply` os segue ao pé da letra: o comando de verificação, os ambientes e o que uma entrega deixa em cada um, como uma tela é provada, a política de publicação e a estratégia de git ([capítulo 6](06-the-documents.md)).
Em um branch ou em uma worktree, ele trabalha no que o `/propose` criou para o slug.

### A página é o escopo

O que a página pede é o que se constrói, e nada em volta.
O `apply/SKILL.md` diz isso em uma linha: "*a página é o escopo; não o amplie*".
Então o `/apply` não acrescenta nenhuma dependência, camada ou ferramenta que a página não nomeou, só abstrai na segunda ocorrência concreta (e a página diz qual foi a primeira), e não escreve travessão em nenhum texto que um usuário lê.

### Quando a página contradiz um documento

Ele para e diz qual.
Ou o documento muda na mesma entrega, ou a página está errada; ele nunca escolhe um dos dois em silêncio.
Uma escolha em silêncio deixaria uma página e um documento que discordam, e a próxima sessão construiria sobre o que lesse primeiro.

### A verificação e a prova

Ele roda o comando de verificação até ficar verde.
Depois prova a entrega do jeito que o docs/05 diz: um screenshot contra a referência, uma execução do começo ao fim, ou uma checagem à mão.
Ele lista o que diverge da referência e corrige, até sobrar só o que ele consegue justificar; uma falha faz parte da prova e é registrada, não escondida.

### O que "feito" quer dizer

Verde não é feito.
Antes de parar, o `/apply` faz tudo isto:

* Escreve na página o que aconteceu: o que divergiu do plano e por quê, o que foi deixado de fora, o que a prova achou, e as decisões tomadas, com um ADR se precisou de um.
* Atualiza os documentos que a entrega mudou: um termo novo no docs/03, uma regra nova no documento dono dela, uma decisão no docs/adr/.
* Marca cada item do Done when.
* Move a página para `work/done/`, e troca a marca da linha no docs/06 de `[>]` para `[x]` ([capítulo 9](09-queue-and-milestones.md)).
* Roda `git add -A` e sugere a mensagem de commit no formato que o docs/05 define.
* A última coisa que ele diz é qual ambiente está em qual versão, e o comando que atualiza os outros.

### Por que ele para no stage

O `/apply` nunca faz commit e nunca faz merge, qualquer que seja a estratégia de git.
Ele põe tudo no stage e entrega a mensagem a você; o commit é seu, e vem depois da sua revisão, na última seção deste capítulo.

## A execução na clínica

A execução partiu de onde o capítulo 10 deixou a clínica: o commit [`3f0b47c`](https://github.com/JCKodel/focus-kit-clinic/commit/3f0b47c1868e69970eefadb4f4a34bdcbada67b2), com a página revisada `work/skeleton.md` e a linha `skeleton` em `[>]` no docs/06, as duas sem commit.
A página pede o app e o servidor vazios em um projeto: uma primeira tela que pergunta ao servidor `GET /api/health` e mostra "Server: ok", um executor de migrations para o SQLite, o `npm run verify`, e um screenshot em tamanho de celular como prova.

Abra o seu host na raiz do projeto, em uma sessão nova, e digite:

```
/apply skeleton
```

Desta vez não há briefing: a página é o briefing.
Eu o rodei sem interface no Claude Code, com uma lista dos comandos de shell que ele podia rodar sozinho: npm, npx e node, `mkdir` e `cp`, e `git add`, `git status` e `git diff`.[^apply-run]
`git commit`, `git push` e `git tag` não estavam na lista, então um commit teria sido recusado, além de ir contra o kit.
Também neguei o `npm run dev` de propósito: uma sessão sem interface que sobe um servidor pode deixá-lo preso à porta, e o docs/05 da clínica quer esse servidor rodando na minha máquina, não dentro do turno do agente.

O agente leu a página e os documentos, instalou os pacotes e um navegador para o Playwright, e escreveu o código, a configuração e os testes.[^apply-run]
Rodou o `npm run verify`, verde na primeira vez, depois subiu o servidor à mão com um arquivo de migration feito para falhar, viu-o parar com código de saída 1 e o nome do arquivo, e apagou o arquivo.
Tentou o `npm run dev`, que foi negado, e tirou o screenshot com uma linha acrescentada a um teste do Playwright.
Atualizou o docs/01, 02, 04, 05 e 06, escreveu na página o que aconteceu e a moveu para `work/done/`.
Tirar a linha do screenshot deixou um erro de formatação, então a verificação ficou vermelha na checagem do Biome; o agente corrigiu e rodou a verificação de novo.
Este é o fim dessa última execução, dos testes do Vitest à build:[^apply-run]

```
> test
> vitest run


 RUN  v5.0.2 .


 Test Files  2 passed (2)
      Tests  7 passed (7)
   Start at  15:21:47
   Duration  104ms (transform 56%, tests 19%, import 18%, worker 7%)


> test:e2e
> playwright test


Running 4 tests using 1 worker

  ✓  1 [phone] › src/features/health/HealthView.e2e.ts:3:1 › shows the server as ok when it answers (113ms)
  ✓  2 [phone] › src/features/health/HealthView.e2e.ts:10:1 › shows the check while the answer is on its way (101ms)
  ✓  3 [phone] › src/features/health/HealthView.e2e.ts:20:1 › shows the server as unreachable when it answers with an error (96ms)
  ✓  4 [phone] › src/features/health/HealthView.e2e.ts:30:1 › shows the server as unreachable when it does not answer (97ms)

  4 passed (1.5s)

> build
> vite build

vite v8.3.1 building client environment for production...
transforming...
✓ 21 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                  0.39 kB │ gzip:  0.28 kB
dist/assets/index-DD_Vn2PP.js  220.36 kB │ gzip: 68.89 kB

✓ built in 52ms
```

Sete testes unitários do executor de migrations e do banco, quatro testes do Playwright dos estados da página em 390×844, e uma build.[^apply-run]
Este é o screenshot que ele salvou como prova, `work/done/skeleton-390x844.png`, como rodou:[^apply-run]

![O screenshot de prova do skeleton em 390×844: o título "Clinic" e a linha "Server: ok", alinhados à esquerda, na fonte do sistema.](../assets/11-skeleton-390x844.png)

O screenshot está como rodou, em inglês: o título "Clinic" (clínica) e a linha "Server: ok" (servidor: ok).
É o que o Visual reference da página descreve, a fonte `system-ui`, 16 pixels de cada lado e as cores padrão do navegador, e nada mais.[^apply-run]
Depois o agente escreveu na página o que aconteceu; esta é essa seção como a execução a deixou, e o original está em inglês, e aqui vai traduzido:[^apply-run]

```markdown
## O que aconteceu

**Construído.** `src/lib/result.ts`; a fatia `health` (`route.server.ts`,
`api.ts`, `useHealth.ts`, `HealthView.tsx`, `strings.ts`,
`HealthView.e2e.ts`); a casca do servidor (`main.server.ts`,
`database.server.ts`, `migrate.server.ts`, `migrations/` vazia); a casca do
app (`src/app/main.tsx`, `src/app/strings.ts`, `index.html`); configuração
de TypeScript, Biome, Vite e Playwright; `.gitignore`.

**Divergiu do plano, e por quê.**

* `@hono/node-server` foi acrescentado ao lado de `hono`: o Hono precisa de
  um adaptador para escutar em uma porta do Node. Faz parte de "Node com
  Hono", registrado no docs/01.
* O servidor não tem build nem executor como o `tsx`: o Node `>=24` roda
  `.ts` direto, removendo os tipos. Consequência, no docs/01: os imports
  levam `.ts`, e `erasableSyntaxOnly` proíbe enums e sintaxes parecidas.
* `npm run dev` é `node --watch src/server/main.server.ts & vite`, o `&` do
  shell em vez de uma ferramenta como `concurrently`, já que a página não
  nomeou tal ferramenta. Ctrl+C para os dois, porque eles dividem o grupo de
  processos do terminal.
* `openDatabase` retorna `Result<DatabaseSync, DatabaseOpenFailed>` em vez
  de lançar, então `throw` também não é fluxo na partida do servidor. É o
  terceiro uso de `Result` (primeiro: o `api.ts` de health; segundo:
  `migrate`).
* `migrate` também retorna `MigrationFailed` quando a pasta não pode ser
  lida ou `schema_migration` não pode ser criada. Nenhum arquivo foi
  alcançado então, e `file` guarda o caminho da pasta. O contrato nomeia só
  o caso por arquivo.
* O estado inalcançável tem dois testes do Playwright (resposta 500,
  requisição abortada), um para cada caso de Behaviour; a página contava
  três estados.
* O código de erro do cliente é `ServerUnreachable`. É um código de
  infraestrutura, como `MigrationFailed` e `DatabaseOpenFailed`, então não é
  um termo do docs/03.
* O npm instalou as versões maiores atuais: TypeScript 7, Vite 8, Vitest 5,
  Playwright 1.63, Biome 2, React 19, Hono 4.

**Deixado de fora.** Nada de Behaviour nem de Contract.

**O que a prova achou.** O screenshot em 390×844 mostra "Clinic" e
"Server: ok" em `system-ui`, alinhados à esquerda com 16px de cada lado,
cores padrão do navegador: nada diverge do Visual reference. Ele foi tirado
por um `page.screenshot` avulso no teste "ok" do Playwright, removido depois
da execução. Uma partida manual com um `0001-broken.sql` temporário que
falha em `src/server/migrations/` saiu com código 1 e
`Migration 0001-broken.sql failed: no such table: missing`, deixou só
`schema_migration` (vazia) no banco, e o arquivo foi removido.

**Decisões.** Os arquivos do Playwright são `*.e2e.ts` ao lado da view
deles, e o Playwright sobe o próprio servidor e o próprio Vite nas portas
3100 e 5174 com um banco na pasta temporária do sistema (docs/04). Nenhum
ADR: toda escolha cabe dentro do ADR-0001.
```

Leia como o relato do agente sobre cada escolha que a página não fez: um pacote adaptador, como o servidor roda o seu TypeScript, como dois processos sobem juntos, e as versões que o npm instalou no dia.
Ele pôs tudo no stage com `git add -A`; este é o `git status --short` da clínica depois disso:[^apply-run]

```
A  .gitignore
A  biome.json
M  docs/01-Architecture.md
M  docs/02-Backend.md
M  docs/04-Conventions.md
M  docs/05-Process.md
M  docs/06-Queue.md
A  index.html
A  package-lock.json
A  package.json
A  playwright.config.ts
A  src/app/main.tsx
A  src/app/strings.ts
A  src/features/health/HealthView.e2e.ts
A  src/features/health/HealthView.tsx
A  src/features/health/api.ts
A  src/features/health/route.server.ts
A  src/features/health/strings.ts
A  src/features/health/useHealth.ts
A  src/lib/result.ts
A  src/server/database.server.test.ts
A  src/server/database.server.ts
A  src/server/main.server.ts
A  src/server/migrate.server.test.ts
A  src/server/migrate.server.ts
A  src/server/migrations/.gitkeep
A  tsconfig.json
A  vite.config.ts
A  work/done/skeleton-390x844.png
A  work/done/skeleton.md
```

O código, a página em `work/done/` com o seu screenshot, e os documentos que a entrega mudou, tudo em uma árvore no stage.
Ele sugeriu esta mensagem de commit, no formato do [§6 do docs/05](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/apply/docs/05-Process.md) da clínica; o original está em inglês, e aqui vai traduzido:[^apply-run]

```
Construir o skeleton: página de health, servidor Hono, migrations, verify

- Fatia health: GET /api/health e uma página que mostra checando, ok, inalcançável
- A partida do servidor abre data/clinic.sqlite e aplica as migrations SQL em ordem
- Result vai para src/lib no seu segundo uso (migrate)
- npm run dev roda cliente e servidor; npm run verify roda todas as checagens
- Testes do Vitest para migrate e para a abertura do banco; Playwright em 390x844

Veja work/done/skeleton.md
```

E as últimas palavras dele foram os ambientes, como o kit pede; o original está em inglês, e aqui vai traduzido:[^apply-run]

```markdown
**Ambientes:**
- **local:** o código está nesta entrega e `data/clinic.sqlite` existe sem migrations para aplicar, mas nada está rodando. Suba com `npm run dev`: o cliente fica em http://localhost:5173 e o servidor na porta 3000.
- **produção:** ainda não existe. A entrega `deploy` vai criá-la.
```

O item "`npm run dev` deixa cliente e servidor rodando localmente" era meu, não da execução: depois da execução eu subi o `npm run dev`, abri a página e `/api/health`, vi os dois responderem, e o mantive rodando durante a revisão.[^apply-run]
O código em si está na tag [`book-v1/apply`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/apply); a Parte III ensina como ele é organizado.

## Revise antes do commit

A mudança no stage é o que o agente diz que fez; a sua revisão confere que ele fez.
Faça a ela estas perguntas:

* Cada item do Done when está marcado, e cada um é verdade?
* O que aconteceu diz o que divergiu, e você teria decidido algo de outro jeito?
* Os documentos que a entrega mudou foram atualizados, e só eles?
* Há algo construído que a página não pediu?
* A verificação e a prova rodam para você?

Peça ao agente cada correção, na mesma sessão, nunca à mão ([capítulo 6](06-the-documents.md)).
A mesma sessão guarda o raciocínio da construção: ela sabe por que fez cada escolha, o que uma sessão nova teria que adivinhar.

Como no capítulo 10, um segundo agente leu a mudança no stage contra a página e o kit, o que roda o `/apply` deste livro, e listou o que achou; eu conferi cada item e aceitei todos.
Enviei a lista para a sessão da execução com `--continue`, o jeito sem interface de digitar na mesma sessão ([capítulo 7](07-brainstorm.md)); em uma sessão interativa, você a envia na sessão onde o `/apply` rodou.
Eu a enviei como estava; o original está em inglês, e aqui vai traduzido:[^apply-run]

```markdown
1. **Um pacote que a página não nomeou.** O kit diz para não acrescentar dependência que a página não nomeou. O agente acrescentou `@hono/node-server` sem parar para perguntar; só o registrou no docs/01.
2. **Uma prova que falta na página.** A afirmação de que uma segunda partida não aplica nada foi provada só por um teste do Vitest. O agente disse isso na resposta, mas o O que aconteceu da página não diz.
3. **Uma explicação no lugar errado.** O agente escreveu por que o `npm run dev` não rodou dentro do próprio item desmarcado do Done when, em vez de no O que aconteceu.
4. **Uma regra que ninguém rodando sem interface consegue seguir.** O docs/05 da clínica ainda diz "uma entrega o deixa rodando", o que um agente sem interface não consegue fazer. Você talvez queira que o documento diga que você mesmo o sobe.
5. **Uma afirmação não testada.** A página diz "Ctrl+C para os dois". Você pode conferir isso quando subir o `npm run dev`: a porta 3000 deve ficar livre depois.
```

O primeiro item é a regra do próprio kit: uma dependência que a página não nomeou é uma pergunta para a pessoa, não uma escolha do agente.
O quarto é uma regra do docs/05 da clínica que um agente sem interface não consegue cumprir, então quem mudou foi o documento, não o comportamento do agente.
O agente corrigiu a página e o docs/05, disse que deveria ter perguntado antes de acrescentar o `@hono/node-server`, e me perguntou se o mantinha.
Respondi "Keep it" (mantenha), na mesma sessão, e ele registrou a minha aprovação na página.[^apply-run]
Ele também salvou duas notas na memória do próprio Claude Code para a clínica, fora do repositório; eu as apaguei, para que as próximas execuções do livro comecem como as suas vão começar.
Este é o diff que a revisão fez nos arquivos do stage:[^apply-run]

```diff
--- a/docs/05-Process.md
+++ b/docs/05-Process.md
@@ -58,8 +58,10 @@
   failure. Green before anything is declared done.
 * **Environments:**
   * local: client and server on the developer's machine with a local SQLite
-    file; a delivery leaves it running with its migrations applied. Command:
-    `npm run dev` (client and server together; migrations apply at start).
+    file. Command: `npm run dev` (client and server together; migrations
+    apply at start). A delivery leaves the code ready to start and names the
+    command; the person starts it, since the agent may run headless and
+    cannot keep a process running.
   * production: a machine at the clinic or a free host; created by the
     `deploy` delivery, which writes its line here.
 * **Proof of a screen:** Playwright screenshots. Client screens at phone
--- a/work/done/skeleton.md
+++ b/work/done/skeleton.md
@@ -120,9 +120,7 @@
       to `work/done/skeleton-390x844.png`; it is not part of `npm run verify`.
 * [x] `npm run verify` is green.
 * [ ] `npm run dev` leaves client and server running locally, with the
-      SQLite file created. The SQLite file exists (`data/clinic.sqlite`,
-      created by a server start); the agent's session was not allowed to
-      start a long-running process, so the person starts `npm run dev`.
+      SQLite file created.
 * [x] docs/02 lists `GET /api/health` and `schema_migration`; docs/01 and
       docs/05 name the local command.
 
@@ -137,14 +135,17 @@
 
 **Diverged from the plan, and why.**
 
-* `@hono/node-server` was added next to `hono`: Hono needs an adapter to
-  listen on a Node port. It is part of "Node with Hono", recorded in docs/01.
+* `@hono/node-server` was added next to `hono` although the page did not
+  name it: Hono needs an adapter to listen on a Node port. The agent should
+  have stopped and asked; it did not. The person approved it at review, so
+  it stays, recorded in docs/01.
 * The server has no build and no runner such as `tsx`: Node `>=24` runs
   `.ts` directly by type stripping. Consequence, in docs/01: imports carry
   `.ts`, and `erasableSyntaxOnly` forbids enums and similar syntax.
 * `npm run dev` is `node --watch src/server/main.server.ts & vite`, the
   shell's `&` instead of a tool like `concurrently`, since the page named no
-  such tool. Ctrl+C stops both, as they share the terminal's process group.
+  such tool. Ctrl+C should stop both, as they share the terminal's process
+  group; this is untested (see What the proof found).
 * `openDatabase` returns `Result<DatabaseSync, DatabaseOpenFailed>` rather
   than throwing, so `throw` is not flow in the server start either. It is
   the third use of `Result` (first: health `api.ts`; second: `migrate`).
@@ -170,6 +171,19 @@
 `Migration 0001-broken.sql failed: no such table: missing`, left only
 `schema_migration` (empty) in the database, and the file was removed.
 
+Not proven outside a test:
+
+* "Starting the server a second time applies no migration" is proven only
+  by the Vitest test that runs `migrate` twice on one database. The server
+  was never started twice, since the only real start was the failing one
+  above.
+* `npm run dev` was not run. The agent's session was headless and not
+  allowed to start a long-running process, so the Done when item stays
+  unticked. `data/clinic.sqlite` exists, created by the failing start
+  above, with no migration recorded. The person starts `npm run dev`.
+* "Ctrl+C stops both" is untested. Check: after stopping `npm run dev`,
+  port 3000 is free (`lsof -i :3000` prints nothing).
+
 **Decisions.** Playwright files are `*.e2e.ts` next to their view, and
 Playwright starts its own server and Vite on ports 3100 and 5174 with a
 database in the system temp folder (docs/04). No ADR: every choice sits
```

O diff está como rodou, em inglês: no docs/05, o ambiente local passa a dizer que a entrega deixa o código pronto para subir e nomeia o comando, e que a pessoa o sobe, porque o agente pode rodar sem interface; na página, o item do Done when volta a ser só a linha da lista, o `@hono/node-server` passa a dizer que a pessoa o aprovou na revisão, o Ctrl+C passa a ser "não testado", e uma lista nova, "Not proven outside a test", diz o que só um teste provou, por que o `npm run dev` não rodou, e como conferir o Ctrl+C.
Nada no código mudou: a revisão corrigiu o registro, que é o que a próxima pessoa lê.
Uma coisa ela deixou sem corrigir: o item do Done when "`npm run dev` deixa cliente e servidor rodando localmente" continua desmarcado na página do meu commit, embora eu o tivesse conferido à mão depois da execução.
Foi uma falha minha: eu deveria ter pedido ao agente, na mesma sessão, que marcasse o item e escrevesse na página como ele foi conferido; não pedi, e a tag publicada não se move.
Na sua, peça essa marca e essa linha antes do commit, para que a resposta a "Cada item do Done when está marcado, e cada um é verdade?" seja sim.
Depois fiz o commit da árvore no stage com a mensagem sugerida:

```
git commit
```

Sem `-m`, o git abre um editor para a mensagem; o meu abriu o nano, eu colei a mensagem sugerida como o agente a deu, assunto, linha em branco e tópicos, salvei e fechei, e o commit existe quando o editor fecha.
O git abre o editor nomeado em `core.editor`, em geral o vi quando nenhum está definido; `git config --global core.editor nano`, ou `git config --global core.editor "code --wait"` para o VS Code, escolhe outro.
O capítulo 17 ensina o resto do git.
Em seguida criei a tag `book-v1/apply` no commit e enviei os dois com push.
A página e a sua construção estão nesse commit único: a unidade de trabalho do capítulo 10, que se desfaz em um passo.

O agente nunca faz commit porque o commit é a sua revisão.
Um commit diz que uma pessoa leu a mudança e a aceita; um agente que faz commit do próprio trabalho pula o único leitor que pode dizer que a construção é o que se queria.
A Parte IV volta a isso pelo lado do git: branches, merges, e o commit como revisão.

## O resto do marco 1

O `skeleton` é a primeira linha do marco 1 da clínica, e o resto se constrói do mesmo jeito.
Para cada linha, na ordem da fila: `/propose <slug>`, leia a página e peça cada correção, `/apply <slug>` em uma sessão nova, revise a mudança no stage, e faça o commit.
Faça o commit de cada linha antes de começar a seguinte, para que cada `/propose` leia o projeto que o último commit deixou; esses commits não levam tag.
Depois do `skeleton` as linhas são `clinic-setup`, `professionals`, `weekly-hours`, `book-appointment` e `cancel-appointment`.

O `clinic-setup` acrescenta o `npm run setup`, que cria a clínica e o dono dela.
Então, quando o capítulo 12 sobe o app com `npm run setup` e `npm run dev`, os dois comandos já são seus.

Uma linha também pode entrar no marco enquanto ele é construído.
O `/apply weekly-hours` achou um login que falhava cerca de uma vez em 300 testes do Playwright: um teste anterior escrevia no banco de teste enquanto a conexão do servidor não tinha tempo de espera para bloqueio.[^clinic-milestone-1-run]
A meu pedido, na revisão do stage, o agente o transformou na linha `e2e-database-busy` e a pôs dentro do marco 1, antes do `book-appointment`; ela foi construída com os mesmos passos.
Por isso o meu marco 1 tem sete commits, contando o `skeleton`.
O seu agente pode achar outra coisa, ou nada, e a sua fila pode ficar diferente da minha.

Espere o que a minha construção encontrou.[^clinic-milestone-1-run]
Duas das seis páginas precisaram de correções antes do `/apply`, e quatro não precisaram de nenhuma.
Três mudanças no stage precisaram de correções: `clinic-setup`, `weekly-hours` e `e2e-database-busy`.
As permissões das minhas execuções sem interface recusaram 25 chamadas, na maioria laços de shell imprimindo arquivos e `git mv`; o agente tomou um caminho permitido a cada vez, como ler os arquivos um a um ou o `mv`, e ninguém rodou nada por ele de fora da sessão.
Duas vezes a mensagem de commit sugerida terminou com um trailer `Co-Authored-By`, que o formato do docs/05 da clínica não tem; pedi a mensagem de novo, na mesma sessão, antes do commit.

Depois compare o seu marco 1 com a tag [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone).
O código dela é o marco 1 como eu o construí: o único commit posterior, do capítulo 12, muda só o docs/06 da clínica, onde põe na fila o que a revisão daquele capítulo achou.

## Pontos-chave

* O `/apply <slug>` constrói a página em uma sessão nova, e a página é o escopo: nenhuma dependência, camada ou ferramenta que a página não nomeou.
* Ele segue o docs/05 ao pé da letra, e quando a página contradiz um documento ele para e diz qual; nunca resolve em silêncio.
* Feito é mais que verde: a prova com as suas divergências, o que aconteceu, os documentos, o Done when, `work/done/`, `[x]`, a árvore no stage, a mensagem sugerida, e os ambientes ditos por último.
* O agente põe no stage, você revisa e faz o commit: confira o Done when, o que aconteceu, os documentos e o que a página não pediu, e peça cada correção na mesma sessão.
* No trunk o commit leva a página e a sua construção juntas: a entrega se desfaz em um passo.

## Exercícios

Estes exercícios usam a clínica, conversando com o agente, nunca à mão.

### Exercício 11.1

Depois dos exercícios 10.1 e 10.2, rode `/apply skeleton` em uma sessão nova e compare a sua mudança no stage com [`book-v1/apply`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/apply).

### Exercício 11.2

Revise a sua mudança no stage com as perguntas de "Revise antes do commit", peça ao agente cada correção, e faça o commit você mesmo.

### Exercício 11.3

Para cada divergência no O que aconteceu da sua página, diga se ela deveria ter sido uma pergunta na página antes do `/apply`.

### Exercício 11.4

Construa o resto do seu marco 1, do `clinic-setup` ao `cancel-appointment`, uma entrega de cada vez com `/propose` e `/apply`, fazendo o commit de cada uma; depois compare o seu código com [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone).

[^apply-run]: A execução do `/apply` deste livro no projeto guiado, 2026-09-28, com o Claude Code 2.1.284 e o modelo `claude-opus-5-5`, a partir do commit 3f0b47c: o comando e as suas permissões, a saída de cada turno, a saída da verificação, o screenshot, a página como a execução a deixou, a revisão e o seu diff, e o status do stage. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/apply-run/README.md>
[^clinic-milestone-1-run]: A construção do marco 1 do projeto guiado deste livro, 2026-09-28, com o Claude Code 2.1.284 e o modelo `claude-opus-5-5`: as seis entregas depois do `skeleton`, cada uma com a revisão da página, a revisão do stage e o commit. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/clinic-milestone-1-run/README.md>
