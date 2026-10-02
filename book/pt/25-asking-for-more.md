# 25. Pedir mais

Depois deste capítulo você sabe dizer por que a primeira resposta de um agente parece final, nomeia as quatro coisas que um agente não propõe se você não pedir, e envia os quatro turnos do protocolo de desafio quando o trabalho vale o que eles custam.
O protocolo de desafio são quatro mensagens, sempre as mesmas, que você envia depois da primeira resposta de um agente; cada mensagem e a resposta do agente a ela é um turno, e as quatro estão escritas, prontas para copiar, na seção "O protocolo de desafio".
No experimento deste livro, um juiz que não sabia qual resposta era qual teria enviado a resposta desafiada em 9 de 9 pares, e o desafio custou de 2,6 a 8 vezes a primeira resposta.[^ask-for-more-run]

## O card que eu aceitei

No Caso A, o projeto de cliente do [capítulo 18](18-project-as-assistant.md), o agente precisava construir cards para o Microsoft Teams, escritos em Adaptive Cards, o formato que o Teams usa para mostrar um card num chat.
O cliente mandou um PowerPoint com os cards que imaginava, e o agente tinha esse arquivo.
Ele não os construiu.
Disse que o desenho parecia mais uma página do que um Adaptive Card, e comentou algo sobre abas e botões, embora o desenho do cliente não tivesse abas.
Eu aceitei a desculpa e os cards que ele fez no lugar.
O cliente ficou insatisfeito com a aparência e disse isso.
Só depois disso o agente ficou um pouco mais proativo e testou de fato o que um card do Teams consegue fazer.

O deslize foi meu tanto quanto do agente: ele chamou o desenho de inviável sem testar, e eu aceitei sem pedir o teste.
Antes dos agentes, eu poderia ter feito o mesmo: olhar um esboço num papel e dizer "isso não é possível", por preguiça, por não conhecer a plataforma ou por qualquer outro motivo, mesmo sendo possível com um pouco mais de esforço e pesquisa.
Os modelos só ampliam esse comportamento.

## Por que a primeira resposta parece final

Três achados explicam por que uma pessoa fica com a primeira resposta, e nenhum deles é sobre o agente.

**A pessoa para no bom o bastante.**
Herbert Simon, o economista e psicólogo que estudou como as pessoas decidem, escreveu em 1956 que "*os organismos se adaptam bem o bastante para 'se contentar'; em geral, eles não 'otimizam'.*"[^simon-1956]
Uma pessoa procura uma resposta boa o bastante para o que consegue ver, e para ali.
A primeira resposta de um agente costuma ser: roda, lê bem, faz o que foi pedido.

**A pessoa toma a resposta do auxílio no lugar de conferir.**
Kathleen Mosier e Linda Skitka definiram o viés de automação em 1996: "*a tendência de usar sinais automatizados como substituto heurístico da busca e do processamento atentos de informação*" (citado em Mosier e Manzey 2019).[^mosier-manzey-2019]
Skitka, Mosier e Burdick mediram isso em 1999, com 80 estudantes numa tarefa de voo simulado, uns com um auxílio automatizado e outros sem.[^skitka-1999]
Nos seis eventos que o auxílio não sinalizou, quem tinha o auxílio acertou 59% das vezes, contra 97% sem ele: deixou passar 41% dos eventos, contra 3%.
Quando o auxílio recomendou algo errado, em seis ocasiões, os participantes seguiram em média 65% das seis recomendações erradas, e todos menos um seguiram ao menos uma.

**A pessoa não tem o tempo ou os meios para melhorá-la.**
Uma pesquisa de 2025 da Microsoft Research e da Carnegie Mellon University pediu a 319 trabalhadores do conhecimento exemplos do seu próprio trabalho com IA generativa.[^lee-2025]
Entre o que os impediu de pensar criticamente sobre uma resposta, 44 citaram a falta de tempo, e 72 disseram que era difícil melhorar a resposta pedindo de novo ao modelo.
Na mesma pesquisa, mais confiança na IA andou junto com menos pensamento crítico, como os próprios trabalhadores relataram; a pesquisa mediu o que eles disseram, não a qualidade do trabalho.

O hábito é comum no trabalho.
Num estudo de campo com 244 consultores do Boston Consulting Group, publicado pela Harvard Business School, 27% (63) entregaram a tarefa ao modelo, e 44% deles (28 de 63) aceitaram o resultado sem mudança.[^randazzo-hbs-26-036]

Uma resposta não conferida custa pouco enquanto a tarefa é uma que o modelo faz bem, e muito quando não é.
Num experimento com consultores da mesma empresa, Dell'Acqua e colegas viram que, em tarefas dentro do que o modelo fazia bem, os consultores com IA terminaram 12,2% mais tarefas, 25,1% mais rápido, com qualidade de 29,9% a 33,9% maior.[^dell-acqua-2026]
Numa tarefa fora disso, quem tinha IA teve 19 pontos percentuais menos chance de acertar: 60% e 70,6% contra 84,5% sem ela.[^dell-acqua-2026]
Nada na resposta diz de que lado dessa linha ela caiu.

