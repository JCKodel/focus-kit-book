# Desenvolvimento Guiado por Especificação

O Desenvolvimento Guiado por Especificação faz um agente de código escrever a decisão antes do código, e as ferramentas que o praticam podem escrever muito mais do que uma feature precisa.
Depois deste capítulo você consegue dizer o que é Desenvolvimento Guiado por Especificação e até onde uma ferramenta leva a especificação, apontar o que o Spec Kit e o OpenSpec acertaram, e dizer onde começa o custo de escrever uma decisão em muitos lugares.

## O problema

Um agente que recebe uma tarefa e nada mais decide o que você não decidiu, no meio da construção ([capítulo 1](01-why-process.md)).
A primeira resposta é escrever a decisão antes do código, num arquivo que o agente lê.
O segundo problema chega com a primeira resposta: cada arquivo escrito é um arquivo que alguém revisa e mantém verdadeiro, e uma ferramenta pode escrever tanto que a especificação vira o trabalho.

## O que é uma especificação

Birgitta Böckeler, da Thoughtworks, comparou três ferramentas que se dizem guiadas por especificação e registrou o que o termo significa.[^bockeler-2025]
Uma especificação, na definição dela, é "*um artefato estruturado, orientado a comportamento [...] escrito em linguagem natural, que expressa a feature do software e serve de guia para agentes de código de IA.*"[^bockeler-2025]
Desenvolvimento Guiado por Especificação (SDD) "*significa escrever uma “especificação” antes de escrever código com IA (“documentação primeiro”). A especificação se torna a fonte da verdade para o humano e para a IA.*"[^bockeler-2025]

Ela encontrou três níveis, conforme quanto tempo a especificação vive e quem a edita:

* **spec-first** (especificação primeiro): uma especificação é escrita primeiro e guia a tarefa em questão;
* **spec-anchored** (ancorado na especificação): a especificação é mantida depois da tarefa e usada para evoluir e manter a feature;
* **spec-as-source** (especificação como fonte): a especificação é a fonte principal ao longo do tempo, e uma pessoa edita só a especificação, nunca o código.

"*Todas as abordagens e definições de SDD que encontrei são spec-first, mas nem todas buscam ser spec-anchored ou spec-as-source.*"[^bockeler-2025]
Das três ferramentas dela, o Kiro é "*a mais simples (ou a mais leve)*" e "*majoritariamente spec-first*", e o Tessl é "*a única dessas três ferramentas que aspira explicitamente a uma abordagem spec-anchored*".[^bockeler-2025]
Ela acrescenta que "*essas ferramentas evoluem muito rápido, então podem já ter mudado desde que as usei*".[^bockeler-2025]

## Duas ferramentas

O Spec Kit, do GitHub, é um conjunto de processos para agentes de código; o seu processo de Desenvolvimento Guiado por Especificação escreve uma constituição uma vez por projeto e, para cada feature, uma especificação, um plano e uma lista de tarefas antes do código.[^spec-kit]
O OpenSpec, da Fission AI, "*acrescenta uma camada leve de especificação para que vocês combinem o que construir antes que qualquer código seja escrito*"; o seu comando de proposta escreve uma pasta por mudança, com uma proposta, especificações, um design e tarefas.[^openspec]
Os dois são spec-first por padrão: a especificação é escrita para a tarefa em questão.

Dei às duas ferramentas, e ao focus-kit, o método que a Parte II ensina, a mesma feature pequena: uma reserva pode ser cancelada até 24 horas antes de começar, e um cancelamento mais tardio é recusado com uma mensagem que diz por quê.[^spec-driven-run]
Cada uma parou antes de escrever código.

## O que elas acertaram

**A decisão é escrita antes do código, em arquivos que o agente lê.**
Uma decisão que vive só na conversa se perde quando a sessão termina ([capítulo 2](02-how-agents-see.md)).
As três ferramentas pararam com a feature decidida em arquivos dentro do projeto, onde uma sessão nova os encontra.

**Algumas decisões são escritas uma vez por projeto.**
A constituição do Spec Kit guarda as regras que toda feature segue, como "mantenha simples" ou "toda regra tem um teste", e o plano de cada feature se confere contra ela.[^spec-driven-run]
Uma regra que vale para o projeto inteiro é decidida uma vez e não é discutida de novo feature por feature.

