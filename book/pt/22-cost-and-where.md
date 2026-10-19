# 22. O que os agentes custam, e onde compensam

Depois deste capítulo você consegue ler uma contagem de tokens nos logs do seu host, medir quanto custaram as entregas de um marco com uma janela e um conjunto de sessões anotados, para que o seu time consiga repetir a contagem, e dizer o que uma sessão nova leva para o seu contexto e o que ela deixa de fora.
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

## O que o Ninjobs registrou em tokens

O Ninjobs é o meu próprio produto, construído com o método que este livro ensina.
O Claude Code guarda um log de cada sessão, com os tokens de cada chamada, e uma vez eu contei esses logs nos 21 dias que o host ainda guardava: 221 sessões e 18.945 chamadas.

| Tipo | Tokens em 21 dias | Parcela |
|---|---:|---:|
| Entrada | 271.807 | 0,01% |
| Escrita no cache | 54.527.957 | 1,4% |
| Leitura do cache | 3.940.576.768 | 98,3% |
| Saída | 13.871.893 | 0,3% |
| Todos | 4.009.248.425 | 100% |

Esses 21 dias são o limite da contagem.
As datas deles, e a regra que decidiu quais sessões ela incluiu, não foram anotadas com ela, e os logs que ela leu já não existem.
Os commits não conseguem reconstruí-los: um commit registra o que mudou, não as chamadas ao modelo que mudaram aquilo.
Então não sobrou uma lista das entregas em que essas 221 sessões trabalharam, e a tabela não pode ser dividida num custo por entrega; dividi-la por uma contagem de páginas tirada de outra janela misturaria duas amostras.

O que a tabela diz é como os tokens dessa amostra se dividem entre os quatro tipos: 98,3% deles foram leituras do cache, o tipo mais barato.

## Por que as leituras do cache são contadas à parte

Cada chamada lê o contexto inteiro de novo, então as leituras do cache dizem quanto contexto cada chamada carregou.
Nessa amostra, isso dá em média uns 208 mil tokens de contexto em cache por chamada (3.940.576.768 / 18.945).
A saída diz quanto o agente escreveu; as leituras do cache dizem quanto ele teve de carregar para escrever.

Contadas juntas, uma esconde a outra.
Uma sessão que cresce um arquivo soma esse arquivo a cada chamada depois dele, então o custo de uma sessão longa cresce mais rápido do que o trabalho feito nela.
Esse é o número que o processo consegue mexer, e a saída é o número que ele não consegue: o código de que uma entrega precisa é o código de que ela precisa.
Mantenha as leituras do cache numa coluna própria, e uma mudança no jeito de o time trabalhar aparece ali primeiro.

## O que uma sessão nova carrega

O [capítulo 1](01-how-agents-see.md) mostrou que tudo o que está na janela de contexto vai junto em cada chamada, e que uma sessão longa também piora em lembrar o que está nela.
O método responde com uma sessão nova por entrega.
O `/apply` começa pelo arquivo de regras, pelos documentos que ele cita e por uma página, então o contexto não tem nada da conversa da entrega anterior.
É a página que torna isso possível: ela leva cada decisão de que a construção precisa, então a sessão não precisa herdar a conversa que as tomou.
A fila está entre esses documentos, e uma sessão a lê inteira, com as linhas concluídas, então o que ela lê no começo cresce com a história do projeto e vai junto em cada chamada da sessão.
A linha de uma frase do capítulo 11 faz esse crescimento ser de uma frase por entrega, não de uma página, mas não o impede.

Então o contexto de uma sessão nova é uma página mais documentos que crescem com o projeto, e tanto o contexto quanto a fatura crescem com essa história, além de crescerem com a entrega.
O que a sessão nova tira é a conversa das entregas anteriores: um time que mantém uma sessão longa por uma semana paga, em cada chamada da sexta-feira, pelos arquivos lidos na segunda.

## Onde um agente compensa

**Ele compensa** no trabalho cuja decisão está escrita e cuja checagem é mecânica.
A página diz o que construir, os testes e a verificação dizem se está construído, e o agente consegue alternar entre escrever e checar sem uma pessoa no meio.
É ali que os tokens compram mais: o tempo da pessoa vai para ler uma página, usar o que foi construído e ler uma mudança em stage.

