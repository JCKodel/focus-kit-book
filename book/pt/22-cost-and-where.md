# 22. O que os agentes custam, e onde compensam

Depois deste capítulo você consegue ler uma contagem de tokens nos logs do seu host, transformá-la num custo por entrega que o seu time consegue repetir, e dizer por que a página e os documentos mantêm esse custo pequeno.
Você também consegue dizer onde um agente se paga, onde ele se paga menos e onde ele não se paga.

## O problema

Pergunte a um time quanto uma entrega custou em tempo de agente, e ninguém sabe.
A fatura chega uma vez por mês, para todos juntos, e nada nela diz que trabalho ela pagou.
Então a decisão de usar um agente, ou de usá-lo mais, é uma sensação: uma pessoa jura por ele, outra acha que ele queima dinheiro, e nenhuma das duas consegue mostrar um número.

## O que um host cobra

Um modelo lê e escreve tokens, as unidades de texto que o [capítulo 1](01-how-agents-see.md) explica: uma palavra comum é um token, uma palavra longa ou rara são alguns.
O host, o programa que você roda, cobra cada chamada ao modelo em tokens, e conta quatro tipos separados.

* **Entrada**: texto novo que o modelo lê pela primeira vez nesta chamada.
* **Escrita no cache**: texto que o host guarda para que chamadas seguintes possam reusá-lo.
* **Leitura do cache**: texto guardado que uma chamada seguinte reusa.
* **Saída**: o texto que o modelo escreve, a sua resposta e os comandos que ele pede ao host para rodar.

O modelo não lembra nada entre uma chamada e outra, então o host manda o contexto inteiro de novo toda vez: as suas próprias instruções, o arquivo de regras, cada arquivo lido até ali e a conversa.
O cache guarda essa parte repetida, e a chamada seguinte a lê de volta por uma fração do preço da entrada nova.
A documentação de preços da Anthropic dá os multiplicadores: uma escrita no cache custa 1,25 vez um token de entrada normal, para um cache de cinco minutos, e uma leitura do cache custa um décimo disso ou menos, conforme o modelo.[^anthropic-pricing]

## O que uma entrega custou no Ninjobs

O Ninjobs é o meu próprio produto, construído com o método que este livro ensina.
O Claude Code guarda um log de cada sessão, com os tokens de cada chamada, e eu contei esses logs nos 21 dias que o host ainda guardava, de 221 sessões e 18.945 chamadas.

| Tipo | Tokens em 21 dias | Parcela |
|---|---:|---:|
| Entrada | 271.807 | 0,01% |
| Escrita no cache | 54.527.957 | 1,4% |
| Leitura do cache | 3.940.576.768 | 98,3% |
| Saída | 13.871.893 | 0,3% |
| Todos | 4.009.248.425 | 100% |

O projeto tinha 93 páginas concluídas, uma por entrega; cada total dividido por 93 dá 43,1 milhões de tokens por entrega, 149 mil deles de saída e 738 mil sem as leituras do cache.

Quarenta e três milhões de tokens parece muito, e 98,3% disso é o tipo mais barato.
A contagem fixa uma linha de base: este projeto, este método, tantos tokens por entrega.

## Por que as leituras do cache são contadas à parte

Cada chamada lê o contexto inteiro de novo, então as leituras do cache dizem quanto contexto cada chamada carregou.
No Ninjobs, isso dá em média uns 208 mil tokens de contexto em cache por chamada (3.940.576.768 / 18.945).
A saída diz quanto o agente escreveu; as leituras do cache dizem quanto ele teve de carregar para escrever.

Contadas juntas, uma esconde a outra.
Uma sessão que cresce um arquivo soma esse arquivo a cada chamada depois dele, então o custo de uma sessão longa cresce mais rápido do que o trabalho feito nela.
Esse é o número que o processo consegue mexer, e a saída é o número que ele não consegue: o código de que uma entrega precisa é o código de que ela precisa.
Mantenha as leituras do cache numa coluna própria, e uma mudança no jeito de o time trabalhar aparece ali primeiro.

## Por que a página e os documentos mantêm as sessões pequenas

O [capítulo 1](01-how-agents-see.md) mostrou que tudo o que está na janela de contexto vai junto em cada chamada, e que uma sessão longa também piora em lembrar o que está nela.
O método responde com uma sessão nova por entrega.
O `/apply` começa pelo arquivo de regras, pelos documentos que ele cita e por uma página, então o contexto tem o que esta entrega precisa e nada da anterior.
É a página que torna isso possível: ela leva cada decisão de que a construção precisa, então a sessão não precisa herdar a conversa que as tomou.
A fila está entre esses documentos, inteira, e o que ele lê no começo vai junto em cada chamada da sessão; a fila cresce a cada entrega, então cada linha tem uma frase (capítulo 11), e a leitura cresce uma frase por entrega, não uma página.

