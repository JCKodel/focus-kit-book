# 12. Começando: `/brainstorm` e `/analyze`

Depois deste capítulo você consegue começar um projeto novo com o `/brainstorm`, ou documentar um projeto existente com o `/analyze`, conversando, e revisar os documentos que cada comando escreve antes de fazer o commit deles (registrá-los no histórico do projeto).
Você também consegue escolher uma stack pelo que o projeto precisa e por quanto o agente a conhece, e guardar o que o código não diz onde o agente lê.

## O problema

Toda sessão seguinte lê os documentos do projeto antes de agir, então eles têm de existir antes da primeira entrega.
Um agente que começa sem nada escrito decide tudo sozinho, e um questionário falha pelo outro lado: pergunta a uma pessoa o que ela ainda não sabe responder, ou o que o código já diz.
O focus-kit tem dois comandos para isso, um para um repositório vazio e outro para um repositório com alguma coisa dentro, e os dois escrevem os mesmos documentos conversando e não escrevem código.

## `/brainstorm`: um projeto novo

O `/brainstorm` é o comando para um repositório que ainda não tem código.
Ele conversa sobre um assunto de cada vez, nesta ordem, e passa ao seguinte quando conseguiria escrever aquele documento sozinho, como diz o arquivo do kit para o comando:

1. **O produto** (docs/00): o que ele é em uma frase, para quem, o que ele não é, como é uma boa decisão aqui.
2. **O vocabulário** (docs/03): as dez a vinte palavras sem as quais o produto não pode ser descrito, cada uma com seu nome no código.
3. **Como ele é construído** (docs/01): a stack e a forma do código, com as duas escolhas do kit, o FOCUS e a estratégia de git, cada uma com a recomendação do agente para essa stack.
4. **As convenções** (docs/04): a língua da documentação e a língua dos identificadores, o estilo, onde ficam os testes, o formato do commit.
5. **Os slots do processo** (docs/05): o comando de verificação, os ambientes, como uma tela é provada, quando um ambiente além da sua máquina é atualizado.
6. **O primeiro marco** (docs/06): de três a oito entregas, uma linha cada, em ordem, e depois a revisão dele; as primeiras são o esqueleto em que as outras se apoiam.

### Um padrão em cada pergunta

O agente pergunta só o que não consegue decidir com um padrão sensato, e diz o padrão junto com a pergunta.
Então "your call" (você decide) é sempre uma resposta válida: o agente mantém o padrão dele, e uma pessoa que não sabe responder ainda recebe um bom documento.
Ele nunca pergunta por uma ferramenta pelo nome quando a pergunta é sobre o que você quer, e pergunta em rodadas de no máximo quatro perguntas, com a recomendação dele primeiro.
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
Na Ninjobs, o mesmo agente errava o design no Flutter, onde tinha poucos exemplos de um design system customizado para aprender, e acertava no React.

**A stack confere a si mesma?**
Um compilador que rejeita um tipo errado e testes que rodam em segundos avisam ao agente que ele errou antes que você precise avisar.
Uma stack em que um erro só aparece em tempo de execução, em uma tela, deixa essa conferência para você.

### O que ele escreve, e onde para

Quando os seis assuntos estão cobertos, o `/brainstorm` escreve o docs/00 a 06, um ADR para cada decisão que uma sessão futura poderia desfazer (a stack, FOCUS ou não, o git, qualquer coisa em que você hesitou), o `AGENTS.md`, o `CLAUDE.md` com a linha `@AGENTS.md`, e uma `work/done/` vazia.
Depois ele mostra a fila e para.
Ele não escreve código, nem configuração, nem arquivo de dependências: a primeira entrega faz isso, com uma página própria, pelo `/propose` em uma sessão nova ([capítulo 14](14-propose.md)).

Para a biblioteca da Parte I, um primeiro marco poderia ser assim, escrito para este capítulo:

````markdown
## Marco 1: uma bibliotecária empresta e recebe de volta

Quando ele fecha, uma bibliotecária consegue cadastrar livros, seus exemplares e
membros, emprestar um exemplar a um membro por 21 dias e registrar a devolução;
um membro com um livro atrasado ou com a inscrição suspensa é recusado.

