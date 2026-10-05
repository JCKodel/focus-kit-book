# 14. `/propose`: uma página

Depois deste capítulo você consegue transformar uma linha da fila em uma página com o `/propose`, ler a página como o registro do que o agente entendeu e do que o `/apply` vai construir, cobrir os buracos dela por conversa antes de existir qualquer código, e dividir uma entrega que não cabe em uma página.

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

O `/propose <slug>` lê antes de perguntar: o docs/00 para o produto e as suas regras, o docs/03 para as palavras que a página precisa usar, o docs/05 para os slots do projeto e o formato da página, o docs/06 para o que vem antes e depois da linha, `work/` para as entregas em andamento, e o docs/01 para onde a mudança mora no código.
Então ele conversa com você até o escopo caber em uma página, e só pergunta onde há mais de uma leitura e nenhum documento a fecha: primeiro a avaliação dele, em prosa, e a recomendação dele primeiro em cada pergunta.
"Você decide" é sempre uma resposta válida, e uma pessoa que não sabe responder ainda recebe uma boa página.

Quando começa, ele marca a linha como `[~]` na fila, então quem a lê vê uma entrega sendo definida, e quando a página está escrita, `work/<slug>.md`, a marca vira `[>]` e ele para.
Quando o escopo espera uma resposta que ninguém deu ainda, ou outra linha ainda não feita, ele escreve a página até onde ela vai e marca a linha como `[?]` no lugar, com o que ela espera (capítulo 16).
Em uma linha que já está `[?]`, ele diz o que a linha espera e só segue quando você diz que está resolvido.
Ele nunca escreve, edita nem gera código, migration, teste ou configuração.
O arquivo do comando no kit dá o motivo: "*separar decidir de fazer é o que impede o escopo de crescer durante a implementação*".
O `/apply` começa em uma sessão nova, com o contexto limpo, e a página é tudo o que ele leva desta conversa, então a página precisa guardar tudo de que a construção precisa.

## A página

O formato é fixado no §3 do docs/05 do projeto e é o mesmo em todo projeto:

* **Objetivo.** Uma frase: o que o usuário consegue fazer depois.
* **Comportamento.** Cenários verificáveis na linguagem do usuário; cada linha vira um teste ou uma checagem manual.
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
  aparece como emprestado a ele, com devolução prevista para 21 dias depois.
* Um membro com um livro atrasado é recusado com "Devolva primeiro os seus
  livros atrasados"; nada é registrado.
* Dois bibliotecários emprestam o último exemplar no mesmo momento: um
  consegue e o outro vê "Este exemplar acabou de ser emprestado a outra pessoa".

**Contrato.**
Tabela `emprestimo` (exemplar_id, membro_id, emprestado_em, devolver_em, devolvido_em anulável);
índice único em exemplar_id onde devolvido_em é nulo.
`emprestar(exemplar, membro, hoje): Result<Emprestimo, RecusaDeEmprestimo>` com
`RecusaDeEmprestimo = "TemLivrosEmAtraso" | "JaEmprestado" | "MembroSuspenso"`.

**Estados.** Os padrões.

**Referência visual.** A tela de empréstimo no arquivo de design, com 390 e
1280 pixels de largura.

**Fora do escopo.**
* Devolver um exemplar: uma entrega própria, `devolver-livro`, a seguinte na fila.
* Reservas: não estão no docs/00.
* Multas: o docs/00 as lista como uma decisão em aberto, então ninguém decide isso aqui.

