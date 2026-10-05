# 10. Os documentos: um lugar para cada fato

Depois deste capítulo você consegue dizer o que guardam cada um dos sete documentos do projeto, os ADRs e o `AGENTS.md`, e decidir a qual deles pertence um fato novo.
Você também consegue mudar qualquer um deles conversando com o agente, e dizer por que isso dá a mesma resposta a toda sessão e a toda pessoa.

## O problema

Uma sessão nova só sabe o que está escrito em arquivos.
Um fato que mora na cabeça de alguém nunca chega até ela, e um fato escrito em vários lugares fica desatualizado em alguns deles, então o agente lê a cópia que encontrar primeiro.
No Ninjobs uma decisão morava em seis lugares, e mantê-los em acordo custava mais que o trabalho.

## Um lugar para cada fato

Cada fato do projeto mora em um lugar, e o agente o lê ali.
O focus-kit dá a esses lugares uma forma fixa: sete documentos numerados, docs/00 a docs/06; uma pasta de decisões, `docs/adr/`; o arquivo de regras, `AGENTS.md`; e `work/`, que guarda uma página por entrega (capítulo 14).
Os números são fixos porque os comandos os citam; o nome depois do número fica na língua da documentação, `00-Product.md` num projeto documentado em inglês e `00-Produto.md` num documentado em português.
O `/brainstorm` ou o `/analyze` os escreve uma vez (capítulo 12); o `/propose` e o `/apply` os leem antes de agir.

## Os sete documentos

**docs/00, o produto.** O que o produto é e para quem: seu propósito em um parágrafo, seu público, como funciona nas palavras do usuário, o que ele não é, os valores contra os quais as decisões são medidas, as perguntas de produto a que toda decisão deve responder sim, e as decisões em aberto, o que ninguém pode fechar sozinho.
Nada pode contradizê-lo sem mudá-lo na mesma entrega.

**docs/01, a arquitetura.** O design em uma frase, a stack com o motivo de cada escolha que tinha alternativa, como o código é organizado, como os dados são acessados, como os erros trafegam, os ambientes, e o que foi tentado e removido de propósito, para que ninguém o reconstrua.

**docs/02, o backend.** Só existe quando um servidor guarda regras que o cliente não deve duplicar: o esquema, as regras de acesso, as funções que o cliente pode chamar.
Senão, é uma linha: não há.

**docs/03, o domínio.** Uma tabela dos termos do projeto, com o identificador que cada um tem no código e o que significa, e depois as entidades e as regras que sempre valem para elas.
A tabela é o vocabulário: toda página, identificador e teste usa os seus termos, e um conceito novo entra aqui antes de entrar em qualquer outro lugar.

**docs/04, as convenções.** A língua dos documentos e dos identificadores, a nomenclatura, o estilo e a ferramenta que o impõe, onde ficam os testes e o que cada nível testa, e o formato de uma mensagem de commit.

**docs/05, o processo.** O processo do kit, o mesmo em todo projeto: a regra, o fluxo da fila ao commit, a forma de uma página, a fila, o commit, o que o processo não tem, e como um marco fecha.
Uma seção é preenchida pelo projeto, "This project" (este projeto), cujos itens são os seus slots: o comando que faz a verificação de uma entrega, os ambientes, como uma tela é provada, quando algo é publicado, e a estratégia de git.
Os comandos leem esses fatos aqui, então nenhum arquivo de comando guarda algum deles.

**docs/06, a fila.** Os marcos, cada um com um parágrafo dizendo o que é verdade quando ele fecha, e sob cada um uma linha por entrega, em ordem, com uma marca para o seu estado (capítulo 13).
É o documento em que você mais mexe: todo o trabalho do projeto, aumentado e editado todos os dias, por conversa.
Ele faz o que um quadro kanban ou um backlog de work items faz num processo ágil, com uma diferença: o agente o lê.
Todo documento é lido, e corrigido quando está errado; a fila é o que dá forma ao produto.

## As duas escolhas

O kit oferece duas escolhas e não impõe nenhuma: a arquitetura e a estratégia de git.
O `/brainstorm` e o `/analyze` explicam cada uma com uma recomendação para a stack do projeto, e registram a resposta.

