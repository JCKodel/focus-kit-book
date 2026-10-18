# 15. Fechando um marco

Depois deste capítulo você consegue fechar um marco: planejar a sua revisão como a última linha do marco, testar à mão cada cláusula do seu parágrafo, e transformar cada achado em uma linha `[ ]` no mesmo marco, sob a revisão.
Você também consegue dizer o que essa revisão lê, o parágrafo à mão e, com a palavra da pessoa, o código alterado desde a base do marco, dividido por áreas com um agente somente leitura em cada uma e um conferente antes que a pessoa veja um candidato, e por que os seus achados não têm revisão própria.

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
A página dela cita como base o commit da revisão do marco anterior, ou, para um primeiro marco, o primeiro commit do projeto, e lista, pelas áreas que o slot Milestone review (revisão de marco) do docs/05 cita, os caminhos que o intervalo desde ele alterou.
O intervalo a partir do commit da revisão anterior guarda todo commit feito depois dele: todas as correções dos achados dessa revisão, que fecham depois dele, e as entregas do marco seguinte que entraram depois dele.
Uma linha livre do marco seguinte não espera a revisão (capítulo 14), então uma entrega cujo commit veio antes do commit da revisão fica fora do intervalo a partir dele.
A leitura custa, então a sessão diz quando chegou a hora e só a começa com a palavra da pessoa: cada área ganha um leitor próprio, que a lê com o repositório inteiro aberto.
O intervalo de um primeiro marco, a partir do primeiro commit do projeto, guarda toda mudança feita depois desse commit, e não o próprio commit.
O que o primeiro commit acrescentou, num projeto novo os arquivos do kit e os documentos (capítulo 10), não está em nenhum diff do intervalo: os leitores só o veem como o repositório contra o qual leem as suas áreas, e a pessoa leu os documentos antes de fazer o commit deles.
O código de cada entrega continua sendo lido onde a sua mudança é pequena o bastante para ser lida: pela revisão da entrega antes de o `/apply` terminar e na mudança em stage antes do seu commit (capítulo 13), e no pull request, quando o time integra as suas entregas por um (capítulo 20); os leitores do marco procuram o que esses não conseguiram ver.

## Teste cada cláusula à mão

Um marco termina com um parágrafo escrito como um teste que uma pessoa consegue conferir no produto.
Para um marco da biblioteca de empréstimos, escrito para este capítulo:

```
Quando ele fecha, um bibliotecário consegue emprestar um exemplar e
registrar a sua devolução, e um membro vê os seus empréstimos com a data
de devolução de cada um.
```

A pessoa roda o teste que a página escreveu para cada cláusula, no produto rodando, ponta a ponta, uma vez, na ordem em que um bibliotecário e um membro as encontrariam: emprestar um exemplar, registrar a sua devolução, abrir os empréstimos do membro e ler as datas de devolução.
A checagem de cada entrega testou a sua própria parte; esta roda todas juntas, como o produto é usado.
Uma pessoa faz isso à mão porque o parágrafo é uma promessa às pessoas que vão usar o produto, e só quem o usa como elas vão usar vê se ela se sustenta.
Uma cláusula que nenhuma entrega atende, ou uma que falha nas mãos da pessoa, é um achado.
Não há nada a confirmar ou rejeitar: a falha aconteceu nas suas mãos.

## Leia o código desde a base, por áreas

O teste à mão vê o produto como um usuário o encontra, e por isso não vê nada que um usuário não consiga ver.
Uma chamada que leva centenas de milissegundos ainda responde.
Uma página que pode ser enquadrada, exibida por outro site dentro do dele para enganar um visitante e levá-lo a um clique, continua parecendo certa.
Dados enviados a um serviço que não deviam alcançar não deixam rastro na tela, e uma função que alcança uma rede que não devia ainda devolve o resultado certo.
Nenhum deles reprova uma cláusula testada à mão; todos eles estão no código.

O marco é toda mudança desde a sua base, e a leitura cobre todas elas.
O `git diff <base>..HEAD` mostra todas: o `git diff` imprime o que mudou entre dois commits, linha a linha, e `<base>..HEAD` é o intervalo da base até o `HEAD`, o commit em que você está, em geral o último (o capítulo 18 ensina o `HEAD`), então o diff traz toda mudança feita depois da base, seja qual for a entrega que a fez.
Uma revisão que recebe um commit lê o que esse commit mudou, a última entrega do marco, e perde as outras.
O `git diff --stat <base>..HEAD` lista os caminhos do intervalo, e a página da revisão os anota por área, para que os caminhos que os leitores leram possam ser conferidos contra ela.

O slot Milestone review do docs/05 diz como o intervalo se divide: as áreas em que as mudanças de um marco se dividem, um leitor para cada, e o modelo em que os seus leitores e o seu conferente rodam, ou o da sessão.
Para a biblioteca de empréstimos, escrito para este capítulo, ele diz:

```
Milestone review: por áreas, um leitor cada: src/features/emprestimos/,
src/features/membros/, src/features/catalogo/, os documentos e o
resto; leitores e conferente no modelo da sessão.
```

Cada área é uma fatia do capítulo 4, porque as mudanças de uma fatia são lidas juntas; os documentos e o resto é a área do que mora fora das fatias.
Uma área grande demais para uma leitura cuidadosa se divide de novo, como `src/features/emprestimos/` se dividiria no empréstimo e na sua `devolucao/`.

