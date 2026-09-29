# `/propose`, uma página

Depois deste capítulo você consegue rodar o `/propose` em uma linha da fila, responder às perguntas dele e ler a página que ele escreve como o registro do que o agente entendeu e do que o `/apply` vai construir.
Você também consegue cobrir os buracos da página por conversa antes do `/apply`, e dividir uma entrega que não cabe em uma página.

## O que ele faz

Todo trabalho em um projeto com o focus-kit é uma entrega: a menor mudança que tem valor, o que outros métodos chamam de tarefa ou item de trabalho.
A fila, o docs/06, lista as entregas em ordem, uma linha cada ([capítulo 9](09-queue-and-milestones.md)).
O `/propose`, cujo arquivo é o `propose/SKILL.md`, pega uma linha e a transforma em uma página, `work/<slug>.md`: o que a entrega precisa fazer, o que ela não deve fazer, e como você vai saber que ela está feita.
A página cabe em uma página para que uma pessoa consiga revisá-la, antes da construção e depois dela: quando o `/apply` a constrói, a mesma página também registra o que aconteceu, o que divergiu e o que foi decidido, como o [§3 do docs/05](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/docs/05-Process.md) da clínica a define.
Se não cabe em uma página, o escopo ainda não foi entendido, e são duas entregas (a última seção deste capítulo).

### De onde vem o slug

Um slug é o nome da entrega, em palavras minúsculas unidas por hífens, como `skeleton` ou `book-appointment`.
Ele é escrito uma vez, na linha da fila, e dali em diante nomeia tudo o que é da entrega: a página `work/<slug>.md`, o argumento do `/propose <slug>` e do `/apply <slug>`, e a última linha do commit que a fecha, `work/done/<slug>.md`.
As primeiras linhas vêm do `/brainstorm` ou do `/analyze`, que escrevem o primeiro marco ([capítulo 7](07-brainstorm.md), [capítulo 8](08-analyze.md)); as linhas seguintes vêm de uma conversa ou da revisão de um marco ([capítulo 9](09-queue-and-milestones.md)).
Se você digita `/propose` sem slug, ele pede um.

### Quando a linha não existe

Você também pode digitar `/propose` com um slug que a fila ainda não tem.
Ele define a entrega do mesmo jeito, acrescenta a linha dela na fila onde ela pertence, e avisa que fez isso.
Uma ideia nova chega assim à fila e à sua página em uma conversa só; você ainda confere, no diff do docs/06, o marco e o lugar onde a linha entrou.

### Como ele sabe o que fazer

Ele lê antes de perguntar.
Ele começa pela descrição que a linha traz na fila; os documentos do projeto dão o resto:

* docs/00, o produto: a quem ele serve, as regras dele, o que ele não é.
* docs/03, o vocabulário: as palavras que a página precisa usar, cada uma com o seu nome no código.
* docs/05, o processo: os slots do projeto (o comando de verificação, como uma tela é provada, a estratégia de git) e o formato da página.
* docs/06, a fila: o que vem antes e depois desta linha.
* `work/`: as entregas em andamento, para que a página nova não colida com uma delas.
* docs/01, a arquitetura: onde a mudança mora no código.

Então ele pergunta, só onde há mais de uma leitura e nenhum documento a fecha: primeiro a avaliação dele, em prosa, e a recomendação dele primeiro em cada pergunta, então "your call" (você decide) é uma resposta válida, como no `/brainstorm` ([capítulo 7](07-brainstorm.md)).
Ele escreve a página no formato do §3 do docs/05 e troca a marca da linha de `[ ]` para `[>]`; um termo novo entra primeiro no docs/03, depois na página.

### Por que não fazer tudo em um passo

O `/propose` nunca escreve, edita nem gera código, migration, teste ou configuração, e o `propose/SKILL.md` diz por quê: "*separar decidir de fazer é o que impede o escopo de crescer durante a implementação*".
Um agente que planeja e constrói no mesmo fôlego toma as decisões no meio da construção, onde você não as vê; a página põe cada decisão onde você consegue lê-la antes de existir qualquer código.
O `/apply` então começa em uma sessão nova ([capítulo 2](02-how-agents-see.md)), com o contexto limpo, e a página é tudo o que ele leva desta conversa, então a página precisa guardar tudo de que a construção precisa.
E a ordem é a barata: um buraco achado na página custa um turno de conversa, um buraco achado na construção custa outro `/apply` (os números estão em "Leia a página antes do `/apply`").

