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
Por padrão você lê o que ela escreveu e então faz o commit, você mesmo ou pedindo ao agente, como em toda mudança que o agente faz (capítulo 13).

O agente termina uma primeira instalação dizendo o que vem depois: num repositório sem código, abra uma sessão nova e digite `/brainstorm`; num repositório com código, abra uma sessão nova e digite `/analyze` (capítulo 9).
Ele escreve o comando como o seu host o invoca, sem slug, já que esses dois não levam nenhum: no Codex, `$brainstorm` ou `$analyze`, e o Copilot não pede slug.

## O que a instalação nunca toca, e como atualizar

O arquivo de setup escreve os arquivos do kit e mais nada.
`docs/`, `work/`, `AGENTS.md` e `CLAUDE.md` pertencem ao projeto: os comandos os escrevem, a começar pelo `/brainstorm` ou pelo `/analyze` (capítulo 9), e o arquivo de setup nunca os toca.
Um `GEMINI.md` que já guarda o texto do próprio projeto o mantém; o kit só acrescenta uma linha no topo.

Para atualizar o kit, diga a mesma frase de novo.
O agente escreve os arquivos do kit como o arquivo de setup os guarda agora, e a mudança que você revisa é só do kit, sem nada do seu projeto.
Ele substitui um arquivo só quando esse arquivo é igual a um que o kit entregou, nesta versão ou numa anterior, e a anterior se confirma pelo histórico do kit, `git show <commit>:SETUP.md` no repositório dele, ou, sem esse histórico à mão, pela sua palavra de que o arquivo nunca foi editado; um nome conhecido ou uma linha `metadata.version` sozinhos não provam isso.
Um comando seu na pasta de um host, ou uma edição que você fez à mão num dos arquivos do kit, uma linha que você acrescentou ao `.claude/skills/propose/SKILL.md`, por exemplo, faz a atualização parar antes de escrever ou remover qualquer arquivo.
O agente mostra a sua edição como um diff contra o arquivo do kit em que ela foi feita, e a mudança do próprio kit nesse arquivo desde então à parte e resumida; ele ainda relata as migrações e o próximo comando, e você decide se fica com a sua edição ou a substitui, sabendo que uma regra que a sua edição acrescentou a um comando pode virar um slot do docs/05 §5, que os comandos seguem (capítulo 7).
Essa verificação foi testada numa cópia dos arquivos do kit do livro, feita fora do repositório do livro: uma linha acrescentada ao `propose/SKILL.md` parou assim a atualização para o focus-kit 2026.10.20.1, e todos os arquivos da cópia ficaram iguais depois.

## O que uma atualização relata

O docs/04, o docs/05, o docs/06 e o `AGENTS.md` pertencem ao projeto: o time escreveu ali as suas regras, as suas escolhas junto, como o comando de verificação ou trabalhar em trunk, e a sua fila.
Quando uma versão nova do kit muda o que esses arquivos deveriam guardar, o arquivo de setup não o escreve.
Ele compara os arquivos com os seus próprios modelos e relata cada migração, uma mudança de que os seus documentos ainda precisam: o caminho, a seção ou a linha, e o texto que ele propõe, na língua da documentação do projeto.
Uma migração pode citar uma regra, uma linha da fila ou um slot.
As suas escolhas ficam: um docs/05 cujo §5 diz "trunk, uma sessão por vez" vê proposto o texto para duas sessões numa pasta, e mantém o seu até o time aceitar a mudança.

Esta é uma parte do relatório que a atualização para o focus-kit 2026.10.20.1 deu no próprio repositório deste livro, encurtada e parafraseada, e traduzida aqui: os documentos do livro são em inglês, e o relatório propôs o texto em inglês. O registro dessa atualização é o `work/done/kit-2026-10-20-1.md`, no repositório do livro.