**A arquitetura.** O FOCUS é a arquitetura do capítulo 7: código organizado em fatias verticais (capítulo 6), toda regra de negócio uma função pura que devolve um Result (capítulo 5), e quatro peças pelas quais um evento flui num só sentido até um novo estado.
O kit dá três respostas: o FOCUS inteiro; só os dois princípios, fatias verticais e exceções como valores, na estrutura que a stack favorecer; ou nenhum dos dois, as convenções do próprio projeto.
O Ninjobs, um app web fino sobre um backend como serviço, escolheu os dois princípios.
Num repositório que já tem código, o padrão é o que o código já faz.
O docs/01 registra a resposta, e um ADR registra o porquê.

**A estratégia de git.** Três respostas, cada uma para um jeito de trabalhar: trunk, tudo no branch principal, uma entrega por vez, para uma pessoa sozinha; um branch por entrega, integrado por um pull request revisado, para trabalho em sequência; um worktree por entrega, uma segunda pasta de trabalho no seu próprio branch, para que vários agentes construam entregas diferentes ao mesmo tempo.
Em todas, a página e a construção de uma entrega são uma mudança que se desfaz em um passo, e o agente nunca faz commit nem merge.
Os capítulos 20 e 21 ensinam as três.
O slot Git do docs/05 registra a resposta, e um ADR registra o porquê.

## ADRs

ADR é a sigla de Architecture Decision Record, registro de decisão de arquitetura.
Um ADR é um arquivo por decisão, `docs/adr/ADR-NNNN-<slug>.md`, com o seu contexto, a decisão, as suas consequências e a sua data.
Michael Nygard propôs o formato em 2011, porque "*uma das coisas mais difíceis de acompanhar durante a vida de um projeto é a motivação por trás de certas decisões*".[^nygard-adr]
Um ADR é emendado, nunca reescrito: quando a decisão muda, uma emenda abaixo dela diz o que mudou e quando, e o motivo original fica acima.
A próxima pessoa que quiser mudá-la de novo lê por que ela era assim, e pesa o motivo antigo em vez de adivinhá-lo.

## AGENTS.md

O `AGENTS.md` é o arquivo de regras do capítulo 2, um formato aberto que os agentes de código leem no início de uma sessão.[^agents-md]
Todo host do capítulo 11 o lê, sozinho ou por um ponteiro; o Claude Code o lê pelo `CLAUDE.md`, que guarda a linha `@AGENTS.md` e, abaixo dela, só o que vale apenas para o Claude Code.
O `AGENTS.md` não cita a ferramenta de nenhum host, então se lê igual em todos.

Ele tem quatro seções curtas: o que ler antes de agir, os inegociáveis, o que não reconstruir, e como trabalhar.
A descrição dos documentos no kit lhe dá três regras: no máximo sessenta linhas, tudo nele aponta para um documento, e nada nele é o único lugar onde uma regra está escrita.
Ele é carregado inteiro em toda sessão, então fica curto; e uma regra que morasse só ali não teria o seu motivo escrito em lugar nenhum.

## Para onde vai um fato novo

Um fato novo tem um dono, e você o encontra fazendo estas perguntas em ordem; a primeira que servir dá o documento:

1. É uma escolha entre alternativas, com um motivo que alguém pode querer rever?
   Um ADR guarda a escolha e o motivo, e o documento que ela governa guarda o resultado.
2. É o que o produto é, para quem, o que ele não é, um valor, ou algo que ninguém fecha sozinho?
   docs/00.
3. É uma palavra, uma entidade, ou uma regra que sempre vale para os dados?
   docs/03.
4. É como a coisa é construída: a stack, onde o código fica, acesso a dados, erros, ambientes?
   docs/01, ou docs/02 quando um servidor guarda a regra.
5. É como código ou texto é escrito: nomenclatura, estilo, testes, commits?
   docs/04.
6. É um fato deste projeto que os comandos leem: o comando de verificação, os ambientes, o git?
   Um slot do docs/05.
