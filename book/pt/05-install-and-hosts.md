# Instalar, e os hosts

Depois deste capítulo você consegue instalar o focus-kit em um repositório com uma frase para o seu agente de código, atualizá-lo dizendo a mesma frase de novo e chamar os quatro comandos dele no Claude Code, no Codex ou no GitHub Copilot.
Você também consegue explicar por que o método não depende do host.

## Instalar

Abra o seu agente de código na raiz do repositório e diga:

```
Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md and do what it says.
```

A frase fica em inglês, como o README do focus-kit a dá; ela diz ao agente para ler o `SETUP.md` e fazer o que ele diz.
O `SETUP.md` é o arquivo de setup do focus-kit: um arquivo de instruções que o agente lê e transforma nos arquivos do kit.[^focus-kit-setup]
Se preferir lê-lo antes, baixe o `SETUP.md` ao lado do repositório e aponte o agente para o arquivo.
Nada é instalado na sua máquina: o agente escreve arquivos no repositório, e só isso.

O seu host pede permissão antes de baixar o arquivo e antes de escrever na pasta de configuração dele, `.claude/` no Claude Code: aprove as duas.
A ferramenta de busca na web de um host pode entregar ao agente um resumo da página, e não o texto, e o arquivo de setup diz que cada arquivo deve ser copiado byte a byte, então um agente cuidadoso pede para baixar o arquivo; quando eu rodei, o Claude Code fez exatamente isso.[^claude-code-run]

A execução que este capítulo mostra foi no projeto guiado, o app de agendamento de uma pequena clínica que você constrói no resto do livro, no repositório público `JCKodel/focus-kit-clinic`.
Cada capítulo que o altera termina com uma tag do capítulo, `book-v1/<slug-do-capítulo>`, no commit que ele cita, para você abrir o projeto como estava em qualquer capítulo.
A execução partiu da tag `book-v1/start`, em que o repositório tem três arquivos: `README.md`, `LICENSE` e `LICENSE-TEXT`.
O Claude Code leu o arquivo de setup, escreveu os arquivos e relatou o que segue, em inglês, como o escreveu, e logo abaixo traduzido:[^claude-code-run]

```markdown
I've installed the focus-kit. I wrote all 36 files that SETUP.md lists, copying each one straight out of SETUP.md with a script. Where a file has a `<name>` placeholder, it was replaced with the command's name. I didn't touch any existing files and didn't stage or commit anything.

**Files written:**
- **Skills (18 files):** in each of `.claude/skills/`, `.agents/skills/` and `.windsurf/skills/`, there's a `SKILL.md` for `brainstorm`, `analyze`, `propose` and `apply`, plus `references/documents.md` under `brainstorm` and `analyze`.
- **Codex:** `.agents/skills/{brainstorm,analyze,propose,apply}/agents/openai.yaml`
- **Copilot:** `.github/prompts/{brainstorm,analyze,propose,apply}.prompt.md`
- **Cursor:** `.cursor/commands/{brainstorm,analyze,propose,apply}.md`
- **Gemini CLI:** `.gemini/commands/{brainstorm,analyze,propose,apply}.toml`, plus `GEMINI.md` (none existed before, so I created it)
- **Antigravity:** `.agents/rules/focus-kit.md`

I ran the checks from section 4 of SETUP.md, and they all pass. The file count is right, the only changes are the new files, and every `propose` and `apply` skill still contains `$ARGUMENTS`. There are no em dashes and no leftover `<name>` placeholders.

**Next step:** this repository has no code yet (just the README and licenses), so start a fresh session and run `/brainstorm`.
```

Tradução:

```markdown
Instalei o focus-kit. Escrevi todos os 36 arquivos que o SETUP.md lista, copiando cada um direto do SETUP.md com um script. Onde um arquivo tem o marcador `<name>`, ele foi substituído pelo nome do comando. Não mexi em nenhum arquivo existente e não preparei nem fiz commit de nada.

**Arquivos escritos:**
- **Skills (18 arquivos):** em cada uma de `.claude/skills/`, `.agents/skills/` e `.windsurf/skills/`, há um `SKILL.md` para `brainstorm`, `analyze`, `propose` e `apply`, mais `references/documents.md` em `brainstorm` e `analyze`.
- **Codex:** `.agents/skills/{brainstorm,analyze,propose,apply}/agents/openai.yaml`
- **Copilot:** `.github/prompts/{brainstorm,analyze,propose,apply}.prompt.md`
- **Cursor:** `.cursor/commands/{brainstorm,analyze,propose,apply}.md`
- **Gemini CLI:** `.gemini/commands/{brainstorm,analyze,propose,apply}.toml`, mais `GEMINI.md` (não existia nenhum antes, então eu o criei)
- **Antigravity:** `.agents/rules/focus-kit.md`

Rodei as verificações da seção 4 do SETUP.md, e todas passam. A contagem de arquivos está certa, as únicas mudanças são os arquivos novos, e toda skill `propose` e `apply` ainda contém `$ARGUMENTS`. Não há travessões e não sobrou nenhum marcador `<name>`.

**Próximo passo:** este repositório ainda não tem código (só o README e as licenças), então comece uma sessão nova e rode `/brainstorm`.
```

