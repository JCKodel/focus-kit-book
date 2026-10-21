# 12. `/propose`: uma página

Depois deste capítulo você consegue transformar uma linha da fila em uma página com o `/propose`, ler a página como o registro do que o agente entendeu e do que o `/apply` vai construir, cobrir os buracos dela por conversa antes de existir qualquer código, e dividir uma entrega que não cabe em uma página.
Você sabe que o `/propose` decide o que os documentos do projeto já respondem, nomeando a fonte na página, e rascunha as linhas de Comportamento com o que precisa falhar e os casos de borda, então o seu trabalho é corrigir a página, não escrevê-la.
Você também consegue explorar um problema que ainda não entende conversando com o agente, antes de existir uma página.

## O problema

Um agente que planeja e constrói no mesmo fôlego toma as decisões no meio da construção, onde você não as vê.
O que você não decidiu, ele decide por você, de um jeito plausível, e você encontra o palpite quando um usuário o encontra.
A página põe cada decisão onde você consegue lê-la antes de existir qualquer código, e corrigi-la ali custa um turno de conversa.

## O que é uma entrega

Todo trabalho em um projeto com o focus-kit é uma entrega: a menor mudança que tem valor, o que outros métodos chamam de tarefa ou item de trabalho.
Ela tem como nome um slug (o nome curto da entrega), palavras minúsculas unidas por hífens, como `emprestar-livro`, escrito uma vez na linha da fila e usado dali em diante para tudo o que é dela: a página `work/<slug>.md`, o argumento do `/propose <slug>` e do `/apply <slug>`, e a última linha do commit que a fecha.
Uma entrega cabe em uma página.
Se não cabe, o escopo ainda não foi entendido, e são duas entregas.

## O que o `/propose` faz

O `/propose <slug>` conversa com você até o escopo caber em uma página, e o que os documentos do projeto já respondem, ele não pergunta: o arquivo do comando no kit manda decidir, escrever a decisão na página e nomear o documento de onde ela veio, então, se o documento estiver errado, você corrige uma vez, na revisão, em vez de responder a mesma pergunta duas vezes.
Ele só pergunta onde os documentos deixam mais de uma leitura e nenhum a fecha: primeiro a avaliação dele, em prosa, e a recomendação dele primeiro em cada pergunta.

Para decidir, ele lê antes de perguntar: o docs/00 para o produto e as suas regras, o docs/03 para as palavras que a página precisa usar, o docs/05 para os slots do projeto e o formato da página, o docs/06 para o que vem antes e depois da linha, `work/` para as entregas em andamento, e o docs/01 para onde a mudança mora no código.
Em uma linha que já está `[?]`, ele diz o que a linha espera e só segue quando você diz que está resolvido; em uma linha cujo `after` nomeia uma linha que ainda não está `[x]`, ele diz o mesmo e não começa, e assim em uma linha cujo token tem `-` primeiro, `(-A)` ou `(--)`, enquanto uma linha acima dela ainda não está `[>]` ou além (capítulo 14).
No trunk ele lê essas marcas na fila da pasta onde a sessão roda; com um branch ou um worktree por entrega, a fila do branch principal, onde ele roda e de cujo `HEAD` parte o worktree da entrega, mostra cada linha como estava até o merge dela, então ele lê a própria linha e cada linha que o seu `after` nomeia e, quando o seu token espera, toda linha acima dela no branch daquele slug, local ou remoto, com as linhas que só um branch tem, reconciliadas pelo slug, e depois de um `git fetch` uma linha cujo branch existe está ocupada, mostre o que mostrar a fila do branch principal (capítulo 14).
Em uma linha que ele pode começar, ele primeiro se coloca onde o slot Git do projeto põe a entrega: no trunk, a pasta onde a sessão roda, sem nada a criar; nos outros casos, o branch ou worktree com o nome do slug, com o remoto consultado antes por esse branch, já que um branch que já está lá quer dizer que a linha está ocupada, depois criado, com o seu branch enviado na hora, antes de a página existir, então a linha fica ocupada em todo clone, ou reutilizado quando a definição é retomada, com o rascunho da página deixado para o slug trazido para ele (capítulos 18 e 19).
A primeira edição dele ali marca a linha como `[~]` na fila, então quem a lê vê uma entrega sendo definida, e fora do trunk a marca e a página vão com o branch da entrega, onde o `/apply` constrói e o merge as leva.
Só quando a página, `work/<slug>.md`, está completamente definida, não apenas escrita, a marca vira `[>]`: uma página escrita enquanto uma questão de escopo ainda está sendo conversada deixa a linha dela `[~]` (o capítulo 14 diz quando uma página está completa).
Com a página escrita, ele julga o token da linha por ela, o que a página tira das páginas acima e em que arquivos o Contrato mexe, e corrige o token na linha quando ela diz outra coisa, dizendo isso (capítulo 14).
Ele termina mostrando essa linha da fila, `[>] emprestar-livro ...` para a página abaixo, e pedindo que você leia e questione a página, e depois rode o `/apply` em uma sessão nova.
Quando descobre, enquanto define, que o escopo espera uma resposta que ninguém deu ainda ou outra linha que precisa ser feita antes, ele escreve a página até onde ela vai e marca a linha como `[?]` no lugar, com `· resume: propose` e o que ela espera.
Ele nunca escreve, edita nem gera código, migration, teste ou configuração.
O README do kit dá o motivo: "*O escopo não cresce durante a implementação porque quem decidiu não está na sala.*"
O `/apply` começa em uma sessão nova, com o contexto limpo, e a página é tudo o que ele leva desta conversa, então a página precisa guardar tudo de que a construção precisa.
O próprio `/propose` roda onde você escolhe: na conversa que pediu a mudança, que guarda o que foi dito ali, ou numa sessão nova, que parte dos documentos e do rascunho da página, quando há um (capítulo 11); nos dois casos, o que só a conversa trouxe vai para a página, e você lê e corrige a página na sessão que a escreveu, antes do `/apply`.

