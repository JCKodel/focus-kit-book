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

No início de 2025, o METR fez um ensaio controlado randomizado com 16 desenvolvedores experientes de código aberto em 246 tarefas reais, em projetos maduros nos quais trabalhavam havia 5 anos em média.[^metr-2025]
Cada tarefa foi sorteada para permitir ou proibir ferramentas de IA.
Antes de começar, os desenvolvedores previram que a IA reduziria o tempo de conclusão em 24%.
Depois do estudo, estimaram que ela tinha reduzido o tempo em 20%.
Na medição, a IA aumentou o tempo de conclusão em 19%.
Eles ficaram mais lentos, e acreditaram que estavam mais rápidos.

Uma pesquisa com equipes aponta na mesma direção.
O relatório DORA de 2024 estimou que, a cada 25% de aumento na adoção de IA, a vazão de entregas caiu 1,5% e a estabilidade das entregas caiu 7,2%.[^dora-2024]
Os autores apontam para o básico da entrega, lotes pequenos e testes sólidos, e suspeitam que as mudanças crescem quando a IA permite produzir mais código no mesmo tempo.[^dora-2024]

## O que dá errado sem processo

Três falhas se repetem quando você entrega uma tarefa a um agente e nada mais.

**O agente preenche lacunas com palpites.**
O que você não decidiu, o agente decide por você, e não avisa.
Os palpites são plausíveis, então parecem certos até um usuário esbarrar em um.

**O escopo cresce durante a construção.**
Pedido para corrigir uma coisa, o agente também renomeia, refatora e acrescenta o que acha que vem depois.
Cada mudança parece útil; juntas, formam uma mudança grande demais para revisar, e revisar é a parte lenta.

**O "pronto" chega sem prova.**
O agente dá a tarefa por terminada porque escreveu o código.
Se compila, se os testes passam, se a tela bate com o design, é uma pergunta que o agente só faz quando algo o obriga a fazer.

As três empurram trabalho para as partes lentas: você decide depois, sob pressão, e verifica mais, com menos contra o que verificar.

## O que é um processo mínimo

Um processo mínimo responde a cada falha com uma peça.

* **Uma decisão por escrito.**
  Antes de o agente construir, o que construir está escrito onde o agente lê.
  Há menos a adivinhar, então ele adivinha menos.
* **Uma página por entrega.**
  A página diz o que entra e o que fica de fora.
  Trabalho que não cabe em uma página são duas entregas, e sua revisão fica do tamanho de uma página.
* **Uma verificação antes do "pronto".**
  Um comando que precisa passar, e a prova de que o resultado funciona, rodados antes de alguém dar o trabalho por terminado.

O método que este livro ensina, o focus-kit, se apoia nessas três peças.

## Processo demais também falha

Um processo pode custar mais do que economiza: cada documento é mais uma coisa para escrever, ler e manter verdadeira.
No Ninjobs (<https://www.ninjobs.app>), meu próprio produto, quinze dias, 87 commits e 35 changes do OpenSpec produziram 37.228 linhas de spec para quatro telas e uma tabela de domínio.[^ninjobs-adr-0022]
O capítulo 4 conta essa história e como o focus-kit nasceu dela.

## Pontos-chave

* Um agente acelera a escrita do código; decidir o que construir e verificar que funciona continuam lentos, e é ali que os projetos perdem tempo.
* Em um ensaio controlado, desenvolvedores experientes ficaram mais lentos com IA e acreditaram que estavam mais rápidos.
* Sem processo, o agente adivinha o que você não decidiu, aumenta o escopo e declara "pronto" sem prova.
* Um processo mínimo dá ao agente uma decisão por escrito, uma página por entrega e uma verificação antes do "pronto".
* Processo demais também falha, quando escrever a spec vira o trabalho.

[^metr-2025]: METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 2025. https://arxiv.org/abs/2507.09089
[^dora-2024]: DORA, "Accelerate State of DevOps Report 2024", 2024. https://dora.dev/research/2024/dora-report/
[^ninjobs-adr-0022]: Ninjobs, repositório privado, contado pelo autor no histórico até 2026-08-29, quando o ADR-0022 do projeto abandonou o OpenSpec: dias com commit e commits pelo `git log`, changes pelo arquivo do OpenSpec, linhas com `wc -l` sobre todos os arquivos de `openspec/`. As telas e a tabela são as que esse ADR lista.
