# 8. Instalação, e os hosts

Depois deste capítulo você consegue instalar o focus-kit num repositório com uma frase para o seu agente de código, atualizá-lo com a mesma frase, sabendo o que a atualização escreve e o que ela só relata a você, e chamar os seus comandos no host que você usa.
Você também consegue dizer por que o método não depende do host.

## O problema

Um método preso a uma ferramenta dura enquanto o time mantém essa ferramenta, e um time raramente concorda em uma só.
Uma pessoa trabalha no Claude Code, outra no Copilot dentro do seu editor, uma terceira experimenta o Codex, e cada host, o programa que roda o agente de código, procura as suas regras e os seus comandos em pastas próprias.
O kit precisa abrir pronto em todos eles, e ser instalado sem pedir a ninguém que instale nada.

## Instalação

Abra o seu agente de código na raiz do repositório e diga:

```
Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md
and do what it says.
```

O endereço é o próprio arquivo, não a página que o GitHub desenha em volta dele, então o agente recebe o texto inteiro.
Esse arquivo é o arquivo de setup do kit: um arquivo de instruções que o agente lê e transforma nos arquivos do kit, os quatro comandos e alguns pequenos arquivos-ponteiro para os hosts que precisam deles.
Nada é instalado na sua máquina; o agente escreve arquivos no repositório, e é só isso.
O seu host pode perguntar antes de baixar o arquivo e antes de escrever na sua própria pasta dentro do repositório, `.claude/` no Claude Code: aprove os dois.

O arquivo de setup manda o agente copiar cada arquivo byte a byte.
Alguns hosts buscam uma página web por uma ferramenta que entrega ao agente um resumo da página em vez do seu texto; se o seu faz isso, peça ao agente que baixe o arquivo e o leia inteiro.

A instalação não coloca nada em stage nem faz commit.
Você lê o que ela escreveu e faz o commit você mesmo, como em toda mudança que o agente faz (capítulo 13).

## O que a instalação nunca toca, e como atualizar

O arquivo de setup escreve os arquivos do kit e mais nada.
`docs/`, `work/`, `AGENTS.md` e `CLAUDE.md` pertencem ao projeto: os comandos os escrevem, a começar pelo `/brainstorm` ou pelo `/analyze` (capítulo 9), e o arquivo de setup nunca os toca.
Um `GEMINI.md` que já guarda o texto do próprio projeto o mantém; o kit só acrescenta uma linha no topo.

Para atualizar o kit, diga a mesma frase de novo.
O agente escreve os arquivos do kit como o arquivo de setup os guarda agora, e a mudança que você revisa é só do kit, sem nada do seu projeto.
Ele substitui um arquivo só quando esse arquivo é um que o kit entregou, nesta versão ou numa anterior.
Um comando seu na pasta de um host, ou uma edição que você fez à mão num dos arquivos do kit, o `.claude/skills/apply/SKILL.md`, por exemplo, faz a atualização parar antes de escrever qualquer arquivo: o agente mostra o diff contra o arquivo do kit, e você decide se fica com o seu ou o substitui.

## O que uma atualização relata

O docs/04, o docs/05, o docs/06 e o `AGENTS.md` pertencem ao projeto: o time escreveu ali as suas regras, as suas escolhas junto, como o comando de verificação ou trabalhar em trunk, e a sua fila.
Quando uma versão nova do kit muda o que esses arquivos deveriam guardar, o arquivo de setup não o escreve.
Ele compara os arquivos com os seus próprios modelos e relata cada migração, uma mudança de que os seus documentos ainda precisam: o caminho, a seção ou a linha, e o texto que ele propõe, na língua da documentação do projeto.
Uma migração pode citar uma regra, uma linha da fila ou um slot.
As suas escolhas ficam: um docs/05 cujo §5 diz "trunk, uma sessão por vez" vê proposto o texto para duas sessões numa pasta, e mantém o seu até o time aceitar a mudança.

Este é o relatório de uma atualização na biblioteca de empréstimos, escrito para este capítulo:

