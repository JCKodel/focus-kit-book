# 24. Adoção em times e empresas

Depois deste capítulo você consegue levar o método a um time ou a uma empresa, responder às resistências de sempre com evidência, e dar a cada papel a sua parte.
Você também consegue rodar um marco como um piloto que mede a si mesmo, e dar forma à proposta para a sua própria empresa.

## O problema

Na maioria dos times cada pessoa já usa IA, cada uma do seu jeito: uma conversa num navegador, outra deixa um agente editar o repositório inteiro, outra se recusa a tocar nisso.
Cada uma paga o seu próprio custo, em tokens e em retrabalho, e ninguém vê, porque não há um padrão comum contra o qual medir.
Quando o time discute o assunto, vence a opinião mais alta, e o [prólogo](00-product-people-process.md) deu nome a essa falha: opinião no lugar de evidência.

## A resistência, e a sua resposta

Três objeções aparecem em todo time.
Cada uma tem uma resposta que pede evidência em vez de fé.

**"O meu jeito funciona."**
Pode ser.
A regra do prólogo vale para ele como para todo o resto: uma afirmação traz a sua fonte.
Pergunte o que ele produziu, medido como: quantas entregas, quantas voltaram, quanto custaram.
Um jeito que funciona consegue mostrar isso, e o método lhe dá os meios, com uma página por entrega e uma contagem de tokens por entrega ([capítulo 23](23-cost-and-where.md)).

**"Processo demais."**
O método tem um regulador para isso ([capítulo 17](17-the-governor.md)): cada passo precisa nomear o erro concreto que teria pegado, ou sai.
O que sobrevive são seis regras e duas checagens.
Um time que acha um passo que não pega nada o remove, e o método espera que ele faça isso.

**"Nós já temos uma ferramenta."**
O método são documentos, e uma ferramenta é onde você os roda.
Os documentos, a fila e as páginas são arquivos Markdown no repositório, e qualquer host que lê arquivos consegue segui-los ([capítulo 11](11-install-and-hosts.md)).
O time mantém o seu host, o seu editor e o seu quadro.

## O que o processo pegou num projeto real

A resposta mais forte para "o que isso teria nos dado?" é um projeto que rodou nele.
O Caso A, um projeto para um cliente em uma plataforma low-code, rodou no método, e quatro das coisas que o seu processo pegou respondem a essa pergunta.

**A base assinada não batia com o que foi construído.**
O documento que o cliente tinha assinado descrevia outra coisa que não o que tinha sido construído.
Uma entrega de pergunta, uma linha da fila cujo único propósito é uma resposta escrita, perguntou ao cliente contra qual dos dois o aceite seria medido, e a resposta voltou por escrito antes que qualquer trabalho dependesse dela.

**Um pedido que não podia ser construído foi encerrado, não absorvido.**
Um pedido tinha sido aceito, e o trabalho nele provou que era tecnicamente impossível.
Ele foi encerrado na fila com o motivo, sem ser construído, quando poderia ter sido largado em silêncio ou torcido em algo que ninguém pediu.

**Uma instalação limpa achou o que o ambiente de desenvolvimento escondia.**
Uma instalação num ambiente limpo falhou numa permissão que o ambiente de desenvolvimento já tinha.
Ela virou três linhas na fila e uma correção no guia de instalação.

**Um segredo foi pego antes de sair.**
Um segredo estava no pacote e teria saído com ele.
Ele foi removido primeiro, e uma varredura foi construída para que o próximo pacote não pudesse levar nenhum.

Nenhuma das quatro é um bug no código.
Cada uma foi pega porque o trabalho estava escrito em linhas e páginas que uma pessoa leu.

## Papéis num time

O método dá cada passo a quem é dono dele.

* **Quem propõe:** quem é dono da decisão.
  Um desenvolvedor propõe uma entrega técnica, um analista uma regra, um gerente uma pergunta ao cliente; o `/propose` é uma conversa, e precisa de alguém que consiga responder ([capítulo 14](14-propose.md)).