**Pronto quando.**
* [ ] Os testes unitários de `emprestar` passam para as três linhas de Comportamento.
* [ ] O teste do repositório prova que o índice único recusa o segundo empréstimo.
* [ ] `npm run verify` está verde.
* [ ] A tela de empréstimo confere com o design nas duas larguras.
```

Leia a página como o relato do agente sobre o que ele entendeu.
Cada linha de Comportamento pode ser conferida; o Contrato é exato; o Fora do escopo nomeia o que alguém poderia ter suposto que estava dentro; o Pronto quando é uma lista que uma máquina ou uma pessoa consegue marcar.

O Contrato é a única seção que precisa ser exata.
O motivo do kit: "*uma tela errada se corrige em uma sessão, uma coluna errada é uma migration*".
Uma tela é código que você reescreve; uma coluna guarda dados, e mudá-la exige mover os dados que já estão lá.

## Leia a página antes do `/apply`

A página é escrita para ser lida, e as perguntas a fazer são estas:

* Cada linha de Comportamento pode ser conferida, como teste ou à mão?
* O Contrato é exato, até os nomes e os tipos?
* O Fora do escopo nomeia algo que você supôs que estava dentro?
* Você discorda de alguma escolha que o agente fez por conta própria?
* O Pronto quando lista o que faria você dizer "pronto", e nada mais vago?

Você pede cada correção na mesma conversa, e o agente escreve a correção: na página, e em qualquer documento que ela toque.
Você não edita a página à mão: o agente sabe qual documento é dono de cada fato, então uma correção que toca o vocabulário ou a fila entra lá também, e a conversa guarda o motivo.

A ordem é a barata.
Um buraco achado na página custa um turno; achado depois do `/apply`, custa outro `/apply`, o comando mais caro, que constrói, testa e prova de novo.
Na Ninjobs, a página da entrega que calcula a pontuação de compatibilidade de um candidato descobriu, enquanto era escrita, que a idade aproximada de um candidato já vazava no primeiro nível de privacidade pelas datas das suas experiências; isso virou uma linha para uma entrega posterior, e nenhum código foi escrito além dela.

Os hosts têm o seu próprio jeito de planejar antes de editar; no Claude Code é o modo de plano (plan mode), em que "*o Claude lê arquivos e propõe um plano, mas não faz nenhuma edição até você aprovar*".[^claude-code-plan-mode]
O modo de plano trabalha dentro de uma sessão, para a mudança do momento.
A página trabalha para o projeto: um arquivo no repositório, em um formato que todo projeto compartilha, escrito a partir dos documentos do projeto e com as palavras deles, marcado na fila, lido por uma sessão nova para construí-lo, e guardado em `work/done/` com o que aconteceu.
Use o modo de plano dentro de uma sessão se ele ajudar você; a página é o que sobrevive à sessão.

## Quando não cabe

Um escopo que não cabe em uma página são duas entregas: o `/propose` diz isso, propõe a divisão e escreve só a primeira página, e a segunda vira uma linha na fila, onde ela pertence.
Na Ninjobs, a linha única da fila para uma vaga de emprego virou seis entregas em um `/propose`: a vaga, o empregador, as tags, a oferta, os benefícios e os idiomas, e o ciclo de vida; a página da primeira dizia que ela era o passo um de seis.
Cada uma das seis foi revisada na sua própria página e construída na sua própria sessão.

## O que o time ganha

A página é a superfície de revisão do time.
Um desenvolvedor, um gerente ou o cliente lê uma página na linguagem do docs/03 e sabe o que está para ser construído, o que não está, e o que "pronto" vai significar, antes de existir uma linha de código.
No Caso A, o mesmo formato de página levou perguntas ao cliente e documentos para a passagem do projeto, então uma única skill de revisão serviu a todo tipo de trabalho (capítulo 23).
E quando a construção termina, a mesma página registra o que aconteceu, então a história de uma decisão é um arquivo, com o nome do seu slug, em todo projeto que o time roda.

## Pontos-chave

* Uma entrega é a menor mudança com valor, com um slug como nome, e cabe em uma página; se não cabe, são duas.
* O `/propose` lê os documentos, só pergunta onde nenhum documento fecha uma leitura, com a recomendação primeiro, marca a linha `[~]` enquanto conversa e `[>]` quando a página está escrita, ou `[?]` quando o escopo espera, e nunca escreve código.
* A página tem um formato fixo; o Contrato é a única seção exata, porque uma coluna errada é uma migration.
* Leia a página antes do `/apply` e cubra cada buraco pedindo ao agente, nunca à mão: um buraco na página custa um turno, depois do `/apply` custa outro `/apply`.
* A página é a superfície de revisão do time, para código e para qualquer outra coisa que caiba em uma página.

[^claude-code-plan-mode]: Anthropic, "Common workflows", documentação do Claude Code, seção "Plan before editing", acesso em 2026-09-28. <https://code.claude.com/docs/en/common-workflows#plan-before-editing>
