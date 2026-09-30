# Projetos que não são software

Depois deste capítulo você consegue conduzir uma proposta, uma análise, um documento de passagem de projeto, uma regra de dados ou um livro como entregas, cada uma numa página cujo Pronto quando uma pessoa consegue marcar.
Você também consegue dizer por que um achado sem linha numa fila se perde.

## O problema

Uma proposta, uma análise ou uma passagem de projeto tem decisões, um escopo e um momento em que está pronta, como o código.
Ela costuma ser escrita sem processo nenhum: um arquivo numa pasta compartilhada, versões chamadas "final" e "final 2", achados enviados por email.
Nada diz o que ainda está pendente, e nada confere se uma decisão tomada numa versão chegou à seguinte.

## Uma entrega é qualquer coisa com valor que cabe numa página

O capítulo 14 definiu uma entrega como a menor mudança que tem valor, e nada nessa definição diz código.
O formato da página se lê igual para um documento:

* **Objetivo.** O que o leitor do documento consegue fazer depois de lê-lo.
* **Comportamento.** O que o leitor consegue fazer, uma linha cada, cada linha uma checagem que uma pessoa faz lendo ou experimentando.
* **Contrato.** A estrutura do documento: as suas seções, o seu formato, os fatos que ele precisa trazer.
* **Fora do escopo.** O que o documento não cobre, e onde isso fica.
* **Pronto quando.** Uma lista que uma pessoa marca.

Estados e Referência visual costumam ser "nenhum", ou o modelo que o documento segue.
Uma página para a biblioteca de empréstimos da Parte I, escrita para este capítulo:

```markdown
# librarian-guide

**Objetivo.** Um bibliotecário novo empresta e recebe de volta um
exemplar no primeiro dia, com este guia e sem treinamento.

**Comportamento.**
* Um bibliotecário que nunca usou o sistema empresta um exemplar seguindo o guia.
* Um bibliotecário encontra, pelo sumário, o que dizer a um membro recusado.

**Contrato.**
Seções: Emprestar, Receber de volta, Recusas.
Recusas lista cada membro de LendRefusal com a mensagem que o membro vê.
Markdown em guide/, e um PDF gerado a partir dele.

**Fora do escopo.**
* Gerenciar membros: tem o seu próprio guia, `admin-guide`.

**Pronto quando.**
* [ ] Cada membro de LendRefusal aparece em Recusas.
* [ ] Uma pessoa que nunca usou o sistema empresta um exemplar só com o guia.
* [ ] O PDF é gerado.
```

O `/apply` escreve o guia como escreveria código: segue a página, roda o que uma máquina consegue conferir (o PDF é gerado, cada recusa está listada), e deixa o resto do Pronto quando para a pessoa marcar.

## Os documentos do Caso A

No Caso A, um projeto para um cliente em uma plataforma low-code, a passagem do projeto foi um conjunto de entregas.[^case-a]
Um desenho da solução, um guia de instalação em três formatos, um documento de passagem e uma apresentação, um pacote de evidências indexado pelos critérios de aceite, um readme do repositório e um registro de trabalho tiveram cada um uma linha na fila e uma página, e cada um passou pelo `/propose` e pelo `/apply` como código.
O pacote de evidências mostra o Contrato como estrutura: indexado pelos critérios de aceite, ele deixa o cliente conferir a entrega critério por critério e encontrar a prova de cada um.

Algumas entregas não produzem nada além da resposta escrita de uma pessoa.
A página de uma entrega de pergunta diz o que é perguntado, a quem, e o que cada resposta possível desbloqueia, e ela está pronta quando a resposta chega (capítulo 21).
Das 73 linhas concluídas do Caso A, 8 foram perguntas a pessoas e cerca de oito foram documentos.[^case-a]

## Trabalho com dados como entregas

