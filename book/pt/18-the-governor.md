# 18. O regulador

Depois deste capítulo você consegue perguntar a tudo o que quer entrar no seu processo, e a cada passo que já está nele, que erro concreto ele teria pegado, e aceitar só uma resposta que nomeie um erro que aconteceu.
Você também consegue listar o que o processo não tem, e dizer o que faz cada um desses trabalhos no lugar.

## O problema

Um processo cresce um passo razoável de cada vez.
Uma checagem aqui, um modelo ali, uma revisão antes de cada construção: cada um faz sentido sozinho, e cada um é pago de novo por toda entrega que vem depois, que o roda, o satisfaz e espera por ele.
Na Ninjobs os passos se acumularam em 29 checagens que nunca pegaram um erro no produto, caras de satisfazer e fáceis de contornar.
Ninguém as acrescentou para atrasar o trabalho; ninguém perguntou o que cada uma tinha pegado.

## A pergunta

O kit escreve uma regra no documento de processo de todo projeto, no §7 do docs/05, "What this process does not have" (o que este processo não tem): quando algo novo é proposto, pergunte que erro concreto isso teria pegado, e aceite uma resposta que nomeie um erro que aconteceu.
O arquivo que descreve o kit a lista entre as regras que todo projeto mantém: nada entra no processo sem nomear o erro concreto que teria pegado.
Este livro chama essa pergunta de regulador, a partir da peça que impede um motor de girar mais rápido do que a sua carga pede.

A resposta precisa nomear um erro que aconteceu, porque um erro possível justifica qualquer coisa: algum erro é sempre possível.
Um erro que aconteceu é um fato que você consegue conferir, no histórico, em uma página ou em um achado.
E o custo que ele precisa superar é pago por toda entrega depois dele.

## Funciona nos dois sentidos

A pergunta decide o que entra, e decide o que fica.

Na Ninjobs, quando eu recomecei o projeto, as 29 checagens saíram: nenhuma delas conseguia nomear um erro no produto que tivesse pegado.
Duas checagens ficaram no lugar delas, ambas protegendo a promessa de privacidade do produto, onde um vazamento é o erro que o produto não pode se permitir: uma prova do que cada nível de privacidade pode mostrar, e um teste das regras de acesso do banco de dados.

O que entrou depois entrou do mesmo jeito.
O Supabase, o fornecedor do banco de dados, traz o seu próprio lint (um verificador automático de problemas), e um dos avisos dele estava em um relatório que ninguém abria.
Ele apontava um índice idêntico a outro que já existia, então toda escrita naquela tabela gravava o mesmo índice duas vezes, e nenhum teste via isso.
Em 2026-09-02 o lint do fornecedor entrou na verificação, e o índice duplicado foi o erro que ele nomeou.
Duas regras vieram com ele: um aviso novo reprova a verificação, e um aviso já decidido vai para uma lista de exceções com o seu motivo.
Uma entrada nessa lista sem um aviso vivo por trás dela também reprova, porque uma lista com entradas mortas é uma lista que ninguém lê mais: o regulador aplicado à própria lista.

No código o regulador tem a sua própria forma, a regra da segunda ocorrência do capítulo 4: uma cópia não é evidência de que uma versão compartilhada é necessária, e duas cópias são o erro que aconteceu.

## O que o processo não tem

O §7 do docs/05 lista oito coisas que o processo não tem.
Cada trabalho ainda é feito, por algo que o processo já tem:

