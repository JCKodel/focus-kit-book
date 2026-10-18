# 4. FOCUS: features, não camadas, e as quatro peças

Depois deste capítulo você consegue organizar o código em fatias verticais, uma pasta por feature, e pôr cada arquivo de uma feature em uma das quatro peças do FOCUS, tela, orquestrador, caso de uso ou repositório, sabendo o que cada uma proíbe.
Você consegue seguir um evento por elas até um novo estado, e responder "o que acontece quando o evento X chega?" com um teste.
Você também consegue decidir qual peça recebe uma dependência como parâmetro, por uma pergunta só: o teste dela passa uma segunda implementação?

## O problema

Muitos projetos separam o código por camada técnica: uma pasta de telas, uma de controllers, uma de services, uma de models, uma de acesso ao banco de dados.
Cada feature fica espalhada por todas elas.
Emprestar um livro em uma biblioteca assim mexe em um arquivo em `views/`, `controllers/`, `services/`, `models/` e `repositories/`, e uma mudança em como o empréstimo funciona é uma mudança em cinco pastas.

O custo cai sobre quem faz a mudança.
Uma pessoa precisa encontrar os cinco arquivos e guardá-los na cabeça ao mesmo tempo; um agente precisa abrir as cinco pastas para aprender o que o empréstimo faz, e cada arquivo que ele carrega para entender a mudança enche o contexto em que ele trabalha.
As pastas dizem de que o código é feito, e nada sobre o que o programa faz.

As regras não se saem melhor.
Na maioria das aplicações, uma regra de negócio mora onde alguém precisou dela primeiro: uma parte em uma tela que esconde um botão, outra no handler que salva o formulário, e uma cópia em uma consulta.
Pergunte "o que acontece quando um bibliotecário empresta este exemplar a este membro?" e ninguém consegue responder lendo um lugar só.
Você descobre rodando o app, clicando e olhando o banco.
Uma pessoa não consegue testar essa resposta sem o app inteiro, e um agente a quem se pede para mudar a regra encontra duas das três cópias e muda essas duas.

FOCUS é o nome que este livro dá a um jeito de sair dos dois problemas: uma pasta por feature, e nela quatro peças, cada uma com um trabalho, e uma direção para tudo o que passa entre elas.

## A regra de dependência

As camadas respondiam a um problema real: regras misturadas com telas e SQL não podem ser mudadas, nem testadas, umas sem as outras.
Robert C. Martin (Uncle Bob) desenhou a resposta em 2012 como círculos concêntricos, com as regras de negócio no centro e o banco de dados, a web e os frameworks na borda, unidos pela regra de dependência, "*dependências de código-fonte só podem apontar para dentro*", então uma regra nunca nomeia uma tela, uma tabela ou uma biblioteca.[^martin-clean-2012]
Martin também perguntou, em 2011, o que as pastas de primeiro nível de um projeto gritam, o sistema ou o framework com que ele foi construído, e pastas chamadas `controllers/` e `models/` gritam o framework.[^martin-screaming]
Este livro mantém a regra de dependência e abandona a pasta por camada, e com ela a cerimônia de uma interface e de um mapeamento em cada fronteira para código que tem uma implementação só.

## Fatias verticais

Uma fatia vertical é uma pasta que guarda tudo de que uma feature precisa: as telas, as chamadas ao servidor, as rotas, as regras, o acesso ao banco de dados e os testes.
Jimmy Bogard deu nome ao estilo em 2018 depois de anos construindo sistemas assim, e deu a regra dele em uma linha: "*Minimize o acoplamento entre as fatias, e maximize o acoplamento dentro de uma fatia.*"[^bogard-vertical-slice]
Código que muda junto mora junto; código que muda por razões diferentes mora separado.

A biblioteca de empréstimos, o exemplo da Parte I, fica organizada assim:

```text
src/features/emprestimos/
    TelaDeEmprestimo.tsx, eventosDeEmprestimo.ts, regras.ts,
    repositorio.server.ts, rota.server.ts,
    regras.test.ts, eventosDeEmprestimo.test.ts,
    repositorio.server.test.ts
src/features/emprestimos/devolucao/   devolver um exemplar
src/features/membros/     o que a biblioteca guarda sobre um membro
src/features/catalogo/    livros e exemplares
src/lib/result.ts         Result, ok e err
```

