# 11. Instalação, e os hosts

Depois deste capítulo você consegue instalar o focus-kit num repositório com uma frase para o seu agente de código, atualizá-lo com a mesma frase, e chamar os seus comandos no host que você usa.
Você também consegue dizer por que o método não depende do host.

## O problema

Um método preso a uma ferramenta dura enquanto o time mantém essa ferramenta, e um time raramente concorda em uma só.
Uma pessoa trabalha no Claude Code, outra no Copilot dentro do seu editor, uma terceira experimenta o Codex, e cada host, o programa que roda o agente de código, procura as suas regras e os seus comandos em pastas próprias.
O kit precisa abrir pronto em todos eles, e ser instalado sem pedir a ninguém que instale nada.

## Instalação

Abra o seu agente de código na raiz do repositório e diga:

```
Read https://github.com/JCKodel/focus-kit/blob/main/SETUP.md and follow its section 1.
```

Esse arquivo é o arquivo de setup do kit: um arquivo de instruções que o agente lê e transforma nos arquivos do kit, os quatro comandos e alguns pequenos arquivos-ponteiro para os hosts que precisam deles.
Nada é instalado na sua máquina; o agente escreve arquivos no repositório, e é só isso.
O seu host pode perguntar antes de baixar o arquivo e antes de escrever na sua própria pasta dentro do repositório, `.claude/` no Claude Code: aprove os dois.

O arquivo de setup manda o agente copiar cada arquivo byte a byte.
Alguns hosts buscam uma página web por uma ferramenta que entrega ao agente um resumo da página em vez do seu texto; se o seu faz isso, peça ao agente que baixe o arquivo e o leia inteiro.

A instalação não coloca nada em stage nem faz commit.
Você lê o que ela escreveu e faz o commit você mesmo, como em toda mudança que o agente faz (capítulo 15).

## O que a instalação nunca toca, e como atualizar

O arquivo de setup escreve os arquivos do kit e mais nada.
`docs/`, `work/`, `AGENTS.md` e `CLAUDE.md` pertencem ao projeto: os comandos os escrevem, a começar pelo `/brainstorm` ou pelo `/analyze` (capítulo 12), e o arquivo de setup nunca os toca.
Um `GEMINI.md` que já guarda o texto do próprio projeto o mantém; o kit só acrescenta uma linha no topo.

Para atualizar o kit, diga a mesma frase de novo.
O agente escreve os arquivos do kit como o arquivo de setup os guarda agora, e a mudança que você revisa é só do kit, sem nada do seu projeto.

## Como cada host encontra os comandos

Um host precisa de duas coisas do repositório: o arquivo de regras, `AGENTS.md`, e os comandos, cada um com o slug que você digita depois dele, o nome da entrega em `work/<slug>.md` (capítulo 14).
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

Cada comando é uma skill, uma pasta com um arquivo `SKILL.md` de instruções que o host carrega quando você a chama.[^claude-code-skills][^codex-skills][^copilot-skills]
O Claude Code lê o `CLAUDE.md` no início de uma sessão, e uma linha `@AGENTS.md` nele importa o arquivo de regras.[^claude-code-memory]
O Codex e o Copilot leem o `AGENTS.md` sozinhos.[^codex-agents-md][^copilot-instructions]
O comando de barra do Copilot vem de um arquivo de prompt que só diz ao agente para ler a skill e segui-la, e pede o slug quando você digita o comando.[^copilot-prompt-files]
O Codex pode rodar uma skill por conta própria quando uma mensagem bate com a descrição dela; um pequeno arquivo ao lado de cada skill desliga isso, para que uma mensagem que por acaso diga "apply" não construa nada que você não pediu.[^codex-skills]
Para o Cursor, a documentação do fornecedor não diz se um slug digitado depois de um comando chega até ele, então nomeie a entrega na sua mensagem se não chegar.

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
Não há número para esse ganho: é uma propriedade de arquivos simples.

## Pontos-chave

* Uma frase para o seu agente instala o focus-kit, e a mesma frase o atualiza; nada é instalado na sua máquina, e nada é colocado em stage nem vai para um commit.
* A instalação escreve só os arquivos do kit e nunca toca `docs/`, `work/`, `AGENTS.md` ou `CLAUDE.md`.
* Cada host encontra as regras e os comandos nas suas próprias pastas, e o arquivo de setup escreve todas elas a cada execução.
* O Claude Code roda um comando como `/propose <slug>`, o Codex como `$propose <slug>`, o Copilot como `/propose`, que pede o slug, o Windsurf como `@propose <slug>`.
* Todo host lê um arquivo de regras no início, lê os arquivos para os quais você aponta e escreve arquivos, e o método não precisa de mais nada.

[^claude-code-memory]: Anthropic, "How Claude remembers your project", documentação do Claude Code, acesso em 2026-09-30. <https://code.claude.com/docs/en/memory>
[^claude-code-skills]: Anthropic, "Extend Claude with skills", documentação do Claude Code, acesso em 2026-09-30. <https://code.claude.com/docs/en/skills>
[^codex-agents-md]: OpenAI, "Custom instructions with AGENTS.md", documentação do Codex, acesso em 2026-09-30. <https://developers.openai.com/codex/guides/agents-md>
[^codex-skills]: OpenAI, "Build skills", documentação do Codex, acesso em 2026-09-30. <https://developers.openai.com/codex/skills>
[^copilot-instructions]: GitHub, "Adding repository custom instructions for GitHub Copilot", GitHub Docs, acesso em 2026-09-30. <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
[^copilot-skills]: GitHub, "About agent skills", GitHub Docs, acesso em 2026-09-30. <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
[^copilot-prompt-files]: GitHub, "Your first prompt file", GitHub Docs, acesso em 2026-09-30. <https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file>
