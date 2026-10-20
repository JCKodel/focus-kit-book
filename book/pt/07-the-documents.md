# 7. Os documentos: um lugar para cada fato

Depois deste capítulo você consegue dizer o que guardam cada um dos sete documentos do projeto, os ADRs, os manuais e o `AGENTS.md`, e decidir a qual deles pertence um fato novo, inclusive um passo do próprio time, que vira um slot do docs/05 que os comandos seguem.
Você também consegue mudar qualquer um deles conversando com o agente, e dizer por que isso dá a mesma resposta a toda sessão e a toda pessoa.

## O problema

Uma sessão nova só sabe o que está escrito em arquivos.
Um fato que mora na cabeça de alguém nunca chega até ela, e um fato escrito em vários lugares fica desatualizado em alguns deles, então o agente lê a cópia que encontrar primeiro.
No Ninjobs uma decisão morava em seis lugares, e mantê-los em acordo custava mais que o trabalho.

## Um lugar para cada fato

Cada fato do projeto mora em um lugar, e o agente o lê ali.
O focus-kit dá a esses lugares uma forma fixa: sete documentos numerados, docs/00 a docs/06; uma pasta de decisões, `docs/adr/`; uma pasta de manuais, `docs/manuals/`, um para cada ação de mais de um comando: rodar o produto a partir de um clone novo, uma feita à mão fora de uma entrega, ou uma prova que o `/apply` roda em outra máquina; o arquivo de regras, `AGENTS.md`; e `work/`, que guarda uma página por entrega.
Os números são fixos porque os comandos os citam; o nome depois do número fica na língua da documentação, `00-Product.md` num projeto documentado em inglês e `00-Produto.md` num documentado em português.
As pastas `docs/`, `docs/adr/`, `docs/manuals/`, `work/` e `work/done/` (onde fica a página de uma entrega feita) ficam em inglês em todo projeto, como o kit as escreve; os arquivos dentro delas levam a língua da documentação, como `docs/manuals/publicar-o-app.md`.
O `/brainstorm`, que define um projeto novo numa conversa, ou o `/analyze`, que lê um repositório existente, os escreve uma vez; o `/propose` e o `/apply` os leem antes de agir.

Um agente responde a partir do que está na sua janela, então o que importa é qual texto chega até ela.
A geração aumentada por recuperação (RAG) é um jeito de levá-lo: a cada pergunta, um recuperador encontra trechos num corpo de texto guardado fora do modelo, e o modelo responde a partir deles.
O termo e o método vêm de um artigo de 2020 de Patrick Lewis e colegas do Facebook AI Research, cujo recuperador buscava num índice da Wikipédia.[^lewis-rag-2020]
Os documentos do focus-kit funcionam como uma recuperação feita para o projeto: o corpo de texto são os próprios documentos do projeto, escritos para esse uso, um lugar para cada fato.
O agente busca o que precisa pelo nome, já que o `AGENTS.md` e os comandos lhe dizem qual documento guarda qual fato, e lê esse documento quando precisa dele, com as suas próprias ferramentas, o que a Anthropic chama de carregar o contexto "*na hora certa*".[^anthropic-context-2025]
Para mim, esse é o principal valor dos documentos.

Todo projeto do focus-kit dá a cada documento o mesmo número, como a descrição dos documentos do kit os numera.
Então o docs/06 é a fila em qualquer projeto do focus-kit, o que fazer, o que está sendo feito e o que está feito, e cada um dos outros números guarda ali o mesmo documento, seja qual for o nome depois dele.

## Os sete documentos

**docs/00, o produto.** O que o produto é e para quem: seu propósito em um parágrafo, seu público, como funciona nas palavras do usuário, o que ele não é, os valores contra os quais as decisões são medidas, as perguntas de produto a que toda decisão deve responder sim, e as decisões em aberto, o que ninguém pode fechar sozinho.
Nada pode contradizê-lo sem mudá-lo na mesma entrega.

**docs/01, a arquitetura.** O design em uma frase, a stack com o motivo de cada escolha que tinha alternativa, como o código é organizado, como os dados são acessados, como os erros trafegam, os ambientes, e o que foi tentado e removido de propósito, para que ninguém o reconstrua.