`TelaDeEmprestimo.tsx` é a tela de empréstimo; `eventosDeEmprestimo.ts` recebe o que a tela pede e responde com o novo estado; `regras.ts` guarda as regras do capítulo 3, como `emprestar`; `repositorio.server.ts` lê e escreve no banco de dados, e `rota.server.ts` é o endereço do empréstimo no servidor.
Um nome terminado em `.server.ts` roda só no servidor, e o código do cliente nunca importa um deles.
Os testes ficam ao lado do código que testam.
Cada um desses arquivos é uma das quatro peças que este capítulo nomeia mais adiante, e o capítulo 5 dá a cada uma o seu teste.
A pasta `features/` fica em inglês, porque é o nome que este livro dá à pasta das fatias, assim como ele diz *feature*, sem traduzir; cada fatia dentro dela tem um nome em português, da biblioteca de empréstimos: `emprestimos/`, `membros/`, `catalogo/`.

A pasta de cima grita a biblioteca: empréstimos, membros, catálogo.
Uma mudança em como o empréstimo funciona mexe em `emprestimos/`, e tirar os empréstimos do produto tira uma pasta.
Em 1972, David Parnas comparou duas maneiras de dividir um mesmo programa em módulos: dividido pelos passos do processamento, uma mudança em como os dados eram guardados mexia em todos os módulos; dividido pelas decisões que provavelmente vão mudar, mexia em um só.
Ele propôs começar "*com uma lista de decisões de projeto difíceis ou de decisões de projeto que provavelmente vão mudar*", de modo que "*cada módulo seja então projetado para esconder tal decisão dos outros*".[^parnas-1972]
Uma pasta por camada divide o código pelos passos por que passa uma requisição; uma fatia aplica o critério de Parnas no tamanho de uma feature, e esconde do resto do programa as decisões da sua feature, como a forma de decidir e de guardar um empréstimo.

## O que é uma feature

Uma feature é uma coisa que o app guarda, nomeada por um termo do vocabulário do projeto (o empréstimo, o membro, o livro), ou uma coisa que o app faz sem guardar nada, nomeada pelo que faz, como uma verificação de `status` que responde se o serviço está no ar.
A fatia dela guarda toda ação sobre ela.
Emprestar e devolver agem os dois sobre o empréstimo: compartilham as regras, a tabela e o repositório dele, então são uma fatia só.
Membros e livros são outras coisas que a biblioteca guarda, cada uma com a sua tabela e as suas telas, então cada uma tem uma fatia própria.

Uma subfeature é uma subpasta.
Devolver um exemplar tem a sua tela e o seu evento, e mora em `emprestimos/devolucao/`, dentro da fatia cujo empréstimo ela encerra.

Um arquivo aparece em uma fatia quando se paga.
Uma feature sem regra não tem `regras.ts`, e uma feature que não guarda nada não tem repositório.
Não guardar nada não a torna menos feature: se ela tem a sua própria rota ou tela, tem a sua própria fatia.

## Onde mora o código compartilhado

O assunto do código decide onde ele mora quando duas features o usam.
Código sobre uma feature fica na fatia dessa feature, e outra fatia importa de lá o que precisa, seja um tipo, uma função de repositório ou uma tela.
`emprestimos/regras.ts` importa o tipo `Membro` de `membros/`, porque um membro é o que aquela fatia guarda; a página de um membro que lista os empréstimos dele importa de `emprestimos/`.
Duas fatias podem importar uma da outra.

O que não pertence a nenhuma feature, a forma de um valor como um endereço de email, ou encanamento como `Result`, sai das fatias para `src/lib/`.
Ele vai para lá no segundo uso e não antes, a regra do capítulo 3, e o arquivo diz onde estão o primeiro e o segundo uso.

## FOCUS, letra por letra

**F, Feature-oriented (orientado a features).** O código é organizado nas fatias verticais acima, e as quatro peças de uma feature moram na pasta dela, lado a lado.

