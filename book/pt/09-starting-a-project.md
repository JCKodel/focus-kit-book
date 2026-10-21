# 9. Começando: `/brainstorm` e `/analyze`

Depois deste capítulo você consegue começar um projeto novo com o `/brainstorm`, ou documentar um projeto existente com o `/analyze`, conversando, e revisar os documentos que cada comando escreve antes de fazer o commit deles (registrá-los no histórico do projeto).
Você também consegue escolher uma stack pelo que o projeto precisa e por quanto o agente a conhece, e guardar o que o código não diz onde o agente lê.

## O problema

Toda sessão seguinte lê os documentos do projeto antes de agir, então eles têm de existir antes da primeira entrega.
Um agente que começa sem nada escrito decide tudo sozinho, e um questionário falha pelo outro lado: pergunta a uma pessoa o que ela ainda não sabe responder, ou o que o código já diz.
O focus-kit tem dois comandos para isso, e o que escolhe entre eles é o código: o `/brainstorm` para um repositório que ainda não tem código da aplicação, mesmo que já tenha um README, anotações ou os arquivos do próprio kit, e o `/analyze` para um repositório com código.
Os dois escrevem os mesmos documentos conversando e não escrevem código; um projeto já documentado não roda nenhum dos dois de novo quando atualiza o kit ([capítulo 8](08-install-and-hosts.md)).

## `/brainstorm`: um projeto novo

O `/brainstorm` é o comando para um repositório que ainda não tem código.
Ele conversa sobre um assunto de cada vez, nesta ordem, e passa ao seguinte quando conseguiria escrever aquele documento sozinho, como diz o arquivo do kit para o comando:

1. **O produto** (docs/00): o que ele é em uma frase, para quem, o que ele não é, como é uma boa decisão aqui.
2. **O vocabulário** (docs/03): as dez a vinte palavras sem as quais o produto não pode ser descrito, cada uma com seu nome no código.
3. **Como ele é construído** (docs/01): a stack e a forma do código, com as duas escolhas do kit, o FOCUS e a estratégia de git, cada uma com a recomendação do agente para essa stack.
4. **As convenções** (docs/04): a língua da documentação e a língua dos identificadores, o estilo, onde ficam os testes.
5. **Os slots do processo** (docs/05): o comando de verificação e os testes lentos que ficam fora dele, os ambientes, como uma tela é provada, quando um ambiente além da sua máquina é atualizado, se a pasta `context/` entra no commit, os manuais (o de rodar o produto, devido pela primeira entrega depois da qual uma pessoa consegue rodá-lo; os outros nenhum ainda, em um projeto novo), e se um segundo par de olhos lê cada entrega antes de ela terminar e o marco inteiro quando ele fecha.
6. **O primeiro marco** (docs/06): de três a oito entregas, uma linha cada, em ordem, cada uma com o seu token de paralelismo, duas letras que dizem se ela pode rodar ao lado das linhas acima dela, quando linhas vão rodar ao mesmo tempo ([capítulo 14](14-queue-states.md)), e depois a revisão dele; as primeiras são o esqueleto em que as outras se apoiam.

Cada slot que ele escreve no docs/05 diz o que e o comando, em poucas linhas, como diz o próprio docs/05 ([capítulo 7](07-the-documents.md)).

Uma pergunta só cobre a revisão: um segundo par de olhos lê cada entrega antes de ela terminar e o marco inteiro quando ele fecha?
O padrão é sim, e a resposta única preenche dois slots.
O slot Delivery review cita quem lê as mudanças de uma entrega antes de o `/apply` terminar, um contexto que não as escreveu ([capítulo 13](13-apply.md)): a revisão do próprio host, uma skill ou um comando que o agente consegue rodar, quando ela pode ficar restrita aos caminhos da entrega, já que outra sessão pode estar trabalhando na mesma pasta; senão, um agente somente leitura, que lê arquivos e não edita nenhum.
O slot Milestone review cita quem lê o código ao fechar um marco ([capítulo 15](15-closing-a-milestone.md)): os leitores do kit sobre os módulos do docs/01, um leitor cada, porque as mudanças de um módulo se leem juntas, no modelo da sessão, o que você já usa.
Você também pode dizer não: se alguém lê o seu trabalho é decisão sua.