### Como você corrige a página

Você pede ao agente, na mesma conversa, e ele escreve a correção: na página, e em qualquer documento que a correção toque.
Você não edita a página à mão ([capítulo 6](06-the-documents.md)): o agente sabe qual documento é dono de cada fato, então uma correção que toca o vocabulário ou a fila entra lá também, e a conversa guarda o motivo da mudança.
"Leia a página antes do `/apply`", abaixo, mostra uma revisão real, com o pedido e o diff.

### Por que não o modo de plano do seu host

Os hosts têm o seu próprio jeito de planejar antes de editar: no Claude Code é o modo de plano (plan mode), em que "*o Claude lê arquivos e propõe um plano, mas não faz nenhuma edição até você aprovar*".[^claude-code-plan-mode]
O modo de plano trabalha dentro de uma sessão, para a mudança do momento.
A página trabalha para o projeto: um arquivo no repositório, no formato que o docs/05 fixa, escrito a partir dos documentos do projeto e com as palavras deles, marcado na fila, lido por uma sessão nova para construí-lo, e guardado em `work/done/` com o que aconteceu, no mesmo commit da construção.
Use o modo de plano dentro de uma sessão se ele ajudar você; a página é o que sobrevive à sessão.

### O Contract, a única seção exata

Uma seção da página precisa ser exata, o Contract: os dados, o schema, a API, os formatos das mensagens.
O `propose/SKILL.md` dá o motivo: "*uma tela errada se corrige em uma sessão, uma coluna errada é uma migration*".
Uma tela é código que você reescreve; uma coluna guarda dados, e mudá-la exige uma migration que carregue os dados que já estão lá.

### Uma unidade de trabalho

Entre os dois comandos a linha fica em `[>]`: a página existe e a construção não; o [capítulo 9](09-queue-and-milestones.md) diz onde a página espera.
A página e a construção dela são uma unidade de trabalho, como diz a seção Choices do `references/documents.md` do kit: uma mudança que se desfaz em um passo.
A clínica está no trunk, e é por isso que a execução abaixo deixa a página sem commit.

## A execução na clínica

