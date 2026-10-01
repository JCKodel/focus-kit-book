# Prólogo: Produto, pessoas e processo

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
O próprio produto é escrito, num documento que o time e o agente leem antes de agir, e o capítulo 10 mostra esse documento e os outros que o acompanham.

## Pessoas

As pessoas, e agora os agentes, são a parte mais importante de uma empresa e a mais frágil.
Três fragilidades se repetem.

**Conhecimento nas mãos de poucos.**
Quando o que um projeto sabe vive em poucas cabeças, vai embora quando elas vão, e nunca chega a um agente, que não sabe nada no início de uma sessão, como o capítulo 2 explica.
A resposta são documentos: o que o projeto sabe fica escrito num lugar onde uma pessoa e um agente leem igualmente.

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
Um passo que não pega nenhum erro concreto sai do processo, e processo demais falha tão certamente quanto processo de menos; os capítulos 1 e 9 mostram a segunda falha, e o capítulo 17 transforma a primeira regra numa pergunta.

O processo que este livro ensina roda sobre documentos que um agente lê, e isso muda a quem o processo serve.
Quando o produto, seu vocabulário, suas decisões e sua fila estão escritos onde o agente os lê, o agente pode responder a qualquer pessoa do time: o que está pendente, como está indo, quem deve uma resposta, o que foi combinado com o cliente.
Dê a ele também os e-mails e as propostas, e o projeto vira um assistente do time inteiro, desenvolvedores e gestores; o capítulo 18 mostra como.
É para esse ganho que este livro foi escrito.

## O que o time ganha

Um produto escrito, conhecimento em documentos em vez de cabeças, e um processo que todos seguem porque cada passo tem um motivo.
O método é o mesmo para um desenvolvedor e para uma empresa.
Ele levou meu próprio produto, a Ninjobs (<https://www.ninjobs.app>), de quatro telas em quinze dias à abertura ao público treze dias depois, a história que o capítulo 9 conta, e conduziu um projeto de cliente de 73 entregas em oito dias de commits, o Caso A, que o capítulo 18 conta.
Os dois repositórios são privados, então todo número que este livro dá sobre eles foi contado por mim ao longo dos seus históricos; a Ninjobs aparece pelo nome, e o Caso A sem o seu dono, o seu cliente ou o seu negócio.

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
