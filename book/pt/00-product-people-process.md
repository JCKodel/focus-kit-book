# Produto, pessoas e processo

Toda empresa que constrói software depende de três coisas: seu produto, suas pessoas e seu processo.
Depois deste prólogo você consegue dizer o que cada uma decide quando parte de quem constrói são agentes de código, e o que este livro dá a cada uma das três.

## De onde vem a ideia

Ouvi a ideia na televisão, de Marcus Lemonis, no seu reality show *The Profit*.
Uma ideia ficou comigo: toda empresa se apoia em três Ps.[^lemonis-3ps]
O site dele os ordena como pessoas, processo e produto.[^lemonis-3ps]
Este livro põe o produto primeiro, porque o produto é aquilo pelo qual todo o resto é julgado.
A ideia vem do mundo dos negócios, e cabe bem no software.

## Produto

Muitos desenvolvedores transformam o próprio desenvolvimento no produto: a melhor solução, a melhor linguagem, o melhor framework.
No caminho, perdem de vista o que importa, o produto que está sendo construído.
O código é compilado e seus usuários nunca o veem; só o produto existe, e tudo é julgado por ele.
Isso não torna o código irrelevante.
A Parte I organiza o código porque uma estrutura clara serve ao produto e ao agente que o altera: a arquitetura vale o que dá a eles, e nunca é um fim em si.
Um projeto escreve seu produto no primeiro documento, o docs/00 (capítulo 10).

## Pessoas

As pessoas, e agora os agentes, são a parte mais importante de uma empresa e a mais frágil.
Três fragilidades se repetem.

**Conhecimento nas mãos de poucos.**
Quando o que um projeto sabe vive em poucas cabeças, vai embora quando elas vão, e nunca chega a um agente, que não sabe nada no início de uma sessão (capítulo 2).
A resposta são documentos: os documentos do projeto guardam o que o projeto sabe, num lugar onde uma pessoa e um agente leem igualmente (capítulo 10).

**Opinião no lugar de evidência.**
"Eu acho" vence uma reunião quando ninguém pergunta a fonte.
A resposta é citá-la: todo número e toda afirmação levam sua fonte, como toda nota deste livro.
Nada neste livro é novo: as práticas da Parte I foram nomeadas por outros, décadas atrás, e cada capítulo diz por quem e onde.
O que há de novo é que um agente de código as segue sem se cansar, uma vez escritas onde ele lê.

**Ego.**
O autor de um trabalho o defende porque é dele, seja esse autor um colega, um agente ou você.
A resposta é um papel: a pessoa interpreta, orienta e valida, e não confia cegamente em ninguém, agente ou colega, incluindo o autor do código.

## Processo

Nenhuma engenharia de software sobrevive sem um processo: quando cada pessoa faz as coisas do seu jeito, o resultado é o caos.
Um processo é seguido porque cada passo tem um propósito, e o propósito é também o teste.
Um passo que não pega nenhum erro concreto sai do processo (capítulo 17), e processo demais falha tão certamente quanto processo de menos (capítulos 1 e 9).

O processo que este livro ensina roda sobre documentos que um agente lê, e isso muda a quem o processo serve.
Quando o produto, seu vocabulário, suas decisões e sua fila estão escritos onde o agente os lê, o agente pode responder a qualquer pessoa do time: o que está pendente, como está indo, quem deve uma resposta, o que foi combinado com o cliente.
Dê a ele também os e-mails e as propostas, e o projeto vira um assistente do time inteiro, desenvolvedores e gestores (capítulo 18).
É para esse ganho que este livro foi escrito.

## O que o time ganha

Um produto escrito, conhecimento em documentos em vez de cabeças, e um processo que todos seguem porque cada passo tem um motivo.
O método é o mesmo para um desenvolvedor e para uma empresa.
Ele levou meu próprio produto, a Ninjobs, de quatro telas em quinze dias à abertura ao público treze dias depois (capítulo 9), e conduziu um projeto de cliente de 73 entregas em oito dias de commits, o Caso A (capítulo 18).[^ninjobs][^case-a]

A Parte I é a base, as práticas que todo leitor precisa compartilhar antes do processo, de por que o processo importa quando a IA escreve rápido até um teste para cada peça de código.
A Parte II é o método, o focus-kit, dos seus documentos ao projeto como assistente do time.
A Parte III é o git e as ferramentas do time.
A Parte IV vai além do código: projetos que não são software, quanto custam os agentes e a adoção numa empresa.

## Pontos-chave

* Toda empresa que constrói software se apoia em três Ps: produto, pessoas e processo.
* O produto é o que é julgado; o código serve a ele, e a Parte I organiza o código para o produto e para o agente que o altera.
* Pessoas e agentes são a parte mais importante e a mais frágil: documentos respondem ao conhecimento nas mãos de poucos, fontes respondem à opinião, e uma pessoa que valida responde ao ego.
* Um processo é seguido porque cada passo tem um propósito; um passo que não pega nenhum erro concreto sai dele.
* Quando o processo roda sobre documentos que um agente lê, o projeto responde ao time inteiro, e é para esse ganho que este livro foi escrito.

[^lemonis-3ps]: Marcus Lemonis Business Team, "3 Key To Business Success: People, Process & Product", acesso em 2026-09-28. <https://marcuslemonis.com/business/3ps-of-business>
[^ninjobs]: Ninjobs, o produto do autor, um repositório privado, contado pelo autor ao longo do seu histórico: a era OpenSpec a partir do seu ADR-0022 (quinze dias, 87 commits, quatro telas); a virada em 2026-08-29 e a abertura ao público em 2026-09-10 a partir dos seus ADRs e do `git log`; 93 páginas concluídas em `work/done/`, 132 commits em 19 dias até 2026-09-23, e as linhas e marcas da fila a partir do docs/06.
[^case-a]: Caso A, um projeto para um cliente em uma plataforma low-code, um repositório privado, contado pelo autor: 80 linhas de fila, 73 delas concluídas, no docs/06; 65 páginas em `work/done/` mais 8 entregas de pergunta cujas páginas ficam fora do repositório; 115 commits em 8 dias ao longo de 10 dias corridos, a partir do `git log`; 16 ADRs. Seu dono, seu cliente e seu negócio não são revelados.