**docs/02, o backend.** Só existe quando um servidor guarda regras que o cliente não deve duplicar: o esquema, as regras de acesso, as funções que o cliente pode chamar.
Senão, é uma linha: não há.

**docs/03, o domínio.** Uma tabela dos termos do projeto, com o identificador que cada um tem no código e o que significa, e depois as entidades e as regras que sempre valem para elas.
A tabela é o vocabulário: toda página, identificador e teste usa os seus termos, e um conceito novo entra aqui antes de entrar em qualquer outro lugar.

**docs/04, as convenções.** A língua dos documentos e dos identificadores, a nomenclatura, o estilo e a ferramenta que o impõe, onde ficam os testes e o que cada nível testa.

**docs/05, o processo.** O processo do kit, o mesmo em todo projeto: a regra, o fluxo da fila ao commit, a forma de uma página, a fila, o commit e o formato da sua mensagem, o que o processo não tem, e como um marco fecha.
Uma seção é preenchida pelo projeto, "This project" (este projeto), cujos itens são os seus dez slots: a língua da documentação, o comando que faz a verificação de uma entrega, com o comando dos testes lentos que ficam fora dele para a revisão de marco, se houver, os ambientes, como uma tela é provada, quando algo é publicado, se a pasta `context/` entra no commit, quem revisa as mudanças de uma entrega antes de o `/apply` terminar, os manuais, quem lê o código quando um marco fecha (a revisão profunda do host, a revisão do próprio host que lê todas as mudanças do marco de uma vez, e que a pessoa dispara; os leitores do kit, um agente só de leitura por área que o slot nomeia, no modelo que o slot nomeia ou no da sessão; um conferente depois de qualquer dos dois; ou ninguém), e a estratégia de git.
Diga o que disser a política de publicação, as últimas palavras do `/apply` dizem qual ambiente está em qual versão.
Um slot diz o que e o comando, em poucas linhas, porque o `/apply` o lê toda vez; os passos vão para um manual, e o que um comando imprime fica na ajuda dele.
Então um slot não diz que entrega criou o seu comando nem como ele funcionava antes: essa história está na página da entrega em `work/done/` e no ADR.
Os comandos leem esses fatos aqui, então nenhum arquivo de comando guarda algum deles.
O projeto pode acrescentar slots próprios ao lado desses dez, e um slot que cita o `/propose` ou o `/apply` é seguido por esse comando sem nenhuma edição no arquivo dele.
Os arquivos de comando são do kit, e a instalação dele os escreve; o slot é um fato do projeto, no documento que os comandos já leem.
Um slot que não cita nenhum dos dois comandos é um fato que os comandos leem como qualquer outro, e todo slot do projeto mantém a forma acima.
No docs/05 da biblioteca de empréstimos, escrito para este capítulo, um time que acompanha a sua fila num quadro acrescenta este:

```markdown
* **Quadro:** `npm run quadro` envia o docs/06 para o quadro do time.
  O /propose e o /apply o rodam sempre que mudam uma marca, e avisam
  quando ele falha.
```

**docs/06, a fila.** Os marcos, cada um com um parágrafo dizendo o que é verdade quando ele fecha, e sob cada um uma linha por entrega, em ordem, com uma marca para o seu estado.
Ele não guarda regras próprias: as marcas, os sufixos como `· after`, que segura uma linha até outra estar feita, a ordem e o que pode rodar ao mesmo tempo estão escritos uma vez, no docs/05 §4, e o cabeçalho do docs/06 aponta para lá, então nenhuma segunda cópia pode se afastar da primeira.
É o documento em que você mais mexe: todo o trabalho do projeto, aumentado e editado todos os dias, por conversa.
Ele faz o que um quadro kanban ou um backlog de work items faz num processo ágil, com uma diferença: o agente o lê.
Todo documento é lido, e corrigido quando está errado; a fila é o que dá forma ao produto.

## As duas escolhas

O kit oferece duas escolhas e não impõe nenhuma: a arquitetura e a estratégia de git.
O `/brainstorm` e o `/analyze` explicam cada uma com uma recomendação para a stack do projeto, e registram a resposta.

