# Como nasceu o focus-kit

No Ninjobs, meu próprio produto, eu abandonei o OpenSpec e escrevi o processo que virou o focus-kit.
Depois deste capítulo você consegue dizer por quê, e a que falha responde cada regra do focus-kit.

## Como era

O Ninjobs começou com o OpenSpec.
Cada funcionalidade era uma change com proposta, especificações, design e tarefas, e cada decisão era escrita de novo nos documentos e nos ADRs do projeto.
Antes de uma entrega contar como pronta, ela precisava passar por 29 verificações.[^ninjobs-adr-0022]
Em quinze dias, isso produziu quatro telas.[^ninjobs-adr-0022]

## O que deu errado

O processo pesava mais do que o trabalho a que servia.
Uma decisão morava em seis lugares que podiam discordar: os documentos, as especificações, as changes, os ADRs, um roteiro e o código.
Toda entrega tinha de mantê-los em acordo, e cada um podia ficar desatualizado sozinho.
As verificações eram caras de satisfazer e baratas de contornar, e nenhuma jamais tinha reprovado um erro do produto.[^ninjobs-adr-0022]
Um OpenSpec mais enxuto não teria ajudado: o custo estava no número de lugares, e não no tamanho de cada arquivo.

## Para onde foi

Em 2026-08-29 eu recomecei o projeto com um processo pequeno o bastante para caber na cabeça.[^ninjobs-adr-0022]

* **Uma página por entrega.** O que construir, e o que fica de fora, cabe em uma página. Se não cabe, são duas entregas.
* **Decidir e fazer em sessões separadas.** O `/propose` conversa e escreve a página; o `/apply` a constrói em uma sessão nova, só com a página e os documentos.
* **Os documentos guardam os fatos.** Os comandos só dizem quais documentos ler e o que nunca fazer.
* **Uma fila**, uma linha por entrega. Sem especificação formal, sem arquivamento, sem pasta de change.
* **O agente nunca faz commit.** Ele prepara o trabalho com `git add`; a pessoa revisa e faz o commit.
* **O regulador.** Tudo o que quiser voltar responde a uma pergunta: que erro concreto isso teria pegado?

Esse processo levou o Ninjobs à abertura ao público em 2026-09-10.[^ninjobs-adr-0026]
Depois eu o transformei no focus-kit, o kit que este livro ensina.

Uma regra veio mais tarde.
Quando o Ninjobs adotou o kit, o `/apply` antigo ainda descrevia coisas que o projeto já tinha mudado nos documentos.[^ninjobs-adr-0026]
Por isso um comando não guarda nenhum fato do projeto: todo fato assim mora em um lugar só, o docs/05, e o comando o lê ali.

## Duas lições além do processo

O recomeço também trocou a stack, de Flutter para React.
O mesmo agente errava o design em Flutter e o acertava em React.
O Flutter conseguiria construir o projeto; o limite era o que o agente tinha visto no treinamento.
Escolha uma stack pelo valor do projeto e pelo quanto o agente a conhece; o capítulo 7 mostra como.

O Ninjobs era construído com FOCUS, a arquitetura da Parte III, aplicada inteira a cada funcionalidade: exibir um campo levava oito arquivos.[^ninjobs-adr-0022]
O FOCUS continuou útil; aplicado em tudo, custava mais do que dava.
Os capítulos 14 e 15 dizem onde ele se paga.

## Pontos-chave

* No Ninjobs, o OpenSpec produziu quatro telas em quinze dias porque cada decisão morava em seis lugares e 29 verificações guardavam a forma, e não o produto.
* A solução foi ter menos lugares: uma página por entrega, documentos que guardam os fatos e comandos que só apontam para eles.
* Decidir e fazer acontecem em sessões separadas, e quem faz o commit é a pessoa, nunca o agente.
* O regulador pergunta a cada acréscimo que erro concreto ele teria pegado.
* Escolha uma stack que o agente conhece, e aplique uma arquitetura só onde ela se paga.

[^ninjobs-adr-0022]: Ninjobs, repositório privado, contado pelo autor no histórico até 2026-08-29, quando o ADR-0022 do projeto abandonou o OpenSpec: dias com commit e commits pelo `git log`, changes pelo arquivo do OpenSpec, linhas com `wc -l` sobre todos os arquivos de `openspec/`. As telas e a tabela são as que esse ADR lista. As causas, a alternativa recusada e a decisão são as do próprio ADR, parafraseadas.
[^ninjobs-adr-0026]: Ninjobs, repositório privado, o ADR-0026 do projeto, datado de 2026-09-21: a data da abertura ao público e a adoção do focus-kit.
