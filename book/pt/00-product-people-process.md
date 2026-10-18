# Prólogo: Produto, pessoas e processo

Um agente de código escreve código mais rápido do que você consegue ler, e os projetos continuam atrasando.
Depois deste prólogo você consegue dizer por quê, o que produto, pessoas e processo decidem cada um quando parte de quem constrói são agentes de código, e as três coisas que um processo mínimo dá a um agente.

## A velocidade mudou o gargalo de lugar

Construir software tem três partes: decidir o que construir, escrever e verificar que funciona.
Um agente torna a escrita quase gratuita.
Decidir e verificar continuam com você.
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

## Três Ps

Toda empresa se apoia em três Ps, pessoas, processo e produto, uma ideia do empresário Marcus Lemonis,[^lemonis-3ps] e este livro põe o produto primeiro, porque o produto é aquilo pelo qual todo o resto é julgado.

### Produto

Muitos desenvolvedores transformam o próprio desenvolvimento no produto: a melhor solução, a melhor linguagem, o melhor framework.
No caminho, perdem de vista o que importa, o produto que está sendo construído.
O código é compilado e seus usuários nunca o veem; só o produto existe, e tudo é julgado por ele.
Isso não torna o código irrelevante.
A Parte I organiza o código porque uma estrutura clara serve ao produto e ao agente que o altera: a arquitetura vale o que dá a eles, e nunca é um fim em si.
O próprio produto é escrito, num documento que o time e o agente leem antes de agir, e o capítulo 7 mostra esse documento e os outros que o acompanham.

### Pessoas

As pessoas, e agora os agentes, são a parte mais importante de uma empresa e a mais frágil.
Três fragilidades se repetem.

**Conhecimento nas mãos de poucos.**
Quando o que um projeto sabe vive em poucas cabeças, vai embora quando elas vão, e nunca chega a um agente, que não sabe nada no início de uma sessão, como o capítulo 1 explica.
A resposta são documentos: o que o projeto sabe fica escrito num lugar onde uma pessoa e um agente leem igualmente.

**Opinião no lugar de evidência.**
"Eu acho" vence uma reunião quando ninguém pergunta a fonte.
A resposta é citá-la: todo número e toda afirmação levam sua fonte, como toda nota deste livro.

**Ego.**
O autor de um trabalho o defende porque é dele, seja esse autor um colega, um agente ou você.
A resposta é um papel: a pessoa interpreta, orienta e valida, e não confia cegamente em ninguém, agente ou colega, incluindo o autor do código.
Validar inclui pedir mais: a primeira resposta de um agente raramente é a melhor que ele pode dar, e ele não oferece o que você não pediu; o capítulo 24, na Parte V, mostra como pedir.

### Processo

Nenhuma engenharia de software sobrevive sem um processo: quando cada pessoa faz as coisas do seu jeito, o resultado é o caos.
Um processo é seguido porque cada passo tem um propósito, e o propósito é também o teste.
Um passo que não pega nenhum erro concreto sai do processo, uma regra que o capítulo 16 transforma numa pergunta, e processo demais falha tão certamente quanto processo de menos: cada documento é mais uma coisa para escrever, ler e manter verdadeira.
Na Ninjobs (<https://www.ninjobs.app>), meu próprio produto, escrever a especificação virou o trabalho; o [capítulo 2](02-spec-driven.md) faz a conta e o [capítulo 6](06-birth-of-focus-kit.md) conta a história.

O processo que este livro ensina roda sobre documentos que um agente lê, e isso muda a quem o processo serve.
Quando o produto, seu vocabulário, suas decisões e sua fila estão escritos onde o agente os lê, o agente pode responder a qualquer pessoa do time: o que está pendente, como está indo, quem deve uma resposta, o que foi combinado com o cliente.
Dê a ele também os e-mails e as propostas, e o projeto vira um assistente do time inteiro, desenvolvedores e gestores; o capítulo 17 mostra como.

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
  Trabalho que não cabe numa página são duas entregas, e sua revisão continua do tamanho de uma página ([capítulo 12](12-propose.md)).
* **Uma verificação antes do "pronto".**
  Um comando que precisa passar, e uma prova de que o resultado funciona, executados antes que alguém chame o trabalho de concluído ([capítulo 13](13-apply.md)).

O método que este livro ensina, o focus-kit, é construído sobre essas três peças, e a Parte II o ensina.

## O que o time ganha

O time aprende para onde vai o seu tempo: desenvolvedores experientes mediram-se 19% mais lentos com IA enquanto acreditavam estar mais rápidos,[^metr-2025] então o ganho está em decidir e verificar, onde as três peças de um processo mínimo trabalham.
Quando o processo roda sobre documentos que um agente lê, o projeto responde ao time inteiro, para um desenvolvedor como para uma empresa, e é para esse ganho que este livro foi escrito.
Nenhum estudo neste livro mede um time com o método e as suas práticas contra o mesmo time sem eles: a evidência de cada capítulo é o seu número, contado num projeto real e dizendo de onde vem, ou a perda que a sua prática evita.
A Ninjobs e o Caso A, um projeto de cliente que rodou sobre o processo e que o capítulo 17 conta, vivem em repositórios privados, então todo número que este livro dá sobre eles foi contado por mim ao longo dos seus históricos.
A Ninjobs aparece pelo nome; o Caso A é um projeto corporativo privado, e o seu nome não poderia ser publicado sem autorização, então aparece sem o seu dono, o seu cliente ou o seu negócio.

A Parte I é a base, as práticas que todo leitor precisa compartilhar antes do processo, de como um agente vê um projeto até um teste para cada peça de código.
A Parte II é o método, o focus-kit, dos seus documentos ao projeto como assistente do time.
A Parte III é o git e as ferramentas do time.
A Parte IV vai além do código: projetos que não são software, quanto custam os agentes e a adoção numa empresa.
A Parte V é a pessoa: por que a primeira resposta de um agente parece final, e como pedir mais.

## Pontos-chave

* Toda empresa que constrói software se apoia em três Ps: o produto, que é o que é julgado; pessoas e agentes, cujas fragilidades são respondidas por documentos, fontes e uma pessoa que valida; e um processo em que cada passo tem um propósito.
* Num ensaio controlado, desenvolvedores experientes foram 19% mais lentos com IA e acreditavam ter sido mais rápidos: decidir e verificar continuam lentos, e é aí que os projetos perdem tempo.
* Sem processo, o agente adivinha o que você não decidiu, aumenta o escopo e declara "pronto" sem prova.
* Um processo mínimo dá ao agente uma decisão por escrito, uma página por entrega e uma verificação antes do "pronto"; processo demais também falha, quando escrever a especificação vira o trabalho.
* Escreva cada decisão onde um agente a lê, e pergunte ao projeto antes de perguntar a um colega.

[^lemonis-3ps]: Marcus Lemonis Business Team, "3 Key To Business Success: People, Process & Product", acesso em 2026-09-28. <https://marcuslemonis.com/business/3ps-of-business>
[^metr-2025]: METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 2025. <https://arxiv.org/abs/2507.09089>
[^dora-2024]: DORA, "Accelerate State of DevOps Report 2024", 2024. <https://dora.dev/research/2024/dora-report/>
