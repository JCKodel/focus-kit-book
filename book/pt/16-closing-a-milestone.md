# Fechando um marco

Depois deste capítulo você consegue fechar um marco: conferir o seu parágrafo no produto rodando, revisar tudo o que ele construiu com o que o seu host oferece, e decidir cada achado.
Então você consegue transformar cada achado confirmado em uma linha de um marco novo, `<M>.1`, em vez de uma correção.

## O problema

Cada página de um marco foi lida antes de o `/apply` construí-la, e cada mudança em stage foi revisada antes do seu commit.
Ninguém olhou para o que elas somam.
Um processo leve não tem barreira entre as entregas, então o risco que ele carrega é a soma: cada entrega certa na sua própria página, e o todo ainda errado.
Uma consulta que era rápida com os dados da primeira página e fica lenta quando cinco entregas enchem as tabelas, uma função auxiliar copiada em quatro features, uma afirmação do marco que nenhuma entrega assumiu: nenhuma delas reprova na revisão de uma entrega só.

## A revisão é uma entrega

O kit fecha essa brecha com uma regra, o §8 do documento de processo que ele escreve, o docs/05.
A última linha de todo marco é a sua revisão, `<milestone>-review`, uma entrega como as outras: o `/propose` escreve a sua página, e o `/apply` a executa.
A página nomeia o que olhar: o intervalo de commits do marco, o seu parágrafo, e o comando de revisão do host com o seu nível.
A execução confere o parágrafo cláusula por cláusula contra o que as entregas construíram, revisa o código, e não corrige nada.
Cada problema que ela relata é um achado, e a decisão sobre cada um é sua.

## Confira o parágrafo

Um marco termina com um parágrafo escrito como um teste que uma pessoa consegue conferir no produto (capítulo 13).
Para um marco da biblioteca de empréstimos, escrito para este capítulo:

```
Quando ele fecha, um bibliotecário consegue emprestar um exemplar e registrar
a sua devolução, e um membro vê os seus empréstimos com a data de devolução
de cada um.
```

Confira o parágrafo no produto rodando, cláusula por cláusula, ponta a ponta, uma vez, na ordem em que um bibliotecário e um membro as encontrariam: emprestar um exemplar, registrar a sua devolução, abrir os empréstimos do membro e ler as datas de devolução.
A checagem de cada entrega testou a sua própria parte; esta roda todas juntas, como o produto é usado.
Uma cláusula que não se sustenta é um achado como outro qualquer, e também uma cláusula que nenhuma entrega atendeu.

## Revise tudo o que o marco construiu

Depois revise o código do marco inteiro, com o que o seu host oferece.
No Claude Code a revisão é o `/code-review`; ele recebe um alvo, como um branch (uma linha de trabalho à parte) ou um intervalo de commits, e um nível que troca confiança por cobertura: `low` e `medium` relatam só os achados de que ele tem mais certeza, e de `high` a `max` ampliam a cobertura e podem incluir achados de que ele tem menos certeza.[^claude-code-review]
Para um marco, o intervalo começa no último commit antes dele e termina no último dele:

```
/code-review high <commit before the milestone>...<last commit of the milestone>
```

Um marco é revisado uma vez, como um todo, então ali a amplitude vale mais do que a certeza, e as decisões abaixo filtram o que é incerto.
A revisão só relata; ela muda os seus arquivos só quando você pede que ela corrija, e aqui você não pede.[^claude-code-review]

Outros hosts oferecem o mesmo olhar.
O Codex tem `/review` em uma sessão e `codex review --base <branch>` no terminal, que revisam as mudanças contra um branch de base.[^codex-review]
O GitHub Copilot revisa pull requests (pedidos de merge que alguém revisa antes), então ali o marco sobe como um pull request do seu primeiro commit ao último.[^copilot-review]

## Decida cada achado

Um achado se lê como um fato, e alguns não são.
A pessoa é o cérebro da operação (capítulo 10): você confere o que o agente escreve contra o que você sabe, e uma revisão é o agente escrevendo.
Isso significa duas coisas: você nunca aceita um achado como verdadeiro sem olhar o código, e nunca descarta um sem dizer por quê.

Então cada achado é confirmado ou rejeitado, com um motivo.
Uma rejeição nomeia o que a revisão não pesou: uma escolha que um documento registra de propósito, uma ordem que outro documento fixa, um teste que já protege o caso, uma escala que o produto não vai alcançar.
Uma confirmação é conferida no código primeiro.
Um achado pode se dividir: uma função duplicada confirmada, uma consulta lenta ao lado dela rejeitada porque a tabela guarda meia dúzia de linhas.

## Uma linha, e não uma correção

