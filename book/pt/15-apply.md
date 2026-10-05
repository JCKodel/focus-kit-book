# 15. `/apply`: construir, verificar, provar, nunca fazer commit

Depois deste capítulo você consegue levar uma página revisada até uma mudança em stage (marcada para o próximo commit, o registro salvo no histórico do projeto) com o `/apply`, e dizer o que "pronto" significa: a verificação verde, uma prova, os documentos atualizados, a página movida e a sua linha marcada.
Então você consegue revisar a mudança em stage contra a página e fazer o commit você mesmo, que é a revisão humana do processo.

## O problema

Um agente a quem se diz "construa isto" para quando o código compila, ou quando os testes que ele escreveu passam.
O que ele construiu em volta do pedido, o que escolheu por conta própria e quais documentos não dizem mais a verdade ficam para alguém achar depois, e esse alguém costuma ser um usuário.
E um agente que faz commit do próprio trabalho põe esse trabalho no histórico do projeto antes que qualquer pessoa o tenha lido.

## O que o `/apply` faz

O `/apply <slug>` constrói a entrega que `work/<slug>.md` descreve, por inteiro, em uma sessão: o código, os testes, a prova e os documentos.
Ele começa em uma sessão nova, então a página é tudo o que ele leva da conversa que a escreveu, e é por isso que o capítulo 14 pede que você leia a página antes de este comando rodar.

### O que ele lê

A página, o `AGENTS.md`, e três dos documentos do projeto: o docs/01, a arquitetura, que diz onde cada peça fica e como os erros circulam; o docs/04, as convenções, que dizem quais testes escrever; e o docs/05, o processo.
O docs/05 guarda os slots do projeto, e o `/apply` os segue ao pé da letra: o comando de verificação, os ambientes e o que uma entrega deixa em cada um, como uma tela é provada, a política de publicação e a estratégia de git.
Então ele marca a linha como `[*]` no docs/06, para a fila mostrar a construção em andamento; em uma linha que está `[?]`, ele primeiro diz o que a linha espera, e só segue quando você diz que está resolvido.

### A página é o escopo

O que a página pede é o que se constrói, e nada em volta.
O arquivo do comando no kit diz isso em uma linha: "*A página é o escopo; não a amplie.*"
Então o `/apply` não acrescenta dependência, camada nem ferramenta que a página não nomeou, e só escreve uma abstração na segunda ocorrência concreta, dizendo qual foi a primeira (capítulo 4).
Um pacote que a página não nomeou é uma pergunta para a pessoa, nunca uma escolha do agente.

### Quando a página contradiz um documento

Ele para e diz qual.
Ou o documento muda na mesma entrega, ou a página está errada; ele nunca escolhe um dos dois em silêncio.
Uma escolha em silêncio deixaria uma página e um documento discordando, e a próxima sessão construiria sobre o que lesse primeiro.

### Quando o trabalho não consegue seguir

Ele para quando a construção precisa de uma resposta que ninguém deu ainda, quando outra linha precisa ser feita antes (uma correção que ele achou vira uma linha `[ ]` acima desta), ou quando você diz que ela está travada.
Ele escreve na página o que foi construído e o que ela espera, deixa a página em `work/`, marca a linha como `[?]` com esse motivo no fim dela, e coloca em stage o que tem (capítulo 16).

### A verificação e a prova

Ele roda o comando de verificação até ficar verde.
Depois prova a entrega do jeito que o docs/05 diz: um screenshot contra o design, uma execução ponta a ponta, ou uma checagem à mão.
Ele lista o que diverge da referência e corrige, até restar só o que ele consegue justificar.
Uma falha faz parte da prova e é registrada, nunca escondida.

### Verde não é pronto

A verificação diz que o código faz o que os testes dele dizem.
Ela não diz nada sobre se a página foi atendida, se os documentos ainda valem, ou se alguém vai conseguir saber depois o que aconteceu.
Então, antes de parar, o `/apply` faz tudo isto:

* Escreve na página o que aconteceu: o que divergiu do plano e por quê, o que foi deixado de lado, o que a prova achou, e as decisões tomadas, com um ADR se foi preciso um.
* Atualiza os documentos que a entrega mudou: um termo novo no docs/03, uma regra nova no documento que é dono dela, uma decisão em docs/adr/.
* Marca cada item do Pronto quando.
* Move a página para `work/done/`, e troca a marca da linha no docs/06 de `[*]` para `[x]`; uma linha `[?]` que esperava só por linhas agora `[x]` volta para `[>]`, ou para `[ ]` quando não tem página.
* Coloca tudo em stage e sugere a mensagem de commit no formato que o docs/05 define.
* A última coisa que ele diz é qual ambiente está em qual versão, e o comando que atualiza os outros.

Pronto é essa lista inteira: a verificação verde, a prova, o que aconteceu escrito na página, os documentos atualizados, a página em `work/done/`, a linha `[x]`, e a mudança em stage.

## `emprestar-livro`, construída

Pegue a página `emprestar-livro` do capítulo 14, revisada e marcada `[>]`, e abra uma sessão nova com `/apply emprestar-livro`.

O agente lê a página, depois o docs/01 para saber que os empréstimos ficam em `src/features/emprestimos/`, o docs/04 para saber quais testes cada peça recebe (capítulo 8), e o docs/05 para saber que a verificação é `npm run verify` e que uma tela é provada por um screenshot.
Ele escreve a migration da tabela `emprestimo` com o seu índice único, a regra `emprestar` como uma função pura que devolve um `Result` (capítulo 5), a chamada do repositório que transforma a falha do índice único na recusa `JaEmprestado`, o orquestrador e a tela de empréstimo.
Cada linha de Comportamento vira um teste: o empréstimo com a devolução prevista para 21 dias depois, a recusa para um livro atrasado, e, contra um banco de dados real em memória, o segundo de dois empréstimos do último exemplar recusado.
Ele não constrói nada para devolver um exemplar, reservas ou multas, porque o Fora do escopo os nomeou.

Se o docs/00 dissesse que um empréstimo dura 14 dias, o agente pararia naquela linha e perguntaria qual é a verdade: os 21 da página ou os 14 do documento.
Qualquer que seja a sua resposta, o outro muda na mesma entrega.

Ele roda `npm run verify` até ficar verde, captura a tela de empréstimo com 390 e 1280 pixels de largura, e compara as duas com o arquivo de design.
Se um botão quebra linha na largura estreita, ele é corrigido; se o arquivo de design não dá um valor para uma cor, a escolha é registrada como uma divergência, com o seu motivo.
Então ele escreve na página o que aconteceu, acrescenta a tabela `emprestimo` ao documento que lista o schema, marca o Pronto quando, move a página para `work/done/emprestar-livro.md`, marca a linha `[x]`, coloca tudo em stage, sugere a mensagem, e termina dizendo qual ambiente roda esta entrega e como atualizar os outros.

## Por que ele para no stage

O `/apply` nunca faz commit e nunca faz merge, qualquer que seja a estratégia de git.
Ele coloca tudo em stage e entrega a mensagem a você; o commit é seu, e vem depois da sua revisão.
O documento de processo do kit dá o fluxo em uma linha: o `/apply` "*constrói, prova, atualiza os documentos, coloca em stage e sugere o commit, nunca faz commit*".

## Revise a mudança em stage

A mudança em stage é o que o agente diz que fez; a sua revisão confere que ele fez.
Leia a mudança contra a página:

* Cada linha de Comportamento foi atendida, cada uma pelo seu teste ou por uma checagem registrada?
* Foi construída alguma coisa que a página não pediu: um arquivo, uma dependência, uma camada?
* A verificação e a prova ficam verdes para você?
* Os documentos que a entrega mudou foram atualizados, e só eles?
* A mensagem sugerida está certa: o assunto, os tópicos, a última linha?

Leia também o que aconteceu, e pergunte-se se você teria decidido alguma divergência de outro jeito.
Peça cada correção ao agente, na mesma sessão, nunca à mão.
A mesma sessão guarda o raciocínio da construção: ela sabe por que fez cada escolha, o que uma sessão nova teria de adivinhar.