* **Nenhuma especificação formal:** a página, `work/<slug>.md`, diz o que a entrega faz, com as palavras da pessoa que a lê.
* **Nenhum spec delta**, o arquivo do OpenSpec que lista só os requisitos que uma mudança acrescenta, altera ou remove, juntado às especificações quando a mudança é arquivada:[^openspec-glossary] os documentos que a entrega muda, na mesma entrega, dizem o que mudou.
* **Nenhuma pasta de mudança:** a página é a mudança, em `work/<slug>.md` enquanto é construída e em `work/done/` depois.
* **Nenhuma tarefa numerada:** as linhas de Comportamento, cada uma um teste ou uma checagem.
* **Nenhuma barreira antes da implementação:** a pessoa que lê a página antes do `/apply`, e pede o que falta.
* **Nenhuma revisão de uma revisão:** cada linha que uma revisão de marco acrescenta passa pela sua própria página, pela sua prova e pelo commit da pessoa.
* **Nenhum subagente especializado**, um agente que outro agente lança para um papel estreito com as suas próprias instruções, como um planejador ou um revisor:[^claude-code-subagents] um agente só, que lê os documentos.
* **Nenhuma ferramenta que as entregas não pediram:** o próprio regulador, que a mantém de fora até uma entrega nomear o erro que ela teria pegado.

## De um projeto para o kit

A pergunta é feita em cada projeto, e um erro que um projeto prova pode mudar o kit que todo projeto instala.

O Caso A, um projeto para um cliente em uma plataforma low-code, lia a sua fila em um quadro kanban, e o quadro mostrou o que as três marcas do kit escondiam (capítulo 16).
Uma entrega só chegava a Doing depois de a página dela estar escrita, e cinco linhas travadas nas respostas do cliente pareciam trabalho que ninguém tinha começado.
O Caso A acrescentou uma marca à mão, `[?]`, para uma linha esperando por uma pessoa: cinco linhas que pareciam paradas eram o erro, e a marca o nomeou.

O erro não era só do Caso A: todo time que lê a fila como um quadro o encontra no dia em que uma linha espera, ou uma entrega está sendo definida.
Então o kit adotou a resposta na sua versão 2026.10.05, seis marcas com `[?]` entre elas, e este livro segue o kit.[^adr-0018]
O regulador decidiu do mesmo jeito: a marca entrou com o erro que a justificava, provado em um projeto, e o kit a levou a todo projeto.

## O que o time ganha

Cada passo de um processo é pago por toda entrega, então um passo que não pega nada é um imposto sobre todas elas.
A Ninjobs chegou à abertura ao público com um processo de seis regras, as que o `SETUP.md` do kit agora lista para todo projeto, e duas checagens, depois de 29 checagens a terem acompanhado por quinze dias que construíram quatro telas.
O regulador mantém um processo desse tamanho, e deixa um time dizer sim a um passo com o erro que o justifica escrito.

## Pontos-chave

* Pergunte a tudo o que quer entrar no processo, e a cada passo que já está nele: que erro concreto isso teria pegado?
* A resposta nomeia um erro que aconteceu; um erro possível justifica qualquer coisa, e cada passo é pago por toda entrega depois dele.
* Um passo que não nomeia erro nenhum sai, e uma lista de exceções reprova em uma entrada sem um aviso vivo.
* Cada uma das oito coisas que o processo não tem tem o seu trabalho feito por algo que ele tem: a página, os documentos, as linhas de Comportamento, a pessoa, o commit da pessoa, um agente só, e o próprio regulador.
* Um erro provado em um projeto pode mudar o kit: as linhas do Caso A que pareciam paradas renderam o `[?]`, e o kit o adotou para todo projeto.

[^openspec-glossary]: Fission AI, "Glossary", OpenSpec 1.13.2. <https://github.com/Fission-AI/OpenSpec/blob/v1.13.2/docs/glossary.md>
[^claude-code-subagents]: Anthropic, "Create custom subagents", documentação do Claude Code, acesso em 2026-09-29. <https://code.claude.com/docs/en/sub-agents>
[^adr-0018]: ADR-0018 deste livro, "six marks", 2026-10-05, o arquivo `ADR-0018-six-marks.md` na sua pasta de decisões. <https://github.com/JCKodel/focus-kit-book/tree/main/docs/adr>