7. É trabalho a fazer?
   O docs/06 guarda a sua linha, e a página em `work/` guarda a entrega.

O `AGENTS.md` nunca é a resposta: quando toda sessão precisa ter um fato em mente, uma linha ali aponta para o seu dono.

Tome a biblioteca de empréstimos da Parte I, e a frase "um membro fica com um exemplar por 21 dias".
Ela guarda três fatos, e cada um tem um dono diferente.
O termo e o seu valor, o prazo de empréstimo de 21 dias que dá a um empréstimo a sua data de devolução, vão para o docs/03, pergunta 3, onde a tabela o nomeia e dá o identificador que o código usa.
A regra que o membro encontra, que um exemplar volta até a sua data de devolução e um membro com um exemplar atrasado não pega mais nada, vai para o docs/00, pergunta 2, nas palavras do usuário, citando o prazo de empréstimo pelo nome.
E se um servidor fixa a data de devolução quando registra um empréstimo, para que nenhum cliente possa mudá-la, como ele faz isso vai para o docs/02, pergunta 4.
O número é escrito uma vez, no docs/03; os outros dois documentos usam o termo.
Uma frase de uma conversa pode guardar vários fatos como esses, e cada um chega ao seu dono, sem nenhum repetir o que outro guarda.

## Documentos vivos

Uma entrega que muda comportamento atualiza o documento dono do fato, na mesma entrega.
A próxima sessão lê a mudança junto com todo o resto e a segue sem que ninguém precise repetir.

Você não edita os documentos à mão, e eu recomendo que não edite.
Converse com o agente: aponte uma lacuna, um detalhe errado, algo a acrescentar, mudar ou remover, e ele encontra o documento dono do fato e escreve a mudança ali, já que os documentos lhe dizem onde mora cada fato, e a conversa guarda o motivo.
A sua parte é interpretar, guiar e validar: dizer o que a mudança significa, direcioná-la, e lê-la antes de fazer o commit.
O texto de um agente parece certo mesmo quando está errado, então você o confere com o que sabe e nunca confia nele às cegas, como não confiaria no de um colega.

As decisões em aberto do docs/00 são onde o agente para.
O docs/00 da biblioteca lista as multas por devolução atrasada como em aberto, então uma página que toca em devoluções atrasadas as nomeia como fora do escopo, e um agente a quem pedem para construí-las para e pergunta, onde de outro modo teria escolhido um valor e uma regra por conta própria.

## O que o time ganha

A mesma resposta em toda sessão e para toda pessoa: um desenvolvedor, um gestor e um agente numa sessão nova que perguntam o prazo de empréstimo leem uma linha em um documento.
No Ninjobs uma decisão morava em seis lugares que podiam discordar, e toda entrega pagava para mantê-los em acordo; com um lugar para cada fato, uma mudança é escrita uma vez e toda sessão seguinte a lê.

## Pontos-chave

* Cada fato mora em um lugar: sete documentos numerados, `docs/adr/`, `AGENTS.md` e `work/`, com números fixos porque os comandos os citam.
* O docs/00 é o produto e as suas decisões em aberto, o docs/01 e o docs/02 como ele é construído, o docs/03 o vocabulário, o docs/04 as convenções, o docs/05 o processo com os slots do projeto, o docs/06 a fila.
* As duas escolhas, a arquitetura (o FOCUS inteiro, os dois princípios, nenhum) e o git (trunk, um branch ou um worktree por entrega), ficam registradas no docs/01 e no docs/05, cada uma com um ADR que é emendado, nunca reescrito.
* Um fato novo vai para o primeiro documento cuja pergunta servir; uma frase pode guardar vários fatos, cada um com o seu dono, e o `AGENTS.md` só aponta para eles.
* Você muda os documentos conversando com o agente, e interpreta, guia e valida o que ele escreve; uma decisão em aberto o faz parar e perguntar.

[^nygard-adr]: Michael Nygard, "Documenting Architecture Decisions", blog da Cognitect, 2011. <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>
[^agents-md]: AGENTS.md, "AGENTS.md", acesso em 2026-09-30. <https://agents.md>
