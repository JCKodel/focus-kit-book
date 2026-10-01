# Regras como funções puras, exceções como valores

Depois deste capítulo você consegue escrever uma regra de negócio como uma função pura que devolve um Result (resultado), distinguir uma exceção de uma recusa e de um erro em qualquer linguagem, e dizer por que um throw nunca deve conduzir o fluxo do programa.
Você também consegue manter as exceções de uma biblioteca fora do seu domínio, de modo que uma biblioteca nova mude um arquivo.

## O problema

Uma regra que mora dentro de uma tela, de um controller ou de uma chamada ao banco de dados não pode ser testada sem essa tela, esse controller ou esse banco.
Uma falha lançada sai da função por uma porta que quem chama não vê, e o compilador não consegue dizer a quem chama quais portas existem.
Os dois hábitos produzem um programa que funciona no caminho feliz e surpreende todo mundo fora dele, e um agente que lê esse código não tem como saber quais falhas eram intencionais.

## Uma função pura

Uma função é pura quando a mesma entrada sempre dá a mesma saída e nada mais acontece: nenhuma leitura de banco de dados, nenhuma escrita em arquivo, nenhum relógio, nenhuma rede.
O teste dela é dado entrando, valor saindo, e não precisa de preparação.
Uma função impura precisa que o mundo seja arrumado antes de rodar, e todo teste paga por essa arrumação.

Uma biblioteca de empréstimos guarda livros e membros.
A regra "um membro com um livro atrasado não pode pegar outro" é uma função pura:

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

A Clean Architecture, como costuma ser praticada, faz isso de outro jeito: o caso de uso, o nome que ela dá à função que guarda uma regra de negócio, recebe os seus repositórios como dependências injetadas, e, como eles fazem I/O, ele vira assíncrono.
O teste dele passa a precisar de um mock ou de um fake para cada repositório, roda mais devagar, e pode passar enquanto o repositório real se comporta de um jeito que o fake nunca implementou.
Este livro mantém a regra pura e síncrona: `podePegarEmprestado` recebe um membro, e não um jeito de buscá-lo.
Buscar e salvar pertencem a um orquestrador, a função que pede os dados aos repositórios, os entrega à regra e salva o que a regra devolve (capítulo 7).
O teste da regra é uma chamada com dados, escrita em um minuto e executada em um milissegundo, sem dependência para arrumar e sem nada nele que possa discordar do banco de dados.

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

Go devolve erros como valores comuns, "*erros são valores*", e os trata com código comum;[^go-errors] Rust põe a falha recuperável no tipo de retorno, `Result<T, E>`;[^rust-result] Scott Wlaschin desenhou a mesma ideia como dois trilhos, sucesso e falha, por onde passa cada passo de um pipeline.[^wlaschin-rop]
A área chama o princípio de "errors as values", erros como valores.
Este livro diz "exceções como valores", e a próxima seção diz por quê.

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

Eric Lippert separou todo valor lançado em quatro tipos em 2008: "fatal", que ninguém consegue tratar; "boneheaded", "*culpa sua mesmo*", o erro deste livro; "vexing", lançado por uma API que poderia ter devolvido um valor, como interpretar um texto que um usuário digitou; e "exogenous", "*realidades externas bagunçadas*", a exceção deste livro.[^lippert-vexing]
A recusa é o tipo que falta nessa lista, porque uma recusa nunca é lançada: é o que uma regra devolve.

Por isso este livro não diz "erros como valores".
Um erro é um bug, e um bug nunca é um valor: é uma correção.
O que viaja em um `Result` é uma exceção ou uma recusa.

## Por que não lançar

Um throw usado para conduzir o fluxo, no lugar de um return, custa quatro coisas.

1. **Uma saída que o ponto de chamada não mostra.**
   Joel Spolsky escreveu em 2003 que as exceções "*são invisíveis no código-fonte*" e "*criam pontos de saída possíveis demais para uma função*".[^spolsky-exceptions]
