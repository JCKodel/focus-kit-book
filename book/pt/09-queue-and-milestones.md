# A fila e os marcos

Depois deste capítulo você consegue ler uma fila, dizer o que cada marca significa e qual comando a muda, e escrever o parágrafo de um marco que uma pessoa consegue conferir.
Você também consegue ordenar as linhas de um marco e acrescentar ou mudar uma linha conversando.

## A linha

Como o `references/documents.md` do kit o define, o docs/06 guarda os marcos do projeto, cada um com um parágrafo que diz o que é verdade quando ele fecha, e sob cada um uma linha por entrega, em ordem.
Uma linha tem três partes, uma marca, um slug e o que a entrega dá, em uma linha:

```
[ ] <slug>    <what it delivers, one line>
```

O slug é o nome da entrega, em palavras minúsculas ligadas por hífens.
Ele dá nome à página da entrega, `work/<slug>.md`, e é o argumento dos comandos, `/propose <slug>`, então a linha, a página e o comando apontam para a mesma entrega.
Você já leu duas filas: a da clínica, que o `/brainstorm` escreveu no [capítulo 7](07-brainstorm.md), em [`book-v1/brainstorm`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/docs/06-Queue.md), e a do CLAHub, que o `/analyze` escreveu no [capítulo 8](08-analyze.md), em [`book-v1-analyze`](https://github.com/JCKodel/clahub/blob/book-v1-analyze/docs/06-Queue.md).

O kit pede uma linha, e o raciocínio vai para a página.
No Ninjobs eu deixei as linhas crescerem: a fila dele tinha 102 entregas em 1.711 linhas, 1.052 delas continuações de uma linha, decisões que pertenciam às páginas.[^ninjobs]
Uma linha que cresce até virar um parágrafo é uma decisão no lugar errado: a página é onde a próxima sessão a procura.

## As marcas

Uma linha tem uma de três marcas:

* `[ ]` ainda não definida: a entrega tem uma linha e nenhuma página.
* `[>]` definida: o `/propose` escreveu a página, `work/<slug>.md`.
* `[x]` feita: o `/apply` a construiu e moveu a página para `work/done/`.

O `/propose` troca `[ ]` por `[>]` quando escreve a página (capítulo 10).
O `/apply` troca `[>]` por `[x]` quando move a página para `work/done/` (capítulo 11).
Uma linha nunca sai da fila; ela muda de marca, então a fila é também o histórico do que foi entregue.

No trunk, a página e a construção entram em um commit, então o `[>]` espera na árvore de trabalho entre os dois comandos; em um branch, a página pode ser commitada nele, e a entrega chega ao branch principal em um merge.
O `/apply` recebe o slug e lê `work/<slug>.md` da árvore de trabalho, então uma sessão nova encontra a página tenha ela sido commitada ou não; a Parte IV ensina o lado do git.

## Marcos

O parágrafo de um marco diz o que é verdade quando o marco fecha, em frases que uma pessoa consegue conferir no produto.
Ele é um teste, e não uma lista das linhas embaixo dele nem um tema: "o dono consegue cadastrar profissionais" dá para conferir, "profissionais" não.
O parágrafo do marco 1 da clínica, citado no [capítulo 7](07-brainstorm.md), é o exemplo: cada frase é algo que o dono ou um cliente consegue fazer.

Um marco tem de três a oito entregas, a regra do `brainstorm/SKILL.md` do kit para o primeiro marco e um bom tamanho para qualquer um.
As primeiras são o esqueleto em que as outras se apoiam; a primeira linha da clínica, `skeleton`, cria o `npm run verify`, que toda entrega seguinte roda.
Depois, cada linha vem depois das linhas de que precisa: um cliente não consegue agendar antes de o dono definir os horários de um profissional.
Fechar um marco, e revisar o conjunto, é o capítulo 12.

## Mudando a fila

Nenhum comando é dono da fila.
Uma ideia nova vira uma linha conversando, em qualquer sessão: você conta ao agente, e ele escreve a linha no marco a que ela pertence, com um slug novo e `[ ]`.
O parágrafo de um marco ou a descrição de uma linha mudam do mesmo jeito, e o slug fica, já que uma página ou um commit pode já usá-lo.
Linhas vêm também da revisão de um marco (capítulo 12) e, num projeto existente, das issues dele (capítulo 8).
Você revisa o diff, como em todo documento ([capítulo 6](06-the-documents.md)).

A fila deste livro é um exemplo.
Depois que os capítulos 7 e 8 ficaram prontos, pedi ao agente que definisse as [duas escolhas](06-the-documents.md#as-duas-escolhas) do kit no capítulo 6, para que os dois capítulos pudessem apontar para elas.
Este é o diff do docs/06 nesse commit.
Ele fica como está no repositório, em inglês: a linha nova diz "Capítulo 6 ganha 'As duas escolhas': FOCUS (quatro peças, inteiro / dois princípios / nenhum) e git (trunk / branch / worktree) em um parágrafo cada, para que os capítulos 7 e 8 apontem para elas; as Partes III e IV ainda as ensinam"; no marco 4, "erros como valores" vira "exceções como valores" no parágrafo e na linha `errors-and-slices`, e a linha `four-pieces` perde "(a lição do Ninjobs do capítulo 4)".

````diff
diff --git a/docs/06-Queue.md b/docs/06-Queue.md
index 52ea9aa..d9ddd9f 100644
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@ -41,6 +41,7 @@ When this milestone closes, a reader can install the kit, document a new or an e
 [x] the-documents          Chapter 6: docs/00 to 06, ADRs, AGENTS.md, and why documents do the work
 [x] brainstorm             Chapter 7: /brainstorm on the guided project, and choosing a stack by what the agent knows (the Ninjobs lesson of chapter 4)
 [x] analyze                Chapter 8: /analyze on the brownfield project
+[x] two-choices            Chapter 6 gains "The two choices": FOCUS (four pieces, whole / two principles / neither) and git (trunk / branch / worktree) in a paragraph each, so chapters 7 and 8 point back to them; Parts III and IV still teach them
 [ ] queue-and-milestones   Chapter 9: the queue, the marks, milestones and their paragraphs
 [ ] propose                Chapter 10: /propose, one page, and splitting what does not fit
 [ ] apply                  Chapter 11: /apply, verify, proof, documents, stage, never commit
@@ -50,11 +51,11 @@ When this milestone closes, a reader can install the kit, document a new or an e
 
 ## M4. Part III, FOCUS architecture
 
-When this milestone closes, a reader can organize code by feature with errors as values, and knows when the four pieces pay their way and when they do not.
+When this milestone closes, a reader can organize code by feature with exceptions as values, and knows when the four pieces pay their way and when they do not.
 
 ```
-[ ] errors-and-slices      Chapter 14: errors as values and vertical slices, the two principles that stand alone
-[ ] four-pieces            Chapter 15: View, Orchestrator, Use Case, Repository, one table and one flow, and when the four pieces pay their way (the Ninjobs lesson of chapter 4)
+[ ] errors-and-slices      Chapter 14: exceptions as values and vertical slices, the two principles that stand alone
+[ ] four-pieces            Chapter 15: View, Orchestrator, Use Case, Repository, one table and one flow, and when the four pieces pay their way
 [ ] testing-and-agents     Chapter 16: testing each piece, and how the architecture helps an agent
 ```
 
````

A linha `two-choices` entrou no meio do M3, onde ela pertence, já `[x]` porque a página e a construção dela entraram em um commit; no mesmo commit, o parágrafo do M4 e as descrições de `errors-and-slices` e `four-pieces` mudaram as palavras e mantiveram os slugs.
Pedi a mudança ao agente e revisei o diff; ninguém editou a fila à mão.

## Pontos-chave

* O docs/06 guarda marcos, cada um com um parágrafo, e uma linha por entrega sob ele: uma marca, um slug e o que ela entrega, em uma linha; o raciocínio vai para a página.
* O slug dá nome à página, `work/<slug>.md`, e é o argumento do `/propose` e do `/apply`.
* Três marcas: `[ ]` não definida, `[>]` a página existe (`/propose`), `[x]` feita (`/apply`); uma linha nunca sai, então a fila é também o histórico.
* O parágrafo de um marco é um teste que uma pessoa confere no produto; de três a oito entregas, o esqueleto primeiro, depois cada linha após as linhas de que precisa.
* Nenhum comando é dono da fila: linhas e parágrafos mudam conversando, em qualquer sessão, com o slug mantido, e você revisa o diff.

## Exercícios

Estes exercícios usam a clínica em `book-v1/brainstorm`, conversando com o agente, nunca à mão; não faça commit de nada, já que os capítulos 10 e 11 movem as marcas de verdade.

### Exercício 9.1

Para cada frase do parágrafo do marco 1, diga a linha que a torna verdadeira.
Se uma frase não tem linha, ou uma linha não serve a nenhuma frase, peça ao agente que corrija a fila e revise o diff.

### Exercício 9.2

Traga uma ideia para a clínica que o briefing do capítulo 7 não exclua, e peça ao agente que a acrescente: uma linha no marco a que ela pertence, ou um marco novo com o seu parágrafo.
Confira o diff: uma linha, um slug novo, `[ ]`, e nenhum raciocínio na linha.

### Exercício 9.3

Peça ao agente que mova `deploy` de volta para o marco 1, e então leia os parágrafos dos dois marcos.
O que mais precisou mudar, e o agente mudou?

[^ninjobs]: Ninjobs, repositório privado, o docs/06 dele na última mudança, 2026-09-22, contado pelo autor: linhas com `wc -l`, entregas como as linhas dentro dos blocos de código que começam com uma marca, continuações como as outras linhas não vazias dentro deles.
