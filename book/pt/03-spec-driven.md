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

A execução partiu de um pequeno projeto TypeScript para uma clínica, em quatro arquivos.[^spec-driven-run]
O código tem um tipo `Appointment` (agendamento), com o nome do cliente, a hora de início e o status `booked` (agendado), uma lista de agendamentos guardada em memória e uma função `book(clientName, startsAt)` que acrescenta um agendamento à lista.
Ele não tem como cancelar, nem regra sobre quem ocupa qual horário, e ainda não tem testes.

Cada ferramenta recebeu o mesmo briefing, palavra por palavra, nas etapas em que o seu caminho pede.
O original está em inglês; aqui vai traduzido:

```markdown
## Funcionalidade

Um cliente pode cancelar o próprio agendamento até 24 horas antes do início. Um agendamento cancelado libera o seu horário. Um cancelamento mais tarde que isso é recusado com uma mensagem que diz por quê.

## Respostas

O armazenamento fica em memória. Não há tela: a funcionalidade é uma função no módulo. O cliente é identificado por `clientName`, sem login. Os horários são a hora local da clínica. Os testes usam `node --test`. Nenhuma notificação é enviada.

## Princípios

Mantenha simples. TypeScript, estrito. Toda regra tem um teste.
```

Quando uma ferramenta perguntou algo que o briefing não respondia, a execução ficou com o padrão da própria ferramenta, ou com "a opção mais simples" quando ela não oferecia nenhum.
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
Esta é a mesma parte da decisão em cada ferramenta: um cancelamento feito a tempo é aceito, e um feito exatamente 24 horas antes conta como a tempo.
Cada trecho aparece em inglês, como a ferramenta o escreveu, e logo abaixo traduzido.

Spec Kit, em `specs/001-cancel-appointment/spec.md`, a primeira das suas histórias de usuário:

```markdown
### User Story 1 - Cancel an appointment in good time (Priority: P1)

A client who has booked an appointment finds they can't make it. At least 24 hours before the
appointment starts, they cancel it. The appointment is marked as cancelled and the client gets
confirmation that the cancellation went through.

**Why this priority**: This is the core ability the feature exists for. Without it nothing else
in this spec applies.

**Independent Test**: Book an appointment more than 24 hours in the future, cancel it as the same
client, and check that it now shows as cancelled.

**Acceptance Scenarios**:

1. **Given** a client has a booked appointment starting 3 days from now, **When** that client
   cancels it, **Then** the appointment's status becomes "cancelled" and the client is told the
   cancellation succeeded.
2. **Given** a client has a booked appointment starting exactly 24 hours from now, **When** that
   client cancels it, **Then** the cancellation is accepted (exactly 24 hours counts as "up to
   24 hours before").
```

Tradução:

```markdown
### História de usuário 1 - Cancelar um agendamento com antecedência (Prioridade: P1)

Um cliente que agendou um horário descobre que não vai poder ir. Pelo menos 24
horas antes do início do agendamento, ele o cancela. O agendamento é marcado
como cancelado e o cliente recebe a confirmação de que o cancelamento foi
feito.

**Por que esta prioridade**: esta é a capacidade central para a qual a
funcionalidade existe. Sem ela, nada mais nesta especificação se aplica.

**Teste independente**: agende um horário a mais de 24 horas no futuro,
cancele-o como o mesmo cliente e confira que agora ele aparece como cancelado.

**Cenários de aceitação**:

1. **Dado** que um cliente tem um agendamento que começa daqui a 3 dias,
   **Quando** esse cliente o cancela, **Então** o status do agendamento passa
   a "cancelled" e o cliente é avisado de que o cancelamento deu certo.
2. **Dado** que um cliente tem um agendamento que começa daqui a exatamente 24
   horas, **Quando** esse cliente o cancela, **Então** o cancelamento é aceito
   (exatamente 24 horas conta como "até 24 horas antes").
```

Uma história de usuário, por que ela tem essa prioridade, como testá-la sozinha e dois cenários na forma Dado, Quando, Então; o segundo é o caso das 24 horas.

OpenSpec, no `specs/appointment-cancellation/spec.md` da mudança, o primeiro dos seus requisitos:

```markdown
### Requirement: Client cancels their own appointment with 24 hours' notice
The system SHALL let a caller cancel an appointment by giving the appointment identifier, the client name, and the current time in clinic local time. The cancellation SHALL succeed when the appointment is booked, belongs to that client name, and starts 24 hours or more after the current time. A successful cancellation SHALL set the appointment's status to `cancelled` and return the appointment. The appointment record SHALL be kept. The system SHALL NOT send any notification.

#### Scenario: Cancelling well ahead of time
- **WHEN** client "Ana" cancels their booked appointment 48 hours before it starts
- **THEN** the cancellation succeeds and the appointment's status is `cancelled`

#### Scenario: Cancelling exactly 24 hours ahead
- **WHEN** client "Ana" cancels their booked appointment exactly 24 hours before it starts
- **THEN** the cancellation succeeds and the appointment's status is `cancelled`
```

