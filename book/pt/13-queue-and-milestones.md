# 13. A fila e os marcos

Depois deste capítulo você consegue ler uma fila, dizer o que cada marca significa, e escrever um parágrafo de marco que uma pessoa consegue conferir.
Você também consegue ordenar um marco de modo que a ordem seja a prioridade, escrever em uma linha qual linha precisa estar feita antes dela, `· after <slug>`, e acrescentar, mover ou mudar uma linha conversando.

## O problema

Um time que guarda o plano em um gerenciador de tarefas, as decisões em um chat e o andamento na cabeça de alguém não consegue responder "o que falta, e o que foi feito?" sem uma reunião.
Um agente não consegue responder de jeito nenhum: ele não sabe nada no começo de uma sessão, então o que não está escrito onde ele lê não existe para ele.
A fila é um arquivo, o docs/06, que diz o que vem a seguir, o que está em andamento e o que foi entregue, em uma ordem que uma pessoa e um agente leem igual.

## A linha

O docs/06 guarda os marcos do projeto, cada um com um parágrafo que diz o que é verdade quando ele fecha, e sob cada um uma linha por entrega, em ordem.
Uma linha tem três partes, uma marca, um slug e o que a entrega dá, em uma linha, e pode terminar nomeando uma linha que precisa estar feita antes dela:

```
[ ] <slug>  <what it delivers, one line> · after <slug>
```

O `· after`, como o `· blocked:` do [capítulo 16](16-queue-states.md), fica em inglês, como o kit o escreve.

O slug é o nome da entrega, em palavras minúsculas unidas por hífens ([capítulo 14](14-propose.md)).
Ele dá nome à página da entrega, `work/<slug>.md`, e é o argumento dos comandos, `/propose <slug>` e `/apply <slug>`, então a linha, a página e os comandos apontam todos para a mesma entrega.

O kit pede uma linha, e o raciocínio vai para a página.
Na Ninjobs eu deixei as linhas crescerem: a fila dela tinha 102 entregas em 1.711 linhas, 1.052 delas continuações de uma linha, decisões que pertenciam às páginas.
Uma linha que cresce até virar um parágrafo é uma decisão no lugar errado, já que a página é onde a próxima sessão a procura.

## As marcas

Uma linha tem uma de seis marcas, que diz onde a entrega dela está:

* `[ ]` ainda não definida: a entrega tem uma linha e nenhuma página.
* `[~]` sendo definida: uma conversa está escrevendo a página dela.
* `[>]` definida: a página dela, `work/<slug>.md`, existe e espera ser construída.
* `[*]` sendo construída: uma sessão a está construindo.
* `[x]` feita: foi construída, e a página dela foi para `work/done/` ([capítulo 15](15-apply.md)).
* `[?]` esperando: não consegue seguir até outra coisa acontecer, e a linha diz o quê.

O [capítulo 16](16-queue-states.md) mostra quem põe cada marca e em que momento, quando uma linha está livre para começar, e como uma linha espera e sai de `[?]`.

Uma linha nunca sai da fila; ela muda de marca.
Então a fila é também o histórico do que foi entregue, na ordem em que foi planejado, e a página em `work/done/` por trás de cada `[x]` diz o que aconteceu.
No trunk (direto na linha principal do histórico) a página espera sem commit (sem ser registrada no histórico) entre os dois comandos, e o `/apply` a lê da árvore de trabalho, então uma sessão nova a encontra tendo ou não havido commit ([capítulo 20](20-git-essentials.md)).

Este é o primeiro marco da biblioteca alguns dias depois do começo do trabalho, escrito para este capítulo:

````markdown
## Marco 1: uma bibliotecária empresta e recebe de volta

Quando ele fecha, uma bibliotecária consegue cadastrar livros, seus exemplares e
membros, emprestar um exemplar a um membro por 21 dias e registrar a devolução;
um membro com um livro atrasado ou com a inscrição suspensa é recusado.

```
[x] esqueleto        app e servidor vazios, npm run verify, primeira captura de tela
[x] catalogo         a bibliotecária cadastra livros e seus exemplares
[x] membros          a bibliotecária cadastra, suspende e reativa membros
[>] emprestar-livro  a bibliotecária empresta um exemplar, e as regras podem recusar
[ ] devolver-livro   a bibliotecária registra a volta · after emprestar-livro
[ ] m1-review        o marco conferido contra o parágrafo dele
```
````

Qualquer pessoa lê o estado nele: três entregas feitas, `emprestar-livro` tem uma página esperando o `/apply`, e duas linhas ainda não têm página, das quais `devolver-livro` vem depois de `emprestar-livro`, já que um exemplar só é devolvido depois de ter sido emprestado.

## Marcos

### O parágrafo é um teste

O parágrafo de um marco diz o que é verdade quando o marco fecha, em frases que uma pessoa consegue conferir no produto rodando.
Ele é um teste, nunca um tema e nunca uma lista das linhas sob ele: "uma bibliotecária consegue emprestar um exemplar a um membro por 21 dias" pode ser conferido, "empréstimos" não.
Toda frase do parágrafo deveria ter uma linha que a torna verdade, e toda linha deveria servir a uma frase; uma frase sem linha, ou uma linha sem frase, é uma fila para corrigir antes de o trabalho começar.

### Tamanho e ordem

