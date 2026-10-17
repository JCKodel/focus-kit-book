# 17. Fechando um marco

Depois deste capítulo você consegue fechar um marco: planejar a sua revisão como a última linha do marco, testar à mão cada cláusula do seu parágrafo, e transformar cada achado em uma linha `[ ]` no mesmo marco, sob a revisão.
Você também consegue dizer o que essa revisão lê, o parágrafo à mão e o código inteiro pela revisão profunda do seu host, e por que os seus achados não têm revisão própria.

## O problema

Cada página de um marco foi lida antes de o `/apply` construí-la, e cada mudança em stage foi revisada antes do seu commit.
Ninguém olhou para o que elas somam.
Um processo leve não tem barreira entre as entregas, então o risco que ele carrega é a soma: cada entrega certa na sua própria página, e o todo ainda errado.
Uma afirmação do marco que nenhuma entrega assumiu, um passo que funciona sozinho e falha quando a entrega seguinte vem depois dele, como um empréstimo que a tela de empréstimo registra e a lista do membro nunca mostra: nenhum deles reprova na revisão de uma entrega só.

## A revisão é uma entrega

O kit fecha essa brecha com uma regra, o §8 do documento de processo que ele escreve, o docs/05.
Um marco é planejado com a sua revisão como a última linha, `<milestone>-review`, uma entrega como as outras: o `/propose` escreve a sua página, e o `/apply` a executa.
A página dela pega o parágrafo do marco cláusula por cláusula e escreve, para cada uma, qual entrega a atende e como uma pessoa a testa.
Ela não corrige nada.
A revisão também lê o código, o único olhar sobre o todo em vez de sobre uma entrega, porque cada página pode estar certa e o todo errado.
A página dela cita o commit que fechou o marco anterior, ou o primeiro commit do projeto para um primeiro marco; quando o slot Milestone review (revisão de marco) do docs/05 cita uma revisão profunda do código, como o `/code-review ultra <base>` do Claude Code, a pessoa a lança contra esse commit, que é o `<base>`.
O agente pode dizer que chegou a hora, e nunca a lança.
O código de cada entrega continua sendo lido onde a sua mudança é pequena o bastante para ser lida: na mudança em stage antes do seu commit (capítulo 15), e no pull request, quando o time integra as suas entregas por um (capítulo 22).

## Teste cada cláusula à mão

Um marco termina com um parágrafo escrito como um teste que uma pessoa consegue conferir no produto.
Para um marco da biblioteca de empréstimos, escrito para este capítulo:

```
Quando ele fecha, um bibliotecário consegue emprestar um exemplar e registrar
a sua devolução, e um membro vê os seus empréstimos com a data de devolução
de cada um.
```

A pessoa roda o teste que a página escreveu para cada cláusula, no produto rodando, ponta a ponta, uma vez, na ordem em que um bibliotecário e um membro as encontrariam: emprestar um exemplar, registrar a sua devolução, abrir os empréstimos do membro e ler as datas de devolução.
A checagem de cada entrega testou a sua própria parte; esta roda todas juntas, como o produto é usado.
Uma pessoa faz isso à mão porque o parágrafo é uma promessa às pessoas que vão usar o produto, e só quem o usa como elas vão usar vê se ela se sustenta.
Uma cláusula que nenhuma entrega atende, ou uma que falha nas mãos da pessoa, é um achado.
Não há nada a confirmar ou rejeitar: a falha aconteceu nas suas mãos.

## Leia o código inteiro uma vez

O teste à mão vê o produto como um usuário o encontra, e por isso não vê nada que um usuário não consiga ver.
Uma chamada que leva centenas de milissegundos ainda responde.
Uma página que pode ser enquadrada, exibida por outro site dentro do dele para enganar um visitante e levá-lo a um clique, continua parecendo certa.
Dados enviados a um serviço que não deviam alcançar não deixam rastro na tela, e uma função que alcança uma rede que não devia ainda devolve o resultado certo.
Nenhum deles reprova uma cláusula testada à mão; todos eles estão no código.

A revisão profunda do código é o comando do host que lê o código inteiro alterado desde um commit base e relata as falhas que acha ali.
O slot Milestone review do docs/05 a cita em uma linha, aqui para a biblioteca de empréstimos, escrita para este capítulo:

```
Milestone review: /code-review ultra <base>
```

A pessoa a lança uma vez, no fechamento do marco, contra o commit que a página da revisão cita.
Um projeto cujo host não oferece uma revisão assim escreve none (nenhuma) no slot e não lança revisão profunda; o teste à mão continua rodando, e nada mais neste capítulo muda para ele.
Um achado que a revisão do código confirma é um achado como os outros, uma linha `[ ]` sob a linha da revisão; um que ela não confirma não é um achado.