```
[ ] esqueleto        app e servidor vazios, npm run verify, primeira captura de tela
[ ] catalogo         a bibliotecária cadastra livros e seus exemplares
[ ] membros          a bibliotecária cadastra, suspende e reativa membros
[ ] emprestar-livro  a bibliotecária empresta um exemplar, e as regras podem recusar
[ ] devolver-livro   a bibliotecária registra uma devolução, e o exemplar fica livre
[ ] m1-review        o marco conferido contra o parágrafo dele
```
````

O parágrafo diz o que uma pessoa consegue conferir quando o marco fecha, e a primeira linha, `esqueleto`, cria o comando de verificação que toda entrega seguinte roda; o [capítulo 13](13-queue-and-milestones.md) ensina a fila.

## `/analyze`: um projeto existente

O `/analyze` é o comando para um repositório que já tem alguma coisa dentro: código, documentos, ou os dois.
Ele funciona como o `/brainstorm`, com um padrão em cada pergunta e os mesmos documentos no fim, mas lê antes de perguntar, e o que o código diz ele não pergunta.

### O que ele lê

O arquivo do kit para o comando manda ler:

* o README e qualquer documentação que já exista;
* os manifestos, como `package.json`, `pyproject.toml` ou `go.mod`;
* a árvore de pastas, dois níveis abaixo;
* os pontos de entrada;
* os testes, e como eles rodam;
* a configuração de CI;
* os assuntos dos últimos cinquenta commits;
* qualquer arquivo de regras de agente que já exista, como `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md` ou `.cursorrules`.

A partir disso ele deduz a stack, como o código está organizado, onde moram as regras de negócio, como os erros viajam, o comando de verificação e os ambientes, e marca cada item como observado.
O que o projeto não tem, ele pula: em um repositório sem código, os documentos descrevem o que os arquivos dizem.

### O que ele pergunta

Uma rodada, de quatro assuntos apenas:

1. A língua da documentação. Padrão: a língua do README.
2. O propósito e o público do produto nas suas palavras, só quando nenhum README os diz.
3. O FOCUS e a estratégia de git. O padrão de cada um é o que o código já faz, e o agente diz o que é, então "your call" o mantém.
4. O primeiro marco: de três a oito entregas, ou de onde lê-las (issues, um arquivo TODO, um roadmap), e depois a revisão dele.

Um arquivo de regras que já existe não fica ao lado do `AGENTS.md`: as regras dele passam para o `AGENTS.md`, e o arquivo guarda só a linha que o importa e o que vale apenas para o host dele (o programa que roda o agente).
Os documentos descrevem o que existe, e não o que deveria existir.
O agente mostra a mudança antes de escrever, e não muda código nenhum.

### Onde o código contradiz a si mesmo

Um código que já viveu um tempo diz duas coisas ao mesmo tempo: um arquivo de estilo pede aspas simples e o código usa duplas, um guia cita uma ferramenta que não está instalada, um README dá um passo de instalação que a configuração não lê.
O `/analyze` não pergunta a você qual lado está certo.
Ele registra uma questão em aberto no documento dono do assunto, diz o que cada lado diz, e não toma partido; resolver isso é uma entrega própria, com uma página.

### Código legado: a strangler fig

Em um código sem arquitetura clara, o padrão para o FOCUS é "nenhum", porque o código não o segue, e o FOCUS inteiro significaria reescrevê-lo.
Há um caminho entre os dois: a strangler fig (figueira estranguladora), o nome que Martin Fowler deu à troca gradual de um sistema antigo, por causa de uma trepadeira que cresce em volta de uma árvore até ficar de pé sozinha.[^strangler-fig]
O código novo cresce ao lado do antigo: toda feature nova é uma fatia vertical no FOCUS ([capítulo 6](06-features-not-layers.md) e [capítulo 7](07-four-pieces.md)), toda parte que uma entrega muda passa para uma, e o código antigo vai embora uma entrega de cada vez enquanto o projeto continua funcionando.
Dê isso como sua resposta à pergunta do FOCUS, por exemplo "FOCUS inteiro, como strangler fig: features novas e toda parte que uma entrega tocar viram fatias verticais; o resto fica até lá", e o `/analyze` escreve isso no docs/01 e em um ADR, para que todo `/propose` e `/apply` seguinte o siga.

## O que o código não diz: a pasta de contexto