2. **Uma assinatura que mente.**
   `function emprestar(...): Emprestimo` não diz nada sobre as três maneiras de falhar, então o compilador não consegue verificar que todo caso é tratado.
   `Result<Emprestimo, RecusaDeEmprestimo>` diz isso no tipo, e um `switch` sobre a recusa que esquece um caso não compila.
3. **Tempo.**
   No benchmark de Stephen Toub, 1.000 throws, cada um capturado através de dez frames assíncronos, levaram 123,03 ms no .NET 8 e 54,68 ms no .NET 9.[^toub-net9]
   A orientação da Microsoft para o ASP.NET Core traça a regra: "*Lançar e capturar exceções é lento em relação a outros padrões de fluxo de código. Por isso, exceções não devem ser usadas para controlar o fluxo normal do programa.*"[^aspnet-best-practices]
   As Framework Design Guidelines dizem "*NÃO use exceções para o fluxo normal de controle, se possível.*"[^fdg-exception-throwing]
4. **Um catch que esconde bugs.**
   Um catch largo o bastante para conduzir o fluxo também captura os bugs que acontecem dentro dele, e eles somem em uma mensagem que ninguém lê.

Uma função devolve um valor, e a sua assinatura diz qual.
Um throw quebra esse contrato: a função "devolve" algo que a assinatura nunca mencionou, por um caminho que quem chama não escreveu e não vê no ponto de chamada.
A maior parte do que um programa trata é uma regra dizendo não, então um programa que lança para recusas tem uma dessas saídas escondidas em cada regra, e quem chama precisa saber de cor quais são.

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
Duas coisas trazem o bug de volta a você: um teste que roda toda chamada ao banco de dados contra um banco de dados real, em memória, e confere o valor que recebe (capítulo 8), e uma linha de log que imprime a `mensagem` antes de o programa responder.

Dois tipos de throw passam pela fronteira intocados.
Um fatal, como acabar a memória, não é tratado por ninguém.
O fluxo de controle próprio de um framework, lançado de propósito, não deve ser capturado por você: o `redirect` do Next.js "*lança um erro, então deve ser chamado **fora** do bloco `try`*",[^nextjs-redirect] e o .NET desfaz uma chamada cancelada lançando, de modo que a pilha de chamadas é "*desfeita assim que um pedido de cancelamento é observado*".[^dotnet-exceptions]
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

## A regra nasce com o teste

O desenvolvimento guiado por testes de Kent Beck escreve o teste antes do código, em um ciclo de três passos: vermelho, o teste falha porque o código ainda não existe; verde, o menor código que o faz passar; depois a limpeza, com o teste ainda verde.[^beck-tdd]
Uma regra pura é o lugar mais fácil de fazer isso, porque o teste é uma chamada com dados.
No Vitest, o executor de testes que o capítulo 8 usa, o teste de `podePegarEmprestado` é:

```ts
it("recusa um membro com um livro atrasado", () => {
	expect(podePegarEmprestado({ id: "m1", emAtraso: 1 })).toEqual({ ok: false, error: "TemLivrosEmAtraso" });
});
```

Rode-o antes de `podePegarEmprestado` existir e ele está vermelho; escreva a função e ele está verde.
Para um agente, é isso que "pronto" quer dizer sempre que pode ser dito em código.
A página de uma entrega lista os seus comportamentos (capítulo 14), cada um vira um teste vermelho, e a entrega está pronta quando todos eles estão verdes e nada que estava verde ficou vermelho.
"Pronto" deixa de ser a opinião do agente e passa a ser a saída do executor de testes, e o [capítulo 8](08-testing-each-piece.md) dá a cada uma das quatro peças o seu teste.

## O que o time ganha