O relatório nomeia cada arquivo que escreveu, confirma as verificações do próprio arquivo de setup e termina com o próximo comando: `/brainstorm`, porque o repositório ainda não tem código (um repositório com código recebe `/analyze`).

Depois, `git status --short` mostrou o que apareceu:[^claude-code-run]

```
?? .agents/
?? .claude/
?? .cursor/
?? .gemini/
?? .github/
?? .windsurf/
?? GEMINI.md
```

Essas linhas guardam 36 arquivos (`git status --short --untracked-files=all` os lista um a um): os quatro comandos uma vez em cada pasta de skills, `.claude/skills/`, `.agents/skills/` e `.windsurf/skills/`, e pequenos arquivos que apontam para eles, para os hosts que precisam.[^focus-kit-setup]
Cada arquivo saiu do arquivo de setup byte a byte.[^claude-code-run]
A instalação não prepara nem faz commit; você revisa os arquivos e faz o commit.

## O que a instalação nunca toca, e como atualizar

Rodar o arquivo de setup de novo substitui os arquivos do kit e nada mais.[^focus-kit-setup]
`docs/`, `work/`, `AGENTS.md` e `CLAUDE.md` são do projeto: os comandos os escrevem, e o arquivo de setup nunca os toca.
Na clínica, nenhum deles existe ainda; o capítulo 7 os escreve.

Para atualizar o kit, diga a mesma frase de novo.
O agente escreve os arquivos do kit como o arquivo de setup os guarda agora, e o `git diff` mostra o que mudou no kit e nada do seu projeto.

## Como um host encontra os comandos

O capítulo 2 mostrou o arquivo de regras, `AGENTS.md`, que o host carrega quando uma sessão começa.
Um host também precisa encontrar os comandos e passar a cada um o slug que você digita depois dele: o nome da entrega, o `<slug>` de `work/<slug>.md`.
Cada host abaixo faz isso a partir de arquivos no repositório.

**Claude Code** lê o `AGENTS.md` sozinho; onde não consegue, um `CLAUDE.md` com a linha `@AGENTS.md` o importa, e o capítulo 7 escreve esse arquivo.[^claude-code-memory]
Ele lê um comando de `.claude/skills/<name>/SKILL.md`.
Você digita `/propose <slug>`, e o slug chega ao comando como `$ARGUMENTS`.[^claude-code-skills]

**Codex** lê o `AGENTS.md` antes de fazer qualquer trabalho.[^codex-agents-md]
Ele lê um comando de `.agents/skills/<name>/SKILL.md`, e você digita `$propose <slug>`.[^codex-skills]
O Codex também pode rodar uma skill por conta própria quando a sua mensagem combina com a descrição dela; o `agents/openai.yaml` ao lado de cada skill desliga isso, para que uma mensagem que por acaso diga "apply" não construa nada que você não pediu.[^codex-skills]

