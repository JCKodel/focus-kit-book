# 3. Simplicidade e resultados: KISS, YAGNI, DRY e exceções como valores

Depois deste capítulo você consegue recusar um trecho de código, um documento ou uma verificação de que nenhuma entrega precisa, dizer qual entre KISS, YAGNI e DRY o recusa, e saber o momento em que uma versão compartilhada é devida: a segunda ocorrência concreta.
Você consegue escrever uma regra de negócio como uma função pura que devolve um `Result` (resultado), e distinguir uma exceção de uma recusa e de um erro em qualquer linguagem.
Você também consegue manter as exceções de uma biblioteca na fronteira, de modo que uma biblioteca nova mude um arquivo, e deixar o compilador recusar um caso que você esqueceu de tratar.

## O que cresceu na Ninjobs

Na Ninjobs, o meu próprio produto, eu deixei a complexidade crescer antes de o processo dela mudar.
Uma entrega tinha que passar por 29 verificações, e nenhuma delas jamais tinha pegado um erro no produto: eram caras de satisfazer e fáceis de contornar.
Uma decisão morava em seis lugares que podiam discordar: os documentos, as especificações, as mudanças, os ADRs, um roteiro e o código.
E porque eu exigia a forma completa, em camadas, da arquitetura em toda feature, formulários triviais incluídos, mostrar um campo em uma tela levava oito arquivos.
A culpa não era da arquitetura; KISS e YAGNI se perderam, uma adição razoável por vez.
O processo que o substituiu manteve duas verificações, cada uma ligada a um erro que ela pega, e um lugar por fato (capítulo 6).

Fred Brooks dividiu a dificuldade do software em duas em 1987: a complexidade essencial, que pertence ao próprio problema, e a complexidade acidental, que as pessoas que constroem acrescentam pelo caminho.[^brooks-silver-bullet]
Ninguém consegue remover a primeira; a segunda é uma escolha, feita um arquivo por vez, e os três princípios deste capítulo são três maneiras de recusá-la.
Um agente deixa mais barato errar essa escolha: ele escreve a camada, a opção e a terceira cópia em segundos, cada uma plausível, e cada uma vira código que alguém precisa ler, revisar e manter verdadeiro.

## KISS: mantenha simples

"Keep it simple, stupid" (mantenha simples, estúpido) é atribuído a Kelly Johnson, o engenheiro aeronáutico que liderou a Skunk Works da Lockheed, cuja regra era que o que os seus engenheiros projetassem tinha de poder ser consertado em campo por um mecânico mediano com um punhado de ferramentas comuns.
A regra é sobre a pessoa que vem depois: o projeto tem que ser simples o bastante para ela, sob pressão, sem o autor na sala, porque uma coisa simples é uma coisa que se entende e se conserta.

No código, a pessoa que vem depois é um colega, um agente em uma sessão nova, ou você daqui a seis meses.
KISS pede a forma mais simples que faz o trabalho: uma função antes de uma classe, um valor antes de uma configuração, um arquivo antes de três.
Os exemplos de código deste livro foram escritos para ele, em TypeScript, curtos o bastante para caber na cabeça; as ideias valem em qualquer linguagem.
Nesta edição, os nomes que o código inventa, de funções, tipos e variáveis, estão em português, sem acentos, como é costume em identificadores; as palavras da própria linguagem, como `function` e `return`, e os nomes das bibliotecas usadas ficam como são.
A data de devolução de um empréstimo na biblioteca de empréstimos, o exemplo da Parte I, é 21 dias depois do empréstimo:

```ts
const DIAS_DE_EMPRESTIMO = 21;

function dataDeDevolucao(hoje: string): string {
	const devolucao = new Date(hoje);
	devolucao.setUTCDate(devolucao.getUTCDate() + DIAS_DE_EMPRESTIMO);
	return devolucao.toISOString().slice(0, 10);
}
```