**A arquitetura.** O FOCUS é a arquitetura do capítulo 4: código organizado em fatias verticais, toda regra de negócio uma função pura que devolve um Result (capítulo 3), e quatro peças pelas quais um evento flui num só sentido até um novo estado.
O kit dá três respostas: o FOCUS inteiro; só os dois princípios, fatias verticais e exceções como valores, na estrutura que a stack favorecer; ou nenhum dos dois, as convenções do próprio projeto.
Com qualquer uma das três, a página, a fila, os documentos, a verificação e o commit funcionam do mesmo jeito.
O que o FOCUS acrescenta está no código: um agente lê uma fatia para uma mudança (capítulo 4), o que os dois princípios também dão, e cada uma das quatro peças tem o seu próprio teste (capítulo 5).
O Ninjobs primeiro exigiu o FOCUS inteiro em toda feature (capítulo 6); depois do recomeço, manteve os dois princípios, fatias verticais e exceções como valores, sem as quatro peças como regra.
Num repositório que já tem código, o padrão é o que o código já faz.
O docs/01 registra a resposta, e um ADR registra o porquê.

**A estratégia de git.** Três respostas, cada uma para um jeito de trabalhar: trunk, tudo no branch principal, para uma pessoa, sozinha ou com várias sessões em linhas livres (linhas da fila que não estão feitas, não estão esperando e não precisam de outra linha feita antes, já definidas ou não) que mexem em arquivos diferentes; um branch por entrega, integrado por um pull request revisado, para trabalho em sequência; um worktree por entrega, uma segunda pasta de trabalho no seu próprio branch, para várias pessoas, ou para uma pessoa cujas entregas mexem nos mesmos arquivos.
Em todas, a página e a construção de uma entrega são uma mudança que se desfaz em um passo, e por padrão o agente coloca em stage e nunca faz commit nem merge por conta própria; quando pedem, ele dá o passo que a pessoa nomeia.
O slot Git pode dizer, em vez disso, que o agente faz o commit, e o merge, pela palavra do slot, que vale como o pedido; a pessoa revisa o commit.
A Parte III ensina as três.
O slot Git do docs/05 registra a resposta, e um ADR registra o porquê.

## ADRs

ADR é a sigla de Architecture Decision Record, registro de decisão de arquitetura.
Um ADR é um arquivo por decisão, `docs/adr/ADR-NNNN-<slug>.md`, com o seu contexto, a decisão, as suas consequências e a sua data.
Michael Nygard propôs o formato em 2011, porque "*uma das coisas mais difíceis de acompanhar durante a vida de um projeto é a motivação por trás de certas decisões*".[^nygard-adr]
Um ADR é emendado, nunca reescrito: quando a decisão muda, uma emenda abaixo dela diz o que mudou e quando, e o motivo original fica acima.
A próxima pessoa que quiser mudá-la de novo lê por que ela era assim, e pesa o motivo antigo em vez de adivinhá-lo.

## Manuais

