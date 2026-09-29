# Fechando um marco

Depois deste capítulo você consegue fechar um marco: conferir o parágrafo dele no produto rodando, revisar tudo o que ele construiu com o que o seu host oferece e decidir cada achado.
Depois você consegue transformar os achados confirmados em linhas de um marco novo, `<M>.1`, em vez de correções.

## Por que revisar o todo

Cada página de um marco foi lida antes de o `/apply` construí-la, e cada mudança no stage foi revisada antes do commit dela.
Ninguém olhou o que elas somam.
O kit fecha essa brecha em uma regra, o §8 do documento de processo que ele escreve, o docs/05, como ele diz desde o commit `bff8414` do focus-kit.
A última linha de todo marco é a revisão dele, `<milestone>-review`, uma entrega como as outras: o `/propose` escreve a página dela, e o `/apply` a roda.
Ela confere o parágrafo do marco cláusula por cláusula contra o que as entregas construíram, e revisa o código com o que o host oferece.
Ela não corrige nada.
Cada achado confirmado vira uma linha `[ ]` em um marco novo logo depois do revisado, numerado com `.1` (o marco 1 é seguido pelo 1.1), que termina com a sua própria revisão; um achado nunca é uma correção no meio do marco seguinte.
Um processo leve não tem portão entre as entregas, então o risco que ele carrega é a soma: cada entrega certa na sua página, e o todo errado.

Esse olhar é a revisão de marco: o parágrafo do marco conferido no produto, depois uma revisão de tudo o que o marco construiu.
Cada problema que ela aponta é um achado, e você o confirma ou o rejeita.

A página da revisão, escrita pelo `/propose m1-review` para um marco 1, diz o que olhar: o intervalo de commits do marco, o parágrafo dele e o comando de revisão do host com o seu nível.
O `/apply m1-review` confere o parágrafo cláusula por cláusula, roda a revisão e para ali, porque as decisões sobre os achados são suas.
A revisão do marco 1 da clínica rodou antes de o kit fazer da revisão uma linha do marco, e por isso o marco 1 da clínica não tem essa linha: eu a rodei sem interface, fora de qualquer entrega.
Os passos dela são os que o `/apply` roda, nas duas próximas seções; as decisões depois deles são suas nos dois casos.

## Confira o parágrafo

O marco 1 da clínica fechou com sete commits, do `skeleton` ao `cancel-appointment`, cada página e cada mudança no stage revisadas por mim antes do commit.[^clinic-milestone-1-run]
Este é o parágrafo dele, do docs/06 da clínica; o original está em inglês, e aqui vai traduzido:

```
Quando ele fecha, o dono consegue cadastrar profissionais e os horários semanais deles,
um cliente consegue agendar um horário livre, e um cliente consegue cancelar até 24 horas antes.
```

O [capítulo 9](09-queue-and-milestones.md) escreveu esse parágrafo como um teste que uma pessoa consegue conferir no produto, então confira.
Em um banco limpo, rode `npm run setup` e `npm run dev`, e tente cada afirmação uma vez, do começo ao fim, na ordem em que o dono e um cliente as encontrariam.
A conferência de cada entrega testou a sua parte; esta roda todas juntas, como o produto é usado.
Eu a fiz antes da revisão:[^closing-a-milestone-run]

* O dono cadastra profissionais: valeu.
* O dono define os horários semanais deles: valeu.
* Um cliente agenda um horário livre: valeu.
* Um cliente cancela até 24 horas antes: valeu.

Uma afirmação que não vale é um achado como qualquer outro, e vai para as decisões abaixo junto com os da revisão.
Nenhuma falhou aqui.

## Revise tudo o que o marco construiu

No Claude Code a revisão é o `/code-review`.
Sem alvo, ele revisa os commits do branch à frente do upstream mais as mudanças sem commit, o que, em um `main` já enviado, é nada.[^claude-code-review]
Ele também aceita um alvo: o caminho de um arquivo, o número de um PR, o nome de um branch ou um intervalo de refs.[^claude-code-review]
O intervalo do marco começa no último commit antes dele, `3f0b47c`, e termina no último dele, `f16f83b`:

