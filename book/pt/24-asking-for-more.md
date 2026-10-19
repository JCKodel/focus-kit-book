# 24. Pedir mais

Depois deste capítulo você consegue enviar o protocolo de desafio, quatro mensagens, sempre as mesmas, que seguem a primeira resposta de um agente e estão escritas, prontas para copiar, na seção com esse nome, quando o trabalho vale o que elas custam; consegue dizer em que fase de uma entrega cada turno pode mudar alguma coisa, para que o protocolo nunca alargue o que a página combinou; e consegue dizer por que essa primeira resposta parece final e quais quatro coisas um agente não propõe se você não pedir.

## O card que eu aceitei

No Caso A, o projeto de cliente do [capítulo 17](17-project-as-assistant.md), o agente precisava construir cards para o Microsoft Teams, escritos em Adaptive Cards, o formato que o Teams usa para mostrar um card num chat.
O cliente mandou um PowerPoint com os cards que imaginava, e o agente tinha esse arquivo.
Ele não os construiu.
Disse que o desenho parecia mais uma página do que um Adaptive Card, e comentou algo sobre abas e botões, embora o desenho do cliente não tivesse abas.
Eu aceitei a desculpa e os cards que ele fez no lugar.
O cliente ficou insatisfeito com a aparência e disse isso.
Só depois disso o agente ficou um pouco mais proativo e testou de fato o que um card do Teams consegue fazer.

O deslize foi meu tanto quanto do agente: ele chamou o desenho de inviável sem testar, e eu aceitei sem pedir o teste.
A segunda das quatro mensagens abaixo teria feito o agente testar o que afirmou e me mostrar um card construído a partir do PowerPoint do cliente antes que eu aceitasse qualquer coisa.

## O protocolo de desafio

O protocolo de desafio são quatro mensagens, sempre as mesmas, que você envia depois da primeira resposta, uma de cada vez, cada uma quando a resposta do agente à anterior termina; cada mensagem e a resposta do agente a ela é um turno.
O experimento que a última seção deste capítulo relata enviou os quatro turnos em inglês; estes são os mesmos, traduzidos, para copiar como estão:

```text
1. Antes de mudar qualquer coisa, me pergunte o que você precisa saber
   para fazer isto bem.
2. O que você disse que não é possível, ou que não vale a pena fazer?
   Teste cada um e me mostre o resultado.
3. Quem lê ou usa isto, quanto tempo tem, e quanto custa cada uso?
   Mude o resultado para caber nisso.
4. O que eu não pedi e que eu ia querer? Acrescente o que valer a
   pena, e me diga o que você deixou de fora.
```

**A fase decide o que um turno pode mudar.**
Num projeto que segue o método, o protocolo nunca alarga uma entrega.
Depois que o `/propose` escreve a página, e antes de o `/apply` rodar, envie-o nessa sessão: as perguntas do agente, os limites que testou e o que acrescentaria vão para a página, que você revisa; nenhum turno autoriza código, já que o `/propose` não escreve nenhum (capítulo 12).
Depois do primeiro resultado do `/apply`, compare com a página o que cada turno encontra.
Um requisito que a página já tem e o resultado deixou passar é uma correção: entra nesta entrega, a verificação e a prova rodam de novo e a página a registra, antes de a entrega fechar.
Uma capacidade nova é uma linha nova: se o turno 4, em `emprestar-livro`, propõe que um membro reserve um exemplar emprestado, essa é uma capacidade que a página põe fora do escopo (capítulo 12).
A resposta é uma linha `[ ]` `reservas`, com um rascunho da página para o que a linha não comporta, definida pelo `/propose` e construída por um `/apply` numa sessão nova, nunca acrescentada à entrega aberta (capítulo 13).
O teste do turno 2 confere o resultado combinado; uma mudança que ele revela fora desse resultado segue a mesma regra.

**O turno 1 põe as perguntas antes do trabalho.**
O agente sabe o que lhe falta melhor do que você consegue adivinhar, e "antes de mudar qualquer coisa" o impede de reconstruir sobre um palpite.
Responda às perguntas dele com o que você sabe: quem usa o resultado, em quê, com quanto tempo, quanto custa.
Essa é a parte do trabalho que nunca esteve na janela dele, e só você a tem.
Uma pergunta que você não sabe responder, diga isso, e deixe o agente escolher.

