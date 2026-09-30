# Como o focus-kit nasceu

No Ninjobs, meu próprio produto, eu abandonei o OpenSpec depois de quinze dias e escrevi o processo que virou o focus-kit.
Depois deste capítulo você consegue contar essa história, como era, o que deu errado e para onde foi, e dizer a que falha responde cada regra do focus-kit.

## Como era

O Ninjobs começou com o OpenSpec, uma das ferramentas de Desenvolvimento Guiado por Especificação do capítulo 3.
Cada feature era uma mudança, uma pasta com sua proposta, suas especificações, seu design e suas tarefas, e cada decisão era escrita de novo nos documentos do projeto e nos seus ADRs, os registros de decisão de arquitetura, um arquivo por decisão (capítulo 10).
Antes de uma entrega contar como pronta, ela precisava passar por 29 verificações.[^ninjobs]

Em quinze dias, isso produziu 87 commits, 35 mudanças e 37.228 linhas de especificação, para quatro telas e uma tabela de dados.[^ninjobs]
Nada do fluxo central do produto existia ainda.

## O que deu errado

Quando eu parei, o registro de decisão que escrevi apontava cinco causas, e quatro revisões independentes do projeto tinham chegado ao mesmo diagnóstico.[^ninjobs]

1. **Retorno visual lento.**
   O app era em Flutter, e quatro mudanças seguidas serviram só para deixar as telas perto do design.
2. **Uma stack que o agente tinha visto pouco.**
   O design customizava o Material 3, o sistema de design do Google, que o Flutter implementa, e o agente tinha visto poucos exemplos disso no treinamento, então chutava valores em pixels.
3. **Oito arquivos para mostrar um campo.**
   Eu exigia a forma completa do FOCUS, as quatro peças do capítulo 7, em toda feature, até num formulário trivial.
   A arquitetura era sólida; eu tinha perdido o KISS e o YAGNI, os dois princípios do capítulo 4 que decidem quando uma peça se paga, e deixei a complexidade crescer.
4. **Verificações que guardavam a forma.**
   As 29 verificações eram caras de satisfazer e baratas de contornar, e nenhuma jamais tinha falhado num erro do produto.
   Uma verificação que nunca pegou um erro do produto é cerimônia.
5. **Seis lugares para uma verdade.**
   Uma decisão morava nos documentos, nas especificações, nas mudanças, nos ADRs, num roteiro do trabalho e no código, e cada um podia ficar desatualizado sozinho.
   Toda entrega tinha de manter os seis em acordo.

Um OpenSpec mais enxuto não teria ajudado.
O custo estava no número de lugares, e não no tamanho de cada arquivo.

## Para onde foi

Em 2026-08-29 eu recomecei, com um processo pequeno o bastante para caber na cabeça, e mudei o app de Flutter para React.[^ninjobs]
Uma entrega virou uma página, `work/<slug>.md`.
Dois comandos faziam o trabalho: o `/propose` conversa comigo e escreve a página, nunca código; o `/apply` constrói a página, faz a verificação e compara a tela com o design.
A fila virou uma linha por entrega.
Das 29 verificações, ficaram duas, ambas voltadas para o próprio produto: uma prova do que cada nível de privacidade de um perfil pode mostrar, e um teste das regras de acesso do banco de dados.
Tudo o que quisesse voltar tinha de responder a uma pergunta, o regulador do capítulo 17: que erro concreto isso teria pegado?
Uma voltou mais tarde, um lint do banco de dados, porque apontou um: um índice duplicado que nenhum teste tinha notado.[^ninjobs]

O Ninjobs abriu ao público em 2026-09-10, treze dias depois do recomeço, com 91 entregas de uma página concluídas.[^ninjobs]
As linhas concluídas da sua fila citam 19 pranchas de design, contra quatro telas nos quinze dias anteriores.[^ninjobs]

Em 2026-09-21 eu tirei o processo do Ninjobs e o transformei no focus-kit, o kit que este livro ensina.[^ninjobs]
O gatilho foi uma divergência: os próprios arquivos de comando do projeto ainda descreviam passos que o seu documento de processo, o docs/05, já tinha mudado.
Dali em diante os comandos não guardam nenhum fato do projeto, e leem todos eles no docs/05.