Parte do trabalho de um projeto é uma ação de mais de um comando, de três tipos.
O primeiro é rodar o produto a partir de um clone novo, de instalar o que ele precisa até a primeira tela ou chamada, e todo projeto o deve.
Rodar um produto se monta ao longo de várias entregas, cada uma acrescentando um passo, e o que o `/apply` diz sobre usar uma entrega fica na conversa dele; então, desde o início, o slot Manuals (manuais) do docs/05 nomeia o manual de rodá-lo, a primeira entrega depois da qual uma pessoa consegue rodar o produto o escreve, e toda entrega que muda um passo o atualiza.
Na biblioteca de empréstimos, escrita para este capítulo, a primeira entrega, o `esqueleto`, que constrói o app e o servidor vazios, escreve `docs/manuals/rodar-o-app-de-um-clone.md`; uma entrega posterior que acrescenta um banco de dados iniciado antes do servidor o atualiza na mesma entrega, e uma que acrescenta uma recusa ao `emprestar-livro` o deixa como está.
O segundo é feito por uma pessoa, à mão, fora de qualquer entrega: publicar o app, desfazer uma versão publicada, trocar um segredo, configurar um serviço.
O terceiro é uma prova que o `/apply` roda em outra máquina: no docs/05 da biblioteca de empréstimos, escrito para este capítulo, o slot Proof of a screen (prova de uma tela) cita o comando que prova uma tela e aponta para `docs/manuals/provar-no-servidor-de-teste.md`, onde o `/apply` encontra os passos para publicar uma prévia no servidor de teste e rodar ali os testes ponta a ponta.
Cada uma dessas ações ganha um manual, um arquivo em `docs/manuals/`, com o nome na língua da documentação dizendo o que ele faz, para que quem precisa dele o encontre pelo nome.
Um manual se sustenta sozinho para quem o executa, sem ter lido mais nada, e guarda seis coisas, como diz o docs/05 do kit: o que ele faz e quando, o que precisa estar pronto antes, os comandos em ordem, como saber que deu certo, como desfazer, e o que quebra se um passo for pulado.
O slot diz o que e o comando, e o manual guarda os passos para quem os executa.
Um comando sozinho, como o que faz a verificação de uma entrega, não precisa de manual: ele fica no seu slot.

No mesmo docs/05, o slot Environments (ambientes) cita o comando que publica o app e aponta para `docs/manuals/publicar-o-app.md`; os passos moram só ali.
O `/analyze` escreve primeiro o manual de rodar o produto, depois os do que um repositório já faz à mão; o `/apply` escreve ou atualiza um quando uma entrega acrescenta ou muda uma dessas coisas; e o `/brainstorm` não escreve nenhum, e nomeia no slot o manual de rodá-lo como devido.
A pasta é criada com o primeiro manual, então não há pasta vazia, e o `AGENTS.md` aponta para ela, para rodar o produto e para o que se faz à mão.

## AGENTS.md

O `AGENTS.md` é o arquivo de regras do capítulo 1, um formato aberto que os agentes de código leem no início de uma sessão.[^agents-md]
Todo host o lê, sozinho ou por um ponteiro; o Claude Code o lê pelo `CLAUDE.md`, que guarda a linha `@AGENTS.md` e, abaixo dela, só o que vale apenas para o Claude Code.
O `AGENTS.md` não cita a ferramenta de nenhum host, então se lê igual em todos.

Ele tem quatro seções curtas: o que ler antes de agir, os inegociáveis, o que não reconstruir, e como trabalhar.
A seção de como trabalhar também diz a partir de onde o agente responde: quando perguntam em que pé as coisas estão, a partir do docs/06 e de `work/`; quando perguntam o que uma entrega decidiu ou por quê, a partir da sua página em `work/done/` e dos ADRs que essa página cita, não da memória nem de uma mensagem de commit.
Então o agente da biblioteca, quando lhe perguntam por que o `emprestar-livro` recusa um membro com um exemplar atrasado, abre `work/done/emprestar-livro.md` e os ADRs que essa página cita, que guardam a resposta.
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
5. É como código ou texto é escrito: nomenclatura, estilo, testes?
   docs/04.
6. É um fato deste projeto que os comandos leem: o comando de verificação, os ambientes, se a pasta `context/` entra no commit, como uma entrega e um marco são revisados, o git?
   Um slot do docs/05, o que e o comando, em poucas linhas.
7. É como rodar o produto a partir de um clone novo, os passos que uma pessoa segue à mão fora de uma entrega (publicar, desfazer uma versão, trocar um segredo, configurar um serviço), ou os de uma prova que o `/apply` roda em outra máquina?
   Um manual em `docs/manuals/`, com o slot guardando o comando e apontando para ele.
8. É trabalho a fazer?
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

Você não edita os documentos à mão, você conversa com o agente para alterá-los, apontando uma lacuna, um detalhe errado, algo a acrescentar, mudar ou remover.
Ele encontra o documento dono do fato e escreve a mudança ali, já que os documentos lhe dizem onde mora cada fato, e a conversa guarda o motivo.
A sua parte é interpretar, guiar e validar: dizer o que a mudança significa, direcioná-la, e lê-la antes de fazer o commit.
O texto de um agente parece certo mesmo quando está errado, então você o confere com o que sabe e nunca confia nele às cegas, como não confiaria no de um colega.