```
Instalado: focus-kit 2026.10.20.1, em cada SKILL.md.
Migrações de processo pendentes, por documento e seção, encurtadas:

* docs/05, números de seção: batem com o modelo (§4 a fila,
  §5 os slots, §6 commit, §8 fechar um marco). Nenhuma.
* docs/05 §4, ordem como prioridade, after e o token (PA) nas
  linhas da fila: falta o token. Proposto: o primeiro parágrafo
  inteiro do modelo, que agora diz: "Uma linha pode levar (PA) depois
  do slug: se o /propose e o /apply dela podem rodar enquanto as
  linhas acima dela estão em andamento. P: a definição não tira
  nada das páginas delas; A: a construção não toca nenhum arquivo
  delas; - espera até que toda linha acima esteja [>] ou além antes
  do /propose, [x] antes do /apply; o after vale para os dois
  comandos, com ou sem token. Quem muda a fila rejulga os tokens
  que a mudança afeta; o /propose corrige um token pela página." E
  o último parágrafo removido: a primeira frase está no §8, a
  segunda no novo primeiro parágrafo.
* docs/05 §5, Git: uma escolha do projeto, não uma migração: trunk,
  com a Publish policy, o agente nunca envia. Nenhuma.

Os outros itens cobrem o docs/05 §§2 e 3, os outros slots do §5,
os §§6 a 8, o docs/04, o docs/06 e o AGENTS.md.
Próximo: /propose ch08-update-2026-10-20-1, quando
kit-2026-10-20-1 estiver [x].
```

Cada item cita um documento e uma seção, e termina num de três resultados.
Ele bate e não precisa de nada, e diz isso: `Nenhuma`.
Ele não tem alguma coisa, e o item dá o texto que o modelo propõe e onde ele entra, como no docs/05 §4.
Ou ele difere por uma escolha que o projeto fez e registrou com uma data ou um ADR, como o slot Git do livro: o item cita essa escolha e não pede mudança.
Todo item é relatado, nunca feito: a atualização não escreve nenhum desses documentos.

Os números de seção vêm primeiro porque os comandos citam o docs/05 pelos números do modelo, o §4 para a fila, o §6 para o commit, e leem pelo número; um docs/05 numerado de outro jeito mandaria cada comando para a seção errada, então essa migração vem antes de qualquer outra, diga o que disser um ADR.
Aplicar as migrações mantém as escolhas do time: a verificação continua `make verify` com as suas verificações, o revisor continua o que o slot cita, o Git continua trunk, e o Milestone review continua com os leitores do kit.

O relatório dá a cada item um desses três resultados; ele compara os documentos com os modelos atuais, nunca uma versão do kit com outra.

A versão do kit é o `metadata.version` em cada `SKILL.md`; o processo é o que o docs/04, o docs/05 e o `AGENTS.md` dizem, porque todo comando os lê, então um kit atualizado cujas migrações não foram aplicadas ainda roda o processo antigo.
A atualização termina quando as migrações são aplicadas, como qualquer mudança: uma linha da fila, definida com o `/propose` e construída com o `/apply`, para que a mudança nas suas regras ou na sua fila tenha uma página, verificação e a sua revisão.

