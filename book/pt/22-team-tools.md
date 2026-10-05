# 22. As ferramentas do time: pull requests, issues e quadros

Depois deste capítulo você consegue levar uma entrega ao branch principal por um pull request cuja revisão lê a página antes do diff, e manter issues e um quadro em sintonia com a fila sem fazer de nenhum deles a fonte da verdade.
Você também consegue dizer por que os documentos de um projeto ficam em docs/ e nunca numa wiki.

## O problema

Uma pessoa trabalhando no trunk revisa a mudança em stage e faz o commit.
Um time precisa de mais duas coisas: uma segunda pessoa que revisa antes do merge, e um jeito de quem nunca abre o repositório, um gerente ou um cliente, ver o progresso.
As estratégias de git do capítulo 20 param no merge: elas dão forma ao histórico, e não dizem nada sobre quem revisou uma mudança ou quem acompanha o trabalho.

## O pull request como a revisão do time

Um pull request é um pedido, feito num host de código como o GitHub, para fazer o merge de um branch em outro.
Ele reúne a descrição, os commits, as verificações automáticas e o diff num só lugar, onde os revisores comentam e aprovam: nas palavras do GitHub, "*Um pull request reúne o contexto de que os revisores precisam para entender uma mudança*".[^gh-prs]
O GitLab chama a mesma coisa de merge request.

Com o focus-kit, um pull request carrega uma entrega:

1. **Um branch por entrega**, com o nome do seu slug.
2. **A página primeiro.** O primeiro commit no branch é `work/<slug>.md`, escrita pelo `/propose`.
   Abra o pull request assim que ele for enviado, e a página pode ser revisada antes de existir qualquer código.
3. **A construção depois.** O `/apply` constrói no mesmo branch; a página vai para `work/done/` e a linha da fila vira `[x]` na mesma mudança.
4. **Um merge.** A entrega chega inteira ao branch principal, com a sua página, o seu código, os seus testes, a sua prova e a sua marca, então a fila no branch principal guarda o que já chegou; um `[~]` ou `[*]` posto em um branch só aparece nele (capítulo 16).

O revisor lê a página, depois o diff contra ela.
Cada linha de Comportamento tem o seu teste ou a sua checagem manual; o Contrato bate com o código até os nomes; nada listado em Fora do escopo foi construído; cada item do Pronto quando está marcado com a sua prova.
Uma mudança no diff que a página não pede é o primeiro achado, qualquer que seja a sua qualidade.

O primeiro revisor pode ser um agente: o comando de revisão do próprio host, ou a revisão de código do GitHub Copilot, que lê as instruções personalizadas e de agente do repositório no branch em revisão, então conhece as mesmas regras que o agente que construiu a mudança.[^copilot-review]
A documentação do GitHub dá o próprio limite: "*Sempre valide o feedback do Copilot com cuidado. Complemente o feedback do Copilot com uma revisão humana.*"[^copilot-review]
A revisão do agente encontra o que uma pessoa cansada lê por cima; a pessoa decide o que é um achado, e aprova o merge.

## Issues

Uma issue é o registro do GitHub para "*ideias, feedback, tarefas ou bugs*", aberta na web por qualquer pessoa com acesso, inclusive gente de fora do time.[^gh-issues]
Isso faz dela uma boa porta de entrada para o relato de bug de um usuário.

Uma linha da fila pode espelhar uma issue, e o slug nomeia as duas: o título da issue começa com o slug, e a linha termina com o número da issue.

```text
[ ] corrigir-data-de-devolucao  devolução um dia antes no fim do mês (#42)
```

O pull request diz "Fixes #42", e o GitHub fecha a issue quando o merge acontece.[^gh-issues]
A fila continua a fonte da verdade, porque o agente lê o repositório e nunca uma página web: uma issue sem linha na fila não existe para o `/propose`.
Então uma issue vira uma linha por conversa, e daí em diante é uma entrega como qualquer outra.

## Quadros

Um quadro mostra o trabalho como cartões em colunas, uma coluna por etapa.
O Azure DevOps, o produto da Microsoft para planejar e construir software, descreve o seu quadro kanban assim: "*os membros do time arrastam cartões entre as colunas para atualizar o status*".[^azure-kanban]
Um gerente abre um quadro; raramente abre um repositório.
Um quadro cujos cartões são movidos à mão, porém, é uma segunda fila, e se afasta da primeira no dia em que alguém esquece de arrastar um cartão.