**C, Clean (limpo).** As peças são as camadas da Clean Architecture de Martin, e mantêm a regra de dependência dela.
No desenho dele, um caso de uso fala com o armazenamento por uma interface que recebe, então uma regra ainda consegue chegar ao I/O, só que por uma porta com outro nome, e o teste dela precisa de um dublê atrás de cada porta.[^martin-clean-2012]
O FOCUS corrige isso com o orquestrador, que busca e salva em volta do caso de uso, então um caso de uso não recebe repositório nenhum: ele é uma função pura, dados entram, um `Result` sai, e ele guarda todo tipo de regra de negócio, uma decisão como quem pode pegar emprestado, uma validação como se um número de cartão está bem formado, uma formatação como a data de devolução se lê para o usuário.

**U, Unidirectional (unidirecional).** Tudo flui em um sentido: um evento, o orquestrador, os casos de uso e repositórios que ele chama, e um novo estado.
Não há binding, o mecanismo que alguns frameworks oferecem em que um campo na tela e um valor na memória atualizam um ao outro nos dois sentidos.
Nenhum estado volta: a tela nunca muda o estado que renderiza, e um caso de uso nunca chama um repositório.
Então "o que acontece quando o evento X chega?" tem uma resposta, e um teste consegue conferi-la.
Esse teste é o teste de um comportamento: "o usuário quer entrar com o Google" é um evento, tudo o que ele dispara é um caminho pelo orquestrador, e o que sai é um estado, um login confirmado ou uma falha, então o teste se lê "dada esta intenção, este estado", sem nada para inspecionar no meio.

**S, Scalable (escalável).** Toda peça é isolada e tem o próprio teste, então uma feature nova acrescenta a própria pasta e os próprios testes e não muda nenhuma outra.
É isso que escalável quer dizer aqui: o projeto pode crescer indefinidamente, feature após feature, sem que uma feature interfira em outra, porque cada feature fica na sua pasta e cada trabalho na sua peça.

## As quatro peças

| Peça | Faz | Proíbe |
|---|---|---|
| Tela | dispara eventos, renderiza o estado que recebe | regras de negócio, acesso a dados, formatação |
| Orquestrador | transforma um evento em um novo estado: valida e formata pelos casos de uso, busca pelos repositórios, aplica as regras pelos casos de uso, pede aos repositórios que salvem, publica o estado | decidir uma regra, persistir |
| Caso de uso | o único lugar de uma regra de negócio, seja uma decisão, uma validação ou uma formatação; puro: dados entram, `Result` sai | I/O, o framework, exceções |
| Repositório | busca e salva; o único lugar em que uma exceção vinda dos dados vira um `Result` | regras de negócio |

Leia primeiro a coluna "Proíbe": ela mantém cada peça no seu trabalho.
Uma tela que decide quem pode pegar emprestado, ou um repositório que decide isso, quebra a tabela, faça o que fizer de certo.

Um evento é o que aconteceu: um toque em "Emprestar", ou uma requisição chegando a um servidor.
Um estado é o que o orquestrador publica depois dele, inteiro: em uma tela, o que a tela renderiza; em um servidor, a resposta à requisição.
Uma tela não é só uma interface gráfica.
O JSON que uma API responde é uma tela, e o texto que uma ferramenta de linha de comando imprime também: a tela é a saída da computação, entrada, processamento, saída, em qualquer forma que deixe o programa.
Ela é burra de propósito: não formata nem uma data; renderiza o texto que o estado traz, e o caso de uso que o formatou tem um teste.

### Drivers e serviços

Um repositório não fala com o disco nem com a rede por conta própria; ele usa um driver, a biblioteca que fala com a coisa de fora.
Os drivers de costume vêm de terceiros: a biblioteca cliente de uma engine de banco de dados, o programa que guarda e consulta os dados, como o SQLite ou o PostgreSQL; um ORM por cima dela, como o Prisma ou o Entity Framework; um cliente HTTP; o SDK de um fornecedor de nuvem, como o do Firebase.
Um projeto escreve um driver só quando a coisa de fora não tem biblioteca: um cliente para a API de um gateway de pagamento, um leitor dos extratos em CSV do banco, um invólucro em volta do Bluetooth do celular.
O driver conhece o protocolo e nada do produto; o repositório conhece as tabelas e as mensagens do produto e nada do protocolo, então um driver pode ser trocado sem que uma regra perceba.

