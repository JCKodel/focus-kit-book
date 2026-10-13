# 11. Instalação, e os hosts

Depois deste capítulo você consegue instalar o focus-kit num repositório com uma frase para o seu agente de código, atualizá-lo com a mesma frase, sabendo o que a atualização escreve e o que ela só relata a você, e chamar os seus comandos no host que você usa.
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
Ele substitui um arquivo só quando esse arquivo é um que o kit entregou, nesta versão ou numa anterior.
Um comando seu na pasta de um host, ou uma edição que você fez à mão num dos arquivos do kit, o `.claude/skills/apply/SKILL.md`, por exemplo, faz a atualização parar antes de escrever qualquer arquivo: o agente mostra o diff contra o arquivo do kit, e você decide se fica com o seu ou o substitui.

## O que uma atualização relata

O docs/04, o docs/05 e o `AGENTS.md` pertencem ao projeto: o time escreveu ali as suas regras, e as suas escolhas junto, como o comando de verificação ou trabalhar em trunk.
Quando uma versão nova do kit muda uma regra que esses arquivos guardam, o arquivo de setup não a escreve.
Ele compara os arquivos com os seus próprios modelos e relata cada migração, uma regra que os seus documentos ainda precisam mudar: o caminho, a seção, e o texto que ele propõe, na língua da documentação do projeto.
As suas escolhas ficam: um docs/05 cujo §5 diz "trunk, uma sessão por vez" vê proposto o texto para duas sessões numa pasta, e mantém o seu até o time aceitar a mudança.

Este é o relatório da atualização para 2026.10.13 na biblioteca de empréstimos, escrito para este capítulo:

```
Instalado: focus-kit 2026.10.13, em cada SKILL.md.
Migrações de processo pendentes: 2.

1. docs/05, §5 This project: acrescentar o slot Manuals.
   "Manuals: docs/manuals/, um arquivo por coisa que uma pessoa faz
   à mão fora de uma entrega, com o nome do que ele faz."
2. AGENTS.md, Read before acting: acrescentar a linha
   "o que uma pessoa faz à mão (publicar, desfazer): docs/manuals/".

docs/ e AGENTS.md não foram alterados.
```

O relatório mantém dois fatos separados.
O `metadata.version` em cada `SKILL.md` diz qual kit está instalado.
O processo é o que o docs/04, o docs/05 e o `AGENTS.md` dizem, porque é isso que todo comando lê, então um kit atualizado cujas migrações não foram aplicadas ainda roda o processo antigo.
A atualização termina quando as migrações são aplicadas, e o método as aplica como aplica qualquer mudança: uma linha da fila, definida com o `/propose` e construída com o `/apply`, para que a mudança nas suas regras tenha uma página, verificação e a sua revisão.

Num projeto já documentado, a atualização relata as migrações primeiro, ou diz que não há nenhuma.
Ela nunca pede que você rode o `/brainstorm` ou o `/analyze` de novo: eles escrevem os documentos de um projeto do zero, e os seus existem.
Uma versão que não muda nenhuma regra dos seus documentos não relata migração: a 2026.10.08.2 só fez o `/apply` mostrar a sua mensagem de commit também na conversa, então os comandos mudaram e nada mais.

Para saber por que uma migração existe, leia o changelog do kit, `CHANGELOG.md` no repositório dele, `CHANGELOG.pt.md` em português.
Ele tem uma entrada por versão, a mais nova primeiro; a versão é a linha `Version:` do `SETUP.md`, o mesmo valor do `metadata.version` em cada `SKILL.md`.
Cada entrada diz o que mudou e o problema que causou a mudança, e um item que começa com `Migration:` (no changelog em português, `Migração:`) diz o que mudar nos documentos do projeto.
A entrada da 2026.10.13 cita, no seu item de migração, o slot Manuals e a linha do `AGENTS.md` do relatório acima.

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
Não há número para esse ganho: é uma propriedade de arquivos simples.

Uma atualização nunca reescreve as regras que o time escreveu.
No changelog do kit, da 2026.10.07, a versão que trouxe o relatório de migrações, até a 2026.10.13, cinco das seis versões mudam uma regra do docs/04, do docs/05 ou do `AGENTS.md`, e a 2026.10.08.2 é a que não muda.
Cada uma dessas cinco chegou a um projeto como uma lista do que mudar e onde, com as regras do próprio time ainda no lugar.

E o próximo comando chega na forma que o seu host reconhece.
A entrada 2026.10.08.1 do changelog registra por quê: um usuário do Codex recebeu a instrução de rodar `/propose`, que o Codex não reconhece, já que o Codex invoca skills com `$`.

## Pontos-chave

* Uma frase para o seu agente instala o focus-kit, e a mesma frase o atualiza; nada é instalado na sua máquina, nada é colocado em stage nem vai para um commit, e um arquivo do kit que você mudou faz a atualização parar antes de escrever.
* O arquivo de setup escreve só os arquivos do kit e nunca toca `docs/`, `work/`, `AGENTS.md` ou `CLAUDE.md`; uma mudança de regra para o docs/04, o docs/05 ou o `AGENTS.md` vem como uma migração no relatório dele, e até o time aplicá-la como uma entrega o processo é o antigo.
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
