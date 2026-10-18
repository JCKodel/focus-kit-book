# 13. `/apply`: construir, verificar, provar, nunca fazer commit

Depois deste capítulo você consegue levar uma página revisada até uma mudança em stage (marcada para o próximo commit, o registro salvo no histórico do projeto) com o `/apply`, e dizer o que "pronto" significa: a verificação verde, uma prova, uma revisão por um contexto que não escreveu a mudança, os documentos atualizados, a página movida e a sua linha marcada.
Então você consegue revisar a mudança em stage contra a página e fazer o commit você mesmo, que é a revisão humana do processo.
E consegue dizer como o `/apply` termina: só a sua entrega em stage, a mensagem sugerida em um bloco `commit` na página e na conversa, os seus próximos passos escritos por extenso e, por último, qual ambiente está em qual versão.

## O problema

Um agente a quem se diz "construa isto" para quando o código compila, ou quando os testes que ele escreveu passam.
O que ele construiu em volta do pedido, o que escolheu por conta própria e quais documentos não dizem mais a verdade ficam para alguém achar depois, e esse alguém costuma ser um usuário.
Quando se pede a ele que confira o próprio trabalho, ele relê o trabalho com o raciocínio que o escreveu, então o que deixou passar ao escrever deixa passar de novo.
Um estudo de 2024 sobre modelos de linguagem grandes em tarefas de raciocínio, de Jie Huang e colegas, concluiu que eles "*têm dificuldade de corrigir as próprias respostas sem feedback externo e, às vezes, o desempenho deles chega a piorar depois da autocorreção*".[^huang-2024]
E um agente que faz commit do próprio trabalho põe esse trabalho no histórico do projeto antes que qualquer pessoa o tenha lido.

## O que o `/apply` faz

O `/apply <slug>` constrói a entrega que `work/<slug>.md` descreve, por inteiro, em uma sessão: o código, os testes, a prova e os documentos.
Ele começa em uma sessão nova, então a página é tudo o que ele leva da conversa que a escreveu, e é por isso que o capítulo 12 pede que você leia a página antes de este comando rodar.

### O que ele lê

A página, o `AGENTS.md`, e três dos documentos do projeto: o docs/01, a arquitetura, que diz onde cada peça fica e como os erros circulam; o docs/04, as convenções, que dizem quais testes escrever; e o docs/05, o processo.
O docs/05 guarda os slots do projeto, e o `/apply` os segue ao pé da letra: o comando de verificação, os ambientes e o que uma entrega deixa em cada um, como uma tela é provada, como as suas mudanças são revisadas antes de ele terminar, a política de publicação e a estratégia de git.
Do docs/06, a fila, ele lê tudo: precisa ver que as linhas que o seu `· after` nomeia estão feitas antes de começar, e nomeia a próxima linha livre quando termina.
Por isso, cada palavra de uma linha é lida por toda construção tanto quanto por toda definição (capítulo 11).
Então, como a sua primeira edição, ele marca a linha como `[*]` no docs/06, para a fila mostrar a construção em andamento; em uma linha que está `[?]`, ele primeiro diz o que a linha espera, e só segue quando você diz que está resolvido.

### A página é o escopo

O que a página pede é o que se constrói, e nada em volta.
O arquivo do comando no kit diz isso em uma linha: "*A página é o escopo; não a amplie.*"
Então o `/apply` não acrescenta dependência, camada nem ferramenta que a página não nomeou, e só escreve uma abstração na segunda ocorrência concreta, dizendo qual foi a primeira (capítulo 3).
Um pacote que a página não nomeou é uma pergunta para a pessoa, nunca uma escolha do agente.

### Quando a página contradiz um documento

Ele para e diz qual.
Ou o documento muda na mesma entrega, ou a página está errada; ele nunca escolhe um dos dois em silêncio.
Uma escolha em silêncio deixaria uma página e um documento discordando, e a próxima sessão construiria sobre o que lesse primeiro.

### Quando o trabalho não consegue seguir

Ele para quando a construção precisa de uma resposta que ninguém deu ainda, quando outra linha precisa ser feita antes (uma correção que ele achou vira uma linha `[ ]` acima desta), quando você diz que ela está travada, ou, na revisão de um marco, quando a leitura do código alterado desde a base do marco deixou parte dele sem ler.
Ele escreve na página o que foi construído e o que ela espera, deixa a página em `work/`, marca a linha como `[?]` com esse motivo no fim dela (capítulo 14).
Ele termina a página com uma mensagem parcial em um bloco `commit` e mostra o mesmo bloco na conversa.
No trunk ele não coloca nada em stage: o trabalho fica sem commit, e fora do índice, até estar inteiro.
Em um branch da entrega ele pode colocar o trabalho parcial em stage para você fazer o commit lá, e o branch fica sem merge até a entrega estar pronta (capítulo 19).