Um serviço é um ajudante que as quatro peças não nomeiam: código técnico que não é regra nem I/O, como gerar o hash de uma senha, comprimir uma imagem ou montar um PDF.
Em geral ele é chamado por um repositório, antes de salvar ou depois de ler, e é testado como uma função.

## Um evento, um novo estado

Um bibliotecário empresta um exemplar a um membro.
O toque em "Emprestar" é o evento, e a tela que mostra o empréstimo, ou o motivo da recusa, é o novo estado.
Estes são os passos entre os dois:

1. **A tela dispara o evento**, `EmprestimoPedido { exemplarId, membroId }`, e não faz mais nada.
2. **O orquestrador o recebe** e confere que ele traz os dois ids; em um servidor o evento é a requisição, então ler o corpo dela faz parte de recebê-lo.
3. **Os repositórios buscam** o membro, por `buscarMembro`, e o exemplar, por `buscarExemplar`.
4. **O caso de uso decide**: `emprestar` devolve um `Emprestimo` com data de devolução 21 dias depois, ou a recusa `TemLivrosEmAtraso` ou `MembroSuspenso`.
5. **O repositório salva**: `inserirEmprestimo` transforma a recusa do índice único a um segundo empréstimo aberto do exemplar em `JaEmprestado`, como o [capítulo 3](03-simplicity-and-results.md) mostrou.
6. **O orquestrador publica o novo estado**, que a tela renderiza: `Emprestado` mostra a data de devolução, `Recusado` "Devolva primeiro os seus livros atrasados.", `Falhou` "Não foi possível acessar o banco da biblioteca. Tente de novo."

O estado e os repositórios de que o orquestrador precisa são tipos no arquivo dele, `eventosDeEmprestimo.ts`:

```ts
type EmprestimoPedido = { exemplarId: string; membroId: string };

type EstadoDoEmprestimo =
	| { tipo: "Emprestado"; emprestimo: Emprestimo }
	| { tipo: "Recusado"; recusa: RecusaDeEmprestimo | "NaoEncontrado" }
	| { tipo: "Falhou"; excecao: BancoDeDadosFalhou };

type RepositoriosDeEmprestimo = {
	buscarMembro(id: string): Result<Membro, "NaoEncontrado" | BancoDeDadosFalhou>;
	buscarExemplar(id: string): Result<Exemplar, "NaoEncontrado" | BancoDeDadosFalhou>;
	inserirEmprestimo(emprestimo: Emprestimo): Result<Emprestimo, "JaEmprestado" | BancoDeDadosFalhou>;
};
```

O orquestrador em si são os passos 3 a 6, em ordem, depois que o evento foi recebido e tipado:

```ts
function estadoDe(erro: RecusaDeEmprestimo | "NaoEncontrado" | BancoDeDadosFalhou): EstadoDoEmprestimo {
	if (typeof erro === "string") return { tipo: "Recusado", recusa: erro };
	return { tipo: "Falhou", excecao: erro };
}

export function emprestimoPedido(
	evento: EmprestimoPedido,
	hoje: string,
	repositorios: RepositoriosDeEmprestimo,
): EstadoDoEmprestimo {
	const membro = repositorios.buscarMembro(evento.membroId);

	if (!membro.ok) return estadoDe(membro.error);

	const exemplar = repositorios.buscarExemplar(evento.exemplarId);

	if (!exemplar.ok) return estadoDe(exemplar.error);

	const emprestimo = emprestar(exemplar.value, membro.value, hoje);

	if (!emprestimo.ok) return estadoDe(emprestimo.error);

	const salvo = repositorios.inserirEmprestimo(emprestimo.value);

	if (!salvo.ok) return estadoDe(salvo.error);
  
	return { tipo: "Emprestado", emprestimo: salvo.value };
}
```