* **Quem aplica:** a sessão de um desenvolvedor, ou várias ao mesmo tempo em worktrees, cada uma na sua entrega ([capítulo 20](20-worktrees.md)).
* **Quem faz o commit e o merge:** uma pessoa, sempre.
  O `/apply` coloca em stage e para; o commit é a revisão humana ([capítulo 15](15-apply.md)).
* **Quem revisa o marco:** o time, no produto rodando, contra o parágrafo do marco ([capítulo 16](16-closing-a-milestone.md)).
* **O gerente** pergunta ao projeto: o que está pendente, como está indo, quem deve uma resposta ([capítulo 18](18-project-as-assistant.md)).

## Um marco como piloto

Não adote o método para uma empresa numa só decisão.
Rode-o num marco de um projeto, e deixe o marco decidir.

1. Instale o kit num repositório existente ([capítulo 11](11-install-and-hosts.md)).
2. Rode o `/analyze`, para que os documentos descrevam o que já existe, e revise-os ([capítulo 12](12-starting-a-project.md)).
3. Escreva um marco de três a oito linhas, cada uma uma entrega de que o time precisa de qualquer forma ([capítulo 13](13-queue-and-milestones.md)).
4. Construa-o com `/propose` e `/apply`, uma página por linha.
5. Feche-o com a sua revisão ([capítulo 16](16-closing-a-milestone.md)).

Meça duas coisas: os tokens por entrega ([capítulo 23](23-cost-and-where.md)), e o que a revisão e as páginas pegaram que de outro modo teria saído.
Depois decida com esses números na mesa, e o marco seguinte vira a comparação.

## A forma de uma proposta

Para levar o método a uma empresa, comece pelos problemas dela, e ligue cada um à parte do método que o responde.
O Caso B, a proposta de uma consultoria para o programa de adoção de um cliente, tinha uma nota interna que fazia exatamente isso.
Em linhas gerais, e com as minhas palavras, a correspondência era esta:

| O problema do cliente | A parte do método |
|---|---|
| O conhecimento mora em poucas cabeças | Os documentos |
| O escopo não está claro | A página |
| Ninguém vê como o trabalho está indo | A fila |
| Cada pessoa trabalha do seu jeito | Os comandos |

Use essa forma para a sua própria empresa: liste os problemas dela nas palavras dela, e ponha ao lado de cada um o documento, o comando, a página ou a fila que o responde.
Um problema sem nada ao lado é um que o método não resolve, e dizer isso torna o resto crível.

A proposta em si não rodou no processo.
Ela não tinha fila nem página, e o [capítulo 22](22-beyond-software.md) conta o que isso lhe custou.

## O que o time ganha

O time inteiro num só processo, em que cada pessoa sabe qual parte é sua e cada decisão está numa página que qualquer um pode ler.
E um piloto que mede a si mesmo: um marco dá uma contagem de tokens por entrega e uma lista do que foi pego.
No Caso A o processo pegou quatro problemas fora do código: uma base que não batia com o que foi construído, um pedido impossível, uma falha de permissão numa instalação limpa, e um segredo no pacote.
Não há número de fora contra o qual comparar a adoção; o próprio marco do piloto é a linha de base.

## Pontos-chave

* Sem um processo comum cada pessoa usa IA do seu jeito, a um custo que ninguém vê, e a opinião mais alta decide.
* Responda a "o meu jeito funciona" pedindo a sua evidência, a "processo demais" com o regulador, e a "nós já temos uma ferramenta" com o fato de que o método são documentos que qualquer host lê.
* No Caso A o processo pegou uma base que não batia com o que foi construído, um pedido impossível, uma falha escondida pelo ambiente de desenvolvimento, e um segredo no pacote.
* Quem é dono da decisão propõe, a sessão de um desenvolvedor aplica, uma pessoa sempre faz o commit, e o time revisa o marco.
* Comece com um marco de três a oito linhas, meça os tokens por entrega e o que foi pego, e então decida.