Tradução:

```markdown
### Requisito: o cliente cancela o próprio agendamento com 24 horas de antecedência
O sistema DEVE permitir que quem chama cancele um agendamento informando o
identificador do agendamento, o nome do cliente e a hora atual, na hora local
da clínica. O cancelamento DEVE dar certo quando o agendamento está agendado,
pertence a esse nome de cliente e começa 24 horas ou mais depois da hora
atual. Um cancelamento bem-sucedido DEVE mudar o status do agendamento para
`cancelled` e devolver o agendamento. O registro do agendamento DEVE ser
mantido. O sistema NÃO DEVE enviar nenhuma notificação.

#### Cenário: cancelar com bastante antecedência
- **QUANDO** a cliente "Ana" cancela o seu agendamento 48 horas antes do
  início
- **ENTÃO** o cancelamento dá certo e o status do agendamento é `cancelled`

#### Cenário: cancelar exatamente 24 horas antes
- **QUANDO** a cliente "Ana" cancela o seu agendamento exatamente 24 horas
  antes do início
- **ENTÃO** o cancelamento dá certo e o status do agendamento é `cancelled`
```

Um requisito em frases com DEVE, depois dois cenários com nome, em linhas QUANDO e ENTÃO; o segundo é o caso das 24 horas.

focus-kit, em `work/cancel.md`, o objetivo e o comportamento da página:

```markdown
**Objective.** Staff can cancel an appointment for the client whose name it
carries, up to 24 hours before it starts. The cancelled appointment frees its
slot, and a refusal comes back with a message that says why.

**Behaviour.** In the scenarios, "now" is the time the caller passes in.
- Ada has appointment 1 on 12 March at 10:00. Staff cancel it at 11 March
  09:00 (25 hours before). The answer is appointment 1 with status cancelled.
- The same thing at exactly 11 March 10:00 (24 hours before) succeeds too.
- The same thing at 11 March 10:01 (23 h 59 min before) is refused with
  `too-late`. The appointment stays booked.
- Cancelling after the start time has passed is refused with `too-late`.
- Cancelling appointment 99 when it does not exist is refused with
  `not-found`.
- Cancelling appointment 1 with the name "Bob" is refused with
  `not-your-appointment`. The appointment stays booked. Names are compared
  exactly as given.
- Cancelling appointment 1 a second time is refused with `already-cancelled`.
- When more than one refusal applies, the first in this order wins:
  `not-found`, `not-your-appointment`, `already-cancelled`, `too-late`.
- After appointment 1 is cancelled, booking another client for 12 March at
  10:00 succeeds.
- A cancelled appointment stays in memory with its number. The next booking
  still gets the next number.
- No notification is sent. Nothing is written outside memory.
```

Tradução:

```markdown
**Objetivo.** A equipe pode cancelar um agendamento para o cliente cujo nome
ele leva, até 24 horas antes do início. O agendamento cancelado libera o seu
horário, e uma recusa volta com uma mensagem que diz por quê.

**Comportamento.** Nos cenários, "agora" é a hora que quem chama informa.
- Ada tem o agendamento 1 em 12 de março às 10:00. A equipe o cancela em 11 de
  março às 09:00 (25 horas antes). A resposta é o agendamento 1 com status
  cancelado.
- O mesmo exatamente em 11 de março às 10:00 (24 horas antes) também dá certo.
- O mesmo em 11 de março às 10:01 (23 h 59 min antes) é recusado com
  `too-late`. O agendamento continua agendado.
- Cancelar depois que a hora de início passou é recusado com `too-late`.
- Cancelar o agendamento 99 quando ele não existe é recusado com `not-found`.
- Cancelar o agendamento 1 com o nome "Bob" é recusado com
  `not-your-appointment`. O agendamento continua agendado. Os nomes são
  comparados exatamente como informados.
- Cancelar o agendamento 1 uma segunda vez é recusado com `already-cancelled`.
- Quando mais de uma recusa se aplica, vale a primeira nesta ordem:
  `not-found`, `not-your-appointment`, `already-cancelled`, `too-late`.
- Depois que o agendamento 1 é cancelado, agendar outro cliente para 12 de
  março às 10:00 dá certo.
- Um agendamento cancelado fica em memória com o seu número. O próximo
  agendamento continua recebendo o próximo número.
- Nenhuma notificação é enviada. Nada é gravado fora da memória.
```

O objetivo em três frases, depois o comportamento como exemplos com data e hora; o segundo é o caso das 24 horas.
A página diz "a equipe" onde o briefing diz "cliente" porque os documentos do projeto que o focus-kit escreveu antes da página definiram a equipe da clínica como único usuário, que agenda e cancela pelo cliente.[^spec-driven-run]

Os três decidem a mesma coisa.
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