Cada linha ou pergunta a um repositório, ou pergunta ao caso de uso, ou transforma uma resposta no estado; nenhuma decide quem pode pegar emprestado.
As recusas são strings e a exceção é um objeto com um `codigo`, então `estadoDe` separa um `Recusado` de um `Falhou` com uma verificação só.
O código mostra mais três coisas:

* **Os repositórios são um parâmetro.** O servidor passa os reais, ligados ao banco dele, e nada mais na função vem de fora.
* **Um teste passa repositórios falsos.** Um repositório falso é uma segunda implementação que responde o que o teste define, então o teste sabe quais repositórios foram chamados, com o quê, e que estado saiu, e o fluxo inteiro de uma feature é provado sem banco e sem tela (o capítulo 5 mostra o teste).
* **O relógio é um valor.** `hoje` é lido uma vez, onde o evento chega, e repassado como dado; nem `emprestimoPedido` nem `emprestar` leem o relógio, então o teste de uma data de devolução passa a data que quiser.

## Dependências só onde existe uma implementação falsa

Uma dependência é algo de que um trecho de código precisa, de fora dele, para rodar: o banco de dados, a rede, o relógio, outro módulo.
Martin Fowler deu nome à prática de entregá-la de fora em 2004: depois de longa discussão, escreveu, "*nos decidimos pelo nome Injeção de Dependência*".[^fowler-injection]
Mark Seemann acrescentou onde as partes reais são montadas: em um lugar, "*o mais perto possível do ponto de entrada da aplicação*", que ele chamou de composition root (raiz de composição).[^seemann-composition-root]

Injetadas em toda parte, as dependências viram a sua própria camada de cerimônia: uma interface para cada classe, um contêiner, um parâmetro que ninguém varia.
Injetar em toda parte resolve um problema real em um SDK, cujos usuários precisam substituir partes que não são deles, e é cerimônia dentro de uma aplicação, onde cada uma dessas interfaces tem uma implementação só, para sempre.
O DRY já dá a regra: o que não tem motivo para existir não existe.
Se, em uma aplicação, só os repositórios têm duas implementações, a real e a falsa que os testes passam, então só os repositórios ganham uma interface, ou um parâmetro; um caso de uso que sempre será aquela única função concreta não ganha nenhum dos dois.
Este livro traça essa linha mais estreita: uma peça recebe uma dependência como parâmetro só onde o teste dela passa uma segunda implementação.

`emprestimoPedido(evento, hoje, repositorios)` é essa linha traçada uma vez: o orquestrador recebe os seus repositórios porque o teste dele passa repositórios falsos.
O resto segue do mesmo teste.

* **Um repositório do servidor recebe o banco de dados que usa**, `buscarMembro(db, id)`, porque o teste dele passa um banco de dados em memória com as migrações reais; o código de início do servidor abre o banco real e o repassa, e essa é a raiz de composição.
* **Um caso de uso não recebe nenhuma.** `emprestar` recebe dados e devolve um valor; o teste dele passa dados, e não há nada para trocar.
* **Uma tela não recebe nenhuma.** Ela tem uma implementação só, e um parâmetro ali existiria por cerimônia, o que o KISS descarta.

## O orquestrador em outros lugares

O orquestrador tem outros nomes em outras stacks, e o trabalho é o mesmo.
No Flutter ele é um BLoC, uma classe que recebe eventos e emite estados;[^bloc] no .NET ele é o padrão Mediator, como na biblioteca MediatR de Jimmy Bogard, em que cada requisição vai para um handler;[^mediatr] no MVVM ele é o view model, e no MVC dos frameworks web o controller é onde o trabalho dele fica; em um servidor ele é o handler da rota que recebe a requisição e devolve a resposta; em um cliente React ele é um hook que guarda o estado e executa o evento.
Em um cliente os repositórios chegam à rede, então o orquestrador espera por eles com `await`; nada mais nele muda.

## Quando uma peça se paga