```
/code-review high 3f0b47c...f16f83b
```

Com três pontos, o git compara o segundo commit com o ponto onde as duas histórias se encontram; como `3f0b47c` é ancestral de `f16f83b`, isso é exatamente os sete commits do marco.
O nível troca cobertura por confiança: em `low` e `medium` a revisão aponta só os achados de que tem mais certeza, e de `high` a `max` ela amplia a cobertura e pode incluir achados de que tem menos certeza.[^claude-code-review]
Escolhi `high`: um marco é revisado uma vez, como um todo, então ali a amplitude vale mais, e as decisões da próxima seção filtram o que é incerto.
A revisão só aponta; ela só muda os seus arquivos quando você acrescenta `--fix`, e aqui você não acrescenta.[^claude-code-review]

Outros hosts oferecem o mesmo olhar.
O Codex tem o `/review` em uma sessão e o `codex review --base <branch>` no terminal, que revisam as mudanças contra um branch base.[^codex-review]
O GitHub Copilot revisa pull requests, então ali o marco sobe como um pull request do primeiro commit ao último.[^copilot-review]

Rodei a revisão sem interface, na raiz da clínica, com permissão para rodar só `git diff`, `git log`, `git show`, `git status`, npm e npx, então uma edição teria sido recusada.[^closing-a-milestone-run]
Ela respondeu com dez achados, cada um com um arquivo, uma linha, um resumo e um cenário de falha.
Estes são os dez resumos, na ordem da execução; o original está em inglês e sem números, e aqui vão traduzidos e numerados, para que as decisões abaixo possam se referir a eles; os cenários estão no registro:[^closing-a-milestone-run]

```
1. O índice único parcial em (professional_id, starts_at) só impede dois agendamentos com exatamente o mesmo início. O invariante 2 do docs/03 diz que um agendamento fica quando os horários semanais mudam, então os horários podem se sobrepor em parte a um agendamento existente, e o índice não cobre esse caso, embora o docs/02 diga que um índice no início basta.
2. Uma colisão de código de agendamento no booking_code UNIQUE (as linhas canceladas também contam) é respondida como 500 DatabaseFailed, que o cliente mostra como 'The server cannot be reached', embora o agendamento em si fosse válido.
3. migrate monta a lista de pendentes fora de qualquer trava e depois aplica cada arquivo dentro de um BEGIN adiado, então dois processos que começam juntos (o servidor e o `npm run setup`, que o docs/02 diz que roda na mesma máquina) aplicam a mesma migração.
4. SlotTaken é detectado comparando o texto em inglês da mensagem de erro do SQLite em vez do código de erro e da restrição, o que quebra em silêncio se o SQLite ou o Node mudar a redação ou se o índice ganhar mais colunas.
5. checkTimeZone aceita só os nomes canônicos de Intl.supportedValuesOf, então recusa nomes IANA de ligação válidos que Intl.DateTimeFormat aceita. Isso vai contra o docs/03, onde UnknownTimeZone quer dizer 'não é um nome IANA'.
6. Quando a recarga dos horários depois de um agendamento recusado (SlotTaken) falha, 'Try again' chama loadSlots(professional) sem o argumento `after`, então a mensagem 'no longer free' e a volta para o dia escolhido se perdem.
7. Uma linha vazia entre as linhas de weekly-hours e as novas linhas de slots/appointments parte a tabela Routes, então as três rotas de book-appointment e cancel-appointment não aparecem como linhas da tabela.
8. book() calcula freeSlots duas vezes sobre a janela inteira de 30 dias (uma com booked vazio, outra com ele) só para testar se um instante faz parte.
9. databaseFailed(c) é copiado de novo (ele já existe em session.server.ts, professionals/route.server.ts e weeklyHours/route.server.ts, e signIn/clinic o escrevem no próprio código), e notFound(c) repete weeklyHours/route.server.ts. Isso quebra a regra de abstração do AGENTS.md.
10. minutesOf é uma cópia exata do auxiliar privado em weeklyHours/rules.ts:24. slotsOf (route.server.ts:100) também carrega todos os profissionais ativos para achar um pelo id.
```