**O turno 2 pede um teste, e não uma dúvida.**
Perguntar "Tem certeza?" convida uma resposta nova escolhida para agradar você.
Sharma e colegas, pesquisadores da Anthropic, mediram isso: depois de "Tem certeza?", os modelos mudaram a primeira resposta entre 32% (GPT-4) e 86% (Claude 1.3) das vezes.[^sharma-2024]
Eles chamam isso de bajulação: o modelo diz à pessoa o que ela parece querer, e abandona uma resposta certa tão fácil quanto uma errada.
Um teste devolve um resultado que não depende do que você parece querer.
"Ou que não vale a pena fazer" pega os limites silenciosos, o que o agente deixou de fora sem dizer que não conseguia fazer.

**O turno 3 nomeia quem lê e o custo.**
Quem usa o resultado, com quanto tempo, e quanto custa cada uso: duas das quatro coisas que um agente não propõe se ninguém pedir, que uma seção abaixo nomeia, numa pergunta só.
"Mude o resultado para caber nisso" pede a mudança, e não um conselho sobre ela.

**O turno 4 pede o que você não pediu, e mantém você decidindo.**
"Valer a pena" pede ao agente que pese cada acréscimo, e "me diga o que você deixou de fora" põe o resto diante de você.
Você continua sendo quem decide, que é o papel que o prólogo dá à pessoa.
Dentro de uma entrega, o que vale a pena acrescentar agora é o que a página já pede; o resto é o que o agente deixou de fora, e vira uma linha.

## Por que a primeira resposta parece final

Três achados explicam por que uma pessoa fica com a primeira resposta, e nenhum deles é sobre o agente.

**A pessoa para no bom o bastante.**
Herbert Simon, o economista e psicólogo que estudou como as pessoas decidem, escreveu em 1956 que "*os organismos se adaptam bem o bastante para 'se contentar'; em geral, eles não 'otimizam'.*"[^simon-1956]
Uma pessoa procura uma resposta boa o bastante para o que consegue ver, e para ali.
A primeira resposta de um agente costuma ser: roda, lê bem, faz o que foi pedido.

**A pessoa toma a resposta do auxílio no lugar de conferir.**
Kathleen Mosier e Linda Skitka definiram o viés de automação em 1996: "*a tendência de usar sinais automatizados como substituto heurístico da busca e do processamento atentos de informação*" (citado em Mosier e Manzey 2019).[^mosier-manzey-2019]
Skitka, Mosier e Burdick mediram isso em 1999, com 80 estudantes numa tarefa de voo simulado, uns com um auxílio automatizado e outros sem.[^skitka-1999]
Nos seis eventos que o auxílio não sinalizou, quem tinha o auxílio acertou 59% das vezes, contra 97% sem ele.[^skitka-1999]
Quando o auxílio recomendou algo errado, em seis ocasiões, todos os participantes que tinham o auxílio, menos um, seguiram ao menos uma das recomendações erradas.[^skitka-1999]

**A pessoa não tem o tempo ou os meios para melhorá-la.**
Uma pesquisa de 2025 da Microsoft Research e da Carnegie Mellon University pediu a 319 trabalhadores do conhecimento exemplos do seu próprio trabalho com IA generativa.[^lee-2025]
Entre o que os impediu de pensar criticamente sobre uma resposta, 44 citaram a falta de tempo, e 72 disseram que era difícil melhorar a resposta pedindo de novo ao modelo.[^lee-2025]
Na mesma pesquisa, mais confiança na IA andou junto com menos pensamento crítico, como os próprios trabalhadores relataram; a pesquisa mediu o que eles disseram, não a qualidade do trabalho.

Uma resposta não conferida custa pouco enquanto a tarefa é uma que o modelo faz bem, e muito quando não é.
Num experimento com consultores do Boston Consulting Group, Dell'Acqua e colegas viram que, em tarefas dentro do que o modelo fazia bem, os consultores com IA terminaram 25,1% mais rápido, com qualidade de 29,9% a 33,9% maior.[^dell-acqua-2026]
Numa tarefa fora disso, quem tinha IA teve 19 pontos percentuais menos chance de acertar do que quem não tinha.[^dell-acqua-2026]
Nada na resposta diz de que lado dessa linha ela caiu.

## O que o agente não propõe

Um agente responde à pergunta que recebeu, com o que está na sua janela de contexto.
Quatro coisas ficam fora dessa pergunta, e por isso ele não as oferece se ninguém pedir.
Nenhuma é falta de habilidade: cada uma precisa de algo que a pergunta não trazia, ou de um trabalho que a pergunta não pediu.
Os exemplos abaixo vêm de um experimento que este livro fez com três tarefas da biblioteca de empréstimos, cada uma enviada a um agente como um pedido curto: um card do Teams com os empréstimos de um membro, um resumo do relatório anual da biblioteca para o seu conselho, e um projeto preparado para um agente que responde às perguntas do time todo dia (a última seção deste capítulo dá os resultados).