### Um padrão em cada pergunta

O agente pergunta só o que não consegue decidir com um padrão sensato, e diz o padrão junto com a pergunta.
Então "your call" (você decide) é sempre uma resposta válida: o agente mantém o padrão dele, e uma pessoa que não sabe responder ainda recebe um bom documento.
Ele nunca pergunta por uma ferramenta pelo nome quando a pergunta é sobre o que você quer (por isso a pergunta da revisão não cita nenhuma), e pergunta em rodadas de no máximo quatro perguntas, com a recomendação dele primeiro.
O que ainda não dá para saber, como um comando de verificação antes de existir qualquer código, ele escreve como "criado pela primeira entrega".

### Escolhendo a stack

Quando a conversa chega a como o projeto é construído, três perguntas escolhem a stack, nesta ordem.

**Do que o projeto precisa?**
Comece pelo valor dele e deixe a linguagem para depois: quem o abre, em que aparelho, que regras nunca podem quebrar, quanto ele pode custar para rodar.
Uma stack que não consegue entregar isso está fora, por mais que o agente a conheça.

**De quanto código público nessa stack o agente aprendeu?**
Um modelo escreve melhor o que viu mais durante o treino, e a medida pública mais próxima disso é quantas pessoas escrevem uma linguagem abertamente.
Pela contagem do GitHub, o TypeScript virou a linguagem mais usada no GitHub em agosto de 2025, com 2.636.006 contribuidores mensais, à frente de Python e JavaScript.[^octoverse]
A contagem é de pessoas e não diz nada sobre linhas de código, então leia-a como um ranking e nunca como um tamanho.
No Ninjobs, o mesmo agente errava o design no Flutter, onde tinha poucos exemplos de um design system customizado para aprender, e acertava no React: o Flutter conseguiria construir o produto, e o limite era o que o agente tinha visto.

**A stack confere a si mesma?**
Um compilador que rejeita um tipo errado e testes que rodam em segundos avisam ao agente que ele errou antes que você precise avisar.
Uma stack em que um erro só aparece em tempo de execução, em uma tela, deixa essa conferência para você.

### O que ele escreve, e onde para

Quando os seis assuntos estão cobertos, o `/brainstorm` escreve o docs/00 a 06, um ADR para cada decisão que uma sessão futura poderia desfazer (a stack, FOCUS ou não, o git, qualquer coisa em que você hesitou), o `AGENTS.md`, o `CLAUDE.md` com a linha `@AGENTS.md`, e uma `work/done/` com um `.gitkeep`, para que a pasta sobreviva a um clone.
Ele não escreve manual, e a `docs/manuals/` é criada com o primeiro.
O slot Manuals (manuais) nomeia o manual de rodar o produto como devido pela primeira entrega depois da qual uma pessoa consegue rodá-lo, de instalar o que ele precisa até a primeira tela ou chamada; os outros vêm com a entrega que acrescenta algo que uma pessoa faz à mão ou uma prova que o `/apply` roda em outra máquina.
O primeiro marco, no docs/06, é um parágrafo que uma pessoa consegue conferir quando o marco fecha e as linhas dele, o esqueleto primeiro; o [capítulo 11](11-queue-and-milestones.md) mostra o da biblioteca de empréstimos e ensina a fila.
Depois ele mostra a fila e para.
Ele não escreve código, nem configuração, nem arquivo de dependências: a primeira entrega faz isso, com uma página própria, pelo `/propose` em uma sessão nova ([capítulo 12](12-propose.md)).

## `/analyze`: um projeto existente

O `/analyze` é o comando para um repositório que já tem código, com ou sem um README ou documentação própria.
Ele funciona como o `/brainstorm`, com um padrão em cada pergunta e os mesmos documentos no fim, mas lê antes de perguntar, e o que o código diz ele não pergunta.

### O que ele lê

