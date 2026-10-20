# 17. O projeto como assistente do time

Depois deste capítulo você consegue guardar os emails, as propostas e as notas de reunião de um projeto onde o agente consegue lê-los, trazer para os documentos o que eles decidem, e perguntar ao projeto, em palavras simples, em que pé ele está e o que rodar a seguir, o que está pendente, como vai o trabalho e quem deve uma resposta.
Você também consegue dizer o que uma pessoa ainda precisa fazer com cada resposta que o agente dá.

## O problema

O desenvolvedor pergunta ao agente sobre o código.
O gerente pergunta ao desenvolvedor sobre o andamento.
Os emails do cliente ficam na caixa de entrada de uma pessoa, e o que foi combinado numa chamada fica na memória de quem estava nela.
Ninguém consegue perguntar ao próprio projeto, então cada pergunta custa o tempo de uma pessoa, e a resposta só é tão boa quanto a memória dessa pessoa naquele dia.

## O que o agente já lê

Um projeto com focus-kit já escreve quase tudo o que um time pergunta, porque o agente precisa disso para construir:

* **Os documentos**: o produto e as suas regras no docs/00, o vocabulário no docs/03, as decisões e os seus motivos nos ADRs.
* **A fila**: cada entrega, uma linha cada, com a marca que diz onde ela está e, numa linha esperando, o que ela espera (capítulo 14).
* **As páginas em `work/`**: o que está definido agora, e o que cada entrega vai fazer.
* **As páginas em `work/done/`**: o que cada entrega concluída fez, e o que aconteceu enquanto era construída.
* **O histórico do git** (capítulo 18): quando cada commit aconteceu, e a qual entrega pertence, já que o commit que fecha uma entrega termina com o caminho da página dela, `work/done/<slug>.md`.

Lidos juntos, eles respondem às perguntas de andamento sem ninguém escrever um relatório.
Pendente é toda linha ainda não `[x]`, na ordem da fila.
Em andamento são as linhas `[~]` e `[*]`, e travado são as linhas `[?]`, cada uma com o seu motivo.
Quanto tempo uma entrega levou vai do commit que acrescentou a linha dela à fila até o commit que a fechou: do pedido ao fim, com as esperas incluídas.
O commit que a fecha não diz isso sozinho, porque no trunk uma entrega é um commit só, que data o fim dela e não o começo; uma linha acrescentada nesse mesmo commit não tem data anterior, e o histórico não sabe dizer quanto tempo ela levou.
Nada disso foi escrito para o gerente; um documento que responde à construção também responde ao time.

## A pasta de contexto

O que o código e os documentos não conseguem dizer fica numa pasta na raiz do projeto, `context/`: os emails do cliente, a proposta, as notas de uma reunião, uma decisão que o cliente tomou numa chamada.
O agente lê texto, então cada item é um par: o original como chegou, guardado como está, e ao lado dele um arquivo Markdown com o mesmo nome mais `.md` (`proposta.pdf.md`) que traz o que o original diz, inteiro, não um resumo dele; o agente pode fazer a conversão, uma vez, quando ele chega, e um item que chega como texto é só o arquivo Markdown.
Escreva ali primeiro cada mensagem que você envia, como registro, e envie uma cópia dela.
Um layout para a biblioteca de empréstimos da Parte I, escrito para este capítulo:

```text
context/
  notas/        um arquivo por reunião, com a data no nome
  recebidos/    cada email ou documento de fora, com seu Markdown
  enviados/     cada mensagem enviada, escrita aqui antes de sair
  registro-de-trabalho.md
```

A pasta guarda o que as pessoas disseram; os documentos guardam o que o projeto decidiu a partir disso.
O `/brainstorm` e o `/analyze` leem a pasta inteira quando começam, então não perguntam o que ela já responde.
Depois disso, nenhuma sessão a relê sozinha.
Quando o cliente decide que multas não existem, a mensagem vai para `context/recebidos/`, e nada muda ainda: você pede ao agente que a leia, e a regra vira uma linha do docs/00; um termo novo vai para o docs/03, e uma entrega nova para a fila no docs/06.
O `/propose` lê ali a decisão, não a mensagem.
Cada mensagem ou documento novo segue o mesmo caminho.
Daí em diante o agente consegue dizer por que uma coisa é como é, e nomear a mensagem que a decidiu.