Ela recebe uma data e devolve uma data, e qualquer pessoa a lê de uma vez.

Em um processo, KISS pede o mesmo a cada passo: o menor número de documentos que guardam o que o projeto sabe, o menor número de comandos que levam uma entrega, o menor número de marcas que dizem onde ela está.
Um passo que alguém recém-chegado não consegue explicar depois de ler uma vez é um passo a questionar.

## YAGNI: você não vai precisar disso

YAGNI, "you aren't gonna need it" (você não vai precisar disso), vem do Extreme Programming, o método que Kent Beck descreveu em *Extreme Programming Explained* em 1999.[^beck-xp]
Martin Fowler rastreia a frase até uma conversa no projeto onde o XP tomou forma: a cada capacidade que um colega dizia que o sistema logo precisaria, Beck respondia que eles não iam precisar dela.[^fowler-yagni]
A regra: uma capacidade que você presume que o software vai precisar depois não é construída agora.

Uma feature presumida de que ninguém precisa desperdiça o esforço de construí-la, e uma que afinal é necessária costuma precisar ser refeita, porque as necessidades mudaram enquanto ela esperava.
Até a feature presumida que se mostra certa paga o atraso e a carga: a feature que tem valor agora espera enquanto ela é construída, e o código dela "*acrescenta alguma complexidade ao software*" enquanto ficar.[^fowler-yagni]
Suponha que alguém espere que a biblioteca empreste por prazos diferentes a tipos diferentes de membro, e escreva isso agora:

```ts
type CategoriaDeMembro = "adulto" | "crianca" | "pesquisador";

type PoliticaDeEmprestimo = {
	diasPara(categoria: CategoriaDeMembro): number;
	renovacoes(categoria: CategoriaDeMembro): number;
};
```

O documento de produto não nomeia nenhuma categoria e nenhuma renovação.
Todo leitor de `emprestar` agora precisa aprender uma política que a biblioteca não tem, todo teste precisa passar uma, e quando as categorias chegarem, não serão estas três.
`DIAS_DE_EMPRESTIMO = 21` é a regra inteira até que uma entrega peça mais.

Fowler traça o limite no mesmo artigo: YAGNI "*só se aplica a capacidades construídas no software para sustentar uma feature presumida, não se aplica ao esforço de deixar o software mais fácil de modificar*".[^fowler-yagni]
Um teste, um nome claro, uma regra tirada de uma tela para uma função própria: isso é qualidade interna, e YAGNI nunca argumenta contra ela.
YAGNI só funciona em código fácil de mudar, porque a promessa é que você vai acrescentar a capacidade quando ela for necessária, e mudança barata é o que torna essa promessa verdadeira.

## DRY: um lugar para cada conhecimento

Andy Hunt e Dave Thomas deram nome ao DRY, "don't repeat yourself" (não se repita), em *The Pragmatic Programmer* em 1999: "*Todo conhecimento deve ter uma representação única, inequívoca e autoritativa dentro de um sistema.*"[^pragmatic-programmer]
A unidade é o conhecimento.
Duas linhas idênticas podem ser dois conhecimentos, e um conhecimento pode estar escrito em duas linhas que não se parecem em nada.

"Um empréstimo dura 21 dias" é um conhecimento.
Escrito como `21` em `dataDeDevolucao` e de novo como "Devolução em 21 dias" na tela de empréstimo, ele está em dois lugares, e no dia em que a biblioteca passar para 14 dias um deles vai ser esquecido.
A tela importa `DIAS_DE_EMPRESTIMO`, e o conhecimento mora em um lugar só.

"O nome de um membro não pode ser vazio" e "o título de um livro não pode ser vazio" são dois conhecimentos que por acaso se leem igual hoje.
Junte os dois em uma regra `naoVazio` compartilhada por membros e livros, e no dia em que um título puder ser vazio para um manuscrito sem título, a mudança chega aos membros também.