```
Instalado: focus-kit 2026.10.16.2, em cada SKILL.md.
Migrações de processo pendentes: 8.

1. docs/05, §2 The flow: trocar "e a resposta para ali, ou, quando
   a pessoa quer defini-la agora, a conversa segue como
   /propose <slug> na mesma sessão, e o que foi dito vira a página"
   por "; o que foi dito e a linha não comporta vai para um rascunho
   work/<slug>.md. A resposta para ali e cita /propose <slug> para
   uma sessão nova, como este host invoca comandos". Depois de "ou
   reusar o existente ao retomar", acrescentar ", trazendo para ele
   qualquer rascunho deixado para o slug".
2. docs/05, §3 The page: depois de "A única seção que precisa ser
   exata", acrescentar ": uma tela errada se corrige numa sessão,
   uma coluna errada é uma migration, e uma regra de acesso errada
   já vazou".
3. docs/05, §4 The queue: depois da tabela de marcas, acrescentar
   "Um quadro pode ler a fila, e as pessoas puxam trabalho dele,
   então uma marca muda na hora: [~] é a primeira edição do
   /propose, [*] a primeira do /apply, e [x] a última do /apply.
   Sem quadro, as marcas não custam nada."
4. docs/05, §5 This project: acrescentar o slot Milestone review
   antes do Git: "Milestone review: o /code-review ultra <base> do
   Claude Code, lançado pela pessoa contra o commit que a página da
   revisão cita."
5. docs/05, §5 Publish policy: acrescentar "Seja qual for, as
   últimas palavras do /apply dizem qual ambiente está em qual
   versão."
6. docs/05, §7: "nenhuma barreira antes da implementação" vira
   "nenhuma barreira antes da implementação além de uma página
   completa".
7. docs/05, §8 Closing a milestone: "Ela não revisa código e não
   corrige nada." vira "Ela não corrige nada." Depois desse
   parágrafo, acrescentar "A revisão também lê o código: a sua
   página cita o commit que fechou o marco anterior, ou o primeiro
   commit, e a pessoa lança o Milestone review do §5 contra ele."
8. AGENTS.md, Non-negotiables, a linha "One delivery": depois de
   "vira uma linha [ ] no docs/06", acrescentar "com um rascunho de
   página para o que a linha não comporta", e terminá-la "citando o
   /propose para uma sessão nova (docs/05 §2)".

docs/ e AGENTS.md não foram alterados.
```

Os itens 1, 3, 4 e 7 mudam uma regra: uma mudança pedida fora do `/apply` para na linha, com um rascunho para o que a linha não comporta, e o próximo `/propose` roda numa sessão nova ([capítulo 11](11-queue-and-milestones.md)); uma marca muda na hora, para que um quadro que lê a fila mostre o que já foi pego ([capítulo 14](14-queue-states.md)); e a revisão de um marco também lê o código, pelo slot que cita a revisão que uma pessoa lança ([capítulo 15](15-closing-a-milestone.md)).
Os itens 2, 5, 6 e 8 mudam só palavras, para uma regra que os documentos já guardam.

A versão do kit é o `metadata.version` em cada `SKILL.md`; o processo é o que o docs/04, o docs/05 e o `AGENTS.md` dizem, porque todo comando os lê, então um kit atualizado cujas migrações não foram aplicadas ainda roda o processo antigo.
A atualização termina quando as migrações são aplicadas, como qualquer mudança: uma linha da fila, definida com o `/propose` e construída com o `/apply`, para que a mudança nas suas regras ou na sua fila tenha uma página, verificação e a sua revisão.

Num projeto já documentado, a atualização relata as migrações primeiro, ou diz que não há nenhuma.
Ela nunca pede que você rode o `/brainstorm` ou o `/analyze` de novo: eles escrevem os documentos de um projeto do zero, e os seus existem.
Uma versão que não pede nada aos seus documentos não relata migração: uma versão que muda só os comandos, como o `/apply` mostrar a sua mensagem de commit também na conversa, não muda mais nada.
Um docs/05 cujo slot Git escolheu um worktree por entrega e não cita pasta recebe uma migração só quando o projeto já trabalha num contêiner, a pasta que o [capítulo 19](19-worktrees.md) organiza com o checkout e uma pasta oculta para o histórico e os worktrees, e essa pasta oculta guarda `repo.git/`.
O relatório então propõe escrever ali o nome dessa pasta e o prefixo que os branches das entregas já usam, para que nada mude de lugar.
Sem contêiner ainda, o slot vale o padrão do kit, que esse capítulo cita, e o relatório não propõe nada.