## O que o agente não propõe

Um agente responde à pergunta que recebeu, com o que está na sua janela de contexto.
Quatro coisas ficam fora dessa pergunta, e por isso ele não as oferece se ninguém pedir.
Nenhuma é falta de habilidade: cada uma precisa de algo que a pergunta não trazia, ou de um trabalho que a pergunta não pediu.
Os exemplos abaixo vêm de um experimento que este livro fez com três tarefas da biblioteca de empréstimos, cada uma enviada a um agente como um pedido curto: um card do Teams com os empréstimos de um membro, um resumo do relatório anual da biblioteca para o seu conselho, e um projeto preparado para um agente que responde às perguntas do time todo dia (a última seção deste capítulo dá os resultados).

**Testar um limite que ele afirmou.**
Quando um agente diz que algo não pode ser feito, diz isso pelo que lembra da ferramenta, e um teste custa turnos que ninguém pediu que ele gastasse.
Na tarefa do card, uma primeira resposta disse com todas as letras que não tinha conseguido conferir o card e deixou a conferência para a pessoa.
Quando lhes pediram um teste, os agentes acharam o que tinham afirmado sem conferir: no card, estilos que o Teams não mostra e elementos que a documentação dele não confirmava; num resumo para um conselho, decisões chamadas de rotina que o próprio relatório punha entre as mais importantes.

**Ajustar o resultado ao tempo de quem lê.**
"Resuma o relatório para o conselho" não diz que o conselho tem pouco tempo e lê no celular.
As três primeiras respostas escreveram o resumo no chat, com tabelas que um celular não mostra; toda resposta desafiada escreveu um arquivo sem tabelas, com as decisões do conselho primeiro.

**Ajustar o resultado ao custo de cada uso.**
"Prepare o projeto para um agente que responde ao time todo dia" não diz que cada pergunta abre uma sessão nova e que o time paga por cada token.
Cada primeira resposta escreveu um guia longo para o agente sem perguntar, e o juiz achou em dois deles valores copiados do código, que ficam velhos sem aviso quando o código muda.

**O que ninguém pediu.**
Um agente que responde à pergunta não acrescenta o que não estava nela.
As respostas desafiadas acrescentaram o que uma pessoa teria querido e não pensou em pedir: um arquivo de conferência que o agente roda contra as notas novas para o guia continuar certo, o vencimento de uma subvenção e o fato de as contas ainda não estarem auditadas, uma lista de perguntas para a direção da biblioteca.

## O protocolo de desafio

O protocolo de desafio são quatro mensagens, sempre as mesmas, que você envia depois da primeira resposta, uma de cada vez, cada uma quando a resposta do agente à anterior termina.
O experimento enviou os quatro turnos em inglês; estes são os mesmos, traduzidos, para copiar como estão:

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
Quem usa o resultado, com quanto tempo, e quanto custa cada uso: duas das quatro coisas que o agente não propõe, numa pergunta só.
"Mude o resultado para caber nisso" pede a mudança, e não um conselho sobre ela.
As técnicas que o agente vai usar quando o custo são tokens estão ensinadas em outro lugar: o arquivo de regras que diz onde mora cada fato ([capítulo 2](02-how-agents-see.md)), e o cache que barateia um contexto repetido ([capítulo 23](23-cost-and-where.md)).

**O turno 4 pede o que você não pediu, e mantém você decidindo.**
"Valer a pena" pede ao agente que pese cada acréscimo, e "me diga o que você deixou de fora" põe o resto diante de você.
Você continua sendo quem decide, que é o papel que o prólogo dá à pessoa.

## O que o protocolo rendeu, e quanto custou

O experimento teve três braços, cada um executado três vezes no mesmo modelo, e cada execução registrou a primeira resposta e depois a resposta após os quatro turnos.[^ask-for-more-run]
No braço do limite, o agente construiu um card do Teams com três abas para um membro da biblioteca, para desktop e celular, com cara de pequeno aplicativo.
No braço do público, resumiu um relatório anual longo para um conselho que decide o orçamento.
No braço do custo, preparou um pequeno projeto para um agente que responde às perguntas do time todo dia, sobre notas que não param de crescer.

Cada par, primeira e desafiada, foi pontuado às cegas em três critérios do braço, de 1 a 5 cada, então um braço soma no máximo 45 nos seus três pares.

| Braço | Primeira | Desafiada |
|---|---|---|
| limite | 31 | 39 |
| público | 36 | 44 |
| custo | 24 | 39 |

O juiz teria enviado a resposta desafiada em todos os 9 pares.

O desafio foi pago em tokens.
Nas três execuções de cada braço, as primeiras respostas custaram 0,82, 1,09 e 3,04 USD, e as sessões desafiadas 6,59, 3,39 e 8,00 USD: de 2,6 a 8 vezes mais.

