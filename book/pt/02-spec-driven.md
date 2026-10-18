# 2. Desenvolvimento Guiado por Especificação

O Desenvolvimento Guiado por Especificação (Spec-Driven Development, ou SDD, o termo que você vai encontrar na mídia) faz um agente de código escrever a decisão antes do código, e as ferramentas que o praticam podem escrever muito mais do que uma feature precisa.
Depois deste capítulo você consegue dizer o que são uma especificação e o Desenvolvimento Guiado por Especificação, apontar o que o Spec Kit e o OpenSpec acertaram, e dizer onde começa o custo de escrever uma decisão em muitos lugares.

## O problema

Um agente que recebe uma tarefa e nada mais decide o que você não decidiu, no meio da construção.
A primeira resposta é escrever a decisão antes do código, num arquivo que o agente lê.
O segundo problema chega com a primeira resposta: cada arquivo escrito é um arquivo que alguém revisa e mantém verdadeiro, e uma ferramenta pode escrever tanto que a especificação vira o trabalho.

## O que é uma especificação

Birgitta Böckeler, da Thoughtworks, comparou três ferramentas que se dizem guiadas por especificação e registrou o que o termo significa.[^bockeler-2025]
Uma especificação, na definição dela, é "*um artefato estruturado, orientado a comportamento [...] escrito em linguagem natural, que expressa a feature do software e serve de guia para agentes de código de IA.*"[^bockeler-2025]
Desenvolvimento Guiado por Especificação (SDD) "*significa escrever uma “especificação” antes de escrever código com IA (“documentação primeiro”). A especificação se torna a fonte da verdade para o humano e para a IA.*"[^bockeler-2025]

> **Nota.** Comportamento, aqui, é o que o software faz do jeito que o usuário vê: nesta situação, acontece isto.
> "Um membro com um livro atrasado é recusado, com a mensagem 'Devolva primeiro os seus livros atrasados'" é comportamento; "acrescentar uma coluna à tabela de empréstimos" não é, é o como.
> Escrita assim, cada linha pode ser conferida por um teste ou por uma pessoa, e é por isso que a página de uma entrega do focus-kit tem uma seção chamada Comportamento.

## Duas ferramentas

O Spec Kit, do GitHub, é um conjunto de processos para agentes de código; o seu processo de Desenvolvimento Guiado por Especificação escreve uma constituição uma vez por projeto e, para cada feature, uma especificação, um plano e uma lista de tarefas antes do código.[^spec-kit]
O OpenSpec, da Fission AI, "*acrescenta uma camada leve de especificação para que vocês combinem o que construir antes que qualquer código seja escrito*"; o seu comando de proposta escreve uma pasta por mudança, com uma proposta, especificações, um design e tarefas.[^openspec]

Dei às duas ferramentas, e ao focus-kit, o método que a Parte II ensina, a mesma feature pequena: uma reserva pode ser cancelada até 24 horas antes de começar, e um cancelamento mais tardio é recusado com uma mensagem que diz por quê.[^spec-driven-run]
Cada uma parou antes de escrever código.

## O que elas acertaram

**A decisão é escrita antes do código, em arquivos que o agente lê.**
Uma decisão que vive só na conversa se perde quando a sessão termina.
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
A diferença é quantos outros arquivos a dizem de novo: uma regra repetida num arquivo é lida de novo nele na revisão, e quando muda, muda em todo arquivo que a repete, ou se contradiz naqueles que ficaram para trás.
Böckeler encontrou o mesmo no Spec Kit: os arquivos dele "*eram repetitivos, tanto entre si quanto com o código que já existia*", e "*muito verbosos e tediosos de revisar.*"[^bockeler-2025]

Uma página basta porque a maior parte do que esses arquivos repetem, o produto, o seu vocabulário, as suas regras e as decisões já tomadas, é a mesma para toda feature.
O focus-kit escreve essa parte uma vez por projeto, em documentos mantidos em dia, então a página de uma feature guarda só o que é novo nela.
O custo é escrever esses documentos e mantê-los verdadeiros; o retorno é uma página por feature, lida e revisada de uma vez, no lugar de uma pasta.
As contagens dizem o que cada ferramenta escreve antes do código; não dizem qual delas constrói software melhor, e uma feature num dia não é um benchmark.

## O que o time ganha

Uma pessoa precisa ler tudo o que é escrito antes do código, porque uma decisão que ninguém leu é uma decisão que ninguém conferiu.
A atenção de uma pessoa não cresce com o número de linhas: quanto mais há para ler, menos atenção cada parte recebe.
Então o ganho é escrever menos.
É por isso que o focus-kit escreve uma página por feature, que o time lê inteira e com atenção, revisa e mantém verdadeira, enquanto uma pasta de arquivos é lida por cima.
O processo que eu rodei sobre o OpenSpec, no Ninjobs, meu próprio produto, produziu 37.228 linhas de especificação para quatro telas (toda linha sob a pasta da ferramenta, contada com `wc -l`), e nada do fluxo principal existia ainda.
As causas foram minhas escolhas tanto quanto a ferramenta, e o [capítulo 6](06-birth-of-focus-kit.md) as conta; a contagem é o que uma especificação custa quando vira o trabalho.
Depois da mudança para uma página por entrega, o produto abriu ao público, e suas 93 páginas concluídas somavam 22.650 linhas.

## Pontos-chave

* Uma especificação é uma descrição escrita, orientada a comportamento, do que o software deve fazer, em linguagem natural, que guia um agente de código; o Desenvolvimento Guiado por Especificação a escreve antes do código.
* O Spec Kit e o OpenSpec acertaram três coisas: a decisão escrita antes do código, as regras do projeto inteiro escritas uma vez e, no OpenSpec, uma pergunta feita antes de escrever.
* Uma regra repetida em muitos arquivos é lida muitas vezes e alterada em muitos lugares; para a mesma feature o Spec Kit e o OpenSpec escreveram uma pasta de arquivos onde o focus-kit escreveu uma página.
* Uma página mais leve por feature é paga com documentos escritos uma vez por projeto.

[^bockeler-2025]: Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", 2025. <https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html>
[^spec-kit]: GitHub, "Spec Kit", acesso em 2026-09-30. <https://github.com/github/spec-kit>
[^openspec]: Fission AI, "OpenSpec", acesso em 2026-09-30. <https://github.com/Fission-AI/OpenSpec>
[^spec-driven-run]: J.C. Ködel, "One Page at a Time", o registro da execução das três ferramentas sobre uma feature, 2026-09, no repositório do livro. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/spec-driven-run>