Nada no FOCUS existe por cerimônia.
Um caso de uso existe quando há uma regra, um repositório quando há I/O, um orquestrador quando um evento leva a um novo estado, e uma tela quando há uma tela para mostrar.
Uma feature que mostra uma lista de livros sem regra nenhuma não tem caso de uso: o orquestrador pergunta ao repositório e publica o que recebeu.
KISS, YAGNI e DRY decidem quando uma peça é escrita: quando uma entrega precisa do trabalho dela, e não antes.
Na Ninjobs eu exigi toda peça em toda feature e um campo levava oito arquivos ([capítulo 3](03-simplicity-and-results.md)); a culpa foi da exigência, e as quatro peças são um lugar para cada trabalho, então uma feature com menos trabalhos tem menos peças.

## O que o time ganha

Uma mudança mexe em uma pasta, e um agente lê uma fatia: uma entrega sobre empréstimo nomeia `emprestimos/`, e o agente carrega a tela, o evento, as regras, o acesso ao banco de dados e os testes deles lado a lado, e nada sobre outra feature, e os testes mostram a ele o que fingir e nada mais.
Quem revisa vê o diff de uma entrega dentro de uma pasta e sabe que ela não mexeu em mais nada.
Toda regra fica em um caso de uso, uma função pura, então ela tem um teste que não precisa de preparação, e "o que acontece quando o evento X chega?" é um teste: chame o orquestrador com o evento e repositórios falsos, e confira o estado que ele devolve.
Cliente e servidor compartilham os casos de uso: o servidor impõe `emprestar`, e o cliente importa `podePegarEmprestado` só para decidir o que mostrar, como deixar "Emprestar" apagado para um membro com um livro atrasado, então a regra é escrita e testada uma vez, e a cópia da decisão no cliente nunca discorda da do servidor.

## Pontos-chave

* Uma fatia vertical guarda tudo de que uma feature precisa em uma pasta; uma feature é uma coisa que o app guarda, ou uma coisa que ele faz sem guardar nada, e código que não pertence a nenhuma feature vai para `lib/` no segundo uso.
* FOCUS é Feature-oriented (fatias verticais), Clean (a regra de dependência, com um caso de uso que não recebe repositório porque o orquestrador busca e salva), Unidirectional (evento, orquestrador, novo estado, nada volta, então um comportamento é um teste) e Scalable (toda peça isolada, com o próprio teste).
* A tela dispara eventos e renderiza o estado sem formatar nada; o orquestrador transforma um evento em um novo estado; um caso de uso guarda uma decisão, uma validação ou uma formatação como função pura; o repositório busca e salva por um driver, e transforma uma exceção vinda dos dados em um `Result`.
* Uma peça recebe uma dependência só onde o teste dela passa uma implementação falsa: orquestradores e repositórios do servidor recebem, casos de uso e telas não, e o relógio é um valor.
* Escreva uma peça quando uma entrega precisar do trabalho dela, e no cliente importe o caso de uso do servidor para decidir o que mostrar, nunca uma segunda cópia da regra.

[^martin-clean-2012]: Robert C. Martin, "The Clean Architecture", The Clean Code Blog, 2012-08-13, acesso em 2026-09-30. <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[^martin-screaming]: Robert C. Martin, "Screaming Architecture", The Clean Code Blog, 2011-09-30, acesso em 2026-09-30. <https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html>
[^bogard-vertical-slice]: Jimmy Bogard, "Vertical Slice Architecture", 2018, acesso em 2026-09-30. <https://www.jimmybogard.com/vertical-slice-architecture/>
[^fowler-injection]: Martin Fowler, "Inversion of Control Containers and the Dependency Injection pattern", martinfowler.com, 2004, acesso em 2026-09-30. <https://martinfowler.com/articles/injection.html>
[^seemann-composition-root]: Mark Seemann, "Composition Root", 2011-07-28, acesso em 2026-09-30. <https://blog.ploeh.dk/2011/07/28/CompositionRoot/>
[^parnas-1972]: D. L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules", Communications of the ACM 15(12), 1972. <https://doi.org/10.1145/361598.361623>
[^bloc]: Bloc, "Bloc State Management Library", documentação, acesso em 2026-09-29. <https://bloclibrary.dev/>
[^mediatr]: Jimmy Bogard, "MediatR", acesso em 2026-09-29. <https://github.com/jbogard/MediatR>