Como o arquivo do kit para o comando lista, ele lê a `context/` inteira quando existe (a seção abaixo), o README e qualquer documentação que já exista, os manifestos, a árvore de pastas, os pontos de entrada, os testes e como eles rodam, a configuração de CI e qualquer script que uma pessoa roda à mão, os assuntos dos commits recentes, e qualquer arquivo de regras de agente que já exista, como `CLAUDE.md` ou `.cursorrules`.

A partir disso ele deduz a stack, como o código está organizado, onde moram as regras de negócio, como os erros viajam, o comando de verificação, quais testes são lentos o bastante para ficar fora dele, e os ambientes, e marca cada item como observado.
O que o projeto não tem, ele pula.

### O que ele pergunta

Uma rodada, de seis assuntos apenas:

1. A língua da documentação. Padrão: a língua do README.
2. O propósito e o público do produto nas suas palavras, só quando nenhum README os diz.
3. O FOCUS e a estratégia de git. O padrão de cada um é o que o código já faz, e o agente diz o que é, então "your call" o mantém.
4. Se a pasta `context/` entra no commit. Padrão: entra quando o repositório fica com o time, e vai para o `.gitignore` quando ele é entregue ou público.
5. As revisões: se um segundo par de olhos lê cada entrega antes de ela terminar e o marco inteiro quando ele fecha. Padrão: sim; a revisão do próprio host quando ela pode ficar restrita aos caminhos de uma entrega, senão um agente somente leitura; e os leitores do kit sobre os módulos do docs/01 no modelo da sessão, ou a revisão profunda do host sobre o intervalo quando o projeto já roda uma ([capítulo 15](15-closing-a-milestone.md)).
6. O primeiro marco: de três a oito entregas, ou de onde lê-las (issues, um arquivo TODO, um roadmap), e depois a revisão dele.

Um arquivo de regras que já existe não fica ao lado do `AGENTS.md`: as regras dele passam para o `AGENTS.md`, e o arquivo guarda só a linha que o importa e o que vale apenas para o host dele (o programa que roda o agente).
Ele escreve os mesmos documentos que o `/brainstorm`, e mais, em `docs/manuals/`, primeiro o manual de rodar o produto a partir de um clone novo, depois um para cada coisa que uma pessoa já faz à mão ali, como um alvo do Makefile, um script de deploy ou os passos de instalação de um README, como diz o arquivo do kit para o comando.
Os documentos descrevem o que existe, e não o que deveria existir.
O agente mostra a mudança antes de escrever, e não muda código nenhum.

### Onde o código contradiz a si mesmo

Um código que já viveu um tempo diz duas coisas ao mesmo tempo: um arquivo de estilo pede aspas simples e o código usa duplas, um guia cita uma ferramenta que não está instalada, um README dá um passo de instalação que a configuração não lê.
O `/analyze` não pergunta a você qual lado está certo.
Ele registra uma questão em aberto no documento dono do assunto, diz o que cada lado diz, e não toma partido; resolver isso é uma entrega própria, com uma página.

### Código legado: a strangler fig

Em um código sem arquitetura clara, o padrão para o FOCUS é "nenhum", porque o código não o segue, e o FOCUS inteiro significaria reescrevê-lo.
Há um caminho entre os dois: a strangler fig (figueira estranguladora), o nome que Martin Fowler deu à troca gradual de um sistema antigo, por causa de uma trepadeira que cresce em volta de uma árvore até ficar de pé sozinha.[^strangler-fig]
O código novo cresce ao lado do antigo: toda feature nova é uma fatia vertical no FOCUS ([capítulo 4](04-focus.md)), toda parte que uma entrega muda passa para uma, e o código antigo vai embora uma entrega de cada vez enquanto o projeto continua funcionando.
Dê isso como sua resposta à pergunta do FOCUS, por exemplo "FOCUS inteiro, como strangler fig: features novas e toda parte que uma entrega tocar viram fatias verticais; o resto fica até lá", e o `/analyze` escreve isso no docs/01 e em um ADR, para que todo `/propose` e `/apply` seguinte o siga.