A execução partiu da clínica depois de `book-v1/brainstorm`, no commit [`3f0b47c`](https://github.com/JCKodel/focus-kit-clinic/commit/3f0b47c1868e69970eefadb4f4a34bdcbada67b2), "Update focus-kit to e7607c5": o kit atualizado como o capítulo 5 ensina, em um commit só dele, então a atualização se desfaz em um passo.
Nessa versão o `/propose` do kit termina pedindo que você leia a página antes do `/apply`, e a execução mostra isso.
A entrega foi a primeira linha da fila, `skeleton`: o PWA e o servidor vazios em um projeto, o `npm run verify` e o primeiro screenshot.
O briefing nomeia a linha e dá a regra para todo o resto; o original está em inglês, e aqui vai traduzido:[^propose-run]

```markdown
# Briefing

## Entrega
A primeira linha da fila: skeleton.

## Regra para uma pergunta que o briefing não responde
Your call. Diga o que escolheu e por quê.
```

Abra o seu host na raiz do projeto, em uma sessão nova, e digite `/propose skeleton`; eu o rodei sem interface no Claude Code e respondi com a regra do briefing.[^propose-run]
O agente leu os documentos e perguntou; o original está em inglês, e aqui vai traduzido:[^propose-run]

````markdown
Li o docs/00 ao 06, os ADRs e `work/` (só `done/`, que está vazia). O git é trunk (ADR-0003), então a página vai para `main` sem branch.

**Minha leitura de `skeleton`:** esta entrega não acrescenta nenhuma regra de negócio. Ela constrói a estrutura de que toda entrega seguinte depende: um projeto TypeScript com um cliente React em Vite e um servidor Hono, Biome, Vitest, Playwright, `npm run verify` e um comando para rodar localmente. Ela também cria o layout vazio `src/features/`, `src/app/`, `src/server/` e `src/lib/` do docs/01, e salva o primeiro screenshot em 390×844. O risco é o escopo crescer: nada do que pertence ao `clinic-setup` (tabelas, login) ou a uma história offline futura deve escorregar para cá. Os documentos deixam quatro pontos abertos que mudam a página.

**1. O que a primeira tela mostra?** Recomendo uma única página do cliente que busca `GET /api/health` e mostra "Server: ok", ou uma mensagem clara se o servidor não puder ser alcançado. O screenshot então prova o caminho inteiro: cliente, proxy, servidor, JSON e o caminho de erro do `Result`. O título seria um neutro "Clinic", porque o nome da clínica não existe até o `clinic-setup`. A opção mais simples é uma página estática sem chamada ao servidor, mas aí nada testa a metade do servidor até o `clinic-setup`.

**2. Onde ficam o banco de dados e o executor de migrations?** Recomendo colocá-los no `skeleton`: ele abre o arquivo SQLite por `node:sqlite` e aplica os arquivos SQL de `src/server/migrations/` em ordem ao iniciar, com um teste de repositório. Isso significa um item exato de contrato, uma tabela de controle `schema_migration (name TEXT PRIMARY KEY, applied_at TEXT NOT NULL)`, e nenhuma tabela de negócio. O `clinic-setup` já é a linha mais pesada do marco 1 (comando de setup, dono, sessões, scrypt, telas de login), então tirar isto de lá o deixa mais leve. A outra opção é deixar tudo para o `clinic-setup`, que cria a primeira tabela real.

**3. Quanto de PWA?** Recomendo um web manifest e um ícone, e nenhum service worker. Agendar precisa da rede de qualquer jeito, e um service worker traz bugs de cache sem benefício para o produto hoje. O comportamento offline seria uma entrega própria, se você um dia quiser. A outra opção é um service worker completo agora, usando `vite-plugin-pwa`.

**4. O que conta como prova por screenshot?** Recomendo uma asserção `toHaveScreenshot` do Playwright cujo PNG de base é commitado ao lado do teste e roda dentro do `npm run verify`. "O screenshot confere" vira então uma checagem mecânica, que é o que o Done when pede. A desvantagem é que as bases dependem das fontes da máquina; isso é aceitável para um desenvolvedor e só importaria se um CI chegasse. A outra opção é salvar os PNGs como arquivos de prova sem conferi-los contra uma base.

**Escolhas que eu faria por conta própria, a menos que você discorde:**
- **Node:** versão 24 ou mais nova declarada em `engines` (você tem a 26).
- **Comandos:** `npm run dev` roda o Vite e o servidor juntos, com o Vite repassando `/api` para o servidor. O servidor servir o cliente construído em um processo fica para o `deploy`.
- **`lib/result.ts`:** ainda não criado. Ele vai para `lib/` no segundo uso, como diz o docs/01, então a fatia de health guardaria o seu `Result` localmente.
- **Arquivo SQLite:** `data/clinic.sqlite`, com `data/` no `.gitignore`.

**Separado do `skeleton`, notado de passagem:** o marco 2 do docs/06 inclui `absences`, mas o docs/00 não diz nada sobre ausências (nem em Mechanics, nem em Rules, nem em Open decisions), e o docs/03 não tem termo para elas. Antes do `/propose absences`, o docs/00 precisa de uma linha sobre isso. Não vou mudar isso agora.

Responda de 1 a 4 (um simples "sim" aceita todas as minhas recomendações) e eu escrevo `work/skeleton.md` e marco a linha como `[>]` no docs/06.
````

O briefing não responde a nenhuma delas, então a resposta foi a regra dele, palavra por palavra; o original está em inglês, e aqui vai traduzido:[^propose-run]

```markdown
Your call. Diga o que escolheu e por quê.
```

O agente escreveu a página, marcou a linha como `[>]`, disse o que escolheu e por quê, e terminou a resposta com o final novo do kit; o original está em inglês, e aqui vai traduzido:[^propose-run]

```markdown
**Antes do `/apply`, leia a página e questione-a:**
- Cada linha de Behaviour pode ser conferida, como teste ou à mão?
- O Contract é exato? As colunas de `schema_migration` e o nome de arquivo `NNNN-<name>.sql` são as partes que custariam uma migration para mudar depois.
- O Out of scope nomeia algo que você supôs que estava dentro, como uso offline ou servir o app construído de um processo?
- Você discorda de alguma das escolhas acima?

Peça cada correção aqui, nesta conversa. Quando a página estiver certa, abra uma sessão nova e digite `/apply skeleton`.
```

Esta é a página como ele a escreveu primeiro, `work/skeleton.md`; o original está em inglês, e aqui vai traduzido, com o código como está:[^propose-run]

````markdown
# skeleton

**Objective.** Um desenvolvedor roda um comando e vê a primeira página do app
em uma tela do tamanho de um celular, respondida pelo servidor, e o
`npm run verify` prova que o projeto inteiro está são.

**Behaviour.**

* Com `npm run dev`, o cliente e o servidor iniciam juntos; abrir o cliente
  em 390×844 mostra o título "Clinic" e a linha "Server: ok".
* Enquanto a resposta está a caminho, a página mostra "Checking the server".
* Quando o servidor não responde, ou responde com erro, a página mostra
  "Server: unreachable" em vez de uma página em branco ou de uma falha.
* Ao iniciar, o servidor cria o arquivo SQLite se ele não existe, aplica
  toda migration ainda não aplicada, na ordem dos nomes de arquivo, e registra
  cada uma.
* Iniciar o servidor uma segunda vez não aplica nenhuma migration.
* Uma migration que falha não é registrada, deixa o banco como estava antes
  daquele arquivo, e interrompe o início com uma mensagem que nomeia o arquivo.
* `npm run verify` roda typecheck, lint, os testes Vitest, os testes
  Playwright e o build, e termina com código de saída 0.
* `npm run verify` falha quando um arquivo que não é código de servidor
  importa um arquivo `*.server.ts` (ADR-0002).
* A página traz um web manifest, então o navegador de um celular oferece
  "Adicionar à tela inicial" com o nome "Clinic" e o ícone do app.

**Contract.**

Rota, sem sessão:

```
GET /api/health
200  { "status": "ok" }
```

Tabela, criada pelo próprio executor de migrations antes de ele ler
`src/server/migrations/`, não por um arquivo de migration:

```sql
CREATE TABLE IF NOT EXISTS schema_migration (
  name       TEXT PRIMARY KEY,  -- the migration's file name, e.g. 0001-clinic.sql
  applied_at TEXT NOT NULL      -- UTC instant, ISO 8601, e.g. 2026-09-28T15:04:05.000Z
);
```

Migrations: arquivos `src/server/migrations/NNNN-<name>.sql`, quatro dígitos,
aplicados na ordem dos nomes de arquivo, cada um na sua própria transação junto
com a sua linha de `schema_migration`. Esta entrega entrega a pasta vazia.

Variáveis de ambiente do servidor:

| Nome | Padrão | Significado |
|---|---|---|
| `PORT` | `3000` | Porta do servidor Hono. |
| `DATABASE_PATH` | `data/clinic.sqlite` | O arquivo SQLite; `data/` é ignorada pelo git. |

Em desenvolvimento, o Vite serve o cliente e repassa `/api/*` para o servidor.

Web manifest: `name` "Clinic", `short_name` "Clinic", `start_url` "/",
`display` "standalone", ícones PNG de 192×192 e 512×512.

Node: `engines` `>=24`.

**States.**

* Vazio: não se aplica, a página não tem lista.
* Carregando: "Checking the server".
* Erro: "Server: unreachable".
* Offline: igual ao erro; não há service worker.

**Visual reference.** Nenhum arquivo de design. Estilo padrão simples e
limpo. Uma tela do cliente na largura de celular (390×844).

**Out of scope.**

* Service worker e uso offline: agendar precisa da rede; uma entrega
  própria, se um dia for desejado.
* O servidor servir o cliente construído em um processo: o `deploy` precisa
  disso, o `deploy` constrói isso.
* O nome real da clínica no título: ele só existe depois do `clinic-setup`.
* Qualquer tabela de negócio, login ou sessão: `clinic-setup`.
* `src/lib/result.ts`: o `Result` mora na fatia de health até uma segunda
  funcionalidade usá-lo (docs/01); espera-se que o `clinic-setup` seja esse
  segundo uso.
* CI: um desenvolvedor, uma máquina; `npm run verify` é o portão.

**Done when.**

* [ ] Os testes de repositório do executor de migrations passam contra um
      arquivo SQLite temporário: aplica em ordem, registra, pula as já
      aplicadas, desfaz e nomeia um arquivo que falha.
* [ ] Os testes Playwright dos três estados da página passam em 390×844, o
      estado "ok" com uma base `toHaveScreenshot` commitada ao lado do teste.
* [ ] `npm run verify` está verde, e falha em uma importação deliberada de um
      arquivo `*.server.ts` pelo cliente (conferida uma vez, depois removida).
* [ ] `npm run dev` deixa cliente e servidor rodando localmente, com o
      arquivo SQLite criado.
* [ ] O docs/02 lista `GET /api/health` e `schema_migration`; o docs/01 e o
      docs/05 nomeiam o comando local.
````

Cada recomendação da rodada está na página como uma decisão, e a página parece pronta: é isso que a próxima seção questiona.

## Leia a página antes do `/apply`

A página é o registro do que o agente entendeu, e é o que o `/apply` vai construir: uma sessão nova lê a página e nada desta conversa.
Como diz o fim do `propose/SKILL.md`, ela é escrita para ser lida por uma pessoa, interpretada e completada, não gerada e aplicada no mesmo fôlego.
Leia-a antes do `/apply`, e cubra cada buraco pedindo ao agente, nunca editando a página à mão ([capítulo 6](06-the-documents.md)): o agente escreve a correção onde ela pertence, na página e em qualquer documento que ela toque.

O custo decide quando lê-la.
Um buraco achado na página custa um turno de conversa; um buraco achado depois do `/apply` custa outro `/apply`, o comando mais caro.
No meu próprio uso, como o `/usage` do Claude Code o mostrou, o `/apply` levou 32% e o `/propose` 16% nas últimas 24 horas, e 47% e 14% nos últimos 7 dias.[^claude-usage]
Os números são aproximados e cobrem todos os meus projetos juntos, mas a proporção é o que importa: o `/apply` custa de duas a mais de três vezes o que o `/propose` custa.

Faça estas perguntas à página:

* Cada linha de Behaviour pode virar um teste ou uma checagem?
* O Contract é exato, ou "none" de propósito?
* O Out of scope nomeia o que você supôs que estava dentro?
* O Done when é mecânico, uma lista que uma máquina ou uma pessoa consegue marcar?
* O agente decidiu algo que você teria decidido de outro jeito? Leia primeiro as escolhas de "your call".

A primeira página do `skeleton` parecia boa, e essa é a armadilha: o texto de um agente parece certo mesmo quando está errado, e quem o valida é você ([capítulo 6](06-the-documents.md)).
Pedi a um segundo agente que a lesse contra os documentos da clínica, o que roda o `/apply` deste livro; ele listou os buracos que achou, e eu conferi cada um contra os documentos e enviei a lista como estava.[^propose-run]
O kit pede cada correção na mesma conversa; eu as enviei em uma sessão nova, digitando `/propose skeleton` com a lista depois do slug.
Funcionou porque o `/propose` lê `work/` primeiro e achou a página; o que essa sessão não tinha era o raciocínio da primeira conversa por trás de cada recomendação.
O pedido, inteiro; o original está em inglês, e aqui vai traduzido:[^propose-run]

```markdown
1. Checagem de import que ninguém pediu. O agente acrescentou "npm run verify falha quando código do cliente importa um arquivo *.server.ts". O docs/05 §7 da clínica diz que uma checagem nova precisa nomear um erro que de fato aconteceu. O agente só diz "sem uma checagem a regra depende só da memória", e não diz qual ferramenta faria a checagem.
2. Ícones sem conteúdo. O manifest pede ícones PNG de 192 e 512, mas nada diz o que eles mostram nem de onde vêm, então o /apply os inventaria.
3. Base do screenshot. O Visual reference só diz "Estilo padrão simples e limpo", e uma base toHaveScreenshot fica presa às fontes de uma máquina. O próprio agente admite isso.
4. Pasta dos testes de migration. Os testes de migration precisam de uma pasta de migrations, mas a página entrega a pasta real vazia e não diz que o executor recebe a pasta como parâmetro.
```

O primeiro buraco é uma regra do próprio docs/05 da clínica, "What this process does not have": uma checagem nova só entra quando nomeia um erro que aconteceu.
O agente me perguntou sobre o manifest e sobre o screenshot, cada pergunta com as suas opções e a recomendação dele primeiro, e eu aceitei as duas recomendações, "Drop manifest (Recommended)" e "Proof file, no baseline (Recommended)", que tiram o manifest da entrega e trocam a base de pixels por um arquivo de prova.[^propose-run]
Ele também tomou uma escolha por conta própria e disse: o executor de migrations e a página de health retornam os dois um `Result`, então ele moveu o `Result` para `src/lib/result.ts` nesta entrega, como o docs/01 pede no segundo uso.
Este é o diff da primeira página para a revisada:[^propose-run]

````diff
--- a/work/skeleton.md
+++ b/work/skeleton.md
@@ -11,17 +11,15 @@
 * While the answer is on its way, the page shows "Checking the server".
 * When the server does not answer, or answers with an error, the page shows
   "Server: unreachable" instead of a blank page or a crash.
-* At start, the server creates the SQLite file if it is missing, applies
-  every migration not applied yet, in file name order, and records each one.
+* At start, the server creates the `data/` folder and the SQLite file if they
+  are missing, applies every migration not applied yet, in file name order,
+  and records each one.
 * Starting the server a second time applies no migration.
 * A migration that fails is not recorded, leaves the database as it was
-  before that file, and stops the start with a message naming the file.
+  before that file, and stops the start with exit code 1 and a message
+  naming the file.
 * `npm run verify` runs typecheck, lint, the Vitest tests, the Playwright
   tests and the build, and ends with exit code 0.
-* `npm run verify` fails when a file that is not server code imports a
-  `*.server.ts` file (ADR-0002).
-* The page carries a web manifest, so a phone browser offers "Add to home
-  screen" with the name "Clinic" and the app's icon.
 
 **Contract.**
 
@@ -32,8 +30,8 @@
 200  { "status": "ok" }
 ```
 
-Table, created by the migration runner itself before it reads
-`src/server/migrations/`, not by a migration file:
+Table, created by the migration runner itself before it reads the folder,
+not by a migration file:
 
 ```sql
 CREATE TABLE IF NOT EXISTS schema_migration (
@@ -42,10 +40,27 @@
 );
 ```
 
-Migrations: files `src/server/migrations/NNNN-<name>.sql`, four digits, applied
-in file name order, each in its own transaction together with its
-`schema_migration` row. This delivery ships the folder empty.
+Migrations: files `NNNN-<name>.sql`, four digits, applied in file name order,
+each in its own transaction together with its `schema_migration` row. Files
+not matching the pattern are ignored. The real folder is
+`src/server/migrations/`; this delivery ships it empty.
 
+Migration runner, `src/server/migrate.server.ts`. It takes the folder as a
+parameter, so tests pass a temporary folder of fixture files and the server
+start passes `src/server/migrations/`:
+
+```ts
+function migrate(db: DatabaseSync, folder: string): Result<string[], MigrationFailed>
+// ok: the file names applied in this call, in order; [] when none
+
+type MigrationFailed = { code: "MigrationFailed"; file: string; message: string }
+// file: the file name that failed; message: the SQLite error text
+```
+
+`Result`, in `src/lib/result.ts`, as docs/01 defines it. First use: the
+health `api.ts`; second use: `migrate`. That second use is why it moves to
+`lib/` in this delivery.
+
 Environment variables of the server:
 
 | Name | Default | Meaning |
@@ -55,9 +70,6 @@
 
 In development, Vite serves the client and forwards `/api/*` to the server.
 
-Web manifest: `name` "Clinic", `short_name` "Clinic", `start_url` "/",
-`display` "standalone", icons 192×192 and 512×512 PNG.
-
 Node: `engines` `>=24`.
 
 **States.**
@@ -67,32 +79,46 @@
 * Error: "Server: unreachable".
 * Offline: same as error; there is no service worker.
 
-**Visual reference.** No design file. Plain, clean default styling. One
-client screen at phone width (390×844).
+**Visual reference.** No design file. One client screen at phone width
+(390×844). Plain, clean default styling, which here means the `system-ui`
+font, 16px padding on each side, the heading and the status line
+left-aligned, and no colours beyond the browser defaults. The proof is a
+screenshot you look at, not a pixel baseline.
 
 **Out of scope.**
 
+* Web manifest, icons and "Add to home screen": the name and the icon
+  belong to the clinic, which exists only after `clinic-setup`; it gets its
+  own delivery, `install`.
 * Service worker and offline use: booking needs the network; its own
   delivery if ever wanted.
+* An automatic check that client code does not import `*.server.ts`: no
+  such import has happened yet (docs/05 §7). The rule lives in docs/01 and
+  ADR-0002 until one does.
+* A `toHaveScreenshot` pixel baseline: without a design file it would only
+  freeze whatever was built, and it breaks with the machine's fonts.
 * The server serving the built client in one process: `deploy` needs it,
   `deploy` builds it.
 * The clinic's real name in the heading: it exists only after
   `clinic-setup`.
 * Any business table, sign-in or session: `clinic-setup`.
-* `src/lib/result.ts`: `Result` lives in the health slice until a second
-  feature uses it (docs/01); `clinic-setup` is expected to be that second
-  use.
 * CI: one developer, one machine; `npm run verify` is the gate.
 
 **Done when.**
 
-* [ ] Repository tests of the migration runner pass against a temporary
-      SQLite file: applies in order, records, skips applied ones, rolls back
-      and names a failing file.
-* [ ] Playwright tests of the three page states pass at 390×844, the "ok"
-      state with a `toHaveScreenshot` baseline committed next to the test.
-* [ ] `npm run verify` is green, and fails on a deliberate client import of
-      a `*.server.ts` file (checked once, then removed).
+* [ ] Vitest tests of `migrate` pass, each against an in-memory SQLite and
+      a temporary folder of fixture `.sql` files: applies in file name
+      order, records each file, skips applied ones, ignores files not
+      matching the pattern, and on a failing file rolls it back, leaves it
+      unrecorded and returns `MigrationFailed` naming it.
+* [ ] One Vitest test, against a temporary directory, shows the server's
+      database opening creates the missing folder and SQLite file.
+* [ ] `migrate` against the real `src/server/migrations/` returns `[]`.
+* [ ] Playwright tests of the three page states pass at 390×844, asserting
+      the texts of Behaviour.
+* [ ] A screenshot of the "ok" state at 390×844 is saved once, as proof,
+      to `work/done/skeleton-390x844.png`; it is not part of `npm run verify`.
+* [ ] `npm run verify` is green.
 * [ ] `npm run dev` leaves client and server running locally, with the
       SQLite file created.
 * [ ] docs/02 lists `GET /api/health` and `schema_migration`; docs/01 and
````

O diff fica como está no registro, em inglês: ele tira do Behaviour a checagem de import e o manifest; no Contract, a migration que falha passa a sair com código 1, os arquivos fora do padrão são ignorados, e entram a assinatura `migrate(db, folder)` do executor, o erro `MigrationFailed` com o arquivo e a mensagem, e o `Result` em `src/lib/result.ts`; o Visual reference ganha a fonte `system-ui`, 16px de margem e as cores padrão do navegador; o Out of scope ganha o manifest, que vira a entrega `install`, a checagem de import e a base de pixels; e o Done when troca a base por testes Vitest do executor contra uma pasta temporária e um screenshot salvo uma vez como prova.
Cada buraco fechou onde o `/apply` teria de adivinhar: a checagem de import e o manifest saíram, com os seus motivos no Out of scope; o executor ganhou uma assinatura e um erro exatos no Contract; e o Done when trocou a base de pixels por testes que o `/apply` consegue rodar e um screenshot que você olha.

## Quando não cabe

Um escopo que não cabe em uma página são duas entregas: o `/propose` diz isso, propõe a divisão e escreve só a primeira página, e a segunda vira uma linha na fila, onde ela pertence ([capítulo 9](09-queue-and-milestones.md)).
Este livro dividiu uma no capítulo 3, que compara o Spec Kit, o OpenSpec e o focus-kit pelo que cada um escreve para a mesma funcionalidade.
A execução medida das ferramentas, com o seu briefing, as suas versões fixadas e as suas contagens, não caberia na página do capítulo, então virou uma entrega própria, `spec-driven-run`.
Este é o diff do docs/06 deste livro no commit dela:

````diff
diff --git a/docs/06-Queue.md b/docs/06-Queue.md
index 2216d99..0f6ead6 100644
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@ -25,6 +25,7 @@ When this milestone closes, a reader who has never followed a process knows why
 
 ```
 [x] how-agents-see         Chapter 2: statelessness, context window, context rot, fresh sessions, from primary sources
+[x] spec-driven-run        SpecKit, OpenSpec and focus-kit run on the same feature and brief; files, lines and words counted and committed for chapter 3
 [ ] spec-driven            Chapter 3: SDD, what SpecKit and OpenSpec got right and where they weighed too much
 [ ] birth-of-focus-kit     Chapter 4: the Ninjobs restart, and the kit that grew and became one file again
 ```
````

Ele fica como está no repositório, em inglês: a linha nova diz "SpecKit, OpenSpec e focus-kit rodados na mesma funcionalidade e no mesmo briefing; arquivos, linhas e palavras contados e commitados para o capítulo 3".
A linha nova fica antes de `spec-driven`, o capítulo que precisa dos números dela, já em `[x]` porque a página e a construção dela entraram em um commit.
A revisão do `skeleton` fez o mesmo em escala pequena: o manifest saiu da página e virou a linha `install` no marco 2 da clínica, antes de `deploy`, em `[ ]`.[^propose-run]

## Pontos-chave

* O `/propose <slug>` transforma uma linha da fila em uma página: ele lê os documentos e `work/`, só pergunta onde nenhum documento fecha uma leitura, com a recomendação primeiro, e escreve a página e a marca `[>]`, nunca código, migration, teste ou configuração; um slug que a fila não tem ganha a sua linha.
* O Contract é a única seção exata: uma tela errada se corrige em uma sessão, uma coluna errada é uma migration.
* Leia a página antes do `/apply`: ela é o que o agente entendeu e o que vai ser construído; cubra cada buraco pedindo ao agente, nunca à mão, porque um buraco na página custa um turno e, depois do `/apply`, custa outro `/apply`.
* A página e a construção dela são uma unidade de trabalho que se desfaz em um passo: um commit no trunk, então a página espera sem commit; um merge do branch nas outras.
* Um escopo que não cabe em uma página são duas entregas: a primeira ganha a página, a segunda uma linha onde ela pertence.

## Exercícios

Estes exercícios usam a clínica, por conversa com o agente, nunca à mão.

### Exercício 10.1

Faça checkout de `book-v1/brainstorm` em um branch seu, atualize o kit como no capítulo 5, rode `/propose skeleton` com o briefing deste capítulo e compare a sua página com a deste capítulo.
Quais diferenças são escolhas de "your call" do agente?

### Exercício 10.2

Revise a sua página com as perguntas de "Leia a página antes do `/apply`" antes de qualquer `/apply`.
Peça ao agente que cubra cada buraco, e leia o diff.

### Exercício 10.3

Peça ao `/propose` `book-appointment` e `cancel-appointment` como uma entrega só.
Ele propõe uma divisão, e onde vai a segunda linha?

[^propose-run]: A execução do `/propose` deste livro no projeto guiado, 2026-09-28, com o Claude Code 2.1.283 e o modelo `claude-opus-5-5`, a partir do commit 3f0b47c: o briefing, os comandos, a saída de cada turno, as perguntas e a resposta, a primeira página, a revisão e o diff dela. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/propose-run/README.md>
[^claude-usage]: `/usage` do Claude Code, lido pelo autor em 2026-09-28, sessões locais em uma máquina, todos os projetos juntos; `work/done/propose-run/usage.txt`. A ferramenta chama os números de aproximados; o autor o leu em três projetos e obteve os mesmos números, então não é uma medida de um projeto. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/propose-run/usage.txt>
[^claude-code-plan-mode]: Anthropic, "Common workflows", documentação do Claude Code, seção "Plan before editing", acesso em 2026-09-28. <https://code.claude.com/docs/en/common-workflows#plan-before-editing>