Num projeto já documentado, a atualização relata as migrações primeiro, ou diz que não há nenhuma.
Ela nunca pede que você rode o `/brainstorm` ou o `/analyze` de novo: eles escrevem os documentos de um projeto do zero, e os seus existem.
Ela cita em vez disso o comando que a primeira linha livre do docs/06 pede, na forma do seu host: o `/propose` e o seu slug para uma linha `[ ]`, o `/apply` e o seu slug para uma `[>]`.
No trunk essa linha é lida na fila da pasta; com um branch ou um worktree por entrega, o branch principal mostra cada linha como estava até o merge dela, então a atualização roda `git fetch` antes, toma como ocupada, antes mesmo de qualquer marca dela ser enviada, uma linha cujo branch existe, mostre o que mostrar o branch principal, e lê a linha de cada slug no branch dele, local ou remoto, e as linhas que só um branch tem, reconciliando-as pelo slug ([capítulo 14](14-queue-states.md)).
Uma versão que não pede nada aos seus documentos não relata migração: uma versão que muda só os comandos, como o `/apply` mostrar a sua mensagem de commit também na conversa, não muda mais nada.
Um docs/05 cujo slot Git escolheu um worktree por entrega e não cita pasta recebe uma migração só quando o projeto já trabalha num contêiner, a pasta que o [capítulo 19](19-worktrees.md) organiza com o checkout e uma pasta oculta para o histórico e os worktrees, e essa pasta oculta guarda `repo.git/`.
O relatório então propõe escrever ali o nome dessa pasta e o prefixo que os branches das entregas já usam, para que nada mude de lugar.
Sem contêiner ainda, o slot vale o padrão do kit, que esse capítulo cita, e o relatório não propõe nada.

Para saber por que uma migração existe, leia o changelog do kit, `CHANGELOG.md` no repositório dele, `CHANGELOG.pt.md` em português.
Ele tem uma entrada por versão, a mais nova primeiro; a versão é a linha `Version:` do `SETUP.md`, o mesmo valor do `metadata.version` em cada `SKILL.md`.
Cada entrada diz o que mudou e o problema que causou a mudança, e uma entrada pode trazer um item que começa com `Migration:` (no changelog em português, `Migração:`), citando o que mudar nos documentos do projeto.
O que uma nova execução compara é o próprio passo 4 do arquivo de setup, uma lista por documento e seção, que cita as seções do docs/05, os slots e as linhas do `AGENTS.md` que confere; cada item é relatado, nunca feito, com um dos três resultados.

## Como cada host encontra os comandos

Um host precisa de duas coisas do repositório: o arquivo de regras, `AGENTS.md`, e os comandos, o `/propose` e o `/apply` cada um com o slug que você digita depois dele, o nome da entrega em `work/<slug>.md` (capítulo 12).
O `/brainstorm` e o `/analyze` começam um projeto, não uma entrega, então não levam slug; para definir ou construir `emprestar-livro`, você digita `/propose emprestar-livro` ou `/apply emprestar-livro`, ou, onde o host pede o slug, responde `emprestar-livro`.
O arquivo de setup escreve o que cada host abaixo precisa:

| Host | Lê as regras de | Lê os comandos de | Você digita |
|---|---|---|---|
| Claude Code | `CLAUDE.md`, que importa o `AGENTS.md`; o `AGENTS.md` sozinho só onde não existe `CLAUDE.md`, a partir da versão 2.1.277 | `.claude/skills/` | `/propose <slug>` |
| Codex | `AGENTS.md` | `.agents/skills/` | `$propose <slug>` |
| GitHub Copilot | `AGENTS.md` | `.agents/skills/`, por um arquivo de prompt em `.github/prompts/` | `/propose`, e ele pede o slug |
| Cursor | `AGENTS.md` | `.agents/skills/`, por um arquivo de comando em `.cursor/commands/` | `/propose` |
| Gemini CLI | `AGENTS.md`, pelo `GEMINI.md` | `.agents/skills/`, por um arquivo de comando em `.gemini/commands/` | `/propose <slug>` |
| Google Antigravity | `AGENTS.md` direto; `.agents/rules/focus-kit.md` é um ponteiro sempre ativo | `.agents/skills/` | `/propose <slug>` |
| Devin Desktop, antes Windsurf | `AGENTS.md` | `.agents/skills/` | `/propose` |
| OpenCode, Zed | `AGENTS.md` | `.agents/skills/` | pedindo a skill |
| Jules, Junie, Warp, Kiro, Roo Code, Cline | `AGENTS.md` | nenhuma | pedindo em palavras o `.agents/skills/propose/SKILL.md` |

