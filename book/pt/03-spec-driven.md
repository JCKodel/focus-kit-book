# Desenvolvimento Guiado por Especificação

O Spec Kit e o OpenSpec fazem um agente de código escrever a decisão antes do código, e em uma funcionalidade pequena eles escrevem muito mais do que ela precisa.
Depois deste capítulo você consegue dizer o que é Desenvolvimento Guiado por Especificação e até onde uma ferramenta leva a especificação, apontar o que essas duas ferramentas acertaram e mostrar, com os números de uma execução registrada, onde elas pesam mais do que a funcionalidade precisa.

## O que é uma especificação

Birgitta Böckeler comparou três ferramentas que se dizem guiadas por especificação e escreveu o que o termo quer dizer.[^bockeler-2025]
Uma especificação, na definição dela, é "*um artefato estruturado e orientado a comportamento [...] escrito em linguagem natural, que expressa a funcionalidade do software e serve de guia para agentes de código de IA*".[^bockeler-2025]
Desenvolvimento Guiado por Especificação (SDD) "*quer dizer escrever uma “especificação” antes de escrever código com IA (“documentação primeiro”). A especificação passa a ser a fonte da verdade para o humano e para a IA*".[^bockeler-2025]

Ela encontrou três níveis, conforme quanto tempo a especificação vive e quem a edita:

* **spec-first** (especificação primeiro): uma especificação é escrita antes e guia a tarefa do momento;
* **spec-anchored** (ancorado na especificação): a especificação é mantida depois da tarefa e usada para evoluir e manter a funcionalidade;
* **spec-as-source** (especificação como fonte): a especificação é a fonte principal ao longo do tempo, e uma pessoa edita só a especificação, nunca o código.

"*Todas as abordagens e definições de SDD que encontrei são spec-first, mas nem todas buscam ser spec-anchored ou spec-as-source*".[^bockeler-2025]
Das três ferramentas dela, o Kiro é "*a mais simples (ou a mais leve)*" e "*principalmente spec-first*".[^bockeler-2025]
O Tessl é "*a única destas três ferramentas que aspira explicitamente a uma abordagem spec-anchored, e está até explorando o nível spec-as-source de SDD*".[^bockeler-2025]
Ela acrescenta que "*essas ferramentas evoluem muito rápido, então talvez já tenham mudado desde que as usei*".[^bockeler-2025]

Este capítulo olha duas outras ferramentas, nas versões que uma execução registrada fixou.
O Spec Kit, do GitHub, é um conjunto de processos para agentes de código, e o seu processo de Desenvolvimento Guiado por Especificação diz: "*Constituição uma vez por projeto; specify → plan → tasks → implement → converge por funcionalidade*".[^spec-kit]
O OpenSpec, da Fission AI, "*acrescenta uma camada leve de especificação para que vocês concordem sobre o que construir antes de qualquer código ser escrito*"; o seu `/opsx:propose` escreve uma pasta por mudança, com uma proposta, especificações, um design e tarefas.[^openspec]
Na execução, as duas foram usadas como spec-first: cada uma escreveu a especificação antes da tarefa, e o que acontece com ela depois a execução não testou.

## Uma funcionalidade, três ferramentas

A execução deu a três ferramentas o mesmo briefing sobre o mesmo projeto TypeScript de quatro arquivos: um cliente pode cancelar o próprio agendamento até 24 horas antes do início, um agendamento cancelado libera o seu horário, e um cancelamento mais tarde que isso é recusado com uma mensagem que diz por quê.[^spec-driven-run]
Cada ferramenta seguiu o seu caminho padrão, cada etapa em uma sessão nova, e parou antes de escrever código.
As três rodaram em 2026-09-25, com o modelo `claude-opus-5-5`.
A terceira ferramenta é o focus-kit, o método que este livro ensina a partir do capítulo 4; aqui ele é uma linha da tabela.

