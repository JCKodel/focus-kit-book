# Por que processo, quando a IA escreve rápido

Um agente de código escreve código mais rápido do que você consegue ler, e os projetos continuam atrasando.
Depois deste capítulo você consegue explicar por quê, e nomear as três coisas que um processo mínimo dá ao agente: uma decisão por escrito, um limite de escopo e uma verificação antes do "pronto".

## A velocidade mudou o gargalo de lugar

Construir software tem três partes: decidir o que construir, escrever e verificar que funciona.
Um agente torna a escrita quase gratuita.
Decidir e verificar continuam com você.
Digitar é rápido.
Decidir e verificar são lentos.
Quando só a escrita acelera, o resultado é mais código esperando uma decisão ou uma revisão.

O METR, Model Evaluation and Threat Research (pesquisa de avaliação de modelos e de ameaças), é uma organização de pesquisa que avalia os modelos de IA de fronteira para informar o público sobre as suas capacidades e os seus riscos.
No início de 2025 ele fez um ensaio controlado randomizado, o desenho que a medicina usa para testar um tratamento, com 16 desenvolvedores experientes de código aberto em 246 tarefas reais, em projetos maduros nos quais eles trabalhavam havia 5 anos em média.[^metr-2025]
Cada tarefa foi sorteada para permitir ou proibir ferramentas de IA.
Antes de começar, os desenvolvedores previram que a IA reduziria seu tempo de conclusão em 24%.
Depois do estudo, estimaram que ela tinha reduzido o tempo em 20%.
Medida, a IA aumentou o tempo de conclusão em 19%.
Eles foram mais lentos, e acreditavam ter sido mais rápidos.

Uma pesquisa com times aponta na mesma direção.
O DORA, DevOps Research and Assessment (pesquisa e avaliação de DevOps), é o programa de pesquisa, hoje parte do Google Cloud, que pesquisa times de software todo ano e publica o relatório State of DevOps.
O relatório de 2024 estimou que, a cada 25% de aumento na adoção de IA, a vazão de entrega caiu 1,5% e a estabilidade de entrega caiu 7,2%.[^dora-2024]
Seus autores apontam para o básico da entrega, lotes pequenos e testes sólidos, e suspeitam que as mudanças ficam maiores quando a IA deixa as pessoas produzirem mais código no mesmo tempo.[^dora-2024]

## O que dá errado sem processo

Três falhas se repetem quando você entrega uma tarefa a um agente e nada mais.

**O agente preenche as lacunas com palpites.**
O que você não decidiu, o agente decide por você, e não avisa.
Os palpites são plausíveis, então parecem certos até um usuário esbarrar em um deles.

**O escopo cresce durante a construção.**
Pedido para corrigir uma coisa, o agente também renomeia, refatora e acrescenta o que acha que vem a seguir.
Cada mudança parece útil; juntas, formam uma mudança grande demais para revisar, e a revisão é a parte lenta.

**O "pronto" chega sem prova.**
O agente declara a tarefa concluída porque escreveu o código.
Se compila, se os testes passam, se a tela bate com o design, é uma pergunta que o agente só faz quando algo o obriga a fazê-la.

As três empurram trabalho para as partes lentas: você decide mais tarde, sob pressão, e verifica mais, com menos contra o que verificar.

## O que é um processo mínimo

Um processo mínimo responde a cada falha com uma peça.

* **Uma decisão por escrito.**
  Antes de o agente construir, o que construir está escrito onde o agente lê.
  Há menos a adivinhar, então ele adivinha menos.
* **Uma página por entrega.**
  A página diz o que entra e o que fica de fora.
  Trabalho que não cabe numa página são duas entregas, e sua revisão continua do tamanho de uma página ([capítulo 14](14-propose.md)).
* **Uma verificação antes do "pronto".**
  Um comando que precisa passar, e uma prova de que o resultado funciona, executados antes que alguém chame o trabalho de concluído ([capítulo 15](15-apply.md)).

O método que este livro ensina, o focus-kit, é construído sobre essas três peças, e a Parte II o ensina.

## Processo demais também falha

Um processo pode custar mais do que economiza: cada documento é mais uma coisa para escrever, ler e manter verdadeira.
Na Ninjobs, meu próprio produto, escrever a especificação virou o trabalho; o [capítulo 3](03-spec-driven.md) faz a conta e o [capítulo 9](09-birth-of-focus-kit.md) conta a história.

## O que o time ganha

O time aprende para onde vai o seu tempo.
Desenvolvedores experientes mediram-se 19% mais lentos com IA enquanto acreditavam estar 20% mais rápidos,[^metr-2025] e times que adotaram mais IA entregaram um pouco menos e quebraram um pouco mais.[^dora-2024]
Digitar nunca foi a parte lenta, então o ganho está em decidir e verificar: uma decisão escrita antes da construção, um escopo que cabe numa página e uma verificação que precisa passar antes que alguém diga "pronto".

## Pontos-chave

* Um agente acelera a escrita de código; decidir o que construir e verificar que funciona continuam lentos, e é aí que os projetos perdem tempo.
* Num ensaio controlado, desenvolvedores experientes foram mais lentos com IA e acreditavam ter sido mais rápidos.
* Sem processo, o agente adivinha o que você não decidiu, aumenta o escopo e declara "pronto" sem prova.
* Um processo mínimo dá ao agente uma decisão por escrito, uma página por entrega e uma verificação antes do "pronto".
* Processo demais também falha, quando escrever a especificação vira o trabalho.

[^metr-2025]: METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 2025. <https://arxiv.org/abs/2507.09089>
[^dora-2024]: DORA, "Accelerate State of DevOps Report 2024", 2024. <https://dora.dev/research/2024/dora-report/>
