# 16. Fechando um marco

Depois deste capítulo você consegue fechar um marco: planejar a sua revisão como a última linha do marco, testar à mão cada cláusula do seu parágrafo, e transformar cada achado em uma linha `[ ]` no mesmo marco, sob a revisão.
Você também consegue dizer por que essa revisão não lê código e por que os seus achados não têm revisão própria.

## O problema

Cada página de um marco foi lida antes de o `/apply` construí-la, e cada mudança em stage foi revisada antes do seu commit.
Ninguém olhou para o que elas somam.
Um processo leve não tem barreira entre as entregas, então o risco que ele carrega é a soma: cada entrega certa na sua própria página, e o todo ainda errado.
Uma afirmação do marco que nenhuma entrega assumiu, um passo que funciona sozinho e falha quando a entrega seguinte vem depois dele, como um empréstimo que a tela de empréstimo registra e a lista do membro nunca mostra: nenhum deles reprova na revisão de uma entrega só.

## A revisão é uma entrega

O kit fecha essa brecha com uma regra, o §8 do documento de processo que ele escreve, o docs/05.
Um marco é planejado com a sua revisão como a última linha, `<milestone>-review`, uma entrega como as outras: o `/propose` escreve a sua página, e o `/apply` a executa.
A página dela pega o parágrafo do marco cláusula por cláusula e escreve, para cada uma, qual entrega a atende e como uma pessoa a testa.
Ela não revisa código e não corrige nada.
O código é lido onde cada mudança é pequena o bastante para ser lida: na mudança em stage antes do commit de cada entrega (capítulo 15), e no pull request, quando o time integra as suas entregas por um (capítulo 21).

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
Aquela revisão leu o código; a revisão de marco do kit não lê mais, já que o código de cada entrega é lido antes do seu commit.
Cada entrega tinha passado nos seus próprios testes e na sua própria revisão; só o olhar sobre o todo os viu.

Eu pus os oito em uma entrega em vez de oito linhas.
A página dela diz, com as suas próprias palavras, que não cabe em uma página e que quebra a regra de propósito, e ela chegou a 879 linhas, a página mais longa do projeto.
As correções se sustentaram: a página mediu a triagem de vagas em cerca de 620 ms no banco de dados de desenvolvimento quando o trabalho começou, e em 94 ms quando terminou.
Mas quando eu mesmo conferi o resultado, achei falhas que os testes dela não tinham pegado.
A causa não foi o processo; foi a minha escolha.
Oito linhas teriam sido oito páginas, cada uma pequena o bastante para ser lida antes de ser construída e conferida depois.

## O que o time ganha

Um teste à mão do produto inteiro vê o que a checagem de nenhuma entrega sozinha consegue ver: uma cláusula que nenhuma entrega assumiu, um passo que falha quando as entregas rodam juntas, encontrados do jeito que um usuário vai encontrá-los, antes dos usuários.
Esse ganho não tem número neste livro.
E como cada achado vira uma linha, o time vê o custo das brechas do marco na fila, ao lado de tudo o que planeja, e não em correções que ninguém revisou.

## Pontos-chave

* Uma revisão de marco olha para o que as entregas somam, o que nenhuma revisão de uma página ou de uma mudança em stage consegue ver.
* Um marco é planejado com a sua revisão como a última linha, `<milestone>-review`, rodada com o `/propose` e o `/apply`: a página dela escreve, para cada cláusula do parágrafo, a entrega que a atende e como uma pessoa a testa; ela não revisa código e não corrige nada.
* A pessoa testa cada cláusula à mão; uma cláusula que nenhuma entrega atende, ou uma que falha nas mãos da pessoa, é um achado.
* Cada achado vira uma linha `[ ]` no mesmo marco, sob a linha da revisão, nunca uma correção no meio do marco seguinte; o marco fecha quando essas linhas estão `[x]`.
* As linhas de achado não têm revisão própria: cada uma passa pela sua própria página, pela sua prova e pelo commit da pessoa.