A resposta é um espelho numa só direção, da fila para o quadro.
No Caso A, um projeto para um cliente em uma plataforma low-code, uma customização registrada no seu docs/05 fazia isso: um script e um pipeline enviavam a fila, numa só direção, ao quadro kanban do projeto no Azure DevOps, então o gerente de projeto acompanhava o progresso no portal sem perguntar a um desenvolvedor.
O `/propose` e o `/apply` atualizavam o quadro sempre que mudavam uma marca, e avisavam sempre que não conseguiam, então um quadro desatualizado nunca ficava em silêncio.
Com as seis marcas do capítulo 16, um espelho as dobra nas três colunas de um quadro: `[ ]` para To Do, `[~]`, `[>]` e `[*]` para Doing, `[x]` para Done; uma linha `[?]` deixa o cartão dela na coluna em que estava e o etiqueta como travado, com o motivo.
O espelho vai numa só direção porque a fila é o único lugar que o agente lê: um cartão movido no quadro não muda nada no repositório, e uma sincronização nas duas direções criaria duas fontes da verdade.
Uma peça ainda não estava provada quando o projeto fechou: a permissão de escrita da identidade do pipeline no quadro.

### Uma marca para a espera

Também faltava uma palavra à fila do Caso A: cinco linhas bloqueadas pelo cliente apareciam como trabalho que ninguém tinha começado, e o Caso A acrescentou uma marca à mão, `[?]`, para uma linha esperando por uma pessoa.
O kit adotou essa marca na sua versão 2026.10.05, com os outros dois motivos de uma linha esperar (capítulo 16).
O que continua uma customização do próprio Caso A são as suas entregas de pergunta, cujo único resultado é uma resposta escrita de alguém de fora do projeto: elas fecham na resposta, não no envio, porque uma sessão certa vez marcou uma delas como concluída quando o email saiu.

## Por que a wiki não é o docs/

O GitHub dá a todo repositório uma wiki, e ela parece a casa natural dos documentos de um projeto.
Ela é um segundo repositório, editado na web, sem pull requests e sem build.
O agente na pasta do projeto não a lê, e nenhuma entrega a muda, então ela se afasta do código na primeira entrega que a esquece.
O docs/ muda no mesmo commit que o código que descreve, e é revisado no mesmo pull request.
Este livro tomou a mesma decisão para si: nenhuma wiki, escrita ou espelhada; uma só fonte gera o site e o PDF.

## O que o time ganha

O gerente vê o progresso sem perguntar a um desenvolvedor, e a revisão lê uma página antes de ler um diff, então uma mudança que ninguém pediu é encontrada na primeira pergunta.
Não há número medido para esse ganho: o quadro do Caso A rodou em um projeto, e a sua permissão de escrita nunca foi provada.

## Pontos-chave

* Um pull request carrega uma entrega: um branch com o nome do slug, a página primeiro, a construção depois, um merge com a página, o código e a marca.
* O revisor lê a página, depois o diff contra ela; um agente pode revisar primeiro, e uma pessoa decide.
* Uma issue espelha uma linha da fila pelo slug, e a fila continua a fonte da verdade, porque o agente lê o repositório.
* Um quadro é um espelho da fila numa só direção, atualizado quando uma marca muda, e nunca em silêncio quando não consegue ser.
* `[?]` começou como a marca do Caso A para linhas que esperam por uma pessoa e hoje é do kit; as entregas de pergunta, que fecham na resposta, continuam uma customização do Caso A.

[^gh-prs]: GitHub Docs, "Pull requests", seção "Working with pull requests", acesso em 2026-09-30. <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>
[^copilot-review]: GitHub Docs, "About GitHub Copilot code review", seções "Agent skills" e "Validating Copilot code reviews", acesso em 2026-09-30. <https://docs.github.com/en/copilot/concepts/agents/code-review>
[^gh-issues]: GitHub Docs, "About issues", acesso em 2026-09-30. <https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues>
[^azure-kanban]: Microsoft Learn, "About Kanban boards", Azure Boards, acesso em 2026-09-30. <https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview>