Leia-os como afirmações: cada um diz onde olhar, e nenhum foi conferido ainda.
Sete entregas tinham passado nas suas próprias revisões, e o todo ainda guardava uma tabela partida no docs/02, um auxiliar copiado em quatro arquivos e uma nova tentativa que perde a sua mensagem.

## Decida cada achado

Um achado se lê como um fato, e alguns não são.
O [capítulo 6](06-the-documents.md) deu a regra: você é o cérebro da operação, e confere o que o agente escreve com o que você sabe.
Aqui isso quer dizer duas coisas: você nunca toma um achado por verdadeiro sem olhar o código, e nunca descarta um sem dizer por quê.

O agente que roda o `/apply` deste livro leu cada achado contra o código e os documentos da clínica e me deu a sua avaliação; eu a conferi e decidi cada um.
Enviei as decisões para a sessão da revisão com `--continue`, o jeito sem interface de digitar na mesma sessão ([capítulo 7](07-brainstorm.md)); em uma sessão interativa, você as digita na sessão da revisão.
Eu as enviei em um pedido que também pedia as linhas, palavra por palavra; o original está em inglês, e aqui vai traduzido:[^closing-a-milestone-run]

```
As minhas decisões sobre os dez achados:

1. Rejeitado. A rota confere os horários livres e insere sem nenhum await no meio, e a clínica roda um processo de servidor, então nenhum outro agendamento consegue se intercalar; freeSlots já recusa um início que se sobrepõe a um agendamento marcado.
2. Rejeitado. O docs/02 registra isso de propósito: uma colisão responde 500 DatabaseFailed e o "Try again" do cliente sorteia um código novo, sem laço de nova tentativa. Com 31^6 códigos, uma colisão é rara demais para mudar isso.
3. Rejeitado. O docs/01 diz que o npm run setup roda uma vez, antes do npm run dev, então os dois nunca começam juntos em um banco novo.
4. Rejeitado. Os testes do repositório, da rota e das regras cobrem SlotTaken com uma inserção de verdade, então uma mudança na redação do SQLite faz o npm run verify falhar no dia em que acontecer.
5. Confirmado. checkTimeZone recusa nomes IANA como US/Eastern e Etc/UTC, que o docs/03 diz que são aceitos.
6. Confirmado. Depois de um 409 SlotTaken cuja recarga de horários falha, o "Try again" perde a mensagem "no longer free" e a data escolhida.
7. Confirmado. A linha vazia parte a tabela Routes do docs/02.
8. Rejeitado. Duas passadas sobre 30 dias de horários de um profissional não custam nada mensurável no tamanho da clínica.
9. Confirmado. databaseFailed tem quatro cópias e notFound duas, contra a regra de abstração do AGENTS.md.
10. Confirmado para o minutesOf duplicado, contra a mesma regra. Rejeitado para a leitura de todos os profissionais ativos: a clínica tem um punhado.

Não corrija nenhum. Escreva cada achado confirmado como uma linha [ ] no docs/06, no marco a que ela pertence, ou em um marco novo com o seu parágrafo se nenhum servir, e diga onde pôs cada uma e por quê. Depois faça o stage com git add.
```

Cada rejeição nomeia o que a revisão não pesou: uma escolha que o docs/02 registra de propósito, uma ordem que o docs/01 fixa, testes que já guardam o caso, uma escala que a clínica não vai alcançar, uma corrida que precisa de um segundo processo de servidor.
Cada confirmação foi conferida no código antes: o Node recusou `US/Eastern`, a linha 292 do `useBooking.ts` chamava `loadSlots` sem o segundo argumento, a linha vazia estava na tabela.
Um achado pode se dividir, como o décimo: o parser duplicado confirmado, a consulta rejeitada.