Toda regra é uma função que um teste chama com dados, então uma regra tem um teste antes de ter uma tela, e um agente a quem se pede para mudar uma regra a encontra em um lugar só, com os casos dela nomeados no tipo.
Toda falha que quem chama precisa tratar está na assinatura, então quem revisa lê o tipo e sabe o que pode dar errado, e o compilador recusa um caso esquecido.
E o custo medido de conduzir o fluxo por throw, o dobro do tempo no .NET 9 e mais de quatro vezes no .NET 8 comparado a um return,[^toub-net9] fica fora do caminho crítico.

## Pontos-chave

* Uma função pura recebe dados e devolve um valor, sem I/O e sem relógio; uma regra de negócio escrita assim é testada só com dados, e buscar e salvar pertencem ao orquestrador em volta dela.
* Uma falha é uma exceção (de fora, capturada na fronteira e devolvida como valor nas palavras do próprio domínio), uma recusa (uma regra dizendo não, devolvida como valor) ou um erro (um bug, nunca capturado); o nome da classe não distingue nenhuma delas.
* Um throw não conduz fluxo: uma função devolve um valor, e um throw é uma saída que a assinatura não mostra, um custo medido e um esconderijo para bugs.
* O único `try`/`catch` mora onde o programa toca o mundo de fora, e ele traduz a exceção da biblioteca no valor do programa; uma biblioteca nova muda só esse arquivo.
* O valor de um `Result` é a checagem exaustiva: um `Record`, `match` ou `switch` que esquece um caso não compila; escreva o teste vermelho antes da regra, e "pronto" é o teste verde.

[^go-errors]: Rob Pike, "Errors are values", The Go Blog, 2015. <https://go.dev/blog/errors-are-values>
[^rust-result]: The Rust Programming Language, "Recoverable Errors with Result", capítulo 9.2, acesso em 2026-09-29. <https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html>
[^wlaschin-rop]: Scott Wlaschin, "Railway Oriented Programming", F# for Fun and Profit, 2014, acesso em 2026-09-30. <https://fsharpforfunandprofit.com/rop/>
[^dart-core]: Dart, "Exception class" e "Error class", referência da API `dart:core`, acesso em 2026-09-29. <https://api.dart.dev/stable/dart-core/Exception-class.html> e <https://api.dart.dev/stable/dart-core/Error-class.html>
[^lippert-vexing]: Eric Lippert, "Vexing exceptions", Fabulous Adventures in Coding, 2008-09-10, acesso em 2026-09-30. <https://ericlippert.com/2008/09/10/vexing-exceptions/>
[^spolsky-exceptions]: Joel Spolsky, "Exceptions", Joel on Software, 2003-10-13, acesso em 2026-09-30. <https://www.joelonsoftware.com/2003/10/13/13/>
[^toub-net9]: Stephen Toub, "Performance Improvements in .NET 9", .NET Blog, 2024-09-12, seção "VM", benchmark `ExceptionThrowCatch`, acesso em 2026-09-30. <https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-9/>
[^aspnet-best-practices]: Microsoft Learn, "ASP.NET Core Best Practices", seção "Minimize exceptions", acesso em 2026-09-30. <https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices>
[^fdg-exception-throwing]: Krzysztof Cwalina e Brad Abrams, "Exception Throwing", Framework Design Guidelines, 2ª edição, 2008, no Microsoft Learn, acesso em 2026-09-30. <https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/exception-throwing>
[^anti-corruption-layer]: Microsoft, "Anti-Corruption Layer pattern", Azure Architecture Center, acesso em 2026-09-30. <https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer>
[^nextjs-redirect]: Next.js, "redirect", referência da API, acesso em 2026-09-30. <https://nextjs.org/docs/app/api-reference/functions/redirect>
[^dotnet-exceptions]: Microsoft Learn, "Best practices for exceptions", .NET, seção "Catch cancellation and asynchronous exceptions", acesso em 2026-09-30. <https://learn.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions>
[^beck-tdd]: Kent Beck, "Test-Driven Development: By Example", Addison-Wesley, 2002.
