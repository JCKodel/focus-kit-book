# 16. O regulador

Depois deste capítulo você consegue perguntar a tudo o que quer entrar no seu processo, e a cada passo que já está nele, que erro concreto ele teria pegado, e aceitar só uma resposta que nomeie um erro que aconteceu, no seu projeto ou em outro cujo registro você consegue abrir e cujas condições o seu compartilha, a um custo que esse erro justifica.
Você também consegue listar o que o processo não tem, dizer o que faz cada um desses trabalhos no lugar, e dizer por que os leitores das revisões, agentes somente leitura, e o seu conferente são o único subagente especializado que ele admite.
E, quando você limita o tamanho de um passo, consegue limitar para onde vão as palavras dele.

## O problema

Um processo cresce um passo razoável de cada vez.
Uma verificação aqui, um modelo ali, uma revisão antes de cada construção: cada um faz sentido sozinho, e cada um é pago de novo por toda entrega que vem depois, que o roda, o satisfaz e espera por ele.
No Ninjobs os passos se acumularam em 29 verificações que nunca pegaram um erro no produto, caras de satisfazer e fáceis de contornar.
Ninguém as acrescentou para atrasar o trabalho; ninguém perguntou o que cada uma tinha pegado.

## A pergunta

O kit escreve uma regra no documento de processo de todo projeto, no §7 do docs/05, "What this process does not have" (o que este processo não tem): quando algo novo é proposto, pergunte que erro concreto isso teria pegado, e aceite uma resposta que nomeie um erro que aconteceu.
Este livro chama essa pergunta de regulador, a partir da peça que impede um motor de girar mais rápido do que a sua carga pede.

A resposta precisa nomear um erro que aconteceu, porque um erro possível justifica qualquer coisa: algum erro é sempre possível.
Um erro que aconteceu é um fato que você consegue conferir, no histórico, em uma página ou em um achado.
Ele não precisa ter acontecido com você: um erro que outro projeto documentou conta quando você consegue abrir o registro dele, mostrar que as condições que o produziram existem no seu projeto e dizer o que a verificação pegaria.
Um risco que ninguém registrou continua reprovando, e um erro real cujas condições o seu projeto não tem não justifica nenhum passo permanente.
E o custo que ele precisa superar é pago por toda entrega depois dele, que roda a verificação, e pelo time, que a mantém funcionando: um erro relevante compra a menor verificação que o pega, não qualquer verificação.

## Funciona nos dois sentidos

A pergunta decide o que entra, e decide o que fica.

No Ninjobs, quando eu recomecei o projeto, aquelas verificações saíram, menos duas: nenhuma delas conseguia nomear um erro no produto que tivesse pegado.
As duas que ficaram protegem a promessa de privacidade do produto, onde um vazamento é o erro que o produto não pode se permitir: uma prova do que cada nível de privacidade pode mostrar, e um teste das regras de acesso do banco de dados.

O que entrou depois entrou do mesmo jeito.
O Supabase, o fornecedor do banco de dados, traz o seu próprio lint (um verificador automático de problemas), e um dos avisos dele estava em um relatório que ninguém abria.
Ele apontava um índice idêntico a outro que já existia, então toda escrita naquela tabela gravava o mesmo índice duas vezes, e nenhum teste via isso.
Em 2026-09-02 o lint do fornecedor entrou na verificação, e o índice duplicado foi o erro que ele nomeou.
Duas regras vieram com ele: um aviso novo reprova a verificação, e um aviso já decidido vai para uma lista de exceções com o seu motivo.
Uma entrada nessa lista sem um aviso vivo por trás dela também reprova, porque uma lista com entradas mortas é uma lista que ninguém lê mais: o regulador aplicado à própria lista.

No código o regulador tem a sua própria forma, a regra da segunda ocorrência do capítulo 3: uma cópia não é evidência de que uma versão compartilhada é necessária, e duas cópias são o erro que aconteceu.

## Um teto, e para onde vão as palavras

O kit faz a pergunta do regulador aos seus próprios arquivos.
Um comando é lido inteiro pelo agente a cada execução, então as regras do próprio repositório do kit, no seu `CLAUDE.md`, mantêm o corpo de um comando em no máximo trinta linhas de prosa para o `/propose` e cinquenta para o `/apply`, sem contar as linhas em branco nem o frontmatter, o bloco de configurações no topo do arquivo.
Um comando diz quais documentos ler, o que fazer e o que nunca fazer; o que é específico de um projeto vai para um slot do docs/05 ([capítulo 7](07-the-documents.md)).

Um comando cheio não para as palavras: elas vão para os arquivos em volta dele.
Esses arquivos são o §1 do `SETUP.md`, os passos que um agente segue para instalar e atualizar o kit ([capítulo 8](08-install-and-hosts.md)); o modelo do docs/05; e o `documents.md`, a referência que o `/brainstorm` e o `/analyze` leem, que descreve cada documento e guarda esse modelo.
Então as mesmas regras dão um teto a eles também: o §1 com no máximo 160 linhas, o modelo do docs/05 com no máximo 260 linhas não vazias, o `documents.md` com no máximo 450, e uma mudança que passaria de um deles remove tanto quanto acrescenta.
Esses tetos valem para quem muda o kit; instalar o kit não põe nenhum deles no seu docs/05.
O erro que os deixou entrar aconteceu no §1: um dos seus passos estava escrito como uma única frase longa, que um agente que o executava não conseguia manter em mente e reescreveu como uma lista para si mesmo.