Se a `context/` entra em commit depende de quem vai ler o repositório.
Quando o repositório fica com o time, faça o commit dela: uma pessoa nova, ou uma sessão nova, encontra o histórico de cada decisão ao lado da decisão.
Quando o próprio repositório é entregue a um cliente, ou vai ser público, liste a pasta no `.gitignore` e deixe só os fatos de engenharia passarem para os documentos.
Uma pasta ignorada continua no disco, então o agente consegue lê-la quando você pede; só o git não a guarda, então faça backup dela em outro lugar.
Dados pessoais e qualquer coisa sob cláusula de confidencialidade ficam fora do repositório em todo caso, porque o git guarda um arquivo removido no seu histórico.
Sem a pasta, o agente não tem correspondência nenhuma: ele lê arquivos, não uma caixa de email.
O repositório deste livro é público, então o docs/05 dele lista a `context/` no `.gitignore` e nunca a cria.

No Caso A, um projeto para um cliente em uma plataforma low-code, o próprio repositório era o entregável contratado.
A pasta de correspondência dele ficou fora do repositório, e só os fatos de engenharia passaram: uma decisão que o cliente tomou numa mensagem virou uma linha de um documento, nunca a mensagem.

## As perguntas que o time faz

Estas são as perguntas que um time faz toda semana, e o arquivo que responde a cada uma:

* **Em que pé estamos, e o que vem a seguir?** As linhas da fila em andamento com as suas marcas, as linhas `[?]` com os seus motivos, e a próxima linha livre com o comando que a começa (a sessão do gerente, mais abaixo, mostra uma resposta).
* **O que está pendente?** As linhas da fila ainda não `[x]`, marco por marco.
* **O que está travado, e esperando o quê?** As linhas `[?]`, e o motivo no fim de cada uma.
* **Como vai o trabalho?** Linhas fechadas e linhas abertas por dia, a partir da fila e das datas dos commits, contra o parágrafo do marco que diz o que "fechado" significa.
* **Quem me deve uma resposta?** A tabela de perguntas enviadas e não respondidas, no registro de trabalho.
* **O que preciso perguntar, e a quem?** As decisões em aberto no docs/00, e as páginas que esperam por alguém.
* **O que combinamos com o cliente?** O docs/00 e os ADRs para o que virou regra; a pasta de contexto para a mensagem de onde veio.
* **Quanto tempo levaram as últimas cinco entregas?** Para cada uma, a data em que a linha dela entrou na fila e a data do commit que a fechou.

O registro de trabalho é um arquivo com duas tabelas, na pasta de contexto, ou no repositório quando não nomeia ninguém privado, mantido em dia pelo agente sempre que uma mensagem sai ou uma resposta chega.
Para a biblioteca de empréstimos, escrito para este capítulo:

```markdown
## Perguntas enviadas

| Enviada | Para        | Sobre                             | Respondida |
|---------|-------------|-----------------------------------|------------|
| dia 3   | direção     | Há multas? De quanto por dia?     | dia 5      |
| dia 4   | setor de TI | Podemos enviar email aos membros? |            |

## Ainda em aberto

| Linha           | Espera por                     | Desde |
|-----------------|--------------------------------|-------|
| aviso-de-atraso | setor de TI: email aos membros | dia 4 |
```

A primeira tabela diz quem foi perguntado sobre o quê, e quando respondeu.
A segunda diz qual linha da fila está travada, por quem, e há quanto tempo, então "quem me deve uma resposta" é uma tabela, e um lembrete a essa pessoa é escrito a partir dela.

O Caso A manteve as duas tabelas: perguntas enviadas, com para quem, sobre o quê e respondida quando; e ainda em aberto, com a linha, o que ela espera e desde quando.
O relatório de fim de dia e a estimativa de prazo e risco para o gerente de projeto dizem que foram escritos a partir da fila e das páginas, não de memória.
O ritmo que a fila deu, linhas fechadas contra linhas abertas por dia, pôs um corte de escopo diante do gerente de projeto no meio do projeto, como uma decisão para ele tomar.

## A pessoa é o cérebro

A resposta do agente pode deixar de fora uma mensagem que ninguém pôs na pasta, ler um rascunho como enviado, ou contar uma linha cuja página diz que ela espera por alguém.
Então a pessoa mantém três tarefas, as mesmas três que o prólogo dá à pessoa para o código.
Ela interpreta: o que a resposta significa para o cliente, o orçamento e a data.
Ela guia: faz a próxima pergunta, e aponta ao agente o arquivo que ele deixou de ler.
Ela valida: abre a linha, a tabela ou o commit em que a resposta se apoia.