**Ele compensa menos** no trabalho cuja decisão ainda está sendo tomada.
Uma conversa de `/propose` é barata em tokens e cara no tempo da pessoa, porque é a pessoa quem decide.
O agente ajuda ali fazendo as perguntas certas na ordem certa, e o custo a observar são as horas de uma pessoa, que nenhuma contagem de tokens mostra.
No Ninjobs, a tabela conta só tokens, e as horas que eu passei decidindo as páginas não estão em nenhuma das suas colunas.

**Ele não compensa** numa stack que o agente viu pouco.
No Ninjobs, antes do método, essa stack foi o Flutter: cada tentativa no design custou tokens e a revisão de uma pessoa, e nenhum dos dois comprou uma tela pronta.
Escolher uma stack pelas perguntas do capítulo 9 é uma decisão de custo tanto quanto técnica.

## Como um time decide

Meça antes de discutir.
O seu host guarda um log de cada sessão na sua máquina, e o log registra os tokens de cada chamada, nos quatro tipos acima.
Antes de dividir os tokens de um marco pelas suas entregas, anote o que você contou, para que outra pessoa consiga contar de novo e chegar ao mesmo número:

* a janela: o primeiro e o último momento contados, e o fuso horário em que o log os escreve;
* as sessões e chamadas dessa janela que trabalharam no marco, incluídas as propostas, as novas tentativas e as sessões compartilhadas com outro trabalho, e a regra que as escolheu;
* as entregas que essas mesmas sessões concluíram;
* o trabalho da janela que não corresponde a nenhuma entrega, contado numa linha própria.

Divida os tokens das chamadas que trabalharam nessas entregas por essas entregas, e você tem os seus tokens por entrega naquele marco.
A linha que não corresponde a nenhuma entrega é informada ao lado, nunca dividida por uma contagem de páginas de outra janela.

Nos logs do Claude Code, uma linha por evento, uma resposta transmitida aos poucos registra o seu uso em mais de uma linha, então conte cada par de `message.id` e `requestId` uma vez só.
Esses nomes são campos do próprio log, e por isso ficam em inglês.

Conte logo depois que o marco fecha: o host apaga os logs mais antigos que o seu prazo de retenção, e no Ninjobs os logs de antes daqueles 21 dias já tinham sumido, e os logs desses 21 dias sumiram depois, então a tabela não pode ser contada de novo.

Depois compare marcos, não fornecedores.
O segundo marco contra o primeiro, no mesmo projeto, diz se o jeito de o time trabalhar ficou mais barato ou mais caro; a tabela de preços de um fornecedor diz o preço de um token, e nada sobre quantos o seu trabalho precisa.
Quando um número muda, as colunas dizem por quê: saída maior quer dizer que mais coisa foi construída, leituras do cache maiores querem dizer que as sessões cresceram.
É por isso que eu não comparo o Ninjobs com nada de fora: eu não tenho outro projeto medido do mesmo jeito, e um número de outro time, de outro modelo ou de outra tabela de preços compararia coisas que não se correspondem.

## O que o time ganha

Um número por entrega que qualquer pessoa do time consegue repetir a partir dos logs do host, porque a sua janela, as suas sessões e as suas entregas estão anotadas, no lugar de uma sensação.
Na amostra que o Ninjobs registrou, 98,3% dos tokens foram leituras do cache, a coluna que o jeito de o time trabalhar consegue mexer.

## Pontos-chave

* Um host cobra quatro tipos de token: entrada, escrita no cache, leitura do cache e saída; uma leitura do cache custa uma fração de um token de entrada, porque o host reenvia o mesmo contexto em cada chamada.
* Conte as leituras do cache à parte, porque elas medem o contexto que cada chamada carregou: uma sessão nova por entrega deixa as conversas anteriores fora dele, e a fila, lida inteira, ainda soma a ele uma frase por entrega.
* Um agente compensa onde a decisão está escrita e a checagem é mecânica, compensa menos onde a decisão ainda está sendo tomada, e não compensa numa stack que ele não viu.
* Meça os tokens por entrega no seu próprio projeto durante um marco, a partir dos logs do host, com a janela, as sessões e as entregas anotadas e o trabalho sem entrega numa linha própria, e compare marcos, não fornecedores.

[^anthropic-pricing]: Anthropic, "Pricing", documentação da Claude Platform, seção "Prompt caching", acesso em 2026-09-30. <https://docs.anthropic.com/en/docs/about-claude/pricing>
