# O regulador, e o que o processo não tem

Depois deste capítulo você consegue fazer uma pergunta a tudo o que quer entrar no seu processo, e a cada passo que já está nele: que erro concreto isso teria pegado?
Você aceita só uma resposta que nomeia um erro que aconteceu.
Você também consegue dizer o que o processo não tem, e o que faz cada um desses trabalhos no lugar.

## A pergunta

O kit escreve uma regra no documento de processo de todo projeto, no §7 do docs/05, "O que este processo não tem": quando algo novo é proposto, pergunte que erro concreto isso teria pegado, e aceite uma resposta que nomeia um erro que aconteceu.
O `SETUP.md`, o arquivo que descreve o kit, põe a mesma regra entre os princípios: nada entra no processo sem nomear o erro concreto que teria pegado.
Este livro chama essa pergunta de regulador, como a peça que impede um motor de girar mais rápido do que a carga pede.

A resposta tem de nomear um erro que aconteceu porque um passo é pago de novo por toda entrega que vem depois dele: cada uma roda o passo, o satisfaz e espera por ele.
Um erro possível justifica qualquer coisa, já que sempre há algum erro possível; um erro que aconteceu é um fato que você consegue conferir, no histórico, em uma página ou em um achado.
O [capítulo 4](04-birth-of-focus-kit.md) mostrou aonde a outra resposta leva: verificações que toda entrega tinha de passar, e que nunca tinham falhado em um erro do produto.

## Um "não" e um "sim"

O "não" veio no [capítulo 10](10-propose.md): o agente acrescentou à página `skeleton` da clínica uma checagem de que o código do cliente nunca importa arquivos do servidor, uma checagem que não nomeava nenhum erro que teria pegado, e ela saiu da página para o Out of scope dela.

O "sim" está no próprio `make verify` deste livro.
O capítulo 8 citou o registro da sua execução do `/analyze` 13 vezes em inglês e 14 vezes em português, porque uma frase em português carregava uma menção sem par em inglês.[^useful-notes]
A verificação de paridade então comparava capítulos, títulos e status, e passou.
A entrega `useful-notes` a estendeu: as duas edições de um capítulo têm de citar as mesmas chaves de nota, cada uma o mesmo número de vezes, e a página dela nomeia a diferença do capítulo 8 como o erro que aconteceu.[^useful-notes]
O erro veio primeiro; a verificação veio depois dele, e conseguiu nomeá-lo.

## Perguntar de novo ao que já está lá

A pergunta vale nas duas direções: ela decide o que entra, e decide o que fica.

No Ninjobs, quando recomecei o projeto, deixei de fora uma verificação que eu mesmo tinha escrito sobre a forma do código.[^ninjobs]
Nenhum erro do produto jamais tinha falhado nela, então ela não tinha nada para nomear.
O Supabase, o fornecedor do banco de dados, distribui o seu próprio lint, e um dos avisos dele ficava em um relatório que ninguém abria.
Ele apontava um índice idêntico a outro que já existia, então toda escrita naquela tabela escrevia o mesmo índice duas vezes.
Nenhum teste viu isso.

Em 2026-09-02 o lint do fornecedor entrou na `verify`, e o índice duplicado foi o erro que ele nomeou.[^ninjobs]
Duas regras vieram junto.
Um aviso novo reprova a `verify`.
Um aviso já decidido vai para uma lista de exceções, com o seu motivo, e uma entrada dessa lista sem um aviso vivo por trás também reprova, porque uma lista com entradas mortas é uma lista que ninguém mais lê.
A primeira regra impede que avisos novos se acumulem de novo em um relatório; a segunda aplica o regulador à própria lista.

## O que o processo não tem

O §7 do docs/05 lista sete coisas que o processo não tem.
Cada trabalho continua sendo feito, por algo que o processo já tem:

* **Spec formal:** a página, `work/<slug>.md`, diz o que a entrega faz, nas palavras da pessoa que a lê.
* **Delta de spec:** no OpenSpec, o arquivo de uma mudança que lista só os requisitos que ela acrescenta, altera ou remove, incorporado às specs quando a mudança é arquivada;[^openspec-glossary] a mudança do OpenSpec no [capítulo 3](03-spec-driven.md) escreveu dois, cada um com o título "Spec Delta".[^spec-driven-run] No focus-kit, os documentos que a entrega muda, na mesma entrega, dizem o que mudou.
* **Pasta de mudança:** a página é a mudança, em `work/<slug>.md` enquanto é construída e em `work/done/` depois.
* **Tarefas numeradas:** as linhas de Behaviour, cada uma um teste ou uma conferência.
* **Portão antes da implementação:** a pessoa que lê a página antes do `/apply`.
* **Subagente especializado:** um agente que outro agente lança para um papel estreito, com as suas próprias instruções, como um planejador ou um revisor.[^claude-code-subagents] No focus-kit, um agente que lê os documentos.
* **Uma ferramenta que as entregas não pediram:** o próprio regulador, que a mantém fora até uma entrega nomear o erro que ela teria pegado.

