# `/analyze`, um projeto existente

Depois deste capítulo você consegue rodar o `/analyze` em um projeto que já existe, com código ou sem, responder à única rodada de perguntas dele e conferir contra o projeto os documentos que ele escreve, antes de fazer o commit.

## O que muda em relação ao `/brainstorm`

O `/analyze` é o comando para um repositório que já tem alguma coisa: código, documentos, ou os dois.
Ele funciona como o `/brainstorm` ([capítulo 7](07-brainstorm.md)): uma sessão nova, um padrão em cada pergunta, "your call" (você decide) como resposta válida, e os mesmos documentos no fim.
A diferença é que ele lê antes de perguntar, e o seu arquivo, `analyze/SKILL.md`, o faz ler isto, nesta ordem:

* o README e toda a documentação que já existe;
* os manifestos, como o `package.json`;
* a árvore de pastas;
* os pontos de entrada;
* os testes, e como eles rodam;
* a configuração de CI;
* os assuntos dos últimos cinquenta commits;
* qualquer arquivo de regras que já exista (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.cursorrules`).

O que o projeto não tem, ele pula: em um projeto sem código não há manifestos, pontos de entrada nem testes para ler, e os documentos descrevem o que os arquivos dizem.
A partir disso ele deduz a stack, como o código está organizado, onde ficam as regras de negócio, como os erros viajam, o comando de verificação e os ambientes.
Depois ele faz uma rodada, de quatro assuntos apenas:

1. O idioma da documentação. Padrão: o idioma do README.
2. O propósito e o público do produto nas suas palavras, só quando nenhum README os diz.
3. O FOCUS e a estratégia de git, as [duas escolhas](06-the-documents.md#as-duas-escolhas) do capítulo 6. O padrão de cada um é o que o código já faz, e o agente diz o que é.
4. O primeiro marco: as primeiras entregas, ou de onde lê-las (issues, um arquivo TODO, um roadmap).

Todo o resto ele decide a partir do que leu e marca como observado: você não é perguntado sobre o que o projeto já responde.
Onde o que ele leu se contradiz, ele registra uma questão em aberto no documento dono do assunto e não pede que você a resolva agora; resolvê-la é uma entrega própria.
Um arquivo de regras que já existe não fica ao lado do `AGENTS.md`: as regras dele passam para o `AGENTS.md`, e o arquivo fica com a linha de importação e só o que vale para aquele host.
Os documentos descrevem o que existe, não o que deveria existir.
Ele mostra o diff antes de escrever, e não muda nenhum código.

### FOCUS em código sem arquitetura

Em código sem uma arquitetura clara, o padrão para o FOCUS é "nenhum", porque o código não o segue, e o FOCUS inteiro significaria reescrevê-lo.
Há um caminho entre os dois, que você dá como resposta: a strangler fig (figueira estranguladora), o nome que Martin Fowler deu à troca gradual de um sistema antigo, por causa de uma trepadeira que cresce em volta de uma árvore até ficar de pé sozinha.[^strangler-fig]
O código novo cresce ao lado do antigo: toda funcionalidade nova é uma fatia vertical em FOCUS, toda parte que uma entrega muda passa para uma fatia vertical, e o código antigo sai uma entrega de cada vez, enquanto o projeto continua funcionando.
Responda à pergunta do FOCUS com isso, por exemplo "FOCUS inteiro, como strangler fig: funcionalidades novas e toda parte que uma entrega tocar viram fatias verticais; o resto fica até lá.", e o `/analyze` escreve isso no docs/01 e em um ADR, para que todo `/propose` e `/apply` seguinte o siga.
Na execução no CLAHub o agente ofereceu a mesma forma só para os dois princípios: o trabalho novo vai migrando para pastas por funcionalidade com o tempo.[^analyze-run]
A Parte III ensina o FOCUS em si.

## Antes de rodar

O código diz o que um projeto faz; raramente diz por quê, para quem, ou o que foi prometido.
Em um projeto corporativo esse conhecimento está em propostas, contratos, e-mails, transcrições de reuniões, tickets e apresentações, e o que o agente não lê, ele tem que adivinhar.
Ponha tudo o que você tem sobre o projeto em uma pasta na raiz, `context/`, como está, sem triagem e sem resumo.
Mantenha-a separada de `docs/`: `context/` é de onde o agente lê, e `docs/` é o que ele escreve.
O comando não procura essa pasta pelo nome, então diga isso na mesma mensagem, `/analyze Read context/ first, whole.` (leia `context/` primeiro, inteira); essa frase é instrução sua, não do kit.

Se a `context/` entra no commit é decisão sua.
Commitada, toda sessão futura consegue lê-la, e tudo o que está nela fica no histórico para todos com acesso ao repositório.
Listada no `.gitignore`, ela fica na sua máquina, e as sessões futuras veem só o que os documentos tiraram dela.
Leia-a procurando o que não pode ser compartilhado antes de escolher.

A execução no CLAHub não teve essa pasta: um projeto de código aberto guarda o seu contexto às claras, no README e nas issues.

## O projeto

O [CLAHub](https://github.com/DamageLabs/clahub) deixa um projeto de código aberto no GitHub pedir aos contribuidores que assinem um Contributor License Agreement (um acordo de licença do contribuidor): o dono escreve o acordo, o contribuidor assina entrando com a conta do GitHub, e todo pull request recebe um check que diz se todos os autores dos commits assinaram.
É uma aplicação Next.js em TypeScript, com as páginas, a API e o webhook do seu GitHub App em um só repositório, sobre um banco SQLite por meio do Prisma; tem 11.902 linhas de código TypeScript, sem contar os testes, e 259 testes que passam.[^brownfield-research]
Ele foi escolhido entre os projetos de código aberto medidos para este livro por ser um produto real com um domínio próprio, muitos testes, e issues abertas escritas como especificações.[^brownfield-research]
O fork deste livro, `JCKodel/clahub`, congela o projeto na tag `book-v1`, o commit do upstream que foi medido, para que a execução possa ser repetida.
Antes da execução o kit foi instalado e commitado em um branch do fork, como mostra o capítulo 5, e assim o `/analyze` começou com a árvore limpa.[^analyze-run]

## A execução no CLAHub

A execução foi respondida a partir de um briefing com uma seção por assunto da rodada, mais a regra para uma pergunta que o briefing não responde.[^analyze-run]
O original está em inglês; aqui vai traduzido:

```markdown
# Briefing

## Idioma da documentação
Inglês.

## Propósito e público
"Your call": o README diz.

## Escolhas
FOCUS: "your call". Git: "your call".

## Primeiro marco
As três issues abertas no upstream, uma entrega cada, nesta ordem:
https://github.com/DamageLabs/clahub/issues/270
https://github.com/DamageLabs/clahub/issues/274
https://github.com/DamageLabs/clahub/issues/268

## Regra para uma pergunta que o briefing não responde
Responda "your call".
```

Abra o seu host na raiz do repositório, em uma sessão nova, e digite `/analyze`; eu o rodei sem interface no Claude Code e respondi com as seções do briefing para os assuntos perguntados, palavra por palavra.[^analyze-run]
Ele leu o README, os guias que já estavam em `docs/`, o `package.json`, o workflow de CI, a árvore, os assuntos dos últimos cinquenta commits, o schema do banco e o código de erros, das actions e do check do CLA, e então fez a sua rodada; o original está em inglês, e aqui vai traduzido:[^analyze-run]

```markdown
Já li o bastante para fazer as minhas perguntas. O código já responde à maior parte. Uma coisa para avisar primeiro: um comando que combinava `find` e `xargs cat` precisava de aprovação e foi negado, porque esta sessão não tem como responder a um pedido de permissão. Li os arquivos que ele cobria um de cada vez, então não falta nada.

**O que encontrei (você não precisa confirmar):**
- **O produto:** um app Next.js 16, uma reescrita do antigo CLAHub em Rails (DamageLabs/clahub, rodando em cla-hub.io). Usa Prisma 7 com SQLite, Auth.js com login do GitHub separado para donos e contribuidores, e um GitHub App que roda os checks dos PRs. Há também uma API REST em `/api/v1`, e ele pode ser auto-hospedado com Docker.
- **Onde ficam as regras:** as regras de negócio estão em `src/lib/cla-check.ts`, as server actions em `src/lib/actions/`, e a validação em `src/lib/schemas/`. O código é organizado por camada técnica, não por funcionalidade.
- **Como os erros viajam:** as server actions retornam um `ActionResult` (sucesso ou falha como valor). As rotas da API retornam um erro JSON estruturado por meio de `apiError()`. `requireOwner` é a exceção: ele lança.
- **Comando de verificação:** `npm run lint && npx tsc --noEmit && npm test && npm run build`, os mesmos checks que o CI roda. O CI também roda os testes ponta a ponta do Playwright.
- **Os arquivos `docs/*.md` existentes** são guias de usuário, e alguns aparecem no site. O site só mostra arquivos de uma lista fixa, então pôr docs/00 a 06 ao lado deles não os publica.
- **Onde o código se contradiz:** estes entram nos documentos como questões em aberto; não vou pedir que você as resolva agora.
  - O `.prettierrc` pede aspas simples, mas o código usa aspas duplas, e o CI não confere a formatação.
  - O CONTRIBUTING menciona o Biome, que não está instalado.
  - O PRD diz que nenhum token OAuth é guardado para contribuidores. O código guarda tokens só dos donos, o que é coerente, mas o PRD também pede um job em segundo plano, e a nova verificação dos PRs é só uma promise que ninguém espera.
  - O PRD pede testes de API e de componentes, mas essas pastas estão vazias.
  - `hono` é uma dependência direta que nenhum arquivo do código importa.

**Quatro perguntas. Cada uma começa com a minha recomendação:**

1. **Idioma da documentação:** inglês, já que o README está em inglês. Você quer outro?

2. **FOCUS:** recomendo **nenhum**. Os documentos descreveriam as convenções atuais como são: Next.js App Router, `lib/` organizado por camada, e erros retornados como valores nas actions e na API. As outras duas opções são:
   - **só os dois princípios:** funcionalidades novas vão em pastas por funcionalidade, e `throw` nunca é usado para controle de fluxo. A estrutura por camadas fica como está, e o trabalho novo vai migrando para pastas por funcionalidade com o tempo.
   - **FOCUS inteiro:** View, Orchestrator, Use Case e Repository em peças separadas. Isso significaria uma refatoração grande.

3. **Git:** recomendo **um branch por entrega**, porque é o que o repositório já faz: branches `feat/`, `fix/` e parecidos, um PR para a `main`, mergeado por uma pessoa. As alternativas são **trunk** ou **uma worktree por entrega**. Nas três, eu nunca faço commit nem merge.

4. **Primeiro marco:** de onde vêm as suas 3 a 8 entregas? Opções:
   - **(a)** Eu as rascunho a partir das contradições acima e dos itens do PRD que o código ainda não faz: log de entregas de webhook, testes de componentes e de API, formatação obrigatória, nova verificação em segundo plano.
   - **(b)** Você me diz: issues do GitHub, uma lista, ou um objetivo.
   - O nome do branch, `book`, me faz pensar que você talvez tenha algo específico em mente.

Assim que você responder, mostro o diff completo antes de escrever qualquer coisa.
```

A resposta foram as seções do briefing para os assuntos perguntados, aqui traduzidas:[^analyze-run]

```markdown
## Idioma da documentação
Inglês.

## Escolhas
FOCUS: "your call". Git: "your call".

## Primeiro marco
As três issues abertas no upstream, uma entrega cada, nesta ordem:
https://github.com/DamageLabs/clahub/issues/270
https://github.com/DamageLabs/clahub/issues/274
https://github.com/DamageLabs/clahub/issues/268
```

O agente não perguntou o propósito, porque o README o diz, e contou o que encontrou sem pedir que você confirmasse.
Para o FOCUS e o git ele recomendou o que o repositório já faz, então o "your call" do briefing manteve os dois, e ele listou as contradições que vai registrar em vez de perguntar qual lado está certo.

Com essa resposta ele escreveu os documentos, e o `git status --short` mostrou:[^analyze-run]

```
?? AGENTS.md
?? CLAUDE.md
?? docs/00-Product.md
?? docs/01-Architecture.md
?? docs/02-Backend.md
?? docs/03-Domain.md
?? docs/04-Conventions.md
?? docs/05-Process.md
?? docs/06-Queue.md
?? docs/adr/
?? work/
```

Essas linhas guardam docs/00 a 06, o `AGENTS.md`, o `CLAUDE.md` com a linha `@AGENTS.md`, o `work/done/.gitkeep`, e um ADR cada em `docs/adr/` para as decisões que o código já incorpora (a reescrita em Next.js, SQLite por meio do Prisma, logins do GitHub separados para donos e contribuidores, checks pelo GitHub App, transações com log de auditoria, erros como valores, repositórios identificados por número, cobertura corporativa por domínio de e-mail) e para as escolhas da rodada, FOCUS e git.[^analyze-run]
Os trechos abaixo são citados na tag do capítulo `book-v1-analyze`, como foram commitados; no repositório eles estão em inglês, e aqui vão traduzidos.
As tags do capítulo do projeto brownfield levam hífen onde as do projeto guiado levam barra (capítulo 5) porque o fork já tem a tag `book-v1`, o upstream congelado, e o git se recusa a criar uma tag `book-v1/analyze` ao lado dela.

O docs/01 é onde o agente escreveu o que deduziu.
Na clínica, como o código é organizado foi uma escolha feita na conversa; aqui ela é lida da árvore.
Esta é a seção How the code is organized (como o código é organizado) de [`docs/01-Architecture.md`](https://github.com/JCKodel/clahub/blob/book-v1-analyze/docs/01-Architecture.md):

```markdown
## Como o código é organizado

As convenções próprias do projeto, organizadas por camada técnica (ADR-0009):

* `src/app/`: rotas. `(marketing)/` páginas públicas (landing, about, docs,
  privacy, terms, why-cla); `agreements/` painel, criar, editar e as
  páginas públicas de assinatura `[owner]` e `[owner]/[repo]`; `settings/api-keys`;
  `auth/signin`; `api/` handlers de rota (`v1/` REST, `badge/`, `health/`,
  `webhooks/github`, `github/` consultas auxiliares, `auth/`).
* `src/components/`: `ui/` primitivos do shadcn, `agreements/` e
  `settings/` componentes de funcionalidade.
* `src/lib/actions/`: server actions, um arquivo por área (agreement,
  signing, signature, exclusion, api-key, audit-log, recheck, contributing),
  mais `result.ts`.
* `src/lib/schemas/`: schemas Zod, compartilhados por formulários, actions e a API.
* `src/lib/`: todo o resto. `cla-check.ts` guarda a regra central (classificação
  dos autores, check runs, nova verificação com retry); `github.ts` o App e os
  handlers de webhook; `access.ts` e `org-membership.ts` os níveis de acesso;
  `audit.ts`, `api-*.ts`, `rate-limit.ts`, `email.ts`, `export-*.ts`,
  `badge.ts`, `branding.ts`, `templates.ts`, `prisma.ts`.
* `src/middleware.ts`: redireciona usuários não autenticados ou que não são donos
  para fora das páginas do dono; `/api/v1` autentica sozinha.
* `src/generated/prisma/`: cliente gerado, nunca editado.

As regras de negócio ficam principalmente em `cla-check.ts`, `access.ts` e nas
server actions; as actions também acessam os dados diretamente por meio do `prisma`.
Não há camada de repositório.
```

Cada linha nomeia uma pasta ou um arquivo que você pode abrir, e o último parágrafo diz o que falta tão claramente quanto o que existe: não há camada de repositório, e o FOCUS inteiro significaria uma refatoração, então o agente manteve as convenções próprias do projeto.

A pesquisa que escolheu o CLAHub descobriu que a configuração do README falha como está escrita: ele manda criar `.env.local`, e a configuração do Prisma lê `.env`.[^brownfield-research]
A execução registrou essa contradição como questão em aberto no docs/01, depois que a revisão da próxima seção pediu ao agente que conferisse a linha contra o código.
Esta é a primeira entrada da seção Open questions (questões em aberto) de [`docs/01-Architecture.md`](https://github.com/JCKodel/clahub/blob/book-v1-analyze/docs/01-Architecture.md):

```markdown
## Questões em aberto

* **Qual arquivo env a CLI do Prisma lê.** O README e o
  `docs/getting-started.md` mandam copiar `.env.local.example` para `.env.local`
  e depois rodar `npm run db:push` / `npx prisma db push`. A CLI do Prisma lê
  só `.env`, então com apenas `.env.local` o `DATABASE_URL` fica indefinido e o
  comando falha, a não ser que a variável seja exportada no shell ou também escrita
  em `.env`. Corrigir os guias, ou fazer `prisma.config.ts` e `prisma/seed.ts`
  carregarem `.env.local` também?
```

Ela diz o que cada lado diz, por que o passo falha, e ambas as saídas, e não toma nenhuma: corrigir os guias ou a configuração é uma entrega com a sua própria página, e o `/analyze` não muda nenhum código.

O docs/06 é a fila (o capítulo 9 ensina as marcas), e o briefing deu como primeiro marco as três issues do upstream, em ordem.
Este é o [`docs/06-Queue.md`](https://github.com/JCKodel/clahub/blob/book-v1-analyze/docs/06-Queue.md):

````markdown
# Fila

## Marco 1: assinaturas atuais, e-mails do dono, dados pessoais

Fecha quando um dono consegue exigir que os contribuidores assinem de novo
depois de uma nova versão do CLA, com um prazo de tolerância opcional, e os
checks dos PRs respeitam isso; quando o e-mail de notificação enviado na
assinatura usa o assunto e o corpo do próprio dono, com o padrão como
alternativa; e quando qualquer usuário consegue baixar os seus dados pessoais
como um arquivo JSON e excluir a sua conta. Fonte: issues do upstream
DamageLabs/clahub #270, #274 e #268, nessa ordem.

```
[ ] resign-on-version-bump       os donos podem exigir nova assinatura quando uma nova versão do CLA é publicada, com um prazo de tolerância opcional (#270)
[ ] custom-email-templates       os donos personalizam o assunto e o corpo do e-mail de nova assinatura com variáveis e uma prévia (#274)
[ ] gdpr-export-and-deletion     os usuários baixam os seus dados em JSON e excluem a sua conta (#268)
```
````

Desde o commit `bff8414` do focus-kit, o `/analyze` termina o primeiro marco com mais uma linha, a revisão dele, `m1-review` ([capítulo 12](12-closing-a-milestone.md)).
Esta execução usou o kit em `26e5e1e`, antes dessa regra, então a sua fila tem uma linha a mais que a de cima.
Cada issue é uma entrega com um slug para a sua página, e o parágrafo diz o que é verdade quando o marco fecha; a próxima seção mostra que a primeira versão dizia bem menos.

## Confira contra o código

Em um projeto novo você confere os documentos contra o que respondeu (capítulo 7).
Em um projeto existente, quase tudo o que o agente escreveu está marcado como observado, então a revisão é uma conferência de fatos:

* toda afirmação observada é verdadeira no código: abra o arquivo que ela nomeia e leia;
* toda questão em aberto é uma contradição que o código tem de fato;
* nada descreve o que deveria existir em vez do que existe.

Na execução, sem interface, o agente escreveu os documentos sem mostrar o diff antes, então toda a conferência veio depois.[^analyze-run]
Quando uma afirmação está errada, peça ao agente, na mesma sessão, que a confira contra o código e a corrija, e deixe que ele escreva a mudança ([capítulo 6](06-the-documents.md)).

A linha Local do docs/01 dizia que a configuração local lê `.env.local`.
Essa é a palavra do README, tomada como fato, e era só meio verdadeira.
O pedido foi este; o original está em inglês, e aqui vai traduzido:[^analyze-run]

```markdown
O docs/01 diz que a configuração local usa .env.local. Confira isso contra o prisma.config.ts e o README, e corrija o docs/01; onde eles discordarem, registre uma questão em aberto.
```

O agente leu a configuração do Prisma, os arquivos de ambiente de exemplo e a configuração dos testes ponta a ponta, e reescreveu a linha; esta é a primeira parte do diff dele:[^analyze-run]

```diff
--- a/docs/01-Architecture.md
+++ b/docs/01-Architecture.md
@@ -82,9 +82,22 @@
 
 ## Environments
 
-* **Local:** `npm run dev` on port 3000, SQLite file from `DATABASE_URL`,
-  `.env.local`; webhooks need a tunnel (ngrok). E2E reuses the running dev
-  server.
+* **Local:** `npm run dev` on port 3000; webhooks need a tunnel (ngrok).
+  Configuration comes from two files read by different tools:
+  * Next.js (`dev`, `build`, `start`) reads `.env.local` (and `.env`).
+  * The Prisma CLI (`db:push`, `migrate`, `db:seed`, `studio`) reads only
+    `.env`: `prisma.config.ts` and `prisma/seed.ts` load it through
+    `import "dotenv/config"`, which ignores `.env.local`.
+  * `DATABASE_URL` is a path relative to the repository root
+    (`file:./clahub.db` in `.env.local.example`); the app and the Prisma CLI
+    both resolve it from there.
+  * Playwright loads `.env.local`, then `.env.test`, without overriding, so
+    locally the E2E run sees the `DATABASE_URL` of `.env.local`. When no dev
+    server is on port 3000, its global setup force-resets and seeds that
+    database; otherwise it reuses the running server and its data.
+
+  Where README, `docs/getting-started.md` and the code disagree, see the
+  open questions below.
 * **CI (GitHub Actions):** on push and PR to `main`: lint, `tsc --noEmit`,
   unit tests, build; then Playwright E2E against a fresh `test.db`.
 * **Production:** https://www.cla-hub.io. `docs/deployment.md` describes a
```

O diff fica como o agente o escreveu, em inglês: a linha nova diz que o Next.js lê `.env.local` (e `.env`), que a CLI do Prisma lê só `.env`, porque `prisma.config.ts` e `prisma/seed.ts` o carregam com `import "dotenv/config"`, que o `DATABASE_URL` é relativo à raiz do repositório, e que o Playwright carrega `.env.local` e depois `.env.test` sem sobrescrever, então localmente um teste ponta a ponta sem servidor de desenvolvimento zera e popula o banco do `.env.local`.
A segunda parte acrescentou a seção de questões em aberto citada acima, com as outras contradições que ele achou enquanto conferia: uma variável que os guias chamam de obrigatória e que nenhum código lê, e uma execução local dos testes ponta a ponta que pode zerar o banco de desenvolvimento; ambas se confirmam no código.
Os documentos se liam bem antes do pedido, e só abrir o arquivo por trás da afirmação mostrou que ela estava errada.

A revisão achou uma segunda lacuna, de insumo e não de fato.
`acceptEdits` é um modo de permissão do Claude Code, a configuração que decide o que o agente faz sem perguntar a você: nele o agente lê, edita arquivos e roda comandos comuns de arquivo, e todo o resto, como o `gh` ou abrir uma página da web, precisa da sua aprovação.[^claude-code-permission-modes]
É a menor permissão de que o comando precisa, e a execução o usou sem interface, sem ninguém para responder, então toda aprovação que o agente pediu foi negada: o host negou a ele tanto o `gh` quanto a leitura das páginas das issues, e ele escreveu a fila só com os números das issues; o original está em inglês, e aqui vai traduzido:[^analyze-run]

````markdown
# Fila

## Marco 1: issues abertas no upstream

Fecha quando as três issues abertas no upstream em DamageLabs/clahub estão
resolvidas, em um branch cada, com a verificação verde, uma página por issue em
`work/done/`. O texto da issue é lido na hora do /propose; as linhas abaixo nomeiam
só a issue.

```
[ ] issue-270    resolver a issue #270 do upstream (https://github.com/DamageLabs/clahub/issues/270)
[ ] issue-274    resolver a issue #274 do upstream (https://github.com/DamageLabs/clahub/issues/274)
[ ] issue-268    resolver a issue #268 do upstream (https://github.com/DamageLabs/clahub/issues/268)
```
````

Numa sessão interativa você veria essa pergunta e aprovaria o `gh issue view` ali mesmo, e a lacuna só chegaria até você se você a negasse.
Sem interface, a correção foi essa aprovação dada de antemão: liberou um comando, `gh issue view`, por mais um turno na mesma sessão, com este pedido; o original está em inglês, e aqui vai traduzido:[^analyze-run]

```markdown
Leia as três issues com gh issue view e reescreva o marco e as linhas dele a partir delas.
```

O agente leu as três issues e reescreveu o marco e as linhas dele como mostra a seção anterior; não mudou mais nada.
A resposta dele também apontou onde as issues batem de frente com as regras documentadas, como excluir logs de auditoria contra a regra de que toda mudança é guardada, e deixou esses pontos para o `/propose` resolver com você.

## Pontos-chave

* O `/analyze` lê o repositório primeiro, com código ou não (o README e a documentação, os manifestos, a árvore, os pontos de entrada, os testes, o CI, os assuntos dos últimos cinquenta commits, qualquer arquivo de regras) e depois faz uma rodada de quatro assuntos.
* Ponha tudo o que você tem sobre o projeto em `context/` e diga ao agente que leia primeiro: o que ele não lê, ele tem que adivinhar.
* O padrão de cada escolha é o que o código já faz, e o agente diz o que é, então "your call" o mantém; uma contradição vira uma questão em aberto para uma entrega futura.
* Em um projeto existente, a revisão é uma conferência de fatos: abra o arquivo por trás de cada afirmação observada.
* Uma correção é um pedido na mesma sessão, nunca uma edição à mão; dê ao agente o que ele precisa para conferir, um arquivo ou uma permissão, e deixe que ele escreva.

## Exercícios

### Exercício 8.1

Clone o fork `JCKodel/clahub` em `book-v1` em um branch seu, instale o kit (capítulo 5), faça o commit (o capítulo 11 mostra como), rode o `/analyze` e responda com o briefing deste capítulo.
Compare o que você obtiver com `book-v1-analyze`: o que difere, e alguma diferença está errada sobre o código?

### Exercício 8.2

Escolha três afirmações do docs/01 ou do docs/04 em `book-v1-analyze` e encontre cada uma no código.
Qual arquivo prova cada uma?

### Exercício 8.3

Rode o `/analyze` em um repositório seu.
Quais questões em aberto ele registrou, e quais delas você teria deixado passar?

[^strangler-fig]: Martin Fowler, "Strangler Fig", 2024. <https://martinfowler.com/bliki/StranglerFigApplication.html>
[^brownfield-research]: A entrega de pesquisa deste livro para o projeto brownfield, 2026-09-25: os candidatos, como cada um foi medido, a escolha, e as linhas de código TypeScript (sem os testes) e os testes que passam do CLAHub no commit do upstream 9d1e666e1d30f271aea9640393229a7cbfbd1b62. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/brownfield-research.md>
[^analyze-run]: A execução do `/analyze` deste livro no projeto brownfield, 2026-09-28, com o Claude Code 2.1.283 e o modelo `claude-opus-5-5`, de `book-v1` até a tag do capítulo `book-v1-analyze`: a instalação do kit, o briefing, os comandos, a saída de cada turno, a rodada e a sua resposta, e as correções. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/analyze-run/README.md>
[^claude-code-permission-modes]: Anthropic, "Choose a permission mode", documentação do Claude Code, acesso em 2026-09-29. <https://code.claude.com/docs/en/permission-modes>