O braço do custo também mediu quanto cada preparação custa em uso.
Cinco perguntas sobre o projeto, cada uma numa sessão nova, foram feitas a cada preparação: as 30 respostas estavam certas, nas primeiras e nas desafiadas.
A cada cinco perguntas, a preparação desafiada saiu 20% e 16% mais barata nas execuções 1 e 2, e 10% mais cara na execução 3.

Os limites são claros.
Três pares por braço é um experimento registrado, não um estudo, e não tem estatística.
O juiz foi uma sessão nova do mesmo modelo que escreveu as respostas, e não o autor, e pode ter o mesmo gosto desse modelo; em alguns pares ele também percebia qual resposta tinha vindo depois.

Então envie o protocolo quando o resultado for usado muitas vezes, ou por alguém com pouco tempo: um card que os membros abrem todo dia, um resumo sobre o qual um conselho decide, uma preparação paga a cada pergunta.
Dispense-o numa resposta que você mesmo confere em um minuto.
Quando o agente diz "não é possível", o turno 2 sozinho é o teste mais barato que existe.

## O que o time ganha

O papel do prólogo, a pessoa que valida e não confia cegamente em ninguém, vira quatro frases que qualquer um do time digita, desenvolvedor ou não.
No experimento, as respostas que elas produziram foram as que um juiz às cegas enviaria em 9 de 9 pares, por 2,6 a 8 vezes o custo da primeira resposta.[^ask-for-more-run]
O que elas evitam é o que os estudos mediram: respostas aceitas sem conferir, vindas de um auxílio, por pessoas sem tempo, em tarefas em que o modelo pode errar sem que isso apareça.[^dell-acqua-2026]

## Pontos-chave

* Uma primeira resposta parece final porque a pessoa para no bom o bastante (Simon), toma a resposta do auxílio no lugar de conferir (viés de automação, Skitka) e não tem o tempo ou os meios para melhorá-la (Lee et al.).
* Um agente não propõe, sem que peçam, testar um limite que afirmou, ajustar o resultado ao tempo de quem lê, ajustá-lo ao custo de cada uso, nem o que ninguém pediu.
* O protocolo de desafio são quatro turnos, enviados um de cada vez depois da primeira resposta: (1) "Antes de mudar qualquer coisa, me pergunte o que você precisa saber para fazer isto bem."; (2) "O que você disse que não é possível, ou que não vale a pena fazer? Teste cada um e me mostre o resultado."; (3) "Quem lê ou usa isto, quanto tempo tem, e quanto custa cada uso? Mude o resultado para caber nisso."; (4) "O que eu não pedi e que eu ia querer? Acrescente o que valer a pena, e me diga o que você deixou de fora."
* O turno 2 pede um teste porque "Tem certeza?" convida a bajulação: depois dela, os modelos mudaram a primeira resposta de 32% a 86% das vezes.
* No experimento do livro a resposta desafiada venceu 9 de 9 pares às cegas e custou de 2,6 a 8 vezes mais; três pares por braço, julgados pelo mesmo modelo, então envie-o onde o resultado é usado com frequência ou lido com pressa.

[^ask-for-more-run]: J.C. Ködel, "One Page at a Time", o registro do experimento do protocolo de desafio, 2026-10, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/ask-for-more-experiment-run>
[^simon-1956]: Herbert A. Simon, "Rational choice and the structure of the environment", 1956. <https://doi.org/10.1037/h0042769>
[^mosier-manzey-2019]: Kathleen L. Mosier e Dietrich Manzey, "Humans and Automated Decision Aids: A Match Made in Heaven?", 2019. <https://d-nb.info/1223023044/34>
[^skitka-1999]: Linda J. Skitka, Kathleen L. Mosier e Mark Burdick, "Does automation bias decision-making?", 1999. <https://web.archive.org/web/2020id_/http://lskitka.people.uic.edu/AutomationBias.pdf>
[^lee-2025]: Hao-Ping Lee et al., "The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers", 2025. <https://doi.org/10.1145/3706598.3713778>
[^randazzo-hbs-26-036]: Steven Randazzo et al., "Cyborgs, Centaurs and Self-Automators: The Three Modes of Human-GenAI Knowledge Work and Their Implications for Skilling and the Future of Expertise", Harvard Business School Working Paper 26-036, 2025. <https://www.hbs.edu/ris/Publication%20Files/26-036_e7d0e59a-904c-49f1-b610-56eb2bdfe6f9.pdf>
[^dell-acqua-2026]: Fabrizio Dell'Acqua et al., "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality", Organization Science, 2026. <https://doi.org/10.1287/orsc.2025.21838>
[^sharma-2024]: Mrinank Sharma et al., "Towards Understanding Sycophancy in Language Models", 2024. <https://arxiv.org/abs/2310.13548>