Sandi Metz deu nome à falha oposta em 2016: "*duplicação é muito mais barata que a abstração errada*".[^metz-wrong-abstraction]
A abstração errada é a função compartilhada que dois chamadores usavam por razões diferentes; cada novo chamador acrescenta um parâmetro e uma condição, até que ninguém consiga mudá-la sem quebrar alguém.
O remédio dela é devolver o código a cada chamador e recomeçar do que cada um precisa.
DRY e Metz concordam: um lugar para cada conhecimento, e uma versão compartilhada só para o que é o mesmo conhecimento.

## Abstração na segunda ocorrência

Os três princípios se encontram em uma regra, que o processo deste livro escreve em todo projeto: uma abstração é escrita na segunda ocorrência concreta, e a entrega que a escreve diz qual foi a primeira.
Uma cópia não é prova de que uma versão compartilhada seja necessária: é um palpite, e YAGNI recusa palpites.
Duas cópias são o erro que já aconteceu, e DRY pede um lugar só.
Nomear a primeira cópia torna o movimento verificável: quem revisa abre as duas e vê que são o mesmo conhecimento, que é o teste de Metz.

Na biblioteca de empréstimos, `Result`, o tipo que carrega um valor ou o que o impediu (a seção dele vem a seguir), aparece primeiro dentro da feature de empréstimos, como o tipo de retorno de `emprestar` em `features/emprestimos/regras.ts`.
Ele fica lá enquanto tem um usuário.
Depois, uma entrega de membros precisa de uma regra que pode recusar, e `Result` seria escrito uma segunda vez; essa entrega o move para `src/lib/result.ts`, a pasta do código que não pertence a nenhuma feature (capítulo 4), e diz isso:

```ts
// Primeiro uso: features/emprestimos/regras.ts (emprestar).
// Segundo uso: features/membros/regras.ts (cadastrar).
export type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };
```

`ok` e `err`, as duas funções que constroem um `Result`, vão junto, e as duas features os importam de lá.
Se o movimento tivesse vindo no primeiro uso, teria sido um palpite que por acaso deu certo; no segundo, é um fato com duas testemunhas.

## Uma função pura

Uma regra que mora dentro de uma tela, de um controller ou de uma chamada ao banco de dados não pode ser testada sem essa tela, esse controller ou esse banco.
Uma função é pura quando a mesma entrada sempre dá a mesma saída e nada mais acontece: nenhuma leitura de banco de dados, nenhuma escrita em arquivo, nenhum relógio, nenhuma rede.
O teste dela é dado entrando, valor saindo, e não precisa de preparação.
Uma função impura precisa que o mundo seja arrumado antes de rodar, e todo teste paga por essa arrumação.

Na biblioteca de empréstimos, a regra "um membro com um livro atrasado não pode pegar outro" é uma função pura:

```ts
type Membro = { id: string; emAtraso: number };

type Recusa = "TemLivrosEmAtraso";

function podePegarEmprestado(membro: Membro): Result<Membro, Recusa> {
	if (membro.emAtraso > 0) return err("TemLivrosEmAtraso");
	return ok(membro);
}
```

Ela lê um membro e responde.
De onde o membro veio, um banco de dados ou um teste, não é assunto dela.
Imutabilidade é a mesma ideia aplicada aos dados: uma função que muda a sua entrada esconde uma segunda saída, então `podePegarEmprestado` devolve o membro que recebeu ou uma recusa, e não muda nada.

A Clean Architecture, como costuma ser praticada, injeta os repositórios no caso de uso que guarda a regra, e o teste dele passa a precisar de um fake para cada um; este livro mantém `podePegarEmprestado` pura, recebendo um membro e não um jeito de buscá-lo, e deixa buscar e salvar para um orquestrador, a função em volta da regra que o capítulo 4 constrói.

## Result: o valor que carrega uma falha

`Result` é um tipo que guarda o valor ou o que o impediu:

```ts
type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

function ok<T>(value: T): Result<T, never> {
	return { ok: true, value };
}

function err<E>(error: E): Result<never, E> {
	return { ok: false, error };
}
```

Quem chama lê `ok` antes de alcançar `value` ou `error`, e o compilador estreita o tipo nessa checagem.

O motivo para carregar uma falha em um valor, seja qual for a forma, um union type como aqui ou um enum, é o que o compilador faz com ela: um `switch` sobre a falha que deixa um caso de fora não compila.
Todo resultado que uma regra pode produzir ou é tratado ou é um erro de compilação, e esse erro é o valor inteiro desta construção: o compilador, e não uma revisão de código, garante que nenhum caso foi esquecido, no dia em que a regra é escrita e no dia em que um caso é acrescentado.
A seção "Todo caso tratado" mostra a checagem em TypeScript.

A área chama o princípio de "errors as values", erros como valores, a partir do "*erros são valores*" do Go;[^go-errors] este livro diz "exceções como valores", e a próxima seção diz por quê.

## Exceção, recusa, erro

Uma falha é uma de três coisas, e o nome da classe nunca diz qual.
As falhas nativas do JavaScript são todas um `Error`, e as do .NET são todas uma `Exception`, então quem decide é a causa.
Dart é a única linguagem que eu vi tornar a diferença visível: o seu `dart:core` tem uma classe `Exception`, "*feita para ser capturada*", e uma classe `Error`, para "*uma falha do programa que o programador deveria ter evitado*".[^dart-core]

* **Uma exceção** é uma falha esperada vinda de fora do programa: o banco de dados caiu, a rede caiu, o disco encheu.
  Nenhum código está errado.
  Ela é capturada na fronteira com o mundo de fora e devolvida como um valor, por dois motivos.
  A exceção pertence ao domínio de onde foi lançada: uma biblioteca de login lança a sua própria `AppleSignInException`, e o domínio da aplicação não tem ideia do que é o login com Apple; tudo o que ele precisa saber é que o login falhou.
  Traduzida em um valor, `LoginFalhou`, a falha passa a falar a língua da aplicação e, como membro de um tipo, entra na checagem exaustiva: toda exceção que a aplicação pode encontrar é tratada, e o compilador prova isso.
* **Uma recusa** é uma regra dizendo não: um membro com livros atrasados, um telefone com dígitos de menos, um horário já ocupado.
  Nada falhou; a regra fez o seu trabalho.
  Ela também é devolvida como um valor, e é o resultado mais comum que um programa trata.
* **Um erro** é um bug: código que está errado.
  Ele nunca é capturado.
  Ele chega à sua tela enquanto você desenvolve e ao seu analytics quando o programa roda, para que você o corrija.

Por isso este livro não diz "erros como valores".
Um erro é um bug, e um bug nunca é um valor: é uma correção.
O que viaja em um `Result` é uma exceção ou uma recusa.

## Por que não lançar

Uma função devolve um valor, e a sua assinatura diz qual.
Um throw usado para conduzir o fluxo, no lugar de um return, custa três coisas.
Ele sai por uma porta que o ponto de chamada não mostra: a função "devolve" algo que a assinatura nunca mencionou, por um caminho que quem chama não escreveu, e cada chamada dentro dela é mais uma porta dessas.
Ele faz a assinatura mentir: `function emprestar(...): Emprestimo` não diz nada sobre as três maneiras de falhar, então o compilador não consegue verificar que todo caso é tratado, enquanto `Result<Emprestimo, RecusaDeEmprestimo>` diz isso no tipo, e um `switch` sobre a recusa que esquece um caso não compila.
E o catch largo o bastante para conduzir o fluxo também captura os bugs que acontecem dentro dele, e eles somem em uma mensagem que ninguém lê.