O código diz o que um projeto faz; raramente diz por que, para quem, ou o que foi prometido.
Esse conhecimento mora em propostas, contratos, e-mails, transcrições de reuniões, tickets e apresentações, e o que o agente não lê, ele tem de adivinhar.
Ponha tudo o que você tem sobre o projeto em uma pasta na raiz, `context/`, como está, sem triagem e sem resumo, e mantenha-a separada de `docs/`: `context/` é de onde o agente lê, `docs/` é o que ele escreve.
Quanto mais a pasta guarda, propostas para o cliente, transcrições de reuniões, e-mails, melhores os documentos que o agente escreve a partir dela, e mais gente do time ele consegue responder, muito além do código.
É a diferença entre "isto foi feito assim porque o cliente pediu, no e-mail do dia 12" e "ninguém sabe por que é assim".
Chegou um documento novo, ponha-o na pasta e peça ao agente que o leia e traga para o projeto o que ele muda: uma regra para o docs/00, um termo para o docs/03, uma linha para a fila.
Nenhum dos dois comandos procura essa pasta pelo nome, então diga isso na mesma mensagem, `/analyze Read context/ first, whole.` (leia `context/` primeiro, inteira); essa frase é instrução sua, e funciona também para o `/brainstorm` quando um briefing ou uma proposta existe antes do código.
Se a pasta entra no commit, e o que nunca pode entrar, é uma decisão própria ([capítulo 18](18-project-as-assistant.md)).

## Revise antes do commit

Nenhum dos dois comandos coloca nada em stage (marcado para o próximo commit) nem faz commit: você lê primeiro o que ele escreveu.
Confira que:

* cada resposta que você deu chegou ao documento dono dela: o produto no docs/00, a stack no docs/01 e no ADR dela, o marco no docs/06;
* cada padrão que o agente manteve é um que você aceita sabendo; cada um que você rejeita é uma correção agora, antes que uma entrega se apoie nele;
* cada ADR registra uma decisão que você tomou, ou diz que a escolha foi do agente;
* em um projeto existente, cada afirmação observada é verdadeira no código (abra o arquivo que ela cita), cada questão em aberto é uma contradição que o código tem de fato, e nada descreve o que deveria existir em vez do que existe.

Quando algo está errado, peça a correção ao agente na mesma sessão, que ainda guarda a conversa, e deixe que ele escreva a mudança; nunca edite à mão, porque o agente sabe que outros documentos a correção toca.
Leia com desconfiança.
O texto de um agente parece certo mesmo quando está errado: um assunto pulado não deixa buraco na prosa, e uma afirmação do README copiada como fato se lê tão bem quanto uma que o agente conferiu.
Só uma conferência contra o que você respondeu, ou contra o código, encontra qualquer um dos dois.

## O que o time ganha

Uma pessoa que não sabe responder a uma pergunta ainda recebe um bom documento, porque toda pergunta traz um padrão; e ninguém é perguntado sobre o que o código já diz, porque o `/analyze` o lê primeiro.
O time começa a primeira entrega com o produto, o vocabulário, as decisões e a fila escritos, e toda contradição que o código tem registrada como pergunta em vez de resolvida por um palpite.
Não há número para esse ganho: este livro não tem uma contagem de projetos começados com e sem os dois comandos.

## Pontos-chave

* O `/brainstorm` conversa sobre seis assuntos em ordem (produto, vocabulário, como é construído, convenções, slots do processo, primeiro marco) e escreve os documentos, os ADRs, o `AGENTS.md` e o `CLAUDE.md`, nunca código; a primeira entrega escreve o código.
* Toda pergunta vem com um padrão, então "your call" é uma resposta válida, e você confere cada padrão que o agente manteve.
* Escolha uma stack pelo que o projeto precisa, depois por quanto código público o agente aprendeu, depois por os tipos e testes deixarem ou não o agente conferir o próprio trabalho.
* O `/analyze` lê o repositório primeiro e pergunta em uma rodada; o padrão de cada escolha é o que o código faz, uma contradição vira uma questão em aberto, e um código legado pode passar para o FOCUS como strangler fig.
* Revise antes do commit, contra as suas respostas e contra o código, e peça ao agente cada correção: o texto dele parece certo mesmo quando está errado.

[^octoverse]: GitHub, "Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1", 2025, o relatório mais recente em 2026-09-28: contribuidores mensais no GitHub, agosto de 2025. <https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/>
[^strangler-fig]: Martin Fowler, "Strangler Fig", 2024. <https://martinfowler.com/bliki/StranglerFigApplication.html>