## A página

O formato é fixado no §3 do docs/05 do projeto e é o mesmo em todo projeto:

* **Objetivo.** Uma frase: o que o usuário consegue fazer depois.
* **Comportamento.** Cenários verificáveis na linguagem do usuário, cada um uma ação com uma entrada concreta e o resultado que o usuário vê, incluídos os casos que precisam falhar e os casos de borda; cada linha vira um teste ou uma checagem manual. O `/propose` os rascunha a partir dos documentos, e você os corrige em vez de escrevê-los.
* **Contrato.** Dados, schema, API, formatos de mensagem, ou "nenhum".
* **Estados.** Vazio, carregando, erro, offline, uma linha cada, ou "os padrões"; só quando há uma tela.
* **Referência visual.** Onde está o design, e os tamanhos de tela; só quando há uma tela.
* **Fora do escopo.** O que não entra, com meia linha de motivo cada.
* **Pronto quando.** Uma lista mecânica: os testes passam, a verificação está verde, o screenshot confere.

Esta é uma página para a biblioteca de empréstimos da Parte I, escrita para este capítulo:

```markdown
# emprestar-livro

**Objetivo.** Um bibliotecário registra que um membro pegou um exemplar
emprestado, e o sistema recusa quando as regras dizem não.

**Comportamento.**
* Um membro sem livros atrasados pega um exemplar disponível, e o exemplar
  aparece como emprestado a ele, com data de devolução 21 dias depois
  (docs/03).
* Um membro com um livro atrasado é recusado com "Devolva primeiro os seus
  livros atrasados"; nada é registrado.
* Um membro suspenso é recusado com "A sua matrícula está suspensa"; nada
  é registrado.
* Dois bibliotecários emprestam o último exemplar no mesmo momento: um
  consegue e o outro vê "Este exemplar acabou de ser emprestado a outra
  pessoa".
* Um membro cujo único empréstimo vence hoje pega um exemplar disponível:
  vencer hoje ainda não é estar em atraso.

**Contrato.**
Tabela `emprestimo`:
* `exemplar_id`, `membro_id`: texto, não nulo.
* `emprestado_em`, `devolver_em`: texto, uma data como `YYYY-MM-DD`, não
  nulo.
* `devolvido_em`: texto, uma data como `YYYY-MM-DD`, nulo enquanto o
  exemplar está fora.
Índice único em `exemplar_id` onde `devolvido_em` é nulo: um empréstimo
aberto por exemplar, e um exemplar cujo empréstimo foi devolvido pode ser
emprestado de novo.
`emprestar(exemplar, membro, hoje):
Result<Emprestimo, RecusaDeEmprestimo>` com `RecusaDeEmprestimo =
"TemLivrosEmAtraso" | "JaEmprestado" | "MembroSuspenso"`.

**Estados.** Os padrões.

**Referência visual.** A tela de empréstimo no arquivo de design, com 390
e 1280 pixels de largura.

**Fora do escopo.**
* Devolver um exemplar: uma entrega própria, `devolver-livro`, a seguinte
  na fila.
* Reservas: não estão no docs/00.
* Multas: o docs/00 as lista como uma decisão em aberto, então ninguém
  decide isso aqui.

**Pronto quando.**
* [ ] Os testes unitários de `emprestar` provam a data de devolução 21
  dias depois, a recusa de um membro com um livro atrasado e de um membro
  suspenso, e que um empréstimo que vence hoje não conta como atraso.
* [ ] Os testes de `emprestimoPedido`, com repositórios falsos, provam
  que um empréstimo é salvo e o seu estado é `Emprestado`, e que cada
  recusa, incluída `JaEmprestado` vinda de `inserirEmprestimo`, dá
  `Recusado` levando essa recusa; para o membro com um livro atrasado e
  o suspenso, nada chama `inserirEmprestimo`.
* [ ] O teste do repositório, com as migrações reais, prova que o
  primeiro empréstimo aberto de um exemplar é salvo e que um segundo
  devolve `JaEmprestado`, e que um exemplar cujo empréstimo foi devolvido
  é emprestado de novo.
* [ ] Testes ponta a ponta provam que um exemplar emprestado mostra o
  membro e a sua data de devolução, e que cada recusa mostra a sua
  mensagem: "Devolva primeiro os seus livros atrasados.", "A sua
  matrícula está suspensa." e, com um empréstimo aberto do exemplar já
  salvo, "Este exemplar acabou de ser emprestado a outra pessoa."
* [ ] `npm run verify` está verde.
* [ ] A tela de empréstimo confere com o design nas duas larguras.
```