### A verificação e a prova

Ele roda o comando de verificação até ficar verde.
Depois prova a entrega do jeito que o docs/05 diz: um screenshot contra o design, uma execução ponta a ponta, ou uma checagem à mão.
Ele lista o que diverge da referência e corrige, até restar só o que ele consegue justificar.
Uma falha faz parte da prova e é registrada, nunca escondida.

### A revisão da entrega

Com a verificação verde e a prova feita, e antes de a página registrar o que aconteceu, o `/apply` faz revisar as mudanças da sua entrega por um contexto que não as escreveu.
Isso acontece dentro da mesma sessão, nunca em uma sessão nova, e o slot de revisão da entrega do docs/05 nomeia o revisor.
A primeira escolha do kit é a revisão do próprio host, uma skill que o agente invoca ou um comando que ele roda, quando o agente consegue mantê-la nos caminhos da entrega.
Senão, é um agente somente leitura: um agente que a sessão lança com o seu próprio contexto, que lê arquivos e roda `git diff` e não edita nada (o capítulo 16 diz mais sobre agentes que um agente lança).
Se o slot não nomeia revisor nenhum, essa revisão não existe, e o seu commit continua sendo a única revisão.

A revisão lê as mudanças da entrega pelos seus caminhos, entre elas os arquivos que a entrega criou, e do docs/06 só o trecho desta linha, contra a página e o docs/04.
Um agente somente leitura lê o `git diff` delas, em stage e fora dele, e abre cada arquivo que a entrega criou, que a sessão cita, já que os escreveu: um arquivo novo é não rastreado, um que o git ainda não guarda, então o `git diff` não mostra nada dele até ele entrar em stage, e o `/apply` só põe em stage depois da revisão.
A revisão do host as lê do seu jeito, mantida nesses caminhos.
Os arquivos de outra sessão na mesma pasta, os que ela criou incluídos, não são desta revisão (capítulo 19).
O revisor traz o que a releitura de quem escreveu não tem, um contexto livre do raciocínio que escreveu a mudança, e mede a mudança contra a página e o docs/04.

O revisor aponta candidatos, defeitos de que suspeita, e não corrige nada ele mesmo.
Um candidato que quebra a página, o docs/04 ou o texto que esta entrega escreveu é corrigido nesta sessão, e a verificação roda de novo.
Todo o resto, um defeito em código que a entrega não tocou ou um desejo que a página não pediu, vira uma linha `[ ]` na fila, porque a página é o escopo.
O revisor fica somente leitura porque a sessão que construiu a mudança sabe por que fez cada escolha, então é essa sessão que faz a correção, e a mudança tem um só autor.

A sua revisão e o seu commit continuam vindo depois dela: ela é uma checagem a mais antes de você ler o diff.
E ela lê uma entrega enquanto essa entrega está aberta, enquanto a revisão de marco lê juntas as entregas do marco ([capítulo 15](15-closing-a-milestone.md)).

### Verde não é pronto

A verificação diz que o código faz o que os testes dele dizem.
Ela não diz nada sobre se a página foi atendida, se os documentos ainda valem, ou se alguém vai conseguir saber depois o que aconteceu.
Então, antes de parar, o `/apply` faz tudo isto:

* Escreve na página o que aconteceu: o que divergiu do plano e por quê, o que foi deixado de lado, o que a prova achou, o que a revisão da entrega achou e o que foi feito de cada candidato, e as decisões tomadas, com um ADR se foi preciso um.
* Atualiza os documentos que a entrega mudou: um termo novo no docs/03, uma regra nova no documento que é dono dela, uma decisão em docs/adr/.
* Quando a entrega acrescenta ou muda algo que uma pessoa faz à mão, como publicar o app, escreve ou atualiza o manual dele em `docs/manuals/` ([capítulo 7](07-the-documents.md)).
* Marca cada item do Pronto quando.
* Move a página para `work/done/`; uma linha `[?]` que espera só por esta, ou por linhas já `[x]`, volta pela fase de retomada ([capítulo 14](14-queue-states.md)).
* Coloca em stage só os caminhos e trechos desta entrega, nunca com `git add -A` ou `git add .`, e avisa o que outra pessoa já tinha colocado em stage, sem tirar do stage.
* Termina a página com a mensagem de commit sugerida em um bloco `commit`, no formato que o docs/05 define, e mostra o mesmo bloco na conversa, onde um bloco cercado fica à parte do resto da resposta. Há um bloco só: um `/apply` retomado substitui o anterior.
* A sua última edição marca a linha como `[x]` no docs/06 e coloca esse trecho em stage, depois de todo o resto estar em stage, então uma linha `[x]` sem nada em stage é uma sessão que parou antes da hora.
* As últimas palavras dele são os seus próximos passos: revisar o diff em stage, fazer o commit (e o merge, em um branch da entrega), e pegar a próxima linha da fila, com o comando escrito como o seu host o invoca, em uma sessão nova, para que uma pessoa nova no kit não procure na documentação o que vem depois. A última coisa que diz é qual ambiente está em qual versão e o comando que atualiza os outros, e ele nunca termina calado sobre isso.