Peça ao agente que nomeie o arquivo por trás de cada resposta.
Uma resposta com um arquivo para abrir é conferida em um minuto; uma resposta sem arquivo é um palpite, por mais bem escrita que esteja.

## A sessão do gerente

Um gerente não precisa de editor de código.
Ele abre o host na pasta raiz do projeto, a que tem o arquivo de regras, e pergunta em palavras simples.
O host carrega o arquivo de regras no início da sessão, e o arquivo de regras manda o agente ler os documentos antes de agir, então a sessão do gerente começa dos mesmos documentos que a do desenvolvedor.

O arquivo de regras também tem uma linha para a pergunta que um gerente faz primeiro: perguntado em que pé as coisas estão, o agente responde a partir da fila e de `work/`, com o próximo comando escrito como aquele host o chama.
Não existe comando de status, porque a fila já é o status.
Perguntada "em que pé estamos?" na biblioteca de empréstimos, uma sessão responde assim, numa resposta escrita para este capítulo:

```text
Marco 1, um bibliotecário empresta e recebe de volta: 4 de 7 feitas.
Em andamento: devolver-livro [*], sendo construída.
Esperando: nenhuma.
Próxima linha livre: formato-devolucao [ ], ainda sem página.
Rode: /propose formato-devolucao (Codex: $propose formato-devolucao)
```

Cada parte dela é lida do docs/06: a contagem do marco, a linha em andamento com a sua marca, as esperas, e a primeira linha livre, com o comando que a tabela do capítulo 8 dá para cada host.
No trunk essa é a fila da pasta onde a sessão roda; com um branch ou um worktree por entrega, o branch principal mostra cada linha como estava até o merge dela, então a sessão pega a linha de cada slug no worktree ou no branch dele, local ou remoto, e as reconcilia pelo slug (capítulo 14): só pela cópia do branch principal, `devolver-livro` leria `[ ]`, e "Em andamento" perderia a construção em curso.
Uma linha `[?]` apareceria em "Esperando" com o seu motivo e a fase em que retoma, como a linha os guarda.
Uma resposta tirada do que a sessão lembra, uma oferta de manter um arquivo de status, ou uma sugestão de criar um comando de status quer dizer que o agente não leu a fila: peça o arquivo por trás da resposta.

Uma pergunta não toca em código, e o modo de plano do host (capítulo 12) impede uma sessão de editar qualquer coisa.
Quando o gerente quer mudar algo, como uma linha nova na fila, o agente a escreve por conversa, como em qualquer sessão, e uma pessoa a revisa e faz o commit, por padrão, ou pede ao agente que o faça; quando a palavra do slot Git deixa o agente fazer o commit, a pessoa revisa o commit depois que ele entra.
Uma mudança no código, por menor que seja, também vira uma linha, com um rascunho da página para o detalhe, e a resposta para ali, nomeando o `/propose` para essa sessão, fora do modo de plano, ou uma sessão nova (capítulo 11).

## O que o time ganha

Um só assistente para engenharia e produto: os mesmos documentos respondem ao "onde fica essa regra" de um desenvolvedor e ao "quem nos deve uma resposta" de um gerente, e ninguém escreve um relatório de andamento à mão.
No Caso A, vinte perguntas a pessoas de fora foram acompanhadas até as respostas, as duas que ficaram em aberto foram nomeadas no fechamento, e o relatório e a estimativa de risco vieram de uma fila que fechava cerca de nove linhas e abria cerca de seis por dia.

## Pontos-chave

* Os documentos, a fila, as páginas e o histórico do git já respondem o que está pendente, o que está em andamento e quanto tempo cada entrega levou.
* A pasta de contexto guarda o que o código não consegue dizer, cada original ao lado do seu Markdown; o `/brainstorm` e o `/analyze` a leem inteira quando começam, um item que chega depois é lido quando você pede, e o que ele decide vai para os documentos, onde o `/propose` o lê; ela entra em commit quando o repositório fica com o time, e fica de fora quando o repositório é entregue ou público.
* Um registro de trabalho com duas tabelas, perguntas enviadas e ainda em aberto, responde "quem me deve uma resposta" e escreve o lembrete.
* Peça o arquivo por trás de cada resposta, e interprete, guie e valide.
* Um gerente abre o host na raiz do projeto e pergunta em palavras simples; o mesmo arquivo de regras faz o agente ler os documentos primeiro; perguntado em que pé as coisas estão, ele responde a partir da fila, lida no trunk no arquivo único dela e com um branch ou um worktree por entrega no worktree ou no branch de cada slug, com o próximo comando; não existe comando de status.