## Cada regra e sua falha

Toda regra do focus-kit existe porque alguma coisa falhou sem ela.

* **Uma página por entrega.**
  Responde aos seis lugares: o que construir e o que fica de fora moram numa página, e um escopo que não cabe são duas entregas (capítulo 14).
* **Decidir e fazer em sessões separadas.**
  Responde à construção que decide enquanto anda: o `/apply` começa limpo, com a página e os documentos, sem a longa conversa que a decidiu, já que um contexto que cresce perde precisão (capítulo 2).
* **Os documentos guardam os fatos; os comandos, nenhum.**
  Responde à divergência: um comando que repete um fato do projeto fica desatualizado quando o documento muda, então ele só diz quais documentos ler (capítulo 10).
* **Uma fila de uma linha por entrega.**
  Responde ao roteiro, que guardava juntos o plano de cada entrega e o seu raciocínio, então ler a lista era ler tudo; a linha diz o quê, e a página guarda o raciocínio (capítulo 13).
* **O agente coloca em stage e a pessoa faz o commit.**
  Responde às 29 verificações que nunca olhavam o produto: a verificação que olha é uma pessoa lendo cada mudança antes que ela entre no histórico (capítulo 15).
* **Nada entra sem dizer o erro que teria pegado.**
  Responde ao crescimento das verificações, cada uma plausível sozinha e todas juntas mais pesadas que o trabalho (capítulo 17).

## Escolha uma stack que o agente conhece bem

O recomeço ensinou uma lição além do processo.
Em Flutter o mesmo agente errava o design o tempo todo; em React ele o acertava.
O Flutter conseguiria construir o produto, e o limite era o que o agente tinha visto no treinamento, então eu escolho uma stack pelas necessidades do produto e pelo quanto o agente a conhece (capítulo 12).

## O que o time ganha

Um processo que carrega o produto em vez de pesar sobre ele.
Antes, quinze dias no Ninjobs deram quatro telas e 37.228 linhas de especificação, com cada decisão em seis lugares e 29 verificações que nunca pegaram um erro do produto.
Depois, treze dias deram a abertura ao público, 91 entregas de uma página cada e 19 pranchas de design entregues, com cada fato num lugar só e duas verificações voltadas para o produto.[^ninjobs]

## Pontos-chave

* No Ninjobs, o OpenSpec deu quatro telas em quinze dias: cada decisão morava em seis lugares, e 29 verificações guardavam a forma e nunca o produto.
* O custo estava no número de lugares, e não no tamanho de cada arquivo; a arquitetura era sólida, e eu perdi o KISS e o YAGNI ao exigir sua forma completa em toda feature.
* O recomeço manteve uma página por entrega, dois comandos, uma linha de fila por entrega, duas verificações e a pergunta do regulador, e chegou à abertura ao público treze dias depois.
* Cada regra do kit responde a uma falha: seis lugares, uma construção que decide enquanto anda, comandos que divergem, um roteiro que misturava plano e raciocínio, verificações cegas ao produto e verificações que cresceram sem ninguém pedir.
* Escolha uma stack pelo produto e pelo quanto o agente a conhece.

[^ninjobs]: Ninjobs, o produto do autor, um repositório privado, contado pelo autor no seu histórico. A era do OpenSpec vem do seu ADR-0022, datado de 2026-08-29: quinze dias e 87 commits pelo `git log`, 35 mudanças pelo arquivo do OpenSpec, 37.228 linhas com `wc -l` sobre todos os arquivos de `openspec/` (o ADR arredonda a própria contagem para cerca de 38,8 mil), as quatro telas e a tabela que ele lista, as 29 verificações, e as cinco causas e as quatro revisões independentes que ele cita, parafraseadas. A abertura ao público em 2026-09-10, as 91 entregas concluídas até ali e a mudança para o focus-kit em 2026-09-21 vêm do seu ADR-0026; o prólogo conta 93 páginas concluídas porque conta até 2026-09-23. As 19 pranchas de design contadas nas linhas concluídas da sua fila, o docs/06. As duas verificações mantidas e o lint que voltou vêm do seu docs/05 e dos seus ADRs.