Leia a página como o relato do agente sobre o que ele entendeu.
Cada linha de Comportamento pode ser conferida; o Contrato é exato; o Fora do escopo nomeia o que alguém poderia ter suposto que estava dentro; o Pronto quando é uma lista que uma máquina ou uma pessoa consegue marcar.
O Pronto quando também diz qual teste do capítulo 5 prova cada linha de Comportamento: as regras nos testes unitários de `emprestar`, que uma recusa não salva nada nos testes do orquestrador, a disputa pelo último exemplar no teste do repositório, e o que a tela mostra nos testes ponta a ponta.
A disputa é do repositório: dois bibliotecários no mesmo instante só se encontram no banco, e nenhuma função pura os vê.
Cada decisão tirada de um documento o nomeia: os 21 dias vêm do docs/03, e as reservas e as multas do Fora do escopo vêm do docs/00.
O agente rascunhou os casos que precisam falhar e o caso de borda: o Contrato já tinha `MembroSuspenso`, então um membro suspenso ganha uma linha, e uma regra sobre livros atrasados implica o dia em que um empréstimo vence, que ainda não é atraso.

O Contrato é a única seção que precisa ser exata.
O motivo do kit: "*uma tela errada se corrige numa sessão, uma coluna errada é uma migration, e uma regra de acesso errada já vazou*".
Uma tela é código que você reescreve; uma coluna guarda dados, e mudá-la exige mover os dados que já estão lá; uma regra de acesso decide quem lê o quê, e uma errada já deixou dados saírem antes que alguém releia a página.
Nenhuma correção posterior desfaz a terceira.
Por isso o Contrato acima dá a cada coluna o seu tipo e se ela pode ser nula, as datas como texto, como o `hoje` do capítulo 3, e a regra do índice em palavras: ele guarda só os empréstimos abertos.

## Leia a página antes do `/apply`

A página é escrita para ser lida, e as perguntas a fazer são estas:

* Cada linha de Comportamento pode ser conferida, como teste ou à mão?
* O Comportamento inclui o que precisa falhar e os casos de borda?
* O Contrato é exato, até os nomes e os tipos?
* O Fora do escopo nomeia algo que você supôs que estava dentro?
* Cada decisão tirada de um documento o nomeia, e você concorda com ela?
* Você discorda de alguma escolha que o agente fez por conta própria?
* O Pronto quando lista o que faria você dizer "pronto", e nada mais vago?

Você pede cada correção na mesma conversa, e o agente escreve a correção: na página, e em qualquer documento que ela toque.
Você não edita a página à mão: o agente sabe qual documento é dono de cada fato, então uma correção que toca o vocabulário ou a fila entra lá também, e a conversa guarda o motivo.
Se o `/propose` pergunta o que um documento já diz, como quantos dias dura um empréstimo quando o docs/03 diz 21, diga isso na conversa: a resposta pertence à página, com a sua fonte.
Se o Comportamento só tem o caminho feliz, um exemplar disponível emprestado a um membro em dia, peça ao agente os casos que precisam falhar e os casos de borda antes do `/apply`: uma pessoa que não conhece a ferramenta sendo construída e deixa o resultado esperado para o agente recebe uma solução, só o caminho feliz, que o cliente rejeita.

A ordem é a barata.
Um buraco achado na página custa um turno; achado depois do `/apply`, custa outro `/apply`, o comando mais caro, que constrói, testa e prova de novo.
No Ninjobs, a página da entrega que calcula a pontuação de compatibilidade de um candidato descobriu, enquanto era escrita, que a idade aproximada de um candidato já vazava no primeiro nível de privacidade pelas datas das suas experiências; isso virou uma linha para uma entrega posterior, e nenhum código foi escrito além dela.