Duas coisas deste livro parecem itens dessa lista.
Ler a página antes do `/apply` ([capítulo 10](10-propose.md)) não é um portão: uma pessoa decide o que pedir ao agente, e o processo não roda nenhuma verificação entre a página e a construção.
O segundo agente que leu a página `skeleton` no capítulo 10 não é um subagente especializado: eu escolhi um leitor uma vez, para uma página, e nenhum passo do processo chama um.

## A mesma pergunta no código

No código o regulador tem a sua própria regra, escrita no texto do `/apply` e no AGENTS.md que o kit escreve: uma abstração é escrita na segunda ocorrência concreta, e a entrega diz qual foi a primeira.
Uma cópia não prova que uma versão compartilhada faz falta; duas cópias são o erro que aconteceu.

A revisão do capítulo 12 achou duas repetições assim na clínica, e elas viraram duas linhas do marco 1.1 dela (a tag ainda o chama de marco 2; o capítulo 12 diz por quê), na tag [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone); o original está em inglês, e aqui vai traduzido:[^closing-a-milestone-run]

```diff
+[ ] route-errors         uma resposta databaseFailed compartilhada e uma notFound compartilhada; as primeiras cópias estão em session.server.ts e weeklyHours/route.server.ts
+[ ] minutes-of           um parser de "HH:MM" compartilhado; a primeira cópia está em weeklyHours/rules.ts, a segunda em appointments/rules.ts
```

Cada linha nomeia a primeira cópia, e a `minutes-of` nomeia também a segunda, então a entrega que construir a versão compartilhada parte das duas.

## Pontos-chave

* Pergunte a tudo o que quer entrar no processo, e a cada passo que já está nele: que erro concreto isso teria pegado?
* A resposta nomeia um erro que aconteceu; um erro possível justifica qualquer coisa, e cada passo é pago por toda entrega depois dele.
* Um passo que não nomeia nenhum erro sai, e uma lista de exceções reprova uma entrada sem aviso vivo.
* Cada uma das sete coisas que o processo não tem tem o seu trabalho feito por algo que ele tem: a página, os documentos, as linhas de Behaviour, a pessoa, um agente.
* No código, uma abstração espera a segunda ocorrência concreta, e a entrega nomeia a primeira.

## Exercícios

Estes exercícios usam a clínica, conversando com o agente, nunca à mão.

### Exercício 13.1

Pergunte ao agente quais são a primeira e a segunda cópia por trás das linhas do seu marco 1.1 que criam uma cópia compartilhada.
Para uma repetição no seu código com uma cópia só, diga por que ela espera.

### Exercício 13.2

Peça ao agente que proponha uma verificação que falta ao seu `npm run verify`, e depois faça a ele a pergunta do regulador.
Fique com a verificação só se a resposta nomear um erro do histórico do seu projeto (`git log`, `work/done/`).

### Exercício 13.3

Para cada um dos sete itens do §7 do docs/05 da sua clínica, diga o que no seu projeto faz o trabalho dele.

[^openspec-glossary]: Fission AI, "Glossary", OpenSpec 1.13.2. <https://github.com/Fission-AI/OpenSpec/blob/v1.13.2/docs/glossary.md>
[^spec-driven-run]: A execução deste livro do Spec Kit, do OpenSpec e do focus-kit sobre um briefing, 2026-09-25: os dois deltas de spec da mudança `add-client-cancellation` do OpenSpec. <https://github.com/JCKodel/focus-kit-book/tree/53109f372125e8aeda200bb2e5bbd1ad7bcc5d61/work/done/spec-driven-run/openspec/feature/openspec/changes/add-client-cancellation/specs>
[^claude-code-subagents]: Anthropic, "Create custom subagents", documentação do Claude Code, acesso em 2026-09-29. <https://code.claude.com/docs/en/sub-agents>
[^useful-notes]: A entrega `useful-notes` deste livro, cuja página registra a diferença do capítulo 8 como o erro que justificou estender a verificação de paridade. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/useful-notes.md>
[^closing-a-milestone-run]: A revisão do marco 1 do projeto guiado deste livro: os achados, as decisões e o diff da fila, de onde as duas linhas são citadas. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/closing-a-milestone-run/README.md>
[^ninjobs]: Ninjobs, um repositório privado: o ADR-0022 dele, emenda de 2026-09-02, e a página daquela entrega, parafraseados; a data é a da emenda.