Um marco tem de três a oito entregas, e depois a revisão dele: a regra do kit para o primeiro marco e um bom tamanho para qualquer um.
As primeiras são o esqueleto em que as outras se apoiam: o `esqueleto` da biblioteca cria o `npm run verify`, que toda entrega seguinte roda.
Depois cada linha vem após as linhas de que precisa: uma bibliotecária não consegue emprestar um exemplar antes de o catálogo ter exemplares e de os membros existirem.

A ordem é a prioridade.
Perguntado qual entrega importa mais, você responde pela fila: a que está mais acima nela; a próxima entrega é a primeira livre para começar ([capítulo 16](16-queue-states.md)).
Não há campo de prioridade nem etiqueta para manter em dia com a ordem.

Quando você acrescenta uma linha e já sabe que ela precisa de outra feita antes, você escreve isso junto, no fim: uma devolução precisa de um empréstimo, então `devolver-livro` termina com `· after emprestar-livro`.
Isso é uma ordem, não uma espera: a linha mantém a sua marca, `[ ]`, e fica livre para começar quando `emprestar-livro` estiver `[x]`.
`emprestar-livro` não leva `after`: as linhas de que ela precisa, `catalogo` e `membros`, já estão `[x]`.
Uma linha escrita `[?]` no lugar pareceria travada sem nada ter dado errado; o capítulo 16 guarda o `[?]` para uma espera descoberta no caminho.

### A revisão, e os seus achados

Um marco é planejado com a sua revisão como a última linha, `<milestone>-review`, uma entrega como as outras, que pega o parágrafo cláusula por cláusula ([capítulo 17](17-closing-a-milestone.md)).
Ela não revisa código e não corrige nada: uma pessoa testa cada cláusula à mão.
Cada achado vira uma linha `[ ]` no mesmo marco, sob a linha da revisão, e essas linhas não têm segunda revisão.

## Mudando a fila

Nenhum comando é dono da fila.
Uma ideia nova vira uma linha conversando, em qualquer sessão: você conta ao agente, e ele escreve a linha no marco a que ela pertence, com um slug novo e `[ ]`.
O parágrafo de um marco ou a descrição de uma linha muda do mesmo jeito, e o slug fica, já que uma página ou um commit pode já usá-lo.
Mover uma linha para cima ou para baixo é mudar a prioridade dela, e acontece do mesmo jeito: você pede ao agente para movê-la.
Linhas também vêm da revisão de um marco e, em um projeto existente, das issues ou do roadmap dele.
Você lê a mudança antes do commit, como com todo documento, e ninguém edita a fila à mão.

## O que o time ganha

A fila é o quadro de status compartilhado do time e o histórico dele em um arquivo: o que vem a seguir, o que está em andamento, o que foi feito e em que ordem, legível por um gerente sem ferramenta nenhuma e por um agente no começo de toda sessão.
Na Ninjobs ela guardou 102 entregas, feitas e ainda não feitas, em um arquivo.
No Caso A, um projeto para um cliente em uma plataforma low-code, o Microsoft Power Apps com o Copilot Studio, o relatório de status e a estimativa de risco para o gerente de projeto foram escritos a partir da fila e das páginas, não de memória, e a fila deu o ritmo: cerca de 9 linhas fechadas e 6 abertas por dia.
O [capítulo 19](19-project-as-assistant.md) conta o resto do Caso A, e o [capítulo 22](22-team-tools.md) mostra como a fila dele foi espelhada no quadro que o gerente de projeto já usava.

O changelog do kit, na entrada 2026.10.08.3, conta por que a ordem está escrita: a regra de que a ordem é a prioridade sempre valeu e não estava escrita em lugar nenhum, então um usuário pediu ao kit um jeito de classificar as entregas.
Escrita como regra, ela dispensa classificação: a fila já é uma.
A fila deste próprio livro mostra o `· after` funcionando: no marco M12 dela, sete linhas terminam com `· after kit-2026-10-13`; cada uma leva capítulos para a versão 2026.10.13 do kit, que o repositório precisava rodar antes, e nenhuma delas parece travada enquanto espera a sua vez.[^queue-m12]

## Pontos-chave

* O docs/06 guarda marcos, cada um com um parágrafo, e uma linha por entrega sob ele: uma marca, um slug e o que ela entrega, em uma linha; o raciocínio vai para a página.
* Seis marcas: `[ ]` não definida, `[~]` sendo definida, `[>]` a página existe, `[*]` sendo construída, `[x]` feita, `[?]` esperando; uma linha nunca sai, então a fila é também o histórico.
* O parágrafo de um marco é um teste que uma pessoa confere no produto, nunca um tema.
* De três a oito entregas, o esqueleto primeiro, cada linha após as linhas de que precisa, e por último a revisão, cujos achados viram linhas sob ela no mesmo marco.
* A ordem é a prioridade: a linha mais acima importa mais, e mover uma linha é mudar a prioridade dela.
* Uma dependência conhecida quando a linha é acrescentada é escrita junto, `· after <slug>`: uma ordem, não uma espera, então a linha mantém `[ ]`.
* Nenhum comando é dono da fila: linhas e parágrafos mudam conversando, em qualquer sessão, com o slug mantido.

[^queue-m12]: J.C. Ködel, "One Page at a Time", a fila, `docs/06-Queue.md`, marco M12, 2026-10, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/blob/main/docs/06-Queue.md>