Pronto é a revisão e essa lista inteira.

## `emprestar-livro`, construída

Pegue a página `emprestar-livro` do capítulo 12, revisada e marcada `[>]`, e abra uma sessão nova com `/apply emprestar-livro`.

O agente lê a página, depois o docs/01 para saber que os empréstimos ficam em `src/features/emprestimos/`, o docs/04 para saber quais testes cada peça recebe (capítulo 5), e o docs/05 para saber que a verificação é `npm run verify` e que uma tela é provada por um screenshot.
Ele escreve a migration da tabela `emprestimo` com o seu índice único, a regra `emprestar` como uma função pura que devolve um `Result` (capítulo 3), a chamada do repositório que transforma a falha do índice único na recusa `JaEmprestado`, o orquestrador e a tela de empréstimo.
Cada linha de Comportamento vira um teste: o empréstimo com a data de devolução 21 dias depois, a recusa para um livro atrasado, a recusa para um membro suspenso, o empréstimo para um membro cujo único livro vence hoje, e, contra um banco de dados real em memória, o segundo de dois empréstimos do último exemplar recusado.
Ele não constrói nada para devolver um exemplar, reservas ou multas, porque o Fora do escopo os nomeou.

Se o docs/00 dissesse que um empréstimo dura 14 dias, o agente pararia naquela linha e perguntaria qual é a verdade: os 21 da página ou os 14 do documento.
Qualquer que seja a sua resposta, o outro muda na mesma entrega.

Ele roda `npm run verify` até ficar verde, captura a tela de empréstimo com 390 e 1280 pixels de largura, e compara as duas com o arquivo de design.
Se um botão quebra linha na largura estreita, ele é corrigido; se o arquivo de design não dá um valor para uma cor, a escolha é registrada como uma divergência, com o seu motivo.

Depois um agente somente leitura lê os arquivos que a entrega criou, a migration e tudo em `src/features/emprestimos/`, e o `git diff` do que ela editou, contra a página e o docs/04, em uma revisão também escrita para este capítulo, e aponta dois candidatos.
O primeiro rascunho de `inserirEmprestimo` transformava toda falha da escrita em `JaEmprestado`, enquanto o docs/04 da biblioteca guarda a fronteira do capítulo 3: a falha do índice único vira `JaEmprestado`, e qualquer outra falha da escrita continua `BancoDeDadosFalhou`.
Nenhum teste dispara isso, já que nos testes só o índice único falha, e está no texto que esta entrega escreveu, então o agente restringe a captura ao erro do índice único e roda a verificação de novo; a chamada do repositório que os capítulos 3 e 4 descrevem é a corrigida.
`inserirEmprestimo` fica em um arquivo que esta entrega criou, então uma revisão só do `git diff` não teria lido nada dele.
O segundo candidato: a recusa para um membro suspenso não diz até quando.
A página nunca pediu isso, então vira a linha `fim-da-suspensao`, posta na fila abaixo de `devolver-livro`, que continua sendo a próxima linha livre.
Então ele escreve na página o que aconteceu, com os dois candidatos e o que foi feito de cada um, acrescenta a tabela `emprestimo` ao documento que lista o schema, marca o Pronto quando, move a página para `work/done/emprestar-livro.md`, coloca em stage só os caminhos desta entrega e, como a sua última edição, marca a linha `[x]` e coloca em stage esse trecho do docs/06.
Se uma edição de outra sessão em `src/features/membros/` está na árvore, ou se o trecho dela do docs/06 já está em stage, o agente deixa os dois como estão e avisa você do que está em stage (capítulo 19).

A página termina com a mensagem sugerida, escrita para este capítulo, e a conversa mostra o mesmo bloco:

```commit
Emprestar um exemplar a um membro

- Cria a tabela emprestimo, um aberto por exemplar por índice único
- Empresta por 21 dias; recusa livros atrasados e membros suspensos
- Recusa o segundo empréstimo do último exemplar como JaEmprestado
- Prova a tela de empréstimo com 390 e 1280 pixels de largura
- Lista a tabela emprestimo no documento do schema

work/done/emprestar-livro.md
```

Depois ele dá os seus próximos passos:

1. Revise o diff em stage: `git diff --staged`.
2. Faça o commit com a mensagem sugerida: `git commit`, e cole o bloco.
3. A próxima linha livre da fila é `devolver-livro`; em uma sessão nova, rode `/propose devolver-livro` no Claude Code, ou `$propose devolver-livro` no Codex (a tabela do capítulo 8).

E termina, por último, nos ambientes, com uma frase também escrita para este capítulo: "O banco de dados de desenvolvimento já tem a migration desta entrega; o ambiente de staging ainda está na entrega anterior, e `npm run migrate -- staging` o atualiza."
Se uma sessão termina sem essa frase, ela não terminou como o kit diz; peça a frase a ela.
Na Ninjobs, uma pessoa que abriu o site publicado achando que ele estava atual, depois de uma sessão que terminou sem essa frase, revisou uma versão que não tinha a entrega.

## Por que ele para no stage

O `/apply` nunca faz commit e nunca faz merge, qualquer que seja a estratégia de git.
Ele coloca em stage só a sua entrega e entrega a mensagem a você; o commit é seu, e vem depois da sua revisão.
O documento de processo do kit dá o fluxo em uma linha: o `/apply` "*constrói, prova, atualiza os documentos, coloca em stage e sugere o commit, nunca faz commit*".

## Revise a mudança em stage

A mudança em stage é o que o agente diz que fez; a sua revisão confere que ele fez.
Leia a mudança contra a página:

* Cada linha de Comportamento foi atendida, cada uma pelo seu teste ou por uma checagem registrada?
* Foi construída alguma coisa que a página não pediu: um arquivo, uma dependência, uma camada?
* A verificação e a prova ficam verdes para você?
* Os documentos que a entrega mudou foram atualizados, e só eles?
* O diff em stage tem só esta entrega, e o agente avisou o que já estava em stage?
* A mensagem sugerida no bloco `commit` no fim da página está certa: o assunto, os tópicos, a última linha?
* O que a revisão da entrega achou, e cada candidato foi corrigido ou virou uma linha `[ ]`?

Se a página não registra revisão nenhuma e o slot do docs/05 nomeia uma, a entrega não terminou como o kit diz; peça a revisão ao agente.
Leia também o que aconteceu, e pergunte-se se você teria decidido alguma divergência de outro jeito.
Peça cada correção ao agente, na mesma sessão, nunca à mão.
A mesma sessão guarda o raciocínio da construção: ela sabe por que fez cada escolha, o que uma sessão nova teria de adivinhar.
Isso vale para o gosto tanto quanto para os defeitos: quando o código funciona mas você o teria escrito de outro jeito, diga o que quer no lugar e por quê, em vez de reescrevê-lo você mesmo.
Uma preferência que deve valer além desta entrega vai para onde a próxima sessão a lê, uma convenção no docs/04 ou uma decisão com o seu motivo em um ADR, escrita nesta mesma entrega.
Seja qual for a memória que o seu host guarda por conta própria, a memória que todo host e todo colega leem são os documentos do projeto.
Na minha experiência, no começo de um projeto o agente muitas vezes faz coisas que não combinam com o gosto ou as necessidades do time; dizer uma vez, para que vá parar em um documento, me custou menos do que corrigir a mesma coisa à mão em toda entrega.
Trate o agente como um novo membro do time: você explica uma vez o que o time quer, em um lugar onde ele pode ler de novo.

Uma pessoa que faz commit depois de muitas entregas boas para de conferir, e toma a palavra do agente no lugar da própria leitura.
Isso é o viés de automação, definido e medido no capítulo 24, e esta revisão o combate de quatro jeitos.
Ela é um conjunto de perguntas respondidas contra uma página que você já leu, não uma olhada no diff.
O registro do que aconteceu, na página, mostra onde o agente decidiu sozinho, então você sabe onde olhar.
Uma página mantém a mudança pequena o bastante para ser lida inteira.
E a verificação e a prova rodaram antes de você olhar, então a sua atenção vai para onde nenhuma checagem chega.

## O commit é a revisão humana