**Testar um limite que ele afirmou.**
Quando um agente diz que algo não pode ser feito, diz isso pelo que lembra da ferramenta, e um teste custa turnos que ninguém pediu que ele gastasse.
Na tarefa do card, uma primeira resposta disse com todas as letras que não tinha conseguido conferir o card e deixou a conferência para a pessoa.[^ask-for-more-run]
Quando lhes pediram um teste, os agentes acharam o que tinham afirmado sem conferir: no card, estilos que o Teams não mostra e elementos que a documentação dele não confirmava; num resumo para um conselho, decisões chamadas de rotina que o próprio relatório punha entre as mais importantes.

**Ajustar o resultado ao tempo de quem lê.**
"Resuma o relatório para o conselho" não diz que o conselho tem pouco tempo e lê no celular.
As três primeiras respostas escreveram o resumo no chat, com tabelas que um celular não mostra; toda resposta desafiada escreveu um arquivo sem tabelas, com as decisões do conselho primeiro.[^ask-for-more-run]

**Ajustar o resultado ao custo de cada uso.**
"Prepare o projeto para um agente que responde ao time todo dia" não diz que cada pergunta abre uma sessão nova e gasta tokens, da conta do time ou do limite de sessão do seu plano.
Cada primeira resposta escreveu um guia longo para o agente sem perguntar, e o juiz achou em dois deles valores copiados do código, que ficam velhos sem aviso quando o código muda.[^ask-for-more-run]

**O que ninguém pediu.**
Um agente que responde à pergunta não acrescenta o que não estava nela.
As respostas desafiadas acrescentaram o que uma pessoa teria querido e não pensou em pedir: um arquivo de conferência que o agente roda contra as notas novas para o guia continuar certo, o vencimento de uma subvenção e o fato de as contas ainda não estarem auditadas, uma lista de perguntas para a direção da biblioteca.

## O que o protocolo rendeu, e quanto custou

O experimento teve três braços, cada um executado três vezes no mesmo modelo, e cada execução registrou a primeira resposta e depois a resposta após os quatro turnos.[^ask-for-more-run]
No braço do limite, o agente construiu um card do Teams com três abas para um membro da biblioteca, para desktop e celular, com cara de pequeno aplicativo.
No braço do público, resumiu um relatório anual longo para um conselho que decide o orçamento.
No braço do custo, preparou um pequeno projeto para um agente que responde às perguntas do time todo dia, sobre notas que não param de crescer.

Cada par, primeira e desafiada, foi pontuado às cegas em três critérios do braço, de 1 a 5 cada, então um braço soma no máximo 45 nos seus três pares.[^ask-for-more-run]

| Braço | Primeira | Desafiada |
|---|---|---|
| limite | 31 | 39 |
| público | 36 | 44 |
| custo | 24 | 39 |

O juiz teria enviado a resposta desafiada em todos os 9 pares.[^ask-for-more-run]

O desafio foi pago em tempo e em tokens.
Somadas as três execuções de cada braço, as sessões desafiadas levaram de 2,9 a 8,8 vezes o tempo das primeiras respostas e escreveram de 2,7 a 9,4 vezes os tokens de saída.[^ask-for-more-run]
Uma sessão de cada vez, uma primeira resposta levou de 24 segundos a pouco mais de 2 minutos, e uma sessão desafiada de 3 a 9 minutos.[^ask-for-more-run]

Numa assinatura fixa, esses tokens saem do limite de sessão do plano: o uso do modelo que um plano permite numa janela de horas, depois do qual o host recusa turnos novos até a janela acabar.
As nove sessões desafiadas do experimento, rodadas em cerca de 45 minutos numa tarde, gastaram o limite do meu plano antes do último turno do protocolo, que nas nove foi enviado de novo cerca de 30 minutos depois.[^ask-for-more-run]
Cada protocolo que você envia gasta uma parte desse limite.
Se você paga por token, o [capítulo 22](22-cost-and-where.md) mostra como transformar tokens em preço.

O braço do custo também mediu quanto cada preparação custa em uso.
Cinco perguntas sobre o projeto, cada uma numa sessão nova, foram feitas a cada preparação: as 30 respostas estavam certas, nas primeiras e nas desafiadas.[^ask-for-more-run]
Em cada uma das três execuções do braço do custo, as cinco perguntas levaram de 14% a 26% menos tempo na preparação desafiada do que na da primeira resposta da mesma execução, e as cinco sessões da preparação desafiada escreveram menos tokens de saída em duas execuções e 9% mais na terceira.[^ask-for-more-run]