## O que o código não diz: a pasta de contexto

O código diz o que um projeto faz e raramente por que, para quem ou o que foi prometido, então ponha tudo o que você tem sobre o projeto em uma pasta na raiz, `context/`, como está (propostas, contratos, e-mails, transcrições de reuniões), e os dois comandos a leem inteira antes de qualquer outra coisa: o `/brainstorm` parte do briefing que existe antes do código, o `/analyze` do que o código não consegue dizer.
O [capítulo 17](17-project-as-assistant.md) mostra como a pasta é mantida e quando ela entra no commit, uma pergunta que os dois comandos fazem, com o padrão acima.

## Revise antes do commit

Nenhum dos dois comandos coloca nada em stage (marcado para o próximo commit) nem faz commit: você lê primeiro o que ele escreveu.
Confira que:

* cada resposta que você deu chegou ao documento dono dela: o produto no docs/00, a stack no docs/01 e no ADR dela, o marco no docs/06;
* cada padrão que o agente manteve é um que você aceita sabendo; cada um que você rejeita é uma correção agora, antes que uma entrega se apoie nele;
* cada ADR registra uma decisão que você tomou, ou diz que a escolha foi do agente;
* cada slot do docs/05 diz o que e o comando, sem passos e sem saída colada; os passos estão num manual;
* o slot Manuals nomeia o manual de rodar o produto: devido, e por qual entrega, em um projeto novo; escrito, em `docs/manuals/`, em um projeto existente;
* em um projeto existente, cada afirmação observada é verdadeira no código (abra o arquivo que ela cita), cada questão em aberto é uma contradição que o código tem de fato, e nada descreve o que deveria existir em vez do que existe;
* em um projeto existente, uma pessoa que não leu mais nada consegue seguir cada manual, e cada comando que um manual dá existe no repositório.

Quando algo está errado, peça a correção ao agente na mesma sessão, que ainda guarda a conversa, e deixe que ele escreva a mudança; nunca edite à mão, porque o agente sabe que outros documentos a correção toca.
Leia com desconfiança.
Um assunto pulado não deixa buraco na prosa, e uma afirmação do README copiada como fato se lê tão bem quanto uma que o agente conferiu.
Só uma conferência contra o que você respondeu, ou contra o código, encontra qualquer um dos dois.

## O que o time ganha

Uma pessoa que não sabe responder a uma pergunta ainda recebe um bom documento, porque toda pergunta traz um padrão; e ninguém é perguntado sobre o que o código já diz, porque o `/analyze` o lê primeiro.
O time começa a primeira entrega com o produto, o vocabulário, as decisões e a fila escritos, e toda contradição que o código tem registrada como pergunta em vez de resolvida por um palpite.

## Pontos-chave

* O `/brainstorm` conversa sobre seis assuntos em ordem (produto, vocabulário, como é construído, convenções, slots do processo, primeiro marco) e escreve os documentos, os ADRs, o `AGENTS.md` e o `CLAUDE.md`, nunca código; a primeira entrega escreve o código.
* Toda pergunta vem com um padrão, então "your call" é uma resposta válida, e você confere cada padrão que o agente manteve.
* Escolha uma stack pelo que o projeto precisa, depois por quanto código público o agente aprendeu, depois por os tipos e testes deixarem ou não o agente conferir o próprio trabalho.
* O `/analyze` lê o repositório primeiro, pergunta em uma rodada e escreve primeiro o manual de rodar o produto, depois um para cada coisa que uma pessoa já faz à mão; o padrão de cada escolha é o que o código faz, uma contradição vira uma questão em aberto, e um código legado pode passar para o FOCUS como strangler fig.
* Revise antes do commit, contra as suas respostas e contra o código, e peça ao agente cada correção.

[^octoverse]: GitHub, "Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1", 2025, o relatório mais recente em 2026-09-28: contribuidores mensais no GitHub, agosto de 2025. <https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/>
[^strangler-fig]: Martin Fowler, "Strangler Fig", 2024. <https://martinfowler.com/bliki/StranglerFigApplication.html>