## Achados viram linhas

O agente não achou nenhum marco que servisse aos cinco achados confirmados: o marco 1 está fechado, e o seguinte, "o dono comanda o dia", trata de ausências, da agenda do dia e da publicação.[^closing-a-milestone-run]
Então ele acrescentou um marco antes desse, com o seu parágrafo, e renumerou "o dono comanda o dia" como marco 3.
Este é o diff do docs/06 da clínica, como a execução o deixou, em inglês:[^closing-a-milestone-run]

````diff
diff --git a/docs/06-Queue.md b/docs/06-Queue.md
index 760ecff..c729d8b 100644
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@ -18,7 +18,22 @@ a client can book a free slot, and a client can cancel up to 24 hours before.
 [x] cancel-appointment   a client cancels up to 24 hours before, or is told why not
 ```
 
-## Milestone 2: the owner runs the day
+## Milestone 2: what the review of milestone 1 found
+
+When it closes, every confirmed finding of the milestone 1 review is
+settled: setup accepts every IANA time zone name, a refused booking keeps
+its message through a failed reload, docs/02 renders whole, and the code
+repeated across features has one shared copy.
+
+```
+[ ] time-zone-names      setup accepts every IANA name the runtime knows, such as US/Eastern and Etc/UTC, as docs/03 says
+[ ] slot-taken-retry     after a refused booking whose slot reload fails, "Try again" keeps the "no longer free" message and the chosen date
+[ ] routes-table         the Routes table of docs/02 renders whole, with the slots and appointments routes as rows
+[ ] route-errors         one shared databaseFailed and one shared notFound answer; the first copies are in session.server.ts and weeklyHours/route.server.ts
+[ ] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
+```
+
+## Milestone 3: the owner runs the day
 
 When it closes, the owner can record a professional's absences, which remove
 their slots, and sees the day's appointments per professional; and the app
````

O marco novo se chama "o que a revisão do marco 1 achou", e o parágrafo dele diz, traduzido: "Quando ele fecha, todo achado confirmado da revisão do marco 1 está resolvido: o setup aceita todo nome IANA de fuso horário, um agendamento recusado mantém a sua mensagem durante uma recarga que falha, o docs/02 aparece inteiro, e o código repetido entre as funcionalidades tem uma cópia compartilhada".
Pela regra do kit desde o `bff8414`, esse marco novo é o marco 1.1, logo depois do marco 1, e ele termina com a sua própria revisão, `m1.1-review`; "o dono comanda o dia" mantém o número 2, então nada é renumerado.
Quando a clínica atualizou o kit, a fila dela foi renomeada para combinar: o [docs/06 da clínica em `a3e2470`](https://github.com/JCKodel/focus-kit-clinic/blob/a3e2470/docs/06-Queue.md) tem o marco 1.1, que termina com `m1.1-review`, e o marco 2, que termina com `m2-review`.

Cada linha diz o que vai ser verdade, e não como corrigir, e as duas linhas sobre código copiado nomeiam a primeira cópia, como a regra de abstração pede.
Cada uma é uma entrega: o `/propose` vai escrever a página dela e o `/apply` vai construí-la, como qualquer outra.

Uma linha, e não uma correção, porque uma correção feita no meio do marco seguinte não tem página nem revisão.
Ninguém lê o escopo dela antes de ela ser construída, ninguém a confere contra uma página depois, e ela cai em um marco cujo parágrafo não fala dela.
Como linha, ela espera a sua vez e ganha as duas.

Pedi à mesma sessão a mensagem de commit de novo, com um item por linha nova, como o docs/05 da clínica pede; depois fiz o commit, criei a tag `book-v1/closing-a-milestone` e enviei os dois.[^closing-a-milestone-run]
A tag [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone) guarda o marco 1 inteiro com a sua fila de achados, para você comparar o seu código com ela; a fila dela mantém os nomes do diff acima, já que uma tag nunca se move.

## Quando os achados viraram uma entrega só

O Ninjobs escreveu a mesma regra no seu processo em 2026-08-29: cada achado confirmado de uma revisão de marco vira uma linha na fila.[^ninjobs]
Quando o marco dele fechou, a revisão tinha oito achados, e eu pus os oito em uma entrega só.[^ninjobs]
A página dela diz, com as suas próprias palavras, que não cabe em uma página e que vai contra o processo de propósito.
Ela chegou a 879 linhas.[^ninjobs]
Quando eu mesmo conferi o resultado, achei falhas que os testes dela não tinham pegado.
A causa não foi o processo; foi a minha escolha.
Oito linhas teriam sido oito páginas, cada uma pequena o bastante para ser lida antes de ser construída e conferida depois.

## Pontos-chave

* Uma revisão de marco olha o que as entregas somam, o que nenhuma revisão de uma página ou de uma mudança no stage consegue ver.
* Confira o parágrafo primeiro, no produto rodando, do começo ao fim, uma vez; uma afirmação que falha é um achado.
* A revisão é a última linha do marco, `<milestone>-review`, rodada com o `/propose` e o `/apply`: ela confere o parágrafo, revisa o intervalo do marco com o que o seu host oferece (no Claude Code, `/code-review high <antes>...<último>`) e não corrige nada.
* Decida cada achado com o seu motivo, depois de olhar o código: nunca confie em um às cegas, nunca descarte um sem ler.
* Um achado confirmado vira uma linha em um marco novo `<M>.1`, e não uma correção: uma correção no meio do marco seguinte não tem página nem revisão.

## Exercícios

Estes exercícios usam a clínica, conversando com o agente, nunca à mão.

### Exercício 12.1

Depois do exercício 11.4, confira cada frase do parágrafo dele no seu app rodando, e anote qualquer uma que não valha.

### Exercício 12.2

Se o seu marco 1 não termina com `m1-review`, peça ao agente que a acrescente como a última linha dele.
Depois rode o `/propose m1-review` e o `/apply m1-review`, e decida cada achado com o seu motivo.

### Exercício 12.3

Peça ao agente que escreva os seus achados confirmados como o marco 1.1, logo depois do marco 1, com o seu parágrafo e `m1.1-review` como a última linha, e confira o diff.

[^claude-code-review]: Anthropic, "Code Review", acesso em 2026-09-28. <https://code.claude.com/docs/en/code-review>
[^codex-review]: OpenAI, "Developer commands", acesso em 2026-09-28. <https://learn.chatgpt.com/docs/developer-commands?surface=cli>
[^copilot-review]: GitHub, "About GitHub Copilot code review", acesso em 2026-09-28. <https://docs.github.com/en/copilot/concepts/agents/code-review>
[^clinic-milestone-1-run]: A construção do marco 1 do projeto guiado deste livro, 2026-09-28, com o Claude Code 2.1.284 e o modelo `claude-opus-5-5`: as seis entregas depois do `skeleton`, cada uma com a revisão da página, a revisão do stage e o commit. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/clinic-milestone-1-run/README.md>
[^closing-a-milestone-run]: A revisão do marco 1 do projeto guiado deste livro, 2026-09-28 e 2026-09-29, com o Claude Code 2.1.284 e o modelo `claude-opus-5-5`, no intervalo 3f0b47c...f16f83b: a conferência do parágrafo, o comando e as suas permissões, cada turno, os achados, as decisões, o diff da fila e a mensagem de commit. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/closing-a-milestone-run/README.md>
[^ninjobs]: Ninjobs, um repositório privado: a regra no docs/05 dele, acrescentada em 2026-08-29; a página da entrega que levou os oito achados da revisão de marco dele, contada pelo autor com `wc -l`. O conteúdo dos achados fica de fora.