Cada comando é uma skill, uma pasta com um arquivo `SKILL.md` de instruções que o host carrega quando você a chama.[^claude-code-skills][^codex-skills][^copilot-skills]
O Claude Code lê o `CLAUDE.md` no início de uma sessão, e uma linha `@AGENTS.md` nele importa o arquivo de regras; a partir da versão 2.1.277 ele lê o `AGENTS.md` sozinho, mas só num repositório sem `CLAUDE.md`, então o kit escreve o `CLAUDE.md` com a importação, que toda versão lê.[^claude-code-memory]
O Codex, o Copilot e o Devin Desktop, antes Windsurf, leem o `AGENTS.md` sozinhos.[^codex-agents-md][^copilot-instructions][^devin-rules]
O Antigravity também lê o `AGENTS.md` direto; a regra que o kit escreve em `.agents/rules/focus-kit.md` é um ponteiro sempre ativo, sem regra própria, um caminho a mais até o `AGENTS.md`, não o único.
O comando de barra do Copilot vem de um arquivo de prompt que só diz ao agente para ler a skill e segui-la, e pede o slug quando você digita o comando.[^copilot-prompt-files]
O Codex pode rodar uma skill por conta própria quando uma mensagem bate com a descrição dela; um pequeno arquivo ao lado de cada skill desliga isso, para que uma mensagem que por acaso diga "apply" não construa nada que você não pediu.[^codex-skills]
As skills do Claude Code levam `disable-model-invocation: true`, que impede o Claude de rodar uma por conta própria: uma mensagem que bate com a descrição de uma skill não basta, e o comando só roda quando você o nomeia.[^claude-code-skills]
Nos outros hosts, invoque os comandos você mesmo; o kit não afirma que cada host garanta o mesmo.
Para o Cursor e o Devin Desktop, nenhum dos dois fornecedores diz na documentação se um slug digitado depois de um comando chega até ele, então nomeie a entrega na sua mensagem se não chegar.
O Copilot lê as duas pastas de skills, e a sua referência da CLI diz o que acontece com uma skill de mesmo nome nas duas: `.agents/skills/` vem antes de `.claude/skills/` e a primeira encontrada vence; o kit escreve o mesmo arquivo nas duas, então qualquer das cópias é o mesmo comando.[^copilot-cli-reference]
O Devin Desktop também lê `.windsurf/skills/`, a pasta do seu nome anterior;[^devin-skills] o arquivo de setup não escreve nada ali e, numa atualização, remove dela os arquivos do próprio kit, para que o host nunca encontre uma cópia mais velha de um comando ao lado da atual em `.agents/skills/`, e um arquivo seu ali é relatado e mantido.

Todo comando termina dizendo o próximo, escrito como o host que o roda o invoca, a última coluna da tabela.
O arquivo de setup cita o `/brainstorm` ou o `/analyze`, para rodar numa sessão nova, o `/propose` cita o `/apply` com o slug da página, e o `/apply` cita a próxima linha da fila.
Na biblioteca de empréstimos, depois de `/propose emprestar-livro`, o Claude Code diz para você rodar `/apply emprestar-livro` numa sessão nova, e o Codex diz para rodar `$apply emprestar-livro`, também numa sessão nova.
O `/propose` pode rodar na conversa que pediu a mudança; o `/apply` sempre começa numa sessão nova, em todo host (capítulo 11).
Os arquivos do kit são os mesmos nos dois; a forma segue o host que os roda.

O arquivo de setup do kit mantém esta tabela atualizada, com a página do fornecedor de onde cada linha foi lida, e só acrescenta um host com a documentação dele em mãos.
A última linha vem da §1 do arquivo de setup: Jules, Junie, Warp, Kiro, Roo Code e Cline leem o `AGENTS.md`, e o kit não conta com nenhuma pasta de skills nem comando de barra deles, então você pede em palavras, "leia `.agents/skills/propose/SKILL.md` e siga-o para `emprestar-livro`", e o host lê o arquivo para o qual você aponta.

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
Uma edição que o time fez num arquivo do kit aparece à parte da mudança do próprio kit, então o time sabe qual é qual, e uma escolha que ele registrou é relatada como dele.