## Uma linha, e não uma correção

Cada achado vira uma linha `[ ]` no mesmo marco, sob a linha da revisão, esperando o `/propose`.
Cada linha diz o que vai ser verdade, nunca como corrigir.
Se o exemplar devolvido continuasse entre os empréstimos do membro, as linhas do marco terminariam assim, escritas para este capítulo:

```
[x] emprestar-livro      o bibliotecário empresta um exemplar
[x] devolver-livro       o bibliotecário registra uma devolução
[x] meus-emprestimos     um membro vê os seus empréstimos e as datas
[x] m1-review            cada cláusula do parágrafo testada à mão
[ ] emprestimo-devolvido o exemplar devolvido sai da lista do membro
```

Cada linha de achado é uma entrega: o `/propose` vai escrever a sua página e o `/apply` vai construí-la.
O marco fecha quando essas linhas estão `[x]`, cada uma com a sua prova.

Uma linha, e não uma correção, porque uma correção feita no meio do marco seguinte não tem página nem revisão.
Ninguém lê o escopo dela antes de ela ser construída, ninguém a confere contra uma página depois, e ela cai em um marco cujo parágrafo não a menciona.
Como linha, ela espera a sua vez, e ganha as duas coisas.
E ela fica no marco cujo parágrafo ela reprova, então esse marco só fecha quando o seu parágrafo se sustenta.

## Nenhuma segunda revisão

As linhas de achado não têm revisão própria.
Cada uma passa pela sua própria página, pela sua prova e pelo commit da pessoa, que é a revisão.
Eu mantenho assim porque uma revisão das correções acha achados próprios, e uma revisão desses acha mais, e um marco que continua abrindo rodadas de correções nunca fecha.

## Quando os achados viraram uma entrega

Na Ninjobs, a revisão na abertura ao público devolveu oito achados, com toda a suíte de testes verde.
Consultas levavam centenas de milissegundos, uma vaga de emprego grande teria estourado o tempo limite, e três dos achados eram sobre segurança.
Aquela revisão leu o código, e ela é a razão de a revisão de marco do kit também lê-lo: cada entrega tinha passado nos seus próprios testes e na sua própria revisão, e só o olhar sobre o todo viu os oito.

Eu pus os oito em uma entrega em vez de oito linhas.
A página dela diz, com as suas próprias palavras, que não cabe em uma página e que quebra a regra de propósito, e ela chegou a 879 linhas, a página mais longa do projeto.
As correções se sustentaram: a página mediu a triagem de vagas em cerca de 620 ms no banco de dados de desenvolvimento quando o trabalho começou, e em 94 ms quando terminou.
Mas quando eu mesmo conferi o resultado, achei falhas que os testes dela não tinham pegado.
A causa não foi o processo; foi a minha escolha.
Oito linhas teriam sido oito páginas, cada uma pequena o bastante para ser lida antes de ser construída e conferida depois.

## O que o time ganha

Um teste à mão do produto inteiro vê o que a checagem de nenhuma entrega sozinha consegue ver: uma cláusula que nenhuma entrega assumiu, um passo que falha quando as entregas rodam juntas, encontrados do jeito que um usuário vai encontrá-los, antes dos usuários.
A leitura do código inteiro soma o que nenhum teste à mão consegue ver, o tipo de falha que a revisão na abertura da Ninjobs achou.
Esse ganho não tem número neste livro.
E como cada achado vira uma linha, o time vê o custo das brechas do marco na fila, ao lado de tudo o que planeja, e não em correções que ninguém revisou.

## Pontos-chave

* Uma revisão de marco olha para o que as entregas somam, o que nenhuma revisão de uma página ou de uma mudança em stage consegue ver.
* Um marco é planejado com a sua revisão como a última linha, `<milestone>-review`, rodada com o `/propose` e o `/apply`: a página dela cita o commit que fechou o marco anterior, escreve para cada cláusula do parágrafo a entrega que a atende e como uma pessoa a testa, e não corrige nada.
* A pessoa testa cada cláusula à mão e lança contra esse commit a revisão profunda do código que o slot Milestone review do docs/05 cita; uma cláusula que nenhuma entrega atende, ou uma que falha nas mãos da pessoa, é um achado, e um achado que a revisão do código confirma é um achado como os outros.
* Cada achado vira uma linha `[ ]` no mesmo marco, sob a linha da revisão, nunca uma correção no meio do marco seguinte; o marco fecha quando essas linhas estão `[x]`.
* As linhas de achado não têm revisão própria: cada uma passa pela sua própria página, pela sua prova e pelo commit da pessoa.