Os hosts têm o seu próprio jeito de planejar dentro de uma sessão, como o modo de plano (plan mode) do Claude Code, em que "*o Claude lê arquivos e propõe um plano, mas não faz nenhuma edição até você aprovar*";[^claude-code-plan-mode] a página é o que sobrevive à sessão: um arquivo no repositório, escrito a partir dos documentos do projeto e com as palavras deles, marcado na fila, lido por uma sessão nova para construí-lo, e guardado em `work/done/` com o que aconteceu.

## Quando não cabe

Um escopo que não cabe em uma página são duas entregas: o `/propose` diz isso, propõe a divisão e escreve só a primeira página, e a segunda vira uma linha na fila, onde ela pertence.
No Ninjobs, a linha única da fila para uma vaga de emprego virou seis entregas em um `/propose`: a vaga, o empregador, as tags, a oferta, os benefícios e os idiomas, e o ciclo de vida; a página da primeira dizia que ela era o passo um de seis.
Cada uma das seis foi revisada na sua própria página e construída na sua própria sessão.

## Quando você ainda não sabe

Alguns escopos não cabem em uma página porque ninguém sabe a resposta ainda: como uma API desconhecida se comporta, ou qual de duas abordagens se sustenta.
Outros métodos chamam o trabalho que descobre isso de spike; aqui ele é uma conversa com o agente, em qualquer sessão, antes de qualquer página.
O agente é um modelo de linguagem com quem você conversa, não um botão que roda um comando fixo, e ele lê os documentos do projeto, então o que ele sugere segue o projeto.
A conversa termina de um de três jeitos: uma linha nova na fila, com um rascunho da página guardando o que a exploração achou quando a linha não o comporta, do qual o `/propose` parte, nessa conversa ou numa sessão nova (capítulo 11); uma decisão que você aceita, escrita no documento que é dono dela (capítulo 7); ou nada, quando o que você achou deixa o plano como está.
Nos meus projetos isso foi raro, e a conversa sempre bastou, então nenhuma marca, comando ou tipo de entrega foi acrescentado para isso: nenhum nomearia um erro que tivesse pegado, que é o regulador do capítulo 16.

## O que o time ganha

A página é a superfície de revisão do time.
Um desenvolvedor, um gerente ou o cliente lê uma página na linguagem do docs/03 e sabe o que está para ser construído, o que não está, e o que "pronto" vai significar, antes de existir uma linha de código.
No Caso A, o mesmo formato de página levou perguntas ao cliente e documentos para a passagem do projeto, então todo tipo de trabalho foi revisado do mesmo jeito, lendo a sua página (capítulo 21).
E quando a construção termina, a mesma página registra o que aconteceu, então a história de uma decisão é um arquivo, com o nome do seu slug, em todo projeto que o time roda.

## Pontos-chave

* Uma entrega é a menor mudança com valor, com um slug como nome, e cabe em uma página; se não cabe, são duas.
* O `/propose` decide o que os documentos respondem e nomeia a fonte na página, só pergunta onde eles deixam mais de uma leitura, com a recomendação primeiro, espera como o `after` e o token da sua linha dizem, julgando-os, fora do trunk, pelo branch de cada slug, começa no branch ou worktree da entrega, onde o slot Git do projeto põe um, enviando o seu branch no momento em que o cria, a reivindicação da linha, ou no trunk na pasta onde a sessão roda, e marca a linha `[~]` ali enquanto conversa e `[>]` quando a página está completamente definida, corrigindo o token pela página, ou `[?]` quando o escopo espera, e nunca escreve código.
* A página tem um formato fixo e é a superfície de revisão do time, para código e para qualquer outra coisa que caiba em uma página; o Contrato é a única seção exata, porque uma coluna errada é uma migration.
* O `/propose` rascunha o Comportamento, incluídos o que precisa falhar e os casos de borda; você lê a página antes do `/apply`, na sessão que a escreveu, e a corrige pedindo ao agente, nunca à mão: um buraco na página custa um turno, depois do `/apply` custa outro `/apply`.
* Quando ninguém sabe a resposta ainda, explore-a conversando com o agente, e termine com uma linha na fila, com um rascunho da página quando a linha não comporta o que você achou, uma decisão escrita onde ela pertence, ou nenhuma das duas; nada novo é preciso para isso.

[^claude-code-plan-mode]: Anthropic, "Common workflows", documentação do Claude Code, seção "Plan before editing", acesso em 2026-09-28. <https://code.claude.com/docs/en/common-workflows#plan-before-editing>