Para saber por que uma migração existe, leia o changelog do kit, `CHANGELOG.md` no repositório dele, `CHANGELOG.pt.md` em português.
Ele tem uma entrada por versão, a mais nova primeiro; a versão é a linha `Version:` do `SETUP.md`, o mesmo valor do `metadata.version` em cada `SKILL.md`.
Cada entrada diz o que mudou e o problema que causou a mudança, e um item que começa com `Migration:` (no changelog em português, `Migração:`) diz o que mudar nos documentos do projeto.
Todos os itens do relatório acima vêm de um item desses, que diz que o relatório confere o docs/05 §§2, 3, 4, 6, 7 e 8, o slot Milestone review, a última frase da Publish policy e a linha do `AGENTS.md` sobre uma mudança pedida fora do `/apply`; desses, ele lista o que os seus documentos ainda não têm.

## Como cada host encontra os comandos

Um host precisa de duas coisas do repositório: o arquivo de regras, `AGENTS.md`, e os comandos, cada um com o slug que você digita depois dele, o nome da entrega em `work/<slug>.md` (capítulo 12).
O arquivo de setup escreve o que cada host abaixo precisa:

| Host | Lê as regras de | Lê os comandos de | Você digita |
|---|---|---|---|
| Claude Code | `CLAUDE.md`, que importa o `AGENTS.md` | `.claude/skills/` | `/propose <slug>` |
| Codex | `AGENTS.md` | `.agents/skills/` | `$propose <slug>` |
| GitHub Copilot | `AGENTS.md` | `.agents/skills/`, por um arquivo de prompt em `.github/prompts/` | `/propose`, e ele pede o slug |
| Cursor | `AGENTS.md` | `.agents/skills/`, por um arquivo de comando em `.cursor/commands/` | `/propose` |
| Gemini CLI | `AGENTS.md`, pelo `GEMINI.md` | `.agents/skills/`, por um arquivo de comando em `.gemini/commands/` | `/propose <slug>` |
| Google Antigravity | `AGENTS.md`, por uma regra em `.agents/rules/` | `.agents/skills/` | `/propose <slug>` |
| Windsurf | `AGENTS.md` | `.windsurf/skills/` | `@propose <slug>` |
| OpenCode, Zed | `AGENTS.md` | `.agents/skills/` | pedindo a skill |

Cada comando é uma skill, uma pasta com um arquivo `SKILL.md` de instruções que o host carrega quando você a chama.[^claude-code-skills][^codex-skills][^copilot-skills]
O Claude Code lê o `CLAUDE.md` no início de uma sessão, e uma linha `@AGENTS.md` nele importa o arquivo de regras.[^claude-code-memory]
O Codex e o Copilot leem o `AGENTS.md` sozinhos.[^codex-agents-md][^copilot-instructions]
O comando de barra do Copilot vem de um arquivo de prompt que só diz ao agente para ler a skill e segui-la, e pede o slug quando você digita o comando.[^copilot-prompt-files]
O Codex pode rodar uma skill por conta própria quando uma mensagem bate com a descrição dela; um pequeno arquivo ao lado de cada skill desliga isso, para que uma mensagem que por acaso diga "apply" não construa nada que você não pediu.[^codex-skills]
Para o Cursor, a documentação do fornecedor não diz se um slug digitado depois de um comando chega até ele, então nomeie a entrega na sua mensagem se não chegar.

Todo comando termina dizendo o próximo, escrito como o host que o roda o invoca, a última coluna da tabela.
O arquivo de setup cita o `/brainstorm` ou o `/analyze`, o `/propose` cita o `/apply` com o slug da página, e o `/apply` cita a próxima linha da fila.
Na biblioteca de empréstimos, depois de `/propose emprestar-livro`, o Claude Code diz para você rodar `/apply emprestar-livro` numa sessão nova, e o Codex diz para rodar `$apply emprestar-livro`.
Os arquivos do kit são os mesmos nos dois; a forma segue o host que os roda.

