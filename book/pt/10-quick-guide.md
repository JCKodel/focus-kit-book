# 10. Do zero à primeira entrega

Depois deste capítulo você consegue levar um projeto, novo ou já com código, de uma sessão vazia do seu host até a primeira entrega com commit, passo a passo.
Cada passo diz o que digitar ou fazer, o que você vê quando deu certo, e o único capítulo que o ensina, então você consegue segui-lo sem nenhum outro capítulo aberto.

## Antes de começar

Você precisa de um repositório git, vazio ou com código, e de um host da tabela do [capítulo 8](08-install-and-hosts.md), o programa que roda o seu agente de código.
O kit é instalado com a única frase que esse capítulo dá, dita ao seu agente na raiz do repositório:

```
Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md
and do what it says.
```

Os passos estão escritos para o Claude Code.
Em outro host, um comando toma a forma da tabela do capítulo 8:

| Host | Você digita |
|---|---|
| Claude Code | `/propose <slug>` |
| Codex | `$propose <slug>` |
| GitHub Copilot | `/propose`, e ele pede o slug |
| Cursor | `/propose` |
| Gemini CLI | `/propose <slug>` |
| Google Antigravity | `/propose <slug>` |
| Devin Desktop, antes Windsurf | `/propose` |
| OpenCode, Zed | pedindo a skill |
| Jules, Junie, Warp, Kiro, Roo Code, Cline | pedindo em palavras o `.agents/skills/propose/SKILL.md` |

O `/apply` toma a mesma forma que o `/propose`, com o slug da entrega depois dele, ou como resposta quando o host o pede, ou, onde nenhum dos dois funciona, na sua mensagem; o `/brainstorm` e o `/analyze` a tomam sem slug, `$brainstorm` no Codex.
No Claude Code um comando só roda quando você o nomeia: uma mensagem que por acaso bate com o que ele faz não inicia nada.

Uma escolha é sua antes do primeiro `/propose`: a estratégia de git, trunk, um branch por entrega ou um worktree por entrega.
O `/brainstorm` e o `/analyze` perguntam com um padrão e escrevem a sua resposta no docs/05: trunk para uma pessoa, e, num projeto com código, o que o repositório já faz.
O [capítulo 18](18-git-essentials.md) e o [capítulo 19](19-worktrees.md) ensinam as três; os passos abaixo supõem trunk.

## Um projeto novo

1. Abra o Claude Code na raiz do repositório vazio e diga a frase acima.
   Você vê os quatro comandos do kit em `.claude/skills/`, nada em stage nem com commit, e o agente nomeando o `/brainstorm` como o próximo passo, numa sessão nova.
   Ensinado no [capítulo 8](08-install-and-hosts.md), "Instalação".
2. Abra uma sessão nova, não a que rodou a instalação, digite `/brainstorm` e responda às perguntas dele, um assunto por vez; "your call" (você decide) mantém o padrão do agente.
   Você vê o docs/00 ao 06, `docs/adr/`, `AGENTS.md`, `CLAUDE.md` e `work/done/` escritos, a fila mostrada, e o agente nomeando o `/propose <slug>` para a primeira linha da fila.
   Ensinado no [capítulo 9](09-starting-a-project.md), "`/brainstorm`: um projeto novo".