Cada achado confirmado vira uma linha `[ ]` em um marco novo, posto logo depois do revisado e numerado com `.1`: o marco 1 é seguido pelo marco 1.1, com o seu próprio parágrafo, então nada muda de número.
Cada linha diz o que vai ser verdade, nunca como corrigir, e uma linha sobre código copiado nomeia a primeira cópia, como pede a regra da segunda ocorrência (capítulo 4).
Cada uma é uma entrega: o `/propose` vai escrever a sua página e o `/apply` vai construí-la.
Nenhum achado confirmado, nenhum marco novo.

Uma linha, e não uma correção, porque uma correção feita no meio do marco seguinte não tem página nem revisão.
Ninguém lê o escopo dela antes de ela ser construída, ninguém a confere contra uma página depois, e ela cai em um marco cujo parágrafo não a menciona.
Como linha, ela espera a sua vez, e ganha as duas coisas.

Faça do `.1` a última rodada, sem revisão própria.
O arquivo do kit deixa um `.1` terminar com a sua própria revisão, que pode abrir um `.2`; eu parei de permitir isso, porque uma revisão das correções acha achados próprios, e uma revisão desses acha mais.
Uma rodada só mantém a revisão como um passo que tem fim.
O `.1` fecha quando as suas linhas estão `[x]` com a sua prova, e o que ele deixou passar é achado pela revisão do marco seguinte.

## Quando os achados viraram uma entrega

Na Ninjobs, a revisão na abertura ao público devolveu oito achados, com toda a suíte de testes verde.[^ninjobs]
Consultas levavam centenas de milissegundos, uma vaga de emprego grande teria estourado o tempo limite, e três dos achados eram sobre segurança.[^ninjobs]
Cada entrega tinha passado nos seus próprios testes e na sua própria revisão; só o olhar sobre o todo os viu.

Eu pus os oito em uma entrega em vez de oito linhas.
A página dela diz, com as suas próprias palavras, que não cabe em uma página e que quebra a regra de propósito, e ela chegou a 879 linhas, a página mais longa do projeto.[^ninjobs]
As correções se sustentaram: a página mediu a triagem de vagas em cerca de 620 ms no banco de dados de desenvolvimento quando o trabalho começou, e em 94 ms quando terminou.[^ninjobs]
Mas quando eu mesmo conferi o resultado, achei falhas que os testes dela não tinham pegado.
A causa não foi o processo; foi a minha escolha.
Oito linhas teriam sido oito páginas, cada uma pequena o bastante para ser lida antes de ser construída e conferida depois.

## O que o time ganha

A revisão de marco pega as falhas que os testes não alcançam, antes dos usuários.
Na Ninjobs ela achou oito com todos os testes verdes, três delas sobre segurança, no dia em que o produto abriu ao público.[^ninjobs]
E como cada achado vira uma linha, o time vê o custo das brechas do marco na fila, ao lado de tudo o que planeja, e não em correções que ninguém revisou.

## Pontos-chave

* Uma revisão de marco olha para o que as entregas somam, o que nenhuma revisão de uma página ou de uma mudança em stage consegue ver.
* A revisão é a última linha do marco, `<milestone>-review`, rodada com o `/propose` e o `/apply`: ela confere o parágrafo cláusula por cláusula no produto rodando, revisa o intervalo do marco com o que o seu host oferece, e não corrige nada.
* Decida cada achado com o seu motivo, depois de olhar o código: nunca confie em um às cegas, nunca descarte um sem motivo.
* Um achado confirmado vira uma linha `[ ]` em um marco novo `<M>.1` logo depois do revisado, nunca uma correção no meio do marco seguinte.
* Um `.1` é a última rodada e não tem revisão própria; a revisão do marco seguinte acha o que ele deixou passar.

[^claude-code-review]: Anthropic, "Code Review", documentação do Claude Code, acesso em 2026-09-28. <https://code.claude.com/docs/en/code-review>
[^codex-review]: OpenAI, "Developer commands", acesso em 2026-09-28. <https://learn.chatgpt.com/docs/developer-commands?surface=cli>
[^copilot-review]: GitHub, "About GitHub Copilot code review", acesso em 2026-09-28. <https://docs.github.com/en/copilot/concepts/agents/code-review>
[^ninjobs]: Ninjobs, o produto do autor, um repositório privado, lido pelo autor na página de `work/done/` da entrega que recebeu os oito achados da sua primeira revisão de marco: os achados (o seu conteúdo parafraseado, os achados de segurança deixados de fora), as suas 879 linhas contadas com `wc -l`, a mais longa das suas 93 páginas, e os tempos de triagem como a página os registra, medidos no banco de dados de desenvolvimento em 2026-09-10.