O seu próprio projeto funciona do mesmo jeito.
Um limite em um arquivo (um arquivo de regras, um prompt, um comando) leva o crescimento para os arquivos ao lado, então o limite vai para onde vão as palavras, e cada limite nomeia o erro a que responde, como qualquer outro passo.

## O que o processo não tem

O §7 do docs/05 lista oito coisas que o processo não tem.
Cada trabalho ainda é feito, por algo que o processo já tem:

* **Nenhuma especificação formal:** a página, `work/<slug>.md`, diz o que a entrega faz, com as palavras da pessoa que a lê.
* **Nenhum spec delta**, o arquivo do OpenSpec que lista só os requisitos que uma mudança acrescenta, altera ou remove, juntado às especificações quando a mudança é arquivada:[^openspec-glossary] os documentos que a entrega muda, na mesma entrega, dizem o que mudou.
* **Nenhuma pasta de mudança:** a página é a mudança, em `work/<slug>.md` enquanto é construída e em `work/done/` depois.
* **Nenhuma tarefa numerada:** as linhas de Comportamento, cada uma um teste ou uma checagem.
* **Nenhuma barreira antes da implementação além de uma página completa:** a página é a única barreira, lida pela pessoa antes do `/apply`, que pede o que falta; o `/apply` recusa uma página que não está completa e aponta o `/propose`.
* **Nenhuma revisão de uma revisão:** cada linha que uma revisão de marco acrescenta passa pela sua própria página, pela sua prova e pelo commit da pessoa.
* **Nenhum subagente além do que um comando abre por slug e dos leitores e do conferente das revisões**, sendo um subagente um agente que outro agente lança, e um especializado um agente lançado para um papel estreito com as suas próprias instruções, como um planejador ou um revisor:[^claude-code-subagents] cada entrega tem um agente só, que lê os documentos, planeja e constrói, o que um comando abre para cada um dos seus slugs incluído, e os leitores e o conferente das revisões são o único tipo especializado, que a próxima seção explica.
* **Nenhuma ferramenta que as entregas não pediram:** o próprio regulador, que a mantém de fora até uma entrega nomear o erro que ela teria pegado.

## Os subagentes que ele admite

Três passos do processo podem lançar agentes próprios.
Um comando digitado com vários slugs ([capítulo 12](12-propose.md)) abre um subagente por slug, e quando o seu `/propose a b` diz para construir também, cada slug ganha um segundo assim que a sua página chega a `[>]`, um novo subagente que roda o `/apply` nela, mandado para o caminho do worktree da entrega quando há um; nenhum deles é especializado: cada um roda um comando inteiro na sua própria linha, o `/propose` ou o `/apply` que o seu comando pede, como rodaria uma sessão nova em que você digitasse esse comando, então cada entrega ainda é construída por um agente só, que lê, planeja e constrói, e nenhum roda um passo que o seu comando digitado sozinho não rodaria.
A revisão da entrega do [capítulo 13](13-apply.md), onde o host não tem uma revisão própria, entrega as mudanças de uma entrega a um agente somente leitura, um contexto à parte, porque o agente que escreveu uma mudança a relê com o raciocínio que a escreveu.
A revisão de marco do [capítulo 15](15-closing-a-milestone.md) entrega as mudanças de um marco a um leitor por área, um agente somente leitura onde o host roda agentes, e um conferente, um agente ou a própria sessão da revisão, marca cada candidato antes que a pessoa o veja.
Esses leitores, e o conferente quando um agente faz esse trabalho, são subagentes especializados no sentido deste capítulo: a sessão lança cada um para um papel estreito, e ele lê arquivos e as mudanças e não edita nada.

O regulador deixou entrar os leitores e o conferente do jeito que deixa entrar qualquer coisa, cada um com um erro que aconteceu, todos no próprio repositório deste livro, que é público:

* **Os leitores.** Um leitor do código que monta o livro, com o repositório inteiro aberto, achou que a função que lista os arquivos do repositório descartava todo arquivo cujo nome tem uma letra fora do ASCII, como `café.md`, então toda verificação do `make verify` o pulava, a varredura que mantém nomes privados fora do livro incluída, e nenhuma delas conseguia ver isso, já que as verificações eram o que estava quebrado.[^m14-review]
* **O leitor da revisão da entrega.** Essa falha estava no arquivo desde a entrega que o escreveu, lida antes do seu commit só pelo agente que a escreveu e pela pessoa que fez o commit, e, achada só na revisão de um marco, virou uma linha própria em vez de uma correção naquela entrega.
* **Os caminhos lidos.** Um leitor daquela mesma revisão leu alguns dos capítulos, e a revisão fechou como se tivesse lido todos.
* **O conferente.** Um leitor disse que um número de um capítulo não tinha linha na tabela de onde vinha; aberta, a tabela o dava, a partir de duas das suas linhas.