**GitHub Copilot** lê o `AGENTS.md` como as instruções do agente.[^copilot-instructions]
Ele lê as skills do kit em `.agents/skills/`.[^copilot-skills]
O comando de barra vem de um arquivo de prompt, `.github/prompts/<name>.prompt.md`, que na clínica só aponta para a skill, [`.github/prompts/propose.prompt.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/install-and-hosts/.github/prompts/propose.prompt.md):

```markdown
---
agent: 'agent'
---
Read `.agents/skills/propose/SKILL.md` and follow it. `$ARGUMENTS` is `${input:slug}`.
```

A última linha diz ao agente para ler a skill e segui-la, e que `$ARGUMENTS` é o valor que você digitar.
Você digita `/propose`, e o Copilot pede o slug, que é o que `${input:slug}` representa.[^copilot-prompt-files]
Arquivos de prompt funcionam no VS Code, no Visual Studio e nas IDEs da JetBrains.[^copilot-prompt-files]

Cursor, Gemini CLI, Google Antigravity, Windsurf e outros estão na tabela da [seção 1 do `SETUP.md`](https://github.com/JCKodel/focus-kit/blob/main/SETUP.md#1-what-to-do), com a página do fornecedor de onde cada linha foi lida; o kit mantém essa tabela atualizada, e este livro não a repete.

## Por que o método não depende do host

Os hosts diferem nas pastas e no caractere que inicia um comando, e concordam em três fatos.
Cada um lê um arquivo de regras quando uma sessão começa, o `AGENTS.md` diretamente ou por um arquivo que aponta para ele; cada um carrega um comando de um arquivo no repositório; e cada um passa ao comando a palavra que você digita depois dele.
O método mora em arquivos comuns, o arquivo de regras do capítulo 2 e os documentos do projeto que uma sessão nova lê, então trocar de host não muda nada nele.
Toda instalação escreve os arquivos de todos os hosts, qualquer que seja o host que a rodou, então o repositório abre pronto em qualquer um deles.[^focus-kit-setup]

O kit também oferece a arquitetura FOCUS e uma estratégia de git, e não impõe nenhuma das duas; as Partes III e IV as ensinam.

## Pontos-chave

* Uma frase para o seu agente instala o focus-kit, e a mesma frase o atualiza; nada é instalado na sua máquina.
* A instalação escreve 36 arquivos, os quatro comandos uma vez em cada pasta de skills e arquivos que apontam para eles para outros hosts, e nunca toca `docs/`, `work/`, `AGENTS.md` ou `CLAUDE.md`.
* O Claude Code roda um comando como `/propose <slug>`, o Codex como `$propose <slug>`, e o Copilot como `/propose`, que pede o slug.
* Todo host lê um arquivo de regras no início da sessão, carrega comandos de arquivos no repositório e passa adiante a palavra digitada depois de um comando, então o método funciona igual em qualquer um deles.
* Os outros hosts estão na tabela do arquivo de setup, que o kit mantém atualizada.

## Exercícios

### Exercício 5.1

Clone o `JCKodel/focus-kit-clinic`, faça checkout de `book-v1/start` em um branch seu e instale o kit com o seu host.
Compare a sua lista de arquivos com `git diff --stat book-v1/start book-v1/install-and-hosts`.

### Exercício 5.2

Diga a frase de instalação de novo e leia o `git status`.
O que a atualização mudou, e o que ela deixou como estava?

### Exercício 5.3

Encontre a linha do seu host na seção 1 do `SETUP.md`, abra a página do fornecedor e chame `/propose` (ou o equivalente no seu host) com um slug inventado.
O projeto ainda não tem documentos para o comando ler: o que o agente diz, e por que isso faz os capítulos 6 e 7 virem a seguir?

[^focus-kit-setup]: J.C. Ködel, "focus-kit", `SETUP.md` no commit 26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b. https://github.com/JCKodel/focus-kit/blob/26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b/SETUP.md
[^claude-code-run]: A instalação do focus-kit feita por este livro no projeto guiado, 2026-09-25, com o Claude Code 2.1.282, de `book-v1/start` até a tag do capítulo `book-v1/install-and-hosts`: o comando, o relatório, a lista de arquivos e a verificação byte a byte, na pasta da execução. https://github.com/JCKodel/focus-kit-book/blob/main/work/done/install-and-hosts-run/README.md
[^claude-code-memory]: Anthropic, "How Claude remembers your project", acesso em 2026-09-25. https://code.claude.com/docs/en/memory
[^claude-code-skills]: Anthropic, "Extend Claude with skills", acesso em 2026-09-25. https://code.claude.com/docs/en/skills
[^codex-agents-md]: OpenAI, "Custom instructions with AGENTS.md", acesso em 2026-09-25. https://developers.openai.com/codex/guides/agents-md
[^codex-skills]: OpenAI, "Build skills", acesso em 2026-09-25. https://developers.openai.com/codex/skills
[^copilot-instructions]: GitHub, "Adding repository custom instructions for GitHub Copilot", acesso em 2026-09-25. https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[^copilot-skills]: GitHub, "About agent skills", acesso em 2026-09-25. https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
[^copilot-prompt-files]: GitHub, "Your first prompt file", acesso em 2026-09-25. https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file