Uma pessoa que faz commit depois de muitas entregas boas para de conferir, e toma a palavra do agente no lugar da própria leitura.
Isso é o viés de automação, definido e medido no capítulo 26, e esta revisão o combate de quatro jeitos.
Ela é um conjunto de perguntas respondidas contra uma página que você já leu, não uma olhada no diff.
O registro do que aconteceu, na página, mostra onde o agente decidiu sozinho, então você sabe onde olhar.
Uma página mantém a mudança pequena o bastante para ser lida inteira.
E a verificação e a prova rodaram antes de você olhar, então a sua atenção vai para onde nenhuma checagem chega.

## O commit é a revisão humana

O agente coloca em stage e sugere a mensagem; a pessoa lê o diff e faz o commit.
Três motivos sustentam essa linha.

* **Nada chega ao histórico sem ser lido por uma pessoa.** Um commit diz que uma pessoa leu a mudança e a aceita; um agente que faz commit do próprio trabalho pula o único leitor que consegue dizer que a construção é o que se queria.
* **Um commit se desfaz em um passo.** A página e a sua construção são um commit no trunk (direto na linha principal do histórico), um merge em um branch (uma linha de trabalho à parte, juntada depois à principal), então uma entrega que se mostra errada sai do projeto com um comando (capítulo 20).
* **A pessoa é dona do que é publicado.** O agente escreveu o código, e a pessoa responde por ele ao time, ao cliente e ao usuário; o commit é onde essa resposta é dada.

Leia o diff em stage, depois faça o commit:

```
git diff --staged
git commit
```

Sem `-m`, o git abre o seu editor para a mensagem; cole a sugerida, salve e feche, e o commit existe quando o editor fecha.

### A mensagem

O formato é o que o docs/05 define, e o kit escreve o mesmo em todo projeto:

```
<subject in the imperative, up to 72 characters>

- <a highlight, one line>
- <up to five of them>

work/done/<slug>.md
```

O assunto diz o que a entrega faz, no imperativo, "Lend a copy to a member" e não "Lent" nem "Lending", com um escopo entre parênteses quando ajuda.
Os tópicos são os destaques, nunca o raciocínio.
A última linha aponta para a página em `work/done/`, onde o raciocínio mora, então quem lê o histórico acha a decisão inteira em um arquivo.

## O que o time ganha

Nada é publicado sem uma checagem e uma pessoa: a verificação e a prova conferem a construção, e uma pessoa lê o diff antes de ele existir no histórico.
E o que divergiu do plano fica escrito onde a próxima pessoa lê.
Na Ninjobs, a página da entrega que permite a um usuário excluir a própria conta dizia que a tabela que registra uma exclusão pendente não teria regra de escrita nenhuma.
A construção descobriu que uma tabela sem regra de escrita não aceita escrita de ninguém, nem das funções do próprio banco de dados, então a página registrou o ajuste: nenhum caminho de escrita alcançável pelo cliente, o que o teste das regras de acesso agora prova.
A decisão e o seu motivo estão na página que a construiu, e o commit que a publicou aponta para lá.

## Pontos-chave

* O `/apply <slug>` constrói a página em uma sessão nova, e a página é o escopo: nenhuma dependência, camada ou ferramenta que a página não nomeou.
* Ele marca a linha como `[*]` quando começa, `[x]` quando termina, e `[?]`, com o que ela espera, quando precisa parar.
* Ele segue o docs/05 ao pé da letra, e quando a página contradiz um documento ele para e diz qual; nunca resolve em silêncio.
* Verde não é pronto: pronto é a verificação verde, a prova, o que aconteceu na página, os documentos atualizados, a página em `work/done/`, a linha `[x]` e a mudança em stage.
* Revise a mudança em stage contra a página, e peça cada correção na mesma sessão.
* Essa revisão é a defesa contra o viés de automação, o hábito de confiar no agente depois de muitas entregas boas.
* O agente coloca em stage e sugere a mensagem; a pessoa lê o diff e faz o commit, então nada chega ao histórico sem ser lido, e uma entrega se desfaz em um passo.