O agente coloca em stage e sugere a mensagem; a pessoa lê o diff e faz o commit.
Três motivos sustentam essa linha.

* **Nada chega ao histórico sem ser lido por uma pessoa.** Um commit diz que uma pessoa leu a mudança e a aceita; um agente que faz commit do próprio trabalho pula o único leitor que consegue dizer que a construção é o que se queria.
* **Um commit se desfaz em um passo.** A página e a sua construção são um commit no trunk (direto na linha principal do histórico), um merge em um branch (uma linha de trabalho à parte, juntada depois à principal), então uma entrega que se mostra errada sai do projeto com um comando (capítulo 18).
* **A pessoa é dona do que é publicado.** O agente escreveu o código, e a pessoa responde por ele ao time, ao cliente e ao usuário; o commit é onde essa resposta é dada.

Leia o diff em stage, depois faça o commit:

```
git diff --staged
git commit
```

Sem `-m`, o git abre o seu editor para a mensagem; copie-a do bloco `commit` no fim da página, cole, salve e feche, e o commit existe quando o editor fecha.
A página guarda a mensagem e a conversa só a repete, então você pode fazer o commit na manhã seguinte, em outra janela, e ainda achá-la.

Quando outra sessão trabalha na mesma pasta, faça o commit de uma entrega por vez, a partir do índice, quando o `git diff --staged` tiver só aquela entrega (capítulo 19).

### A mensagem

O formato é o que o docs/05 define, e o kit escreve o mesmo em todo projeto:

```
<assunto no infinitivo, até 72 caracteres>

- <um destaque, uma linha>
- <até cinco deles>

work/done/<slug>.md
```

O assunto diz o que a entrega faz, no infinitivo, como uma ordem, "Emprestar um exemplar a um membro" e não "Emprestou" nem "Emprestando", com um escopo entre parênteses quando ajuda.
Os tópicos são os destaques, nunca o raciocínio.
A última linha aponta para o caminho real da página, onde o raciocínio mora, então quem lê o histórico acha a decisão inteira em um arquivo: `work/done/<slug>.md` quando a entrega está pronta.

Um `/apply` travado escreve uma mensagem parcial no mesmo formato.
Ela diz que é parcial e nomeia o que trava, nunca dá a entender que a verificação passou ou que a entrega está pronta, e a sua última linha é `work/<slug>.md`, onde a página espera.

Se o seu agente responde com linhas de `git commit -m` e nenhum bloco `commit` na página, a entrega não terminou como o kit diz; peça o bloco a ele.

## O que o time ganha

Nada é publicado sem uma checagem e uma pessoa: a verificação e a prova conferem a construção, e uma pessoa lê o diff antes de ele existir no histórico.
Um defeito que uma entrega escreveu é achado por um leitor que não o escreveu, e corrigido nessa entrega, antes de você ler o diff.
E o que divergiu do plano fica escrito onde a próxima pessoa lê: na Ninjobs, a página da entrega que permite a um usuário excluir a própria conta dizia que a tabela que registra uma exclusão pendente não teria regra de escrita nenhuma, e a construção descobriu que uma tabela sem regra de escrita não aceita escrita de ninguém, nem das funções do próprio banco de dados.
Então a página registrou o ajuste, nenhum caminho de escrita alcançável pelo cliente, o que o teste das regras de acesso agora prova, e o commit que a publicou aponta para essa página.

## Pontos-chave

* O `/apply <slug>` constrói a página em uma sessão nova e segue o docs/05 ao pé da letra: a página é o escopo, sem dependência, camada ou ferramenta que ela não nomeou, e quando a página contradiz um documento ele para e diz qual, sem nunca resolver em silêncio.
* Ele marca a linha como `[*]` com a sua primeira edição, `[x]` com a última, depois do stage, e `[?]`, com o que ela espera, quando precisa parar.
* Verde não é pronto: pronto é a lista inteira, da revisão por um contexto que não escreveu a mudança à linha marcada `[x]`.
* Ele termina a página com a mensagem sugerida em um bloco `commit` e mostra o mesmo bloco na conversa, também quando para travado; as últimas palavras dele são os seus próximos passos, cada comando escrito por extenso, e, por último, qual ambiente está em qual versão e o comando que atualiza os outros.
* Revise a mudança em stage contra a página, peça cada correção na mesma sessão, dizendo o que quer no lugar e por quê, e faça você o commit: essa revisão é a defesa contra o viés de automação, o hábito de confiar no agente depois de muitas entregas boas.

[^huang-2024]: Jie Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet", 2024. <https://arxiv.org/abs/2310.01798>
