# Produto, pessoas e processo

Toda empresa que constrói software depende de três coisas: seu produto, suas pessoas e seu processo.
Depois deste prólogo você consegue dizer o que cada uma ensina quando parte de quem constrói são agentes de código, e qual parte do livro responde a cada uma.

## De onde vem a ideia

Ouvi a ideia na televisão, de Marcus Lemonis, no reality show dele, *The Profit*.
Do que o programa trata não importa aqui; uma ideia ficou comigo: toda empresa se apoia em três P's.[^lemonis-3ps]
O site dele os ordena como pessoas, processo e produto.[^lemonis-3ps]
Este livro põe o produto primeiro, porque o produto é o que julga todo o resto.
A ideia vem dos negócios, não do software, e serve bem ao software.

## Produto

Muitos desenvolvedores transformam o próprio desenvolvimento no produto: a melhor solução, a melhor linguagem, o melhor framework.
No caminho, perdem de vista o que importa, o produto que estão construindo.
No fim do dia o código é compilado e os usuários nunca o veem; só o produto existe, e tudo é julgado por ele.
Isso não torna o código irrelevante.
A Parte III organiza o código porque uma estrutura clara serve ao produto e ao agente que o altera: a arquitetura vale o que dá a eles, e nunca é um fim em si.
Um projeto escreve o seu produto no primeiro documento, docs/00 (capítulo 6).

## Pessoas

As pessoas, e agora os agentes, são a parte mais importante de uma empresa e a mais frágil.
Três fragilidades se repetem.

**Conhecimento na mão de poucos.**
Quando o que um projeto sabe vive em poucas cabeças, vai embora quando elas vão, e nunca chega a um agente, que não sabe nada no início de uma sessão nova (capítulo 2).
A resposta são documentos: os documentos do projeto guardam o que o projeto sabe, onde uma pessoa e um agente leem (capítulo 6).

**Opinião no lugar de evidência.**
"Eu acho" vence uma reunião quando ninguém pede a fonte.
A resposta é citá-la: todo número e toda afirmação trazem a sua fonte, como faz cada nota deste livro.

**Ego.**
O autor de um trabalho o defende porque é dele, seja esse autor um colega, um agente ou você.
A resposta é um papel: a pessoa interpreta, guia e valida, e não confia cegamente em ninguém, agente ou colega, incluindo o autor do código.

## Processo

Nenhuma engenharia de software sobrevive sem um processo: quando cada pessoa faz do seu jeito, o resultado é caos.
Uma vez alguém me perguntou no LinkedIn como eu garanto que todos numa empresa sigam o mesmo padrão.
A pergunta me pegou de surpresa, e respondi com uma pergunta: "Você tem uma empresa de profissionais, ou uma creche cheia de crianças?"
O processo que uma empresa define não é uma sugestão, porque tem um propósito.

O propósito também é o teste.
Um passo que não pega nenhum erro concreto sai do processo (o regulador, capítulo 13), e processo demais falha tanto quanto processo de menos (capítulo 1, capítulo 4).
A evidência de que um processo importa quando um agente escreve o código está no capítulo 1.

## Por que este livro, e o Caso B

Este livro também é o material de um programa de adoção para uma empresa, o Caso B, que já usa IA e não tem um jeito comum de usá-la: cada pessoa decide sozinha o que pedir, onde e a que custo.
O que o livro dá a uma empresa assim é o que este prólogo nomeou: um produto por escrito, conhecimento em documentos em vez de cabeças, e um processo que todos seguem porque cada passo tem um motivo.
O método é o mesmo para um desenvolvedor e para uma empresa.
A Parte I é o porquê, a Parte II o processo, a Parte III o código, a Parte IV o git da equipe, e a Parte V o que vai além do código, do quanto os agentes custam e onde compensam (capítulo 24) à adoção numa empresa (capítulo 25).

## Pontos-chave

* Toda empresa que constrói software se apoia em três P's: produto, pessoas e processo.
* O produto é o que é julgado; o código serve a ele, e a Parte III organiza o código para o produto e para o agente que o altera.
* Pessoas e agentes são a parte mais importante e a mais frágil: documentos respondem ao conhecimento na mão de poucos, fontes respondem à opinião, e uma pessoa que valida responde ao ego.
* O processo de uma empresa é seguido porque cada passo tem um propósito; um passo que não pega nenhum erro concreto sai dele.
* O método é o mesmo para um desenvolvedor e para uma empresa, e este livro também é o material de um programa de adoção (Caso B).

[^lemonis-3ps]: Marcus Lemonis Business Team, "3 Key To Business Success: People, Process & Product", acesso em 2026-09-28. https://marcuslemonis.com/business/3ps-of-business