3. Leia os documentos contra a lista de conferência do capítulo 9 e peça ao agente cada correção na mesma sessão.
   Depois coloque em stage, pelo nome, só os arquivos que a instalação relatou ter escrito e os que o `/brainstorm` escreveu; nunca `git add -A`, `git add .` ou uma pasta inteira como `.claude/`, que levariam junto uma anotação ou uma edição sua ao lado deles.
   Uma parte dessa lista, para completar com o relato da instalação e os arquivos que o `/brainstorm` escreveu, não para copiar como está:

   ```
   git add AGENTS.md CLAUDE.md work/done/.gitkeep
   git add .claude/skills/propose/SKILL.md
   ```

   Leia o que está em stage com `git diff --staged`, como o passo 7 faz: um arquivo que nem a instalação nem o `/brainstorm` escreveram não é deste commit, mesmo um posto em stage antes de você começar, e nomear caminhos não o tira de lá; descubra de quem ele é, e tire-o com `git rm --cached <caminho>` quando souber que ele pode ficar para um commit próprio, o que mantém o arquivo no disco; o `git restore --staged`, que o capítulo 19 usa, precisa de um primeiro commit existindo.
   Então `git commit -m "Adicionar o kit e os documentos do /brainstorm"`, uma mensagem escrita para este capítulo, só o assunto, já que ainda não há página para a sua última linha.
   Você vê um commit no `git log` com os documentos, o `AGENTS.md`, o `CLAUDE.md` e os arquivos do kit nas pastas do host, e nada mais; daqui em diante, o seu docs/05 é dono do formato de cada mensagem.
   Ensinado no [capítulo 9](09-starting-a-project.md), "Revise antes do commit".
4. Numa sessão nova, digite `/propose <slug>`, com o slug da primeira linha da fila, e responda ao que os documentos deixam em aberto.
   Você vê `work/<slug>.md` escrito, a linha dele no docs/06 marcada `[>]`, e o agente pedindo que você leia a página e depois rode o `/apply <slug>` numa sessão nova.
   Ensinado no [capítulo 12](12-propose.md), "O que o `/propose` faz".
5. Leia a página com as perguntas do capítulo 12, e peça ao agente cada correção nessa mesma sessão.
   Você vê uma página em que cada linha de Comportamento pode ser conferida, cujo Fora do escopo nomeia o que você supunha que entrava, e nenhuma pergunta em aberto.
   Ensinado no [capítulo 12](12-propose.md), "Leia a página antes do `/apply`".
6. Abra uma sessão nova, nunca a que rodou o `/propose`, porque a página precisa bastar sozinha, e digite `/apply <slug>`.
   Você vê a verificação verde, a página movida para `work/done/`, a linha dela marcada `[x]`, a entrega em stage, a mensagem sugerida num bloco `commit`, na página e na conversa, e os seus próximos passos, começando por usar o que a entrega mudou; quando a entrega é a primeira depois da qual uma pessoa consegue rodar o produto, como o esqueleto, também o manual de rodá-lo em `docs/manuals/`.
   Ensinado no [capítulo 13](13-apply.md), "O que o `/apply` faz".
7. Use o que a entrega construiu como o usuário dela usaria, no ambiente que a última frase do `/apply` nomeia: para a `emprestar-livro` do capítulo 12, empreste um exemplar e tente cada recusa que a página dela lista; para um documento, abra o que ele gera e leia, sem tela nenhuma a inventar.
   Depois leia a mudança em stage com `git diff --staged` contra a página, e peça ao agente cada correção na mesma sessão.
   Você vê a entrega fazer o que a página dela diz, só esta entrega em stage, cada linha de Comportamento respondida, e uma mensagem cuja última linha é `work/done/<slug>.md`.
   Ensinado no [capítulo 13](13-apply.md), "Revise a mudança em stage".
8. Digite `git commit` e cole a mensagem do bloco `commit` no fim da página.
   Você vê um commit novo no `git log`, com a página em `work/done/` e a construção dela.
   Ensinado no [capítulo 13](13-apply.md), "O commit é a revisão humana".

Um projeto deixado depois do passo 3 está pronto para o kit: qualquer sessão posterior lê os documentos dele e começa no passo 4.

## Um projeto existente

1. Instale como no passo 1 do projeto novo, na raiz do repositório com código.
   Você vê os mesmos arquivos do kit, nenhum arquivo do seu código alterado, e o agente nomeando o `/analyze` como o próximo passo, numa sessão nova.
   Ensinado no [capítulo 8](08-install-and-hosts.md), "O que a instalação nunca toca, e como atualizar".
2. Ponha o que o código não diz numa pasta `context/` na raiz, como está: propostas, contratos, e-mails, transcrições de reuniões, tickets.
   Você vê uma pasta ao lado do código, sem nada ordenado nem resumido.
   Ensinado no [capítulo 17](17-project-as-assistant.md), "A pasta de contexto".