E o próximo comando chega na forma que o seu host reconhece, porque um host pode não reconhecer a forma de outro: o Codex não reconhece `/propose`, já que o Codex invoca skills com `$`.

## Pontos-chave

* Uma frase para o seu agente instala o focus-kit, e a mesma frase o atualiza; nada é instalado na sua máquina, nada é colocado em stage nem vai para um commit, e um arquivo do kit que você mudou faz a atualização parar antes de escrever, com a sua edição mostrada como um diff contra o arquivo do kit em que ela foi feita.
* O arquivo de setup escreve só os arquivos do kit e nunca toca `docs/`, `work/`, `AGENTS.md` ou `CLAUDE.md`; uma mudança de que o docs/04, o docs/05, o docs/06 ou o `AGENTS.md` precisa, uma regra, uma linha da fila ou um slot, vem como uma migração no relatório dele, uma lista por documento e seção em que uma escolha que o projeto registrou é relatada como essa escolha, e até o time aplicá-la como uma entrega o processo é o antigo.
* O changelog do kit, a entrada mais nova primeiro, diz para cada versão o que mudou, o problema que causou a mudança e, num item que começa com `Migração:`, quando a entrada tem um, o que mudar nos documentos do projeto.
* Cada host encontra as regras e os comandos nas suas próprias pastas: o Claude Code roda um comando como `/propose <slug>`, o Codex como `$propose <slug>`, o Copilot como `/propose`, que pede o slug, o Devin Desktop como `/propose`, e Jules, Junie, Warp, Kiro, Roo Code e Cline pedindo em palavras o arquivo da skill; o `/brainstorm` e o `/analyze` não levam slug; todo comando cita o próximo nessa forma; o Copilot pega uma skill de `.agents/skills/` antes de `.claude/skills/`, o mesmo arquivo nas duas.
* Todo host lê um arquivo de regras no início, lê os arquivos para os quais você aponta e escreve arquivos, e o método não precisa de mais nada.

[^claude-code-memory]: Anthropic, "How Claude remembers your project", documentação do Claude Code, acesso em 2026-10-18. <https://code.claude.com/docs/en/memory>
[^claude-code-skills]: Anthropic, "Extend Claude with skills", documentação do Claude Code, acesso em 2026-10-18. <https://code.claude.com/docs/en/skills>
[^codex-agents-md]: OpenAI, "Custom instructions with AGENTS.md", documentação do Codex, acesso em 2026-09-30. <https://developers.openai.com/codex/guides/agents-md>
[^codex-skills]: OpenAI, "Build skills", documentação do Codex, acesso em 2026-09-30. <https://developers.openai.com/codex/skills>
[^copilot-instructions]: GitHub, "Adding repository custom instructions for GitHub Copilot", GitHub Docs, acesso em 2026-09-30. <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
[^copilot-skills]: GitHub, "About agent skills", GitHub Docs, acesso em 2026-09-30. <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
[^copilot-cli-reference]: GitHub, "GitHub Copilot CLI command reference", GitHub Docs, acesso em 2026-10-19. <https://docs.github.com/en/copilot/reference/cli-command-reference>
[^copilot-prompt-files]: GitHub, "Your first prompt file", GitHub Docs, acesso em 2026-09-30. <https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file>
[^devin-skills]: Cognition, "Skills Overview", Devin Docs, acesso em 2026-10-17. <https://docs.devin.ai/cli/extensibility/skills/overview>
[^devin-rules]: Cognition, "Rules & AGENTS.md", Devin Docs, acesso em 2026-10-17. <https://docs.devin.ai/cli/extensibility/rules>
