# Como nasceu o focus-kit

No Ninjobs, meu próprio produto, eu abandonei o OpenSpec e escrevi o processo que virou o focus-kit.
Depois deste capítulo você consegue dizer por quê, e a que falha responde cada regra do focus-kit.

## Como era

O Ninjobs começou com o OpenSpec.
Cada funcionalidade era uma change com proposta, especificações, design e tarefas, e cada decisão era escrita de novo nos documentos e nos ADRs do projeto, os registros de decisão de arquitetura, um arquivo por decisão.
Antes de uma entrega contar como pronta, ela precisava passar por 29 verificações.[^ninjobs]
Em quinze dias, isso produziu quatro telas.[^ninjobs]

## O que deu errado

O processo pesava mais do que o trabalho a que servia.
Uma decisão morava em seis lugares que podiam discordar: os documentos, as especificações, as changes, os ADRs, um roteiro e o código.
Toda entrega tinha de mantê-los em acordo, e cada um podia ficar desatualizado sozinho.
As verificações eram caras de satisfazer e baratas de contornar, e nenhuma jamais tinha reprovado um erro do produto.[^ninjobs]
Um OpenSpec mais enxuto não teria ajudado: o custo estava no número de lugares, e não no tamanho de cada arquivo.

## Para onde foi

Em 2026-08-29 eu recomecei o projeto com um processo pequeno o bastante para caber na cabeça.[^ninjobs]

* **Uma página por entrega.** O que construir, e o que fica de fora, cabe em uma página. Se não cabe, são duas entregas.
* **Decidir e fazer em sessões separadas.** O `/propose` conversa e escreve a página; o `/apply` a constrói em uma sessão nova, só com a página e os documentos: um contexto que cresce perde precisão ([capítulo 2](02-how-agents-see.md)), então a construção começa limpa, com o alvo escrito, sem a conversa que o decidiu.
* **Os documentos guardam os fatos.** Os comandos só dizem quais documentos ler e o que nunca fazer.
* **Uma fila**, uma linha por entrega. Sem especificação formal, sem arquivamento, sem pasta de change. O roteiro guardava juntos o plano de cada entrega e o seu raciocínio, então ler a lista era ler tudo; a fila guarda uma linha por entrega, e a página guarda o raciocínio.
* **O agente nunca faz commit.** Ele prepara o trabalho com `git add`; a pessoa revisa e faz o commit. Nenhuma das 29 verificações jamais tinha pegado um erro do produto, então a verificação que olha o produto é a revisão que a pessoa faz de cada commit.
* **O regulador.** Tudo o que quiser voltar responde a uma pergunta: que erro concreto isso teria pegado?

Esse processo levou o Ninjobs à abertura ao público em 2026-09-10.[^ninjobs]
Depois eu o transformei no focus-kit, o kit que este livro ensina.

Uma regra veio mais tarde.
Quando o Ninjobs adotou o kit, o `/apply` antigo ainda descrevia coisas que o projeto já tinha mudado nos documentos.[^ninjobs]
Por isso um comando não guarda nenhum fato do projeto: todo fato assim mora em um lugar só, o docs/05, o documento de processo, cuja seção "This project" (este projeto) os guarda, e o comando o lê ali (o [capítulo 6](06-the-documents.md) descreve cada documento).

## Uma lição além do processo

O recomeço também trocou a stack, de Flutter para React.
O mesmo agente errava o design em Flutter e o acertava em React.
O Flutter conseguiria construir o projeto; o limite era o que o agente tinha visto no treinamento.
Escolha uma stack pelo valor do projeto e pelo quanto o agente a conhece; o capítulo 7 mostra como.

## Pontos-chave

* No Ninjobs, o OpenSpec produziu quatro telas em quinze dias porque cada decisão morava em seis lugares e 29 verificações guardavam a forma, e não o produto.
* A solução foi ter menos lugares: uma página por entrega, documentos que guardam os fatos e comandos que só apontam para eles.
* Decidir e fazer acontecem em sessões separadas, e quem faz o commit é a pessoa, nunca o agente.
* O regulador pergunta a cada acréscimo que erro concreto ele teria pegado.
* Escolha uma stack que o agente conhece.

[^ninjobs]: Ninjobs, repositório privado, contado pelo autor no histórico até 2026-08-29, quando o ADR-0022 do projeto abandonou o OpenSpec: dias com commit e commits pelo `git log`, changes pelo arquivo do OpenSpec, linhas com `wc -l` sobre todos os arquivos de `openspec/`. As telas e a tabela são as que esse ADR lista. As causas, a alternativa recusada e a decisão são as do próprio ADR, parafraseadas; o roteiro que guardava o raciocínio de cada plano e a sessão limpa com um alvo escrito vêm dos pareceres independentes que esse ADR cita, também parafraseados. O ADR-0026 do projeto, datado de 2026-09-21, dá a data da abertura ao público e a adoção do focus-kit.