**A ferramenta pergunta antes de escrever.**
O OpenSpec leu o código antes de escrever a mudança, descobriu que a feature supunha algo que o código não tinha, e parou com uma pergunta: ofereceu duas opções, recomendou uma, e só escreveu a mudança depois da resposta.[^spec-driven-run]
O Spec Kit, no seu caminho padrão, deu com a mesma lacuna e não perguntou nada; escreveu a sua própria resposta sob "Assumptions" (premissas) na especificação, onde você só a encontra lendo a especificação.[^spec-driven-run]
Uma pergunta custa um turno antes do código; um palpite custa uma revisão, ou um usuário que esbarra nele.

## Onde começa o custo de muitos lugares

Para a mesma feature, o Spec Kit escreveu 8 arquivos e 756 linhas.[^spec-driven-run]
O OpenSpec escreveu 6 arquivos e 180 linhas.[^spec-driven-run]
O focus-kit escreveu 1 página de 82 linhas.[^spec-driven-run]
Cada um desses arquivos é algo que uma pessoa revisa antes de o código ser escrito.

A feature tem uma regra sobre tempo: até 24 horas antes.
O Spec Kit a repete em cada um dos seus 8 arquivos, o OpenSpec em 4 dos seus 6, o focus-kit na sua única página.[^spec-driven-run]
As três decidem a mesma coisa.
A diferença é quantos outros arquivos a dizem de novo: uma regra escrita em 8 lugares é lida 8 vezes na revisão, e quando muda, muda em 8 lugares, ou se contradiz naqueles que ficaram para trás.
Böckeler encontrou o mesmo no Spec Kit: os arquivos dele "*eram repetitivos, tanto entre si quanto com o código que já existia*", e "*muito verbosos e tediosos de revisar.*"[^bockeler-2025]

A página única tem um preço.
O focus-kit paga por ela com documentos escritos uma vez por projeto e mantidos em dia, o produto, seu vocabulário, suas decisões e sua fila ([capítulo 10](10-the-documents.md)), para que uma feature precise só do que é novo nela.
A troca é decidir uma vez por projeto e depois escrever uma página por feature ([capítulo 14](14-propose.md)).
As contagens dizem o que cada ferramenta escreve antes do código; não dizem qual delas constrói software melhor, e uma feature num dia não é um benchmark.

## O que o time ganha

Uma página por feature, em vez de uma pasta por feature, é o que o time lê, revisa e mantém verdadeiro.
Na Ninjobs, meu próprio produto, quinze dias com o OpenSpec produziram 37.228 linhas de especificação para quatro telas, e nada do fluxo principal existia ainda.[^ninjobs]
As causas foram além da ferramenta, e o [capítulo 9](09-birth-of-focus-kit.md) as conta; a contagem é o que uma especificação custa quando vira o trabalho.
Depois da mudança para uma página por entrega, o produto abriu ao público, e suas 93 páginas concluídas somavam 22.650 linhas.[^ninjobs]

## Pontos-chave

* Uma especificação é uma descrição escrita, orientada a comportamento, do que o software deve fazer, em linguagem natural, que guia um agente de código; o Desenvolvimento Guiado por Especificação a escreve antes do código.
* Conforme quanto tempo a especificação vive, uma ferramenta é spec-first (escrita para a tarefa), spec-anchored (mantida para cuidar da feature) ou spec-as-source (a única coisa que uma pessoa edita).
* O Spec Kit e o OpenSpec acertaram três coisas: a decisão escrita antes do código, as regras do projeto inteiro escritas uma vez e, no OpenSpec, uma pergunta feita antes de escrever.
* Uma regra repetida em muitos arquivos é lida muitas vezes e alterada em muitos lugares; para a mesma feature o Spec Kit escreveu 8 arquivos, o OpenSpec 6, o focus-kit 1 página.
* Uma página mais leve por feature é paga com documentos escritos uma vez por projeto; as contagens mostram o que cada ferramenta escreve, não qual constrói software melhor.

[^bockeler-2025]: Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", 2025. <https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html>
[^spec-kit]: GitHub, "Spec Kit", acesso em 2026-09-30. <https://github.com/github/spec-kit>
[^openspec]: Fission AI, "OpenSpec", acesso em 2026-09-30. <https://github.com/Fission-AI/OpenSpec>
[^spec-driven-run]: J.C. Ködel, "One Page at a Time", o registro da execução das três ferramentas sobre uma feature, 2026-09, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/spec-driven-run>
[^ninjobs]: Ninjobs, o produto do autor, um repositório privado, contado pelo autor ao longo do seu histórico: os quinze dias e as quatro telas a partir do seu ADR-0022, que abandonou o OpenSpec em 2026-08-29; as 37.228 linhas com `wc -l` sobre todos os arquivos em `openspec/` até esse dia; as 93 páginas concluídas em `work/done/` e as suas 22.650 linhas com `wc -l`, até 2026-09-23.