Eles leem e apontam candidatos, e os leitores do marco listam os caminhos que leram; o que se corrige é decidido pelo `/apply` ou pela pessoa, e os leitores e o conferente não corrigem nada.
O conferente trabalha dentro da única revisão, antes que a pessoa veja um candidato, então o processo continua sem revisão de uma revisão: a pessoa decide o que conta.
A exceção não abre mais nada: um subagente lançado só para planejar, construir ou corrigir ainda precisa nomear o seu erro, e até um nomear, fica de fora.

## O erro que rendeu uma marca

A pergunta é feita em cada projeto, e o regulador decide ali; o erro que ele aceita pode vir daquele projeto ou do registro de outro.
No Caso A, um projeto para um cliente em uma plataforma low-code, linhas esperando as respostas do cliente pareciam trabalho parado no seu quadro, e foi esse erro que deixou entrar a marca que o projeto acrescentou à mão, `[?]` (o [capítulo 14](14-queue-states.md) conta a história).
Esse erro aconteceu no Caso A, e é dali que a marca veio, não um pedágio que todo time paga: um time cujas linhas também esperam alguém de fora tem o erro documentado no capítulo 14 e pode acrescentar o `[?]` antes que o seu próprio quadro o engane.

O primeiro erro dos leitores, acima, funciona do mesmo jeito para um time que constrói as suas próprias verificações.
O registro que a entrada dos leitores cita é público, e diz por que os arquivos sumiam: a listagem pedia os nomes ao `git ls-files` sem `-z`, e sem ele o git põe entre aspas um nome que tem uma letra fora do ASCII, então o arquivo era pulado.
Se as suas verificações listam os arquivos do repositório do mesmo jeito, e os seus arquivos podem ter nomes assim, como os de um time que escreve em português podem ter, as condições são suas, e a verificação é pequena: listar com `-z`, e provar uma vez que um arquivo chamado `café.md` chega a toda verificação.
Se as suas verificações nunca listam arquivos, ou os seus nomes são todos ASCII, o mesmo registro é real e não justifica nada no seu projeto.
E se a única verificação que o pegasse fosse alguém lendo todo nome de arquivo antes de cada commit, o erro continuaria relevante e a verificação ficaria de fora, porque toda entrega pagaria por ela à mão.

## O que o time ganha

Cada passo de um processo é pago por toda entrega, então um passo que não pega nada é um imposto sobre todas elas.
O Ninjobs chegou à abertura ao público com um processo de uma página por entrega, dois comandos, uma linha de fila por entrega, duas verificações e a pergunta do regulador (o [capítulo 6](06-birth-of-focus-kit.md) conta a história), depois de as verificações antigas o terem acompanhado por quinze dias que construíram quatro telas.
O regulador mantém um processo desse tamanho, e deixa um time dizer sim a um passo com o erro que o justifica escrito, o seu ou um que outro projeto documentou onde valem as mesmas condições, sem pagar por esse erro antes.
A única exceção traz os erros que a justificam, então o time a confere do jeito que confere qualquer passo, e os leitores ficam no trabalho que esses erros lhes deram.

## Pontos-chave

* Pergunte a tudo o que quer entrar no processo, e a cada passo que já está nele: que erro concreto isso teria pegado?
* A resposta nomeia um erro que aconteceu; um erro possível justifica qualquer coisa, e cada passo é pago por toda entrega depois dele.
* Um passo que não nomeia erro nenhum sai, e uma lista de exceções reprova em uma entrada sem um aviso vivo; um limite no tamanho de um passo vem com limites nos arquivos para onde vão as suas palavras, e uma mudança que passaria de um deles remove tanto quanto acrescenta.
* Cada uma das oito coisas que o processo não tem tem o seu trabalho feito por algo que ele tem: a página, os documentos, as linhas de Comportamento, a pessoa, o commit da pessoa, um agente só, e o próprio regulador; os subagentes que ele admite são o que um comando abre por slug, o do `/propose` e, quando ele diz para construir também, o do `/apply`, cada um aquele agente só na sua própria linha, e os leitores e o conferente das revisões, o único tipo especializado, cada um com um erro que aconteceu.
* O regulador decide em cada projeto, com um erro que aconteceu ali ou um que outro projeto documentou cujas condições ele compartilha, e compra a menor verificação que o pega: o `[?]` do Caso A entrou porque linhas em espera pareciam trabalho parado, e um time cujas linhas esperam alguém de fora pode acrescentá-lo sem esse erro antes.

[^openspec-glossary]: Fission AI, "Glossary", OpenSpec 1.13.2. <https://github.com/Fission-AI/OpenSpec/blob/v1.13.2/docs/glossary.md>
[^claude-code-subagents]: Anthropic, "Create custom subagents", documentação do Claude Code, acesso em 2026-09-29. <https://code.claude.com/docs/en/sub-agents>
[^m14-review]: J.C. Ködel, "One Page at a Time", o registro da revisão do M14, 2026-10-16, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/m14-review.md>