| Ferramenta | Linha | Arquivos | Linhas | Palavras |
|---|---|---:|---:|---:|
| Spec Kit | instalado | 29 | 5.074 | 30.174 |
| Spec Kit | uma vez por projeto | 1 | 71 | 429 |
| Spec Kit | por funcionalidade | 8 | 756 | 6.498 |
| OpenSpec | instalado | 12 | 2.590 | 27.015 |
| OpenSpec | uma vez por projeto | 3 | 32 | 140 |
| OpenSpec | por funcionalidade | 6 | 180 | 2.201 |
| focus-kit | instalado | 36 | 2.049 | 14.700 |
| focus-kit | uma vez por projeto | 17 | 277 | 2.577 |
| focus-kit | por funcionalidade | 1 | 82 | 602 |

"Instalado" é o que a ferramenta põe no seu projeto antes de você escrever qualquer coisa: comandos, skills, modelos, scripts.
"Uma vez por projeto" é o que você escreve uma vez e toda funcionalidade reaproveita.
"Por funcionalidade" é o que uma funcionalidade custa, e se repete a cada funcionalidade.
As contagens vêm de `find`, `wc -l` e `wc -w` sobre os arquivos que cada etapa deixou.[^spec-driven-run]

Esta é uma execução: um modelo, um dia, uma funcionalidade.
O agente não é determinístico, então uma segunda execução dá o mesmo tipo de saída, não os mesmos números.
Todo arquivo das linhas "uma vez por projeto" e "por funcionalidade" está guardado na pasta da execução, e o README dela diz como repetir a execução.[^spec-driven-run]

## O que elas acertaram

**A decisão é escrita antes do código, em arquivos que o agente lê.**
O capítulo 2 mostrou por que uma decisão que só existe na conversa se perde.
As três ferramentas pararam antes do código com a funcionalidade decidida em arquivos dentro do projeto, onde uma sessão nova os encontra.

**Algumas decisões são escritas uma vez por projeto.**
A constituição do Spec Kit guarda as regras que toda funcionalidade segue.
Na execução, ela transformou os princípios do briefing (manter simples, TypeScript estrito, um teste para cada regra) em um arquivo, e o plano da funcionalidade tem uma seção que se confere contra ele.
Uma regra que vale para o projeto inteiro é decidida uma vez e não é discutida de novo a cada funcionalidade.

**A ferramenta pergunta antes de escrever.**
O OpenSpec leu o código antes de criar a mudança e parou com uma pergunta: "*"Um agendamento cancelado libera o seu horário" não muda nada hoje, porque horários nunca ficam reservados*".[^spec-driven-run]
O briefing supunha horários, e o código não tinha nenhum.
Ele ofereceu duas opções, recomendou uma e só escreveu a mudança depois da resposta.

O Spec Kit não perguntou nada.
Ele encontrou a mesma lacuna e escreveu a resposta em "Assumptions" (suposições), na especificação: um horário é identificado pela hora de início, e a funcionalidade acrescenta essa verificação ao agendamento.[^spec-driven-run]
O README dele oferece o esclarecimento como uma etapa extra "*quando você precisa de controles de qualidade adicionais*"; a execução seguiu o caminho padrão e não a rodou.[^spec-kit]
A decisão foi a mesma sobre a qual o OpenSpec perguntou, e você só a encontra lendo a especificação.

## Onde elas pesaram demais

Por funcionalidade, o Spec Kit escreveu 8 arquivos e 756 linhas, o OpenSpec 6 arquivos e 180 linhas, e o focus-kit 1 página de 82 linhas.[^spec-driven-run]
Cada um desses arquivos é algo que uma pessoa precisa revisar antes de o código ser escrito.

O briefing tem uma regra de tempo: até 24 horas antes.
O Spec Kit a repete em 8 dos seus 8 arquivos, o OpenSpec em 4 dos seus 6, o focus-kit no seu 1.[^rule-count]
O mesmo caso, um cancelamento exatamente 24 horas antes, fica assim em cada ferramenta.
Os trechos estão em inglês, como as ferramentas os escreveram.

Spec Kit, em `spec.md`:

```markdown
2. **Given** a client has a booked appointment starting exactly 24 hours from now, **When** that
   client cancels it, **Then** the cancellation is accepted (exactly 24 hours counts as "up to
   24 hours before").
```

Um cenário de aceitação na forma Dado, Quando, Então, com uma nota sobre como ler "até".

OpenSpec, no `spec.md` da mudança:

```markdown
#### Scenario: Cancelling exactly 24 hours ahead
- **WHEN** client "Ana" cancels their booked appointment exactly 24 hours before it starts
- **THEN** the cancellation succeeds and the appointment's status is `cancelled`
```

Um cenário com nome, debaixo de um requisito, em linhas QUANDO e ENTÃO.

focus-kit, em `work/cancel.md`:

```markdown
- The same thing at exactly 11 March 10:00 (24 hours before) succeeds too.
```

Uma linha dos cenários da página, que reaproveita o exemplo da linha de cima.

Os três dizem a mesma coisa.
A diferença é quantos outros arquivos dizem isso de novo: uma regra escrita em 8 lugares é lida 8 vezes na revisão e, quando muda, muda em 8 lugares.
Böckeler encontrou o mesmo no Spec Kit: os arquivos dele "*eram repetitivos, tanto entre si quanto em relação ao código que já existia*" e "*muito prolixos e cansativos de revisar*".[^bockeler-2025]

A linha leve não sai de graça.
O focus-kit é o que mais escreve uma vez por projeto, 17 arquivos e 277 linhas, e o seu `/propose` ainda editou dois deles, acrescentando 6 linhas e removendo 3 em `docs/03` e `docs/06`.[^spec-driven-run]
A troca é decidir uma vez por projeto, em documentos que você mantém atualizados, e depois escrever uma página por funcionalidade.
A execução diz o que cada ferramenta escreve antes do código; não diz qual delas constrói software melhor.

## Pontos-chave

* Uma especificação é uma descrição escrita, orientada a comportamento, do que o software precisa fazer, em linguagem natural, que guia um agente de código; o Desenvolvimento Guiado por Especificação a escreve antes do código.
* Conforme quanto tempo a especificação vive, uma ferramenta é spec-first (escrita para a tarefa), spec-anchored (mantida para cuidar da funcionalidade) ou spec-as-source (a única coisa que uma pessoa edita).
* O Spec Kit e o OpenSpec acertaram em três coisas: a decisão escrita antes do código em arquivos que o agente lê, regras escritas uma vez por projeto e uma pergunta feita antes de escrever.
* Em uma funcionalidade registrada, o Spec Kit escreveu 8 arquivos e 756 linhas e o OpenSpec 6 e 180, repetindo uma regra na maioria deles, e cada arquivo é algo que você revisa.
* Uma página mais leve por funcionalidade se paga com documentos escritos uma vez por projeto; a execução mostra o que cada ferramenta escreve, não qual constrói software melhor.

[^bockeler-2025]: Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", 2025. https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
[^spec-kit]: GitHub, "Spec Kit", v1.0.11. https://github.com/github/spec-kit/tree/v1.0.11
[^openspec]: Fission AI, "OpenSpec", 1.13.2. https://github.com/Fission-AI/OpenSpec/tree/v1.13.2
[^spec-driven-run]: A execução deste livro do Spec Kit, do OpenSpec e do focus-kit sobre um briefing, 2026-09-25: as contagens, o ambiente e como repetir no README; as perguntas e respostas de cada ferramenta no seu `questions.md`, na mesma pasta. https://github.com/JCKodel/focus-kit-book/blob/53109f372125e8aeda200bb2e5bbd1ad7bcc5d61/work/done/spec-driven-run/README.md
[^rule-count]: Contado na pasta da execução com `grep -rliE '24 ?h|24-hour|24 hours' <tool>/feature | wc -l`, contra o número de arquivos por funcionalidade: Spec Kit 8 de 8, OpenSpec 4 de 6, focus-kit 1 de 1.