O arquivo de setup do kit mantém esta tabela atualizada, com a página do fornecedor de onde cada linha foi lida, e só acrescenta um host com a documentação dele em mãos; outros hosts que leem o `AGENTS.md` ainda conseguem rodar um comando quando você pede a skill dele em palavras.

## Por que o método não depende do host

Os hosts diferem nas pastas e no caractere que inicia um comando, e compartilham três fatos.
Cada um lê um arquivo de regras no início de uma sessão, o `AGENTS.md` direto ou por um ponteiro.
Cada um lê os arquivos para os quais você aponta.
Cada um consegue escrever arquivos.

O método não precisa de mais nada.
Ele mora em arquivos simples: o arquivo de regras, os documentos do projeto que uma sessão nova lê, as páginas em `work/` e os comandos, que só dizem quais documentos ler e o que nunca fazer.
O arquivo de setup escreve os arquivos de todos os hosts, seja qual for o host que o roda, então o repositório abre pronto em qualquer um deles, e uma pessoa que troca de host encontra os mesmos documentos, a mesma fila e os mesmos comandos.

## O que o time ganha

Um repositório abre pronto em qualquer host, então cada pessoa fica com o host que prefere e o time ainda compartilha um processo, e trocar de host não muda nada no projeto.

Uma atualização nunca reescreve as regras que o time escreveu.
Uma versão que pede uma mudança nos documentos do projeto chega ao projeto como uma lista do que mudar e onde, com as regras do próprio time ainda no lugar, e o time a aplica como aplica qualquer mudança.

E o próximo comando chega na forma que o seu host reconhece, porque um host pode não reconhecer a forma de outro: o Codex não reconhece `/propose`, já que o Codex invoca skills com `$`.

## Pontos-chave

* Uma frase para o seu agente instala o focus-kit, e a mesma frase o atualiza; nada é instalado na sua máquina, nada é colocado em stage nem vai para um commit, e um arquivo do kit que você mudou faz a atualização parar antes de escrever.
* O arquivo de setup escreve só os arquivos do kit e nunca toca `docs/`, `work/`, `AGENTS.md` ou `CLAUDE.md`; uma mudança de que o docs/04, o docs/05, o docs/06 ou o `AGENTS.md` precisa, uma regra, uma linha da fila ou um slot, vem como uma migração no relatório dele, e até o time aplicá-la como uma entrega o processo é o antigo.
* O changelog do kit, a entrada mais nova primeiro, diz para cada versão o que mudou, o problema que causou a mudança e, num item de migração, o que mudar nos documentos do projeto.
* Cada host encontra as regras e os comandos nas suas próprias pastas: o Claude Code roda um comando como `/propose <slug>`, o Codex como `$propose <slug>`, o Copilot como `/propose`, que pede o slug, o Windsurf como `@propose <slug>`; todo comando cita o próximo nessa forma.
* Todo host lê um arquivo de regras no início, lê os arquivos para os quais você aponta e escreve arquivos, e o método não precisa de mais nada.

[^claude-code-memory]: Anthropic, "How Claude remembers your project", documentação do Claude Code, acesso em 2026-09-30. <https://code.claude.com/docs/en/memory>
[^claude-code-skills]: Anthropic, "Extend Claude with skills", documentação do Claude Code, acesso em 2026-09-30. <https://code.claude.com/docs/en/skills>
[^codex-agents-md]: OpenAI, "Custom instructions with AGENTS.md", documentação do Codex, acesso em 2026-09-30. <https://developers.openai.com/codex/guides/agents-md>
[^codex-skills]: OpenAI, "Build skills", documentação do Codex, acesso em 2026-09-30. <https://developers.openai.com/codex/skills>
[^copilot-instructions]: GitHub, "Adding repository custom instructions for GitHub Copilot", GitHub Docs, acesso em 2026-09-30. <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
[^copilot-skills]: GitHub, "About agent skills", GitHub Docs, acesso em 2026-09-30. <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
[^copilot-prompt-files]: GitHub, "Your first prompt file", GitHub Docs, acesso em 2026-09-30. <https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file>