3. Abra uma sessão nova, não a que rodou a instalação, digite `/analyze` e responda à única rodada dele; cada padrão é o que o código já faz.
   Você vê a mudança mostrada antes de ser escrita, depois os documentos do passo 2 do projeto novo, o manual de rodar o produto a partir de um clone novo e um para cada coisa que uma pessoa já faz à mão, em `docs/manuals/`, cada afirmação deduzida marcada como observada, e o agente nomeando o `/propose <slug>`.
   Ensinado no [capítulo 9](09-starting-a-project.md), "`/analyze`: um projeto existente".
4. Confira cada afirmação observada contra o código, abrindo o arquivo que ela cita, e então revise e faça o commit como no passo 3 do projeto novo, colocando em stage pelo nome só o que a instalação e o `/analyze` escreveram, a partir de uma árvore sem mudança sua, com `/analyze` na mensagem.
   Você vê um commit com os documentos, o `AGENTS.md`, o `CLAUDE.md` e os arquivos do kit nas pastas do host, e nada do seu código.
   Ensinado no [capítulo 9](09-starting-a-project.md), "Revise antes do commit".
5. Numa sessão nova, digite `/propose <slug>` para a primeira linha da fila: com o código já lá, não há esqueleto a construir, então ela é a menor mudança de que o primeiro marco precisa.
   Você vê uma página cujo Pronto quando roda o comando de verificação que o `/analyze` observou, e o agente pedindo que você a leia.
   Ensinado no [capítulo 12](12-propose.md), "O que o `/propose` faz".

Dali em diante, siga os passos 5 a 8 do projeto novo, sem mudança.

Os testes e a CI que já existem são o comando de verificação, ou parte dele, como o `/analyze` os registrou no docs/05.
O backlog que já existe é lido para o primeiro marco pelo `/analyze`, de três a oito linhas, e o resto espera na ferramenta dele.
Nada mais no repositório muda até que uma entrega o toque.

## O ciclo depois da primeira entrega

A próxima entrega é a primeira linha livre da fila ([capítulo 11](11-queue-and-milestones.md)).
Cada entrega é uma página, uma construção e um commit, os passos 4 a 8 do projeto novo.
Um marco fecha com a sua revisão, a última linha dele, uma entrega como as outras ([capítulo 15](15-closing-a-milestone.md)).

## Quando parar um piloto

Um piloto, um marco rodado no método para ver se ele compensa ([capítulo 23](23-adoption.md)), não está compensando quando aparece um de três sinais:

* as páginas são escritas e ninguém as lê antes do `/apply`;
* a fila não é o plano que o time segue;
* "pronto" ainda é dito sem a verificação verde.

Quando ele para, os documentos ficam: são a documentação do projeto de um jeito ou de outro.

## O que o time ganha

Qualquer pessoa do time, desenvolvedora ou não, vai de uma sessão vazia a uma primeira entrega com commit seguindo uma lista, cada passo a um link do seu motivo.

## Pontos-chave

* Antes do primeiro `/propose` você precisa de um repositório, de um host, do kit instalado com uma frase e de uma resposta à pergunta de git; trunk serve a uma pessoa.
* Um projeto novo: instalar, `/brainstorm` numa sessão nova, revisar os documentos e fazer o commit deles, `/propose` da primeira linha, ler a página, `/apply` numa sessão nova, usar o que ele construiu, ler a mudança em stage, fazer o commit.
* Um projeto existente: `context/` primeiro, depois o `/analyze` numa sessão nova, cada afirmação observada conferida contra o código; a primeira entrega é a menor mudança de que o primeiro marco precisa, conferida pelo comando de verificação que o `/analyze` observou.
* Os documentos são o primeiro commit do projeto, e um projeto parado ali está pronto para qualquer sessão posterior.
* Um piloto para quando as páginas ficam sem leitura, a fila não é o plano ou "pronto" é dito sem a verificação; os documentos ficam.