A maior parte do que um programa trata é uma regra dizendo não, então um programa que lança para recusas tem uma saída escondida em cada regra, quem chama e o agente que lê o código precisam saber de cor quais falhas eram intencionais, e cada recusa paga por uma exceção lançada e capturada: no benchmark de Stephen Toub, mil throws, cada um capturado através de dez chamadas assíncronas, levaram cerca de um oitavo de segundo no .NET 8.[^toub-net9]

## Onde mora o catch

Exceções só existem onde o programa toca o mundo de fora: uma chamada ao banco de dados, uma requisição de rede, um arquivo, o armazenamento do celular.
Então esse é o único lugar onde mora um `try`/`catch`, e ele faz uma coisa: transforma a exceção da biblioteca no valor do programa.

```ts
type BancoDeDadosFalhou = { codigo: "BancoDeDadosFalhou"; mensagem: string };

function consultar<T>(executar: () => T): Result<T, BancoDeDadosFalhou> {
	try {
		return ok(executar());
	} catch (lancado) {
		const mensagem = lancado instanceof Error ? lancado.message : String(lancado);
		return err({ codigo: "BancoDeDadosFalhou", mensagem });
	}
}
```

Toda chamada ao banco de dados roda dentro de `consultar`, e nada depois dele sabe qual biblioteca de banco de dados está em uso.
O domain-driven design chama um tradutor assim de camada anticorrupção, cujo "*propósito central ... é proteger o modelo de domínio*";[^anti-corruption-layer] este livro dá um passo a mais e traduz as exceções também.
Troque a biblioteca de banco de dados e `consultar` muda; o resto do programa não.

A mesma fronteira pode transformar uma exceção em uma recusa.
Quando dois membros pegam o último exemplar no mesmo instante, um índice único no banco de dados recusa a segunda escrita.
O código que rodou a escrita lê essa falha e devolve a recusa `JaEmprestado`, já que nada quebrou: a regra valeu, no único lugar onde duas requisições não podem competir.
Qualquer outra falha da mesma escrita continua `BancoDeDadosFalhou`.

Um catch largo assim também captura um bug lançado dentro de `executar`, e o transforma em `BancoDeDadosFalhou`.
Duas coisas trazem o bug de volta a você: um teste que roda toda chamada ao banco de dados contra um banco de dados real, em memória, e confere o valor que recebe (capítulo 5), e uma linha de log que imprime a `mensagem` antes de o programa responder.

Dois tipos de throw passam pela fronteira intocados, um fatal, como acabar a memória, e o fluxo de controle próprio de um framework, lançado de propósito.
Então a regra fica assim: capture na fronteira com o mundo de fora, traduza, e deixe todo o resto passar.

## Todo caso tratado

Um `Result` compensa quando o compilador confere o tratamento.
Em TypeScript, um `Record` sobre o tipo da recusa precisa nomear cada membro:

```ts
type RecusaDeEmprestimo = "TemLivrosEmAtraso" | "JaEmprestado" | "MembroSuspenso";

const mensagem: Record<RecusaDeEmprestimo, string> = {
	TemLivrosEmAtraso: "Devolva primeiro os seus livros atrasados.",
	JaEmprestado: "Este exemplar acabou de ser emprestado a outra pessoa.",
	MembroSuspenso: "A sua matrícula está suspensa.",
};
```

Acrescente uma recusa às regras e esqueça a mensagem dela, e o build falha, antes que algum usuário veja uma tela em branco.
Em Rust e em Dart, um `match` ou um `switch` exaustivo faz o mesmo; em Go, um linter.

## Os mesmos princípios em um processo

> **Cuidado.** Um agente escreve mais do que código nessa velocidade: escreve também scripts, verificações, regras e passos, cada um plausível, e um processo cresce como o código cresce, uma adição razoável por vez.
> Enquanto este livro era escrito, o agente propôs que todo marco terminasse com um passo de revisão, uma boa ideia; a revisão achou erros, que abriram um marco de correções, cuja própria revisão abriu um segundo, e um terceiro estava a caminho quando eu o interrompi.
> O que eu devia estar fazendo era ler os capítulos e dizer o que mudar.
> Por conta própria, o agente tinha entrado numa espiral de verificações que verificavam verificações, e uma pergunta é o que a interrompe: que erro concreto este passo teria pegado?