Os limites são claros.
Três pares por braço é um experimento registrado, não um estudo, e não tem estatística.
O juiz foi uma sessão nova do mesmo modelo que escreveu as respostas, e não o autor, e pode ter o mesmo gosto desse modelo; em alguns pares ele também percebia qual resposta tinha vindo depois.

Então gaste o tempo e os tokens do protocolo onde o resultado os paga de volta: um resultado usado muitas vezes ou por alguém com pouco tempo, como um card que os membros abrem todo dia, um resumo sobre o qual um conselho decide, uma preparação que gasta tokens a cada pergunta.
Dispense-o numa resposta que você mesmo confere em um minuto.
Quando o agente diz "não é possível", o turno 2 sozinho é o teste mais barato que existe.

## O que o time ganha

O papel do prólogo, a pessoa que valida e não confia cegamente em ninguém, vira quatro frases que qualquer um do time digita, desenvolvedor ou não.
No experimento, as respostas que elas produziram foram as que um juiz às cegas enviaria em 9 de 9 pares, por cerca de 3 a 9 vezes o tempo e os tokens de saída da primeira resposta.[^ask-for-more-run]
O que elas evitam é o que os estudos mediram: respostas aceitas sem conferir, vindas de um auxílio, por pessoas sem tempo, em tarefas em que o modelo pode errar sem que isso apareça.[^dell-acqua-2026]

## Pontos-chave

* Uma primeira resposta parece final porque a pessoa para no bom o bastante (Simon), toma a resposta do auxílio no lugar de conferir (viés de automação, Skitka) e não tem o tempo ou os meios para melhorá-la (Lee et al.).
* Um agente não propõe, sem que peçam, testar um limite que afirmou, ajustar o resultado ao tempo de quem lê, ajustá-lo ao custo de cada uso, nem o que ninguém pediu.
* O protocolo de desafio são quatro turnos, enviados um de cada vez depois da primeira resposta: (1) "Antes de mudar qualquer coisa, me pergunte o que você precisa saber para fazer isto bem."; (2) "O que você disse que não é possível, ou que não vale a pena fazer? Teste cada um e me mostre o resultado."; (3) "Quem lê ou usa isto, quanto tempo tem, e quanto custa cada uso? Mude o resultado para caber nisso."; (4) "O que eu não pedi e que eu ia querer? Acrescente o que valer a pena, e me diga o que você deixou de fora."
* A fase decide o que um turno pode mudar: enquanto o `/propose` define uma entrega, o que os turnos encontram vai para a página e nenhum turno autoriza código; depois do primeiro resultado do `/apply`, um requisito que a página tem e o resultado deixou passar é corrigido e provado nessa entrega, e uma capacidade nova vira uma linha `[ ]` para o `/propose` e um `/apply` numa sessão nova, assim como uma mudança que o teste do turno 2 revela fora do resultado combinado.
* O turno 2 pede um teste porque "Tem certeza?" convida a bajulação, uma resposta nova escolhida para agradar.
* Envie o protocolo onde o resultado é usado com frequência ou lido com pressa: ele custa cerca de 3 a 9 vezes o tempo e os tokens de saída da primeira resposta, que um assinante paga com o limite de sessão do plano, e a sua evidência são três pares por braço, julgados pelo mesmo modelo.

[^ask-for-more-run]: J.C. Ködel, "One Page at a Time", o registro do experimento do protocolo de desafio, 2026-10, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/ask-for-more-experiment-run>
[^simon-1956]: Herbert A. Simon, "Rational choice and the structure of the environment", 1956. <https://doi.org/10.1037/h0042769>
[^mosier-manzey-2019]: Kathleen L. Mosier e Dietrich Manzey, "Humans and Automated Decision Aids: A Match Made in Heaven?", 2019. <https://d-nb.info/1223023044/34>
[^skitka-1999]: Linda J. Skitka, Kathleen L. Mosier e Mark Burdick, "Does automation bias decision-making?", 1999. <https://web.archive.org/web/2020id_/http://lskitka.people.uic.edu/AutomationBias.pdf>
[^lee-2025]: Hao-Ping Lee et al., "The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers", 2025. <https://doi.org/10.1145/3706598.3713778>
[^dell-acqua-2026]: Fabrizio Dell'Acqua et al., "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality", Organization Science, 2026. <https://doi.org/10.1287/orsc.2025.21838>
[^sharma-2024]: Mrinank Sharma et al., "Towards Understanding Sycophancy in Language Models", 2024. <https://arxiv.org/abs/2310.13548>
