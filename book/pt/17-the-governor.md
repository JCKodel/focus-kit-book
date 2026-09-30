# O regulador

Depois deste capítulo você consegue perguntar a tudo o que quer entrar no seu processo, e a cada passo que já está nele, que erro concreto ele teria pegado, e aceitar só uma resposta que nomeie um erro que aconteceu.
Você também consegue listar o que o processo não tem, e dizer o que faz cada um desses trabalhos no lugar.

## O problema

Um processo cresce um passo razoável de cada vez.
Uma checagem aqui, um modelo ali, uma revisão antes de cada construção: cada um faz sentido sozinho, e cada um é pago de novo por toda entrega que vem depois, que o roda, o satisfaz e espera por ele.
Na Ninjobs os passos se acumularam em 29 checagens que nunca pegaram um erro no produto, caras de satisfazer e fáceis de contornar (capítulo 9).[^ninjobs]
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

Na Ninjobs, quando eu recomecei o projeto, as 29 checagens saíram: nenhuma delas conseguia nomear um erro no produto que tivesse pegado.[^ninjobs]
Duas checagens ficaram no lugar delas, ambas protegendo a promessa de privacidade do produto, onde um vazamento é o erro que o produto não pode se permitir: uma prova do que cada nível de privacidade pode mostrar, e um teste das regras de acesso do banco de dados.[^ninjobs]

O que entrou depois entrou do mesmo jeito.
O Supabase, o fornecedor do banco de dados, traz o seu próprio lint (um verificador automático de problemas), e um dos avisos dele estava em um relatório que ninguém abria.
Ele apontava um índice idêntico a outro que já existia, então toda escrita naquela tabela gravava o mesmo índice duas vezes, e nenhum teste via isso.
Em 2026-09-02 o lint do fornecedor entrou na verificação, e o índice duplicado foi o erro que ele nomeou.[^ninjobs]
Duas regras vieram com ele: um aviso novo reprova a verificação, e um aviso já decidido vai para uma lista de exceções com o seu motivo.
Uma entrada nessa lista sem um aviso vivo por trás dela também reprova, porque uma lista com entradas mortas é uma lista que ninguém lê mais: o regulador aplicado à própria lista.

No código o regulador tem a sua própria forma, a regra da segunda ocorrência do capítulo 4: uma cópia não é evidência de que uma versão compartilhada é necessária, e duas cópias são o erro que aconteceu.

## O que o processo não tem

O §7 do docs/05 lista sete coisas que o processo não tem.
Cada trabalho ainda é feito, por algo que o processo já tem:

* **Nenhuma especificação formal:** a página, `work/<slug>.md`, diz o que a entrega faz, com as palavras da pessoa que a lê (capítulo 14).
* **Nenhum spec delta**, o arquivo do OpenSpec que lista só os requisitos que uma mudança acrescenta, altera ou remove, juntado às especificações quando a mudança é arquivada:[^openspec-glossary] os documentos que a entrega muda, na mesma entrega, dizem o que mudou.
* **Nenhuma pasta de mudança:** a página é a mudança, em `work/<slug>.md` enquanto é construída e em `work/done/` depois.
* **Nenhuma tarefa numerada:** as linhas de Comportamento, cada uma um teste ou uma checagem.
* **Nenhuma barreira antes da implementação:** a pessoa que lê a página antes do `/apply`, e pede o que falta.
* **Nenhum subagente especializado**, um agente que outro agente lança para um papel estreito com as suas próprias instruções, como um planejador ou um revisor:[^claude-code-subagents] um agente só, que lê os documentos.
* **Nenhuma ferramenta que as entregas não pediram:** o próprio regulador, que a mantém de fora até uma entrega nomear o erro que ela teria pegado.

## O regulador decide por projeto

A pergunta dá respostas diferentes em projetos diferentes, e deve dar.

O Caso A, um projeto para um cliente em uma plataforma low-code, acrescentou uma quarta marca à sua fila, `[?]`, para uma linha esperando por uma pessoa.[^case-a]
As três marcas do kit leem `[>]` como "definida e esperando para ser construída", e cinco linhas travadas nas respostas do cliente pareciam trabalho que ninguém tinha começado.[^case-a]
Esse era o erro, e a marca o nomeou.

Este livro considerou a mesma marca para a sua própria fila e a rejeitou.[^adr-0013]
A sua única resposta de fora é a aprovação do autor aos trechos anonimizados, e essa aprovação é um item do Pronto quando de uma página, então nenhuma linha da sua fila jamais espera por uma pessoa.
A mesma marca, a mesma pergunta, e duas respostas, cada uma tirada do histórico do próprio projeto.

## O que o time ganha

Cada passo de um processo é pago por toda entrega, então um passo que não pega nada é um imposto sobre todas elas.
A Ninjobs chegou à abertura ao público com um processo de seis regras, as que o `SETUP.md` do kit agora lista para todo projeto, e duas checagens, depois de 29 checagens a terem acompanhado por quinze dias que construíram quatro telas.[^ninjobs]
O regulador mantém um processo desse tamanho, e deixa um time dizer sim a um passo com o erro que o justifica escrito.

## Pontos-chave

* Pergunte a tudo o que quer entrar no processo, e a cada passo que já está nele: que erro concreto isso teria pegado?
* A resposta nomeia um erro que aconteceu; um erro possível justifica qualquer coisa, e cada passo é pago por toda entrega depois dele.
* Um passo que não nomeia erro nenhum sai, e uma lista de exceções reprova em uma entrada sem um aviso vivo.
* Cada uma das sete coisas que o processo não tem tem o seu trabalho feito por algo que ele tem: a página, os documentos, as linhas de Comportamento, a pessoa, um agente só, e o próprio regulador.
* O regulador decide por projeto: o Caso A acrescentou uma marca para linhas esperando por uma pessoa, e este livro, cujas linhas nunca esperam por uma, não.

[^ninjobs]: Ninjobs, o produto do autor, um repositório privado, lido pelo autor no seu ADR-0022, para as 29 checagens, os quinze dias e as quatro telas da era antes da virada e as duas checagens mantidas depois dela, e na emenda de 2026-09-02 e no seu docs/05 §5, para o lint do banco de dados e a sua lista de exceções, parafraseado.
[^openspec-glossary]: Fission AI, "Glossary", OpenSpec 1.13.2. <https://github.com/Fission-AI/OpenSpec/blob/v1.13.2/docs/glossary.md>
[^claude-code-subagents]: Anthropic, "Create custom subagents", documentação do Claude Code, acesso em 2026-09-29. <https://code.claude.com/docs/en/sub-agents>
[^case-a]: Caso A, um projeto para um cliente em uma plataforma low-code, um repositório privado, lido pelo autor no seu docs/05 e nos seus ADRs: a quarta marca e o motivo registrado para ela. O seu dono, o seu cliente e o seu negócio não são revelados.
[^adr-0013]: ADR-0013 deste livro, "three marks only", 2026-09-24. <https://github.com/JCKodel/focus-kit-book/blob/main/docs/adr/ADR-0013-three-marks.md>
