# 6. Como o focus-kit nasceu

No Ninjobs, meu próprio produto, eu abandonei o OpenSpec depois de quinze dias e escrevi o processo que virou o focus-kit.
Depois deste capítulo você consegue contar essa história, como era, o que deu errado e para onde foi, e dizer a que falha responde cada regra do focus-kit.

## Como era

O Ninjobs começou com o OpenSpec, uma das ferramentas de Desenvolvimento Guiado por Especificação do capítulo 2.
Cada feature era uma mudança, uma pasta com sua proposta, suas especificações, seu design e suas tarefas, e cada decisão era escrita de novo nos documentos do projeto e nos seus ADRs, os registros de decisão de arquitetura, um arquivo por decisão.
Antes de uma entrega contar como pronta, ela precisava passar por 29 verificações.

Em quinze dias, isso produziu 37.228 linhas de especificação, para quatro telas e uma tabela de dados.
Nada do fluxo central do produto existia ainda.

## O que deu errado

Quando eu parei, o registro de decisão que escrevi apontava cinco causas, e quatro revisões independentes do projeto tinham chegado ao mesmo diagnóstico.

1. **Retorno visual lento.**
   O app era em Flutter, e quatro mudanças seguidas serviram só para deixar as telas perto do design.
2. **Uma stack que o agente tinha visto pouco.**
   O design customizava o Material 3, o sistema de design do Google, que o Flutter implementa, e o agente tinha visto poucos exemplos disso no treinamento, então chutava valores em pixels.
3. **Oito arquivos para mostrar um campo.**
   Eu exigia a forma completa do FOCUS, as quatro peças do capítulo 4, em toda feature, até num formulário trivial.
   A arquitetura era sólida; eu tinha perdido o KISS e o YAGNI, os dois princípios do capítulo 3 que decidem quando uma peça se paga, e deixei a complexidade crescer.
4. **Verificações que guardavam a forma.**
   As 29 verificações eram caras de satisfazer e baratas de contornar, e nenhuma jamais tinha falhado num erro do produto.
   Uma verificação que nunca pegou um erro do produto é cerimônia.
5. **Seis lugares para uma verdade.**
   Uma decisão morava nos documentos, nas especificações, nas mudanças, nos ADRs, num roteiro do trabalho e no código, e cada um podia ficar desatualizado sozinho.
   Toda entrega tinha de manter os seis em acordo.

Um OpenSpec mais enxuto não teria ajudado.
O custo estava no número de lugares, e não no tamanho de cada arquivo.

## Para onde foi

Em 2026-08-29 eu recomecei, com um processo pequeno o bastante para caber na cabeça, e mudei o app de Flutter para React, onde o mesmo agente acertou o design.
Uma entrega virou uma página, `work/<slug>.md`.
Dois comandos faziam o trabalho: o `/propose` conversa comigo e escreve a página, nunca código; o `/apply` constrói a página, faz a verificação e compara a tela com o design.
A fila virou uma linha por entrega.
Das 29 verificações, ficaram duas, ambas voltadas para o próprio produto: uma prova do que cada nível de privacidade de um perfil pode mostrar, e um teste das regras de acesso do banco de dados.
Tudo o que quisesse voltar tinha de responder a uma pergunta, o regulador: que erro concreto isso teria pegado?
Uma verificação voltou mais tarde, porque apontou um erro que tinha acontecido.

O Ninjobs abriu ao público em 2026-09-10, treze dias depois do recomeço, com 91 entregas de uma página concluídas.
As linhas concluídas da sua fila citam 19 pranchas de design, contra quatro telas nos quinze dias anteriores.

Em 2026-09-21 eu tirei o processo do Ninjobs e o transformei no focus-kit, o kit que este livro ensina.
O gatilho foi uma divergência: os próprios arquivos de comando do projeto ainda descreviam passos que o seu documento de processo, o docs/05, já tinha mudado.
Dali em diante os comandos não guardam nenhum fato do projeto, e leem todos eles no docs/05.

## Cada regra e sua falha

O kit mantém seis regras em todo projeto, as que o seu `SETUP.md` lista no §2, e toda regra existe porque alguma coisa falhou sem ela.
Qualquer outra verificação é do próprio projeto.

* **Uma entrega é uma página.**
  Responde à pasta de cada mudança, com uma proposta, especificações, um design e tarefas para uma feature: o que construir e o que fica de fora moram numa página, e um escopo que não cabe são duas entregas (capítulo 12).
* **Decidir e fazer em sessões separadas.**
  Responde à construção que decide enquanto anda: o `/apply` começa limpo, com a página e os documentos, sem a longa conversa que a decidiu, já que um contexto que cresce perde precisão; o `/propose` não escreve código e o `/apply` não amplia o escopo.
* **O agente coloca em stage e sugere a mensagem do commit.**
  O agente nunca faz commit nem merge por conta própria; quando pedem, ele dá o passo que a pessoa nomeia.
  Responde às 29 verificações que nunca olhavam o produto: a verificação que olha é uma pessoa lendo cada mudança antes que ela entre no histórico (capítulo 13).
* **O que é específico do projeto são slots no docs/05 do projeto.**
  O comando de verificação, os ambientes, a prova e a estratégia de git são preenchidos uma vez ali, e o `/apply` os lê.
  Responde à divergência: um comando que repete um fato do projeto fica desatualizado quando o documento muda, então o comando só diz qual slot ler (capítulo 7).
* **Os documentos são vivos.**
  Uma entrega que muda um comportamento atualiza o documento dono dele, na mesma entrega.
  Responde aos seis lugares: cada fato tem um dono, e a entrega que muda o fato muda o dono, então nenhuma cópia fica desatualizada sozinha (capítulo 7).
* **Nada entra sem dizer o erro concreto que teria pegado.**
  Responde ao crescimento das verificações, cada uma plausível sozinha e todas juntas mais pesadas que o trabalho (capítulo 16).

A fila de uma linha por entrega serve a essas regras sem ser uma delas.
Ela responde ao roteiro, que guardava juntos o plano de cada entrega e o seu raciocínio, então ler a lista era ler tudo; a linha diz o quê, e a página guarda o raciocínio (capítulo 11).

## O que o time ganha

Um processo que carrega o produto em vez de pesar sobre ele.
Antes, o processo antigo deu ao Ninjobs quatro telas em quinze dias, com cada decisão repetida em muitos lugares e verificações que nunca pegaram um erro do produto.
Depois, uma página por entrega deu a abertura ao público em treze dias, com cada fato num lugar só e duas verificações voltadas para o produto.

## Pontos-chave

* O custo estava no número de lugares, e não no tamanho de cada arquivo; a arquitetura era sólida, e eu perdi o KISS e o YAGNI ao exigir sua forma completa em toda feature.
* Comece do mínimo que se sustentou no Ninjobs: uma página por entrega, dois comandos, uma linha de fila por entrega, duas verificações e a pergunta do regulador.
* Cada uma das seis regras do kit responde a uma falha: uma feature espalhada por uma pasta de arquivos, uma construção que decide enquanto anda, verificações cegas ao produto, comandos que divergem, uma decisão guardada em muitos lugares e verificações que cresceram sem ninguém pedir; qualquer outra verificação é do próprio projeto.