As decisões em aberto do docs/00 são onde o agente para.
O docs/00 da biblioteca lista as multas por devolução atrasada como em aberto, então uma página que toca em devoluções atrasadas as nomeia como fora do escopo, e um agente a quem pedem para construí-las para e pergunta, onde de outro modo teria escolhido um valor e uma regra por conta própria.

## O que o time ganha

A mesma resposta em toda sessão e para toda pessoa: um desenvolvedor, um gestor e um agente numa sessão nova que perguntam o prazo de empréstimo leem uma linha em um documento.
Com um lugar para cada fato, uma mudança é escrita uma vez e toda sessão seguinte a lê, onde no Ninjobs toda entrega pagava para manter em acordo as seis cópias de uma decisão.
Um manual põe os passos que uma pessoa segue à mão onde essa pessoa os procura, num arquivo que se encontra pelo nome, e tira os passos de uma prova do slot que todo `/apply` lê antes da sua primeira edição.
O manual de rodar o produto, devido desde o início, deixa uma pessoa rodar o que um marco construiu sem as conversas das entregas que lhe acrescentaram, cada uma, um passo.
Um passo do próprio time, como atualizar o seu quadro, mora no docs/05 dele e sobrevive a toda atualização dos comandos do kit, já que uma atualização escreve só os arquivos do kit e para, sem escrever nada, diante de um que tenha uma edição que ela não reconhece.
O que mais valorizo: toda sessão e toda pessoa recuperam um fato do mesmo lugar, e, em outro projeto do focus-kit, do mesmo número.

## Pontos-chave

* Cada fato mora em um lugar: sete documentos numerados, `docs/adr/`, `docs/manuals/`, `AGENTS.md` e `work/`; o docs/00 é o produto e as suas decisões em aberto, o docs/01 e o docs/02 como ele é construído, o docs/03 o vocabulário, o docs/04 as convenções, o docs/05 o processo com os slots do projeto, cada um o que e o comando, os dez do kit e os que o projeto acrescenta e os comandos seguem, o docs/06 a fila, cujas regras estão escritas uma vez no docs/05 §4, com números fixos porque os comandos os citam, os mesmos em todo projeto.
* As duas escolhas, a arquitetura (o FOCUS inteiro, os dois princípios, nenhum) e o git (trunk, um branch ou um worktree por entrega), ficam registradas no docs/01 e no docs/05, cada uma com um ADR que é emendado, nunca reescrito; o método funciona do mesmo jeito com qualquer uma delas.
* Rodar o produto a partir de um clone novo é o manual que todo projeto deve, escrito pela primeira entrega depois da qual uma pessoa consegue rodá-lo; uma ação de mais de um comando feita à mão fora de uma entrega, ou uma prova que o `/apply` roda em outra máquina, também tem o seu, em `docs/manuals/`, para quem o executa, sem ter lido mais nada; o slot guarda o comando e aponta para ele, o `/analyze` escreve primeiro o manual de rodá-lo, o `/apply` escreve ou atualiza um, e o `/brainstorm` não escreve nenhum e nomeia o de rodá-lo como devido.
* Um fato novo vai para o primeiro documento cuja pergunta servir; uma frase pode guardar vários fatos, cada um com o seu dono, e o `AGENTS.md` só aponta para eles, e diz ao agente para responder o que uma entrega decidiu a partir da sua página e dos ADRs.
* Você muda os documentos conversando com o agente, e interpreta, guia e valida o que ele escreve; uma decisão em aberto o faz parar e perguntar.

[^nygard-adr]: Michael Nygard, "Documenting Architecture Decisions", blog da Cognitect, 2011. <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>
[^agents-md]: AGENTS.md, "AGENTS.md", acesso em 2026-09-30. <https://agents.md>
[^lewis-rag-2020]: Patrick Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", 2020. <https://arxiv.org/abs/2005.11401>
[^anthropic-context-2025]: Anthropic, "Effective context engineering for AI agents", 2025. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