Assim o contexto fica do tamanho da entrega, e a fatura também.
Um time que mantém uma sessão longa por uma semana paga, em cada chamada da sexta-feira, pelos arquivos lidos na segunda.

## Onde um agente compensa

**Ele compensa** no trabalho cuja decisão está escrita e cuja checagem é mecânica.
A página diz o que construir, os testes e a verificação dizem se está construído, e o agente consegue alternar entre escrever e checar sem uma pessoa no meio.
É ali que os tokens compram mais: o tempo da pessoa vai para ler uma página e uma mudança em stage.

**Ele compensa menos** no trabalho cuja decisão ainda está sendo tomada.
Uma conversa de `/propose` é barata em tokens e cara no tempo da pessoa, porque é a pessoa quem decide.
O agente ajuda ali fazendo as perguntas certas na ordem certa, e o custo a observar são as horas de uma pessoa, que nenhuma contagem de tokens mostra.
No Ninjobs, tudo o que o agente escreveu para uma entrega, a sua página incluída, deu em média 149 mil tokens de saída, e as horas que eu passei decidindo essas páginas não estão em nenhuma coluna da tabela.

**Ele não compensa** numa stack que o agente viu pouco.
No Ninjobs, antes do método, o agente chutava os valores em pixels de um design personalizado em Flutter do qual tinha poucos exemplos para aprender, e tela após tela chegava perto do design sem alcançá-lo.
Cada tentativa custou tokens e a revisão de uma pessoa, e nenhum dos dois comprou uma tela pronta.
Escolher uma stack que o agente conhece é uma decisão de custo tanto quanto técnica.

## Como um time decide

Meça antes de discutir.
O seu host guarda um log de cada sessão na sua máquina, e o log registra os tokens de cada chamada, nos quatro tipos acima.
Conte um marco, divida pelas páginas que ele concluiu, e você tem os seus tokens por entrega.

Nos logs do Claude Code, uma linha por evento, uma resposta transmitida aos poucos registra o seu uso em mais de uma linha, então conte cada par de `message.id` e `requestId` uma vez só.
Esses nomes são campos do próprio log, e por isso ficam em inglês.

Conte logo depois que o marco fecha: o host apaga os logs mais antigos que o seu prazo de retenção, e no Ninjobs os logs de antes daqueles 21 dias já tinham sumido.

Depois compare marcos, não fornecedores.
O segundo marco contra o primeiro, no mesmo projeto, diz se o jeito de o time trabalhar ficou mais barato ou mais caro; a tabela de preços de um fornecedor diz o preço de um token, e nada sobre quantos o seu trabalho precisa.
Quando um número muda, as colunas dizem por quê: saída maior quer dizer que mais coisa foi construída, leituras do cache maiores querem dizer que as sessões cresceram.
É por isso que eu não comparo o Ninjobs com nada de fora: eu não tenho outro projeto medido do mesmo jeito, e um número de outro time, de outro modelo ou de outra tabela de preços compararia coisas que não se correspondem.

## O que o time ganha

Um número por entrega que qualquer pessoa do time consegue repetir a partir dos logs do host, no lugar de uma sensação.
No Ninjobs ele é de 43,1 milhões de tokens por entrega.

## Pontos-chave

* Um host cobra quatro tipos de token: entrada, escrita no cache, leitura do cache e saída; uma leitura do cache custa uma fração de um token de entrada, porque o host reenvia o mesmo contexto em cada chamada.
* No Ninjobs uma entrega custou 43,1 M de tokens, quase todos leituras do cache.
* As leituras do cache são contadas à parte porque medem quanto contexto cada chamada carregou, e é isso que a página, uma sessão nova por entrega e as linhas da fila de uma frase mantêm pequeno.
* Um agente compensa onde a decisão está escrita e a checagem é mecânica, compensa menos onde a decisão ainda está sendo tomada, e não compensa numa stack que ele não viu.
* Meça os tokens por entrega no seu próprio projeto durante um marco, a partir dos logs do host, e compare marcos, não fornecedores.

[^anthropic-pricing]: Anthropic, "Pricing", documentação da Claude Platform, seção "Prompt caching", acesso em 2026-09-30. <https://docs.anthropic.com/en/docs/about-claude/pricing>
