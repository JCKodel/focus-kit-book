# O projeto como assistente do time

Depois deste capítulo você consegue guardar os emails, as propostas e as notas de reunião de um projeto onde o agente os lê, e perguntar ao projeto, em palavras simples, o que está pendente, como vai o trabalho e quem deve uma resposta.
Você também consegue dizer o que uma pessoa ainda precisa fazer com cada resposta que o agente dá.

## O problema

O desenvolvedor pergunta ao agente sobre o código.
O gerente pergunta ao desenvolvedor sobre o andamento.
Os emails do cliente ficam na caixa de entrada de uma pessoa, e o que foi combinado numa chamada fica na memória de quem estava nela.
Ninguém consegue perguntar ao próprio projeto, então cada pergunta custa o tempo de uma pessoa, e a resposta só é tão boa quanto a memória dessa pessoa naquele dia.

## O que o agente já lê

Um projeto com focus-kit já escreve quase tudo o que um time pergunta, porque o agente precisa disso para construir:

* **Os documentos** (capítulo 10): o produto e as suas regras no docs/00, o vocabulário no docs/03, as decisões e os seus motivos nos ADRs.
* **A fila** (capítulo 13): cada entrega, uma linha cada, com a sua marca: `[ ]` ainda não definida, `[>]` definida e esperando para ser construída, `[x]` concluída.
* **As páginas em `work/`** (capítulo 14): o que está definido agora, e o que cada entrega vai fazer.
* **As páginas em `work/done/`**: o que cada entrega concluída fez, e o que aconteceu enquanto era construída.
* **O histórico do git** (capítulo 19): quando cada commit aconteceu, e a qual entrega pertence, já que o commit que fecha uma entrega termina com o slug dela.

Lidos juntos, eles respondem às perguntas de andamento sem ninguém escrever um relatório.
Pendente são as linhas `[ ]` e `[>]`, na ordem da fila.
Em andamento são as páginas em `work/`.
Quanto tempo uma entrega levou é a distância entre o primeiro commit que tocou a página dela e o commit que a moveu para `work/done/`.
Nada disso foi escrito para o gerente; um documento que responde à construção também responde ao time.

## A pasta de contexto

O que o código e os documentos não conseguem dizer fica numa pasta na raiz do projeto, `context/` (capítulo 12): os emails do cliente, a proposta, as notas de uma reunião, uma decisão que o cliente tomou numa chamada.
Guarde tudo em Markdown, porque o agente lê texto: um PDF ou um email exportado vira um arquivo Markdown uma vez, quando chega, e o agente pode fazer a conversão.
Escreva ali primeiro cada mensagem que você envia, como registro, e envie uma cópia dela.
Um layout para a biblioteca de empréstimos da Parte I, escrito para este capítulo:

```text
context/
  notes/        one file per meeting, named by its date
  received/     each email or document from outside, as Markdown
  sent/         each message sent, written here before it goes out
  work-record.md
```

A pasta guarda o que as pessoas disseram; os documentos guardam o que o projeto decidiu a partir disso.
Quando o cliente decide que multas não existem, a mensagem vai para `context/received/`, e a regra vira uma linha do docs/00, onde o `/propose` a lê.

Se a `context/` entra em commit depende de quem vai ler o repositório.
Quando o repositório fica com o time, faça o commit dela: uma pessoa nova, ou uma sessão nova, encontra o histórico de cada decisão ao lado da decisão.
Quando o próprio repositório é entregue a um cliente, ou vai ser público, liste a pasta no `.gitignore` e deixe só os fatos de engenharia passarem para os documentos.
Uma pasta ignorada continua no disco, então o agente a lê em toda sessão; só o git não a guarda, então faça backup dela em outro lugar.
Dados pessoais e qualquer coisa sob cláusula de confidencialidade ficam fora do repositório em todo caso, porque o git guarda um arquivo removido no seu histórico.

No Caso A, um projeto para um cliente em uma plataforma low-code, o próprio repositório era o entregável contratado.[^case-a]
A pasta de correspondência dele ficou fora do repositório, e só os fatos de engenharia passaram: uma decisão que o cliente tomou numa mensagem virou uma linha de um documento, nunca a mensagem.

## As perguntas que o time faz

Estas são as perguntas que um time faz toda semana, e o arquivo que responde a cada uma:

* **O que está pendente?** As linhas `[ ]` e `[>]` da fila, marco por marco.
* **Como vai o trabalho?** Linhas fechadas e linhas abertas por dia, a partir da fila e das datas dos commits, contra o parágrafo do marco que diz o que "fechado" significa (capítulo 13).
* **Quem me deve uma resposta?** A tabela de perguntas enviadas e não respondidas, no registro de trabalho.
* **O que preciso perguntar, e a quem?** As decisões em aberto no docs/00, e as páginas que esperam por alguém.
* **O que combinamos com o cliente?** O docs/00 e os ADRs para o que virou regra; a pasta de contexto para a mensagem de onde veio.
* **Quanto tempo levaram as últimas cinco entregas?** As datas dos commits dos seus cinco slugs.