O capítulo 16, o regulador, transforma essa pergunta na regra que todo passo do processo precisa responder: um passo entra quando nomeia o erro concreto que teria pegado, e sai quando não nomeia nenhum.

## O que o time ganha

Menos para ler, menos para revisar e menos para manter verdadeiro: cada arquivo, opção e verificação que não é escrito é um que nenhuma pessoa revisa, nenhum agente carrega em uma sessão e nenhuma entrega precisa satisfazer, enquanto a Ninjobs fazia toda entrega passar por 29 verificações que nunca tinham pegado um erro.
Toda regra é uma função que um teste chama com dados, então uma regra tem um teste antes de ter uma tela, e um agente a quem se pede para mudá-la a encontra em um lugar só, com os casos dela nomeados no tipo.
Toda falha que quem chama precisa tratar está na assinatura, então quem revisa lê o tipo e sabe o que pode dar errado, e um caso esquecido é um erro de compilação.

## Pontos-chave

* A complexidade acidental é a parte que as pessoas acrescentam; ela é uma escolha, e KISS (a forma mais simples que faz o trabalho), YAGNI (nada construído para uma necessidade presumida) e DRY (um lugar para cada conhecimento) são três maneiras de recusá-la.
* Uma abstração é escrita na segunda ocorrência concreta, e a entrega diz qual foi a primeira; em um processo, um passo só entra quando nomeia o erro concreto que teria pegado.
* Uma regra de negócio é uma função pura: dados entrando, um `Result` saindo, sem I/O e sem relógio; buscar e salvar pertencem ao orquestrador em volta dela.
* Uma falha é uma exceção (de fora, capturada na fronteira e devolvida nas palavras do próprio domínio), uma recusa (uma regra dizendo não, devolvida como valor) ou um erro (um bug, nunca capturado); um throw não conduz fluxo.
* O valor de um `Result` é a checagem exaustiva: um `Record`, `match` ou `switch` que esquece um caso não compila.

[^brooks-silver-bullet]: Frederick P. Brooks Jr., "No Silver Bullet: Essence and Accidents of Software Engineering", IEEE Computer 20(4), 1987.
[^beck-xp]: Kent Beck, "Extreme Programming Explained: Embrace Change", Addison-Wesley, 1999.
[^fowler-yagni]: Martin Fowler, "Yagni", martinfowler.com, 2015-05-26, acesso em 2026-09-30. <https://martinfowler.com/bliki/Yagni.html>
[^pragmatic-programmer]: Andrew Hunt e David Thomas, "The Pragmatic Programmer", Addison-Wesley, 1999; edição de 20 anos, 2019.
[^metz-wrong-abstraction]: Sandi Metz, "The Wrong Abstraction", 2016-01-20, acesso em 2026-09-30. <https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction>
[^go-errors]: Rob Pike, "Errors are values", The Go Blog, 2015. <https://go.dev/blog/errors-are-values>
[^dart-core]: Dart, "Exception class" e "Error class", referência da API `dart:core`, acesso em 2026-09-29. <https://api.dart.dev/stable/dart-core/Exception-class.html> e <https://api.dart.dev/stable/dart-core/Error-class.html>
[^toub-net9]: Stephen Toub, "Performance Improvements in .NET 9", .NET Blog, 2024-09-12, seção "VM", benchmark `ExceptionThrowCatch`, acesso em 2026-09-30. <https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-9/>
[^anti-corruption-layer]: Microsoft, "Anti-Corruption Layer pattern", Azure Architecture Center, acesso em 2026-09-30. <https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer>