A leitura roda em qualquer host.
Onde o host roda agentes, a sessão lança um agente somente leitura por área, o agente do capítulo 13 que lê arquivos e não edita nada, todos em paralelo.
Onde ele não roda nenhum, a pessoa abre uma sessão nova por área e entrega a ela a sua área.
Cada leitor tem o repositório inteiro aberto e lê as mudanças da sua área procurando o que a revisão própria de nenhuma entrega conseguiu ver: o trabalho de uma entrega contra o de outra, um documento contra outro, o todo contra o docs/01.
Ele aponta candidatos, cada um por arquivo e linha, e os caminhos que leu; um candidato é o que um revisor aponta antes que alguém aja sobre ele.

A página da revisão compara os caminhos lidos com os do intervalo.
Quando faltam alguns, a página diz quais, e a linha da revisão espera como `[?]` com `· resume: apply` e `· blocked: <o que foi lido>` (capítulo 14) até que eles sejam lidos, porque um leitor que leu parte da sua área aponta do mesmo jeito que um que a leu inteira.

Um conferente, um agente ou a própria sessão da revisão, abre o arquivo de cada candidato e o marca antes que a pessoa o veja: visto quando é verdadeiro no arquivo hoje, latente quando nada o dispara hoje, ou fraco quando a afirmação não se sustenta como foi dita.
O candidato de um leitor é uma afirmação sobre um arquivo, e algumas não se sustentam quando o arquivo é aberto; o conferente gasta essa abertura para que a pessoa não precise gastá-la.
Três candidatos da biblioteca de empréstimos, escritos para este capítulo, um por marca, como o conferente os entrega à pessoa:

```
src/features/membros/meusEmprestimos.server.ts:12
  a consulta de meus-emprestimos lê a tabela emprestimo direto; o
  código de empréstimo mora em src/features/emprestimos/, e as outras
  fatias o importam
  visto: verdadeiro hoje, e nenhum teste à mão o mostra
src/features/membros/meusEmprestimos.server.ts:14 e
src/features/emprestimos/devolucao/repositorio.server.ts:21
  cada um escreve a sua condição de empréstimo aberto, devolvido_em nulo
  latente: iguais hoje; divergem no dia em que um empréstimo ganhar
  outro estado
src/features/emprestimos/devolucao/repositorio.server.ts:18
  devolver-livro registra a devolução de um exemplar nunca emprestado
  fraco: o seu UPDATE só casa com um empréstimo aberto e recusa o resto
```

O visto e o latente ficam cada um entre duas fatias, que a revisão de nenhuma entrega lê juntas, e o fraco, sem conferência, gastaria o tempo da pessoa com uma afirmação que o arquivo desmente.

Os leitores e o conferente não corrigem nada.
Um candidato só vira achado quando a pessoa o confirma, e então é um achado como os outros, uma linha `[ ]` sob a linha da revisão.
Um projeto cujo slot Milestone review diz none (nenhuma) não tem leitura do código, e o teste à mão continua rodando.

## Uma linha, e não uma correção

Cada achado vira uma linha `[ ]` no mesmo marco, sob a linha da revisão, esperando o `/propose`.
Cada linha diz o que vai ser verdade, nunca como corrigir.
Se o exemplar devolvido continuasse entre os empréstimos do membro, as linhas do marco terminariam assim, escritas para este capítulo:

```
[x] emprestar-livro      o bibliotecário empresta um exemplar
[x] devolver-livro       o bibliotecário registra uma devolução
[x] meus-emprestimos     um membro vê os seus empréstimos e as datas
[x] m1-review            o parágrafo testado à mão, o código lido
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
O código delas ainda é lido com o todo: a revisão do marco seguinte cita o commit desta revisão como base, então na biblioteca de empréstimos o intervalo de `m2-review` começa no commit de `m1-review` e guarda a correção de `emprestimo-devolvido`.
Eu mantenho assim porque uma revisão das correções acha achados próprios, e uma revisão desses acha mais, e um marco que continua abrindo rodadas de correções nunca fecha.

## Quando os achados viraram uma entrega

No Ninjobs, a revisão na abertura ao público devolveu oito achados, com toda a suíte de testes verde.
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
A leitura do código inteiro soma o que nenhum teste à mão consegue ver, o tipo de falha que a revisão na abertura do Ninjobs achou.
O conferente gasta o tempo da pessoa com os candidatos que se sustentam, e os caminhos que cada leitor lista fazem uma parte do marco deixada sem ler aparecer na página, em vez de passar como lida.
E como cada achado vira uma linha, o time vê o custo das brechas do marco na fila, ao lado de tudo o que planeja, e não em correções que ninguém revisou.

## Pontos-chave

* Uma revisão de marco olha para o que as entregas somam, o que nenhuma revisão de uma página ou de uma mudança em stage consegue ver.
* Um marco é planejado com a sua revisão como a última linha, `<milestone>-review`, rodada com o `/propose` e o `/apply`: a página dela cita como base o commit da revisão do marco anterior, ou o primeiro commit do projeto para um primeiro marco, escreve para cada cláusula do parágrafo a entrega que a atende e como uma pessoa a testa, e não corrige nada.
* A pessoa testa cada cláusula à mão e, com a palavra da pessoa, a sessão lê o intervalo desde a base pelas áreas do slot, um agente somente leitura em cada uma listando os caminhos que leu, e um conferente marca cada candidato; uma cláusula que nenhuma entrega atende, uma que falha nas mãos da pessoa, ou um candidato que a pessoa confirma é um achado.
* Cada achado vira uma linha `[ ]` no mesmo marco, sob a linha da revisão, nunca uma correção no meio do marco seguinte; o marco fecha quando essas linhas estão `[x]`.
* As linhas de achado não têm revisão própria: cada uma passa pela sua própria página, pela sua prova e pelo commit da pessoa.