As regras de segurança de um banco de dados decidem quem pode ler ou escrever cada linha, e são trabalho com valor como uma tela.
Na Ninjobs, seis das suas 93 páginas concluídas mudaram só regras do banco de dados, e nada mais.[^ninjobs]
Uma delas foi a regra "nenhuma escrita enquanto uma exclusão está pendente": ela foi garantida no próprio banco de dados, por uma regra de acesso, e provada pelo teste das regras de acesso do projeto.[^ninjobs]
A construção descobriu que uma regra geral também bloquearia as funções do próprio banco de dados, então a regra virou "nenhum caminho de escrita alcançável a partir do cliente", e a página registrou por quê.

Uma regra no banco de dados vale para todo cliente que um dia falar com ele, e o teste dela é o Pronto quando que a prova.

## Este livro

Este livro é escrito com o kit: uma página por capítulo em `work/`, uma fila de marcos no docs/06, e `make verify` como o seu comando de verificação.
As suas checagens são a paridade das duas edições, as suas regras de prosa e uma varredura contra a sua lista de exposição, então um capítulo está pronto quando elas estão verdes e o autor aprovou cada trecho sobre um caso privado.

## O Caso B, o contraste

O Caso B é a proposta de uma consultoria para o programa de adoção de um cliente, e ele não rodou no processo.[^case-b]
Uma análise da proposta foi escrita com uma disciplina deste livro: cada número trazia a sua procedência, se vinha da proposta, de uma medição, de uma estimativa ou da experiência.
Ela encontrou seis falhas.
Entre elas, a proposta nomeava a ferramenta errada, um risco contratual, e fixava um escopo sem fixar quanto trabalho esse escopo cobria, o que a deixava aberta a um crescimento que ninguém pagaria.

Os achados não tinham linha na fila nem página para carregá-los.
Dois dias depois, a versão seguinte da proposta ainda continha pelo menos um deles.[^case-b]
A análise estava certa, e estar certa não bastou: cada achado precisava de uma linha, e de uma página cujo Pronto quando dissesse "a próxima versão nomeia a ferramenta certa", para que a falha ficasse aberta à vista de todos até uma pessoa marcá-la.

## O que o time ganha

Um só processo para todo tipo de trabalho que o time faz, então a mesma fila, a mesma página e a mesma revisão carregam código, documentos, perguntas e regras de dados.
No Caso A, cerca de 16 das suas 73 linhas concluídas foram perguntas ou documentos, e na Ninjobs seis de 93 páginas foram regras do banco de dados, todas pelos mesmos dois comandos.[^case-a][^ninjobs]

## Pontos-chave

* Uma entrega é qualquer coisa com valor que cabe numa página, seja código ou não.
* Para um documento, o Comportamento é o que o seu leitor consegue fazer, o Contrato é a sua estrutura, e o Pronto quando é uma lista que uma pessoa marca.
* Uma pergunta a uma pessoa também é uma entrega, pronta quando a resposta chega.
* Uma regra do banco de dados é uma entrega com um teste, garantida onde todo cliente a encontra.
* Um achado sem linha se perde: a análise do Caso B estava certa, e pelo menos uma das suas falhas sobreviveu na versão seguinte.

[^case-a]: Caso A, um projeto para um cliente em uma plataforma low-code, um repositório privado, contado pelo autor na sua fila no docs/06 e nas suas páginas: 73 linhas concluídas, 8 delas entregas de pergunta e cerca de 8 entregas de documento, o conjunto da passagem do projeto nomeado aqui. O seu dono, o seu cliente e o seu negócio não são revelados.
[^case-b]: Caso B, a proposta de uma consultoria para o programa de adoção de um cliente, arquivos privados lidos pelo autor: três versões da proposta, uma apresentação, uma nota interna e uma análise; a proposta não rodou no processo. O seu dono e o seu cliente não são revelados.
[^ninjobs]: Ninjobs, o produto do autor, um repositório privado, contado pelo autor no seu `work/done/`: 93 páginas concluídas até 2026-09-23, 6 delas mudando só regras do banco de dados; a regra da exclusão pendente e o seu teste lidos na sua página.