O registro de trabalho é um arquivo com duas tabelas, na pasta de contexto, ou no repositório quando não nomeia ninguém privado, mantido em dia pelo agente sempre que uma mensagem sai ou uma resposta chega.
Para a biblioteca de empréstimos, escrito para este capítulo:

```markdown
## Perguntas enviadas

| Enviada | Para                   | Sobre                                        | Respondida |
|---------|------------------------|----------------------------------------------|------------|
| dia 3   | bibliotecário-chefe    | Multas existem, e de quanto por dia?         | dia 5      |
| dia 4   | setor de TI            | O sistema pode enviar email aos membros?     |            |

## Ainda em aberto

| Linha          | Espera por                       | Desde |
|----------------|----------------------------------|-------|
| overdue-notice | setor de TI: email aos membros   | dia 4 |
```

A primeira tabela diz quem foi perguntado sobre o quê, e quando respondeu.
A segunda diz qual linha da fila está bloqueada, por quem, e há quanto tempo, então "quem me deve uma resposta" é uma tabela, e um lembrete a essa pessoa é escrito a partir dela.

O Caso A manteve as duas tabelas: perguntas enviadas, com para quem, sobre o quê e respondida quando; e ainda em aberto, com a linha, o que ela espera e desde quando.[^case-a]
Vinte perguntas a pessoas de fora do projeto foram registradas ali, e duas ainda estavam sem resposta quando ele fechou.[^case-a]
O relatório de fim de dia e a estimativa de prazo e risco para o gerente de projeto dizem que foram escritos a partir da fila e das páginas, não de memória.
A fila deu o ritmo: cerca de nove linhas fechadas e cerca de seis linhas novas abertas por dia, então a lista aberta encolhia cerca de três por dia.[^case-a]
Esse ritmo pôs um corte de escopo diante do gerente de projeto no meio do projeto, como uma decisão para ele tomar.

## A pessoa é o cérebro

A resposta do agente parece certa mesmo quando está errada: fluente, formatada e segura de si.
Ela pode deixar de fora uma mensagem que ninguém pôs na pasta, ler um rascunho como enviado, ou contar uma linha cuja página diz que ela espera por alguém.
Então a pessoa mantém três tarefas, as mesmas três que o prólogo dá à pessoa para o código.
Ela interpreta: o que a resposta significa para o cliente, o orçamento e a data.
Ela guia: faz a próxima pergunta, e aponta ao agente o arquivo que ele deixou de ler.
Ela valida: abre a linha, a tabela ou o commit em que a resposta se apoia.

Peça ao agente que nomeie o arquivo por trás de cada resposta.
Uma resposta com um arquivo para abrir é conferida em um minuto; uma resposta sem arquivo é um palpite, por mais bem escrita que esteja.

## A sessão do gerente

Um gerente não precisa de editor de código.
Ele abre o host (capítulo 11) na pasta raiz do projeto, a que tem o arquivo de regras, e pergunta em palavras simples.
O host carrega o arquivo de regras no início da sessão (capítulo 2), e o arquivo de regras manda o agente ler os documentos antes de agir, então a sessão do gerente começa dos mesmos documentos que a do desenvolvedor.

Uma pergunta não toca em código, e o modo de plano do host (capítulo 14) impede uma sessão de editar qualquer coisa.
Quando o gerente quer mudar algo, como uma linha nova na fila, o agente a escreve por conversa, como em qualquer sessão (capítulo 13), e uma pessoa revisa e faz o commit (capítulo 15).

## O que o time ganha

Um só assistente para engenharia e produto: os mesmos documentos respondem ao "onde fica essa regra" de um desenvolvedor e ao "quem nos deve uma resposta" de um gerente, e ninguém escreve um relatório de andamento à mão.
No Caso A, vinte perguntas a pessoas de fora foram acompanhadas até as respostas, as duas que ficaram em aberto foram nomeadas no fechamento, e o relatório e a estimativa de risco vieram de uma fila que fechava cerca de nove linhas por dia.[^case-a]

## Pontos-chave

* Os documentos, a fila, as páginas e o histórico do git já respondem o que está pendente, o que está em andamento e quanto tempo cada entrega levou.
* A pasta de contexto guarda o que o código não consegue dizer, em Markdown; ela entra em commit quando o repositório fica com o time, e fica de fora quando o repositório é entregue ou público.
* Um registro de trabalho com duas tabelas, perguntas enviadas e ainda em aberto, responde "quem me deve uma resposta" e escreve o lembrete.
* A resposta do agente parece certa mesmo quando está errada: peça o arquivo por trás dela, e interprete, guie e valide.
* Um gerente abre o host na raiz do projeto e pergunta em palavras simples; o mesmo arquivo de regras faz o agente ler os documentos primeiro.

[^case-a]: Caso A, um projeto para um cliente em uma plataforma low-code, um repositório privado com a sua correspondência guardada fora dele, contado pelo autor: 20 perguntas registradas a pessoas de fora e 2 sem resposta no fechamento, das duas tabelas do seu registro de trabalho; cerca de 9 linhas fechadas e 6 abertas por dia, das suas 73 linhas concluídas no docs/06 e dos 8 dias de commits no `git log`. O seu dono, o seu cliente e o seu negócio não são revelados.
