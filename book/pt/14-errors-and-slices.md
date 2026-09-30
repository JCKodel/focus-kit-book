# Exceções como valores e fatias verticais

Depois deste capítulo você consegue organizar o código por funcionalidade, em fatias verticais, e devolver toda exceção como um valor.
Você sabe distinguir uma exceção de uma recusa e de um erro em qualquer linguagem, dizer por que um throw nunca deve conduzir o fluxo do programa e manter as exceções de uma biblioteca fora do seu domínio.
Você também sabe que os dois princípios funcionam sem as quatro peças do capítulo 15.

## Dois princípios que se sustentam sozinhos

Fatias verticais e exceções como valores não precisam de nenhuma das quatro peças, a tela, o orquestrador, o caso de uso e o repositório.
Qualquer estrutura que a sua stack favoreça consegue pôr cada funcionalidade em uma pasta e devolver exceções como valores: essa é a segunda resposta do kit para a arquitetura, entre [as duas escolhas](06-the-documents.md#as-duas-escolhas) do capítulo 6, e o capítulo 15 acrescenta as peças.
A clínica adotou o FOCUS inteiro no capítulo 7, então o código dela mostra os dois princípios.
Todo excerto abaixo vem do projeto guiado na tag do capítulo [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone), a tag anotada que marca o código que o capítulo 12 deixou, e é citado como rodou.

## Fatias verticais

Uma fatia vertical é uma pasta que guarda tudo o que uma funcionalidade precisa: as telas, as chamadas ao servidor, as rotas, as regras, o SQL e os testes.[^vertical-slice]
Não há pasta por tecnologia ou camada, nem `controllers/`, nem `models/`.
Uma subfuncionalidade é uma subpasta, como `authentication/change-password/`; a clínica ainda não tem nenhuma.

Esta é a saída de `git ls-tree -r --name-only book-v1/closing-a-milestone src/features/appointments`, a [fatia dos agendamentos](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone/src/features/appointments), 22 arquivos:

```text
src/features/appointments/BookingView.e2e.ts
src/features/appointments/BookingView.tsx
src/features/appointments/CancelView.e2e.ts
src/features/appointments/CancelView.tsx
src/features/appointments/RememberedView.tsx
src/features/appointments/api.ts
src/features/appointments/clinicTime.test.ts
src/features/appointments/clinicTime.ts
src/features/appointments/e2e.server.ts
src/features/appointments/remembered.test.ts
src/features/appointments/remembered.ts
src/features/appointments/repository.server.test.ts
src/features/appointments/repository.server.ts
src/features/appointments/route.server.test.ts
src/features/appointments/route.server.ts
src/features/appointments/rules.test.ts
src/features/appointments/rules.ts
src/features/appointments/strings.ts
src/features/appointments/styles.ts
src/features/appointments/useBooking.ts
src/features/appointments/useCancel.ts
src/features/appointments/useRemembered.ts
```

Os três arquivos `View.tsx` são as telas: agendar, cancelar com um código, e os agendamentos que o celular lembra.
Os três hooks `use*.ts` guardam o estado que cada tela mostra, e `strings.ts` e `styles.ts` guardam as palavras e a aparência dela.
`api.ts` é o lado do cliente de cada chamada ao servidor; `route.server.ts` é o lado do servidor, as rotas HTTP.
`rules.ts` guarda as regras (os horários livres, um agendamento, o prazo de cancelamento), `repository.server.ts` guarda o SQL, `clinicTime.ts` lê datas no fuso horário da clínica, e `remembered.ts` guarda no celular uma cópia de cada agendamento.
Um nome terminado em `.server.ts` roda só no servidor, e o código do cliente nunca importa um deles.
Os arquivos `.test.ts` são testes unitários, os `.e2e.ts` conduzem as telas em um navegador, e `e2e.server.ts` guarda os passos que eles compartilham.

Uma funcionalidade é uma coisa que o app guarda, nomeada por um termo do docs/03 do projeto (o agendamento, o profissional, os horários semanais), e a fatia dela guarda toda ação sobre ela.
Agendar e cancelar agem os dois sobre o agendamento, então compartilham as regras dele (`rules.ts`), o SQL dele (`repository.server.ts`), as rotas dele (`route.server.ts`), as chamadas dele (`api.ts`) e a lista que o celular lembra (`remembered.ts`): são uma fatia só.
Os horários semanais e os profissionais são outras coisas que a clínica guarda, cada uma com a sua tabela e a sua tela, então cada uma tem uma fatia própria, `weeklyHours` e `professionals`.
Uma mudança no agendamento mexe nesta pasta, e remover o agendamento remove esta pasta.
A fatia também delimita o que um agente lê em uma entrega sobre agendamento, assunto do capítulo 16.

A [fatia de health](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone/src/features/health), a verificação do servidor do primeiro marco, tem 6 arquivos:

```text
src/features/health/HealthView.e2e.ts
src/features/health/HealthView.tsx
src/features/health/api.ts
src/features/health/route.server.ts
src/features/health/strings.ts
src/features/health/useHealth.ts
```

Ela não tem `rules.ts`, porque não tem regra, nem `repository.server.ts`, porque não guarda nada: um arquivo aparece em uma fatia quando se paga.

Aquilo de que o código trata decide onde fica o código que duas funcionalidades usam.
O código sobre uma coisa que o app guarda fica na fatia dela, e outra fatia importa dali o que precisa, seja uma função de repositório, um tipo, uma chamada do cliente ou uma tela; duas fatias podem importar uma da outra.
`findClinic` e `findActiveProfessionals` são importadas cada uma por `appointments/route.server.ts` e por `weeklyHours/route.server.ts`, um segundo uso, e ficam em `clinic/` e `professionals/`, porque cada uma lê a coisa que a sua fatia guarda.
O que duas funcionalidades compartilham e não pertence a nenhuma coisa que o app guarda sai das fatias para `src/lib/`: a forma de um valor (`email.ts`, `id.ts`, `name.ts`) ou encanamento (`request.ts`, `result.ts`).
`email.ts`, `id.ts`, `name.ts` e `request.ts` dizem cada um, em um comentário, onde estão o primeiro e o segundo uso, como "First use: health/api.ts (`skeleton`); second use: clinic/api.ts." em `request.ts`; `result.ts` é usado por toda funcionalidade.
É a regra da segunda ocorrência do [capítulo 13](13-the-governor.md#a-mesma-pergunta-no-codigo), aplicada a pastas: o código que não pertence a nenhuma coisa vai para `lib/` no segundo uso, e não antes.

## Exceção, recusa, erro

Um erro é um bug: um código errado, corrigido quando é achado e nunca tratado.
Uma exceção é uma falha de fora do programa, como uma conexão perdida ou um disco cheio: nenhum código está errado, e ela é tratada onde acontece.
O nome da classe não distingue os dois: as falhas nativas do JavaScript são todas um `Error`, e as do .NET são todas uma `Exception`, então quem decide é a causa, nunca o nome.
Em quarenta anos programando, vi uma linguagem tornar a diferença visível: o Dart, cujo `dart:core` tem uma classe `Exception`, feita para ser capturada, e uma classe `Error`, para uma falha do programa que o programador deveria ter evitado.[^dart-core]

Eric Lippert separa todo valor lançado em quatro tipos, cujos nomes ficam em inglês aqui:[^lippert-vexing]

* "Fatal" (fatal): "*não é culpa sua, você não consegue evitá-las e não consegue limpar a bagunça delas de forma sensata*", como a memória acabar; ninguém captura uma.
* "Boneheaded" (estúpida): "*culpa sua mesmo, você poderia tê-las evitado, então são bugs no seu código*"; o erro deste livro.
* "Vexing" (irritante): "*o resultado de decisões de design infelizes*", uma falha que uma API lança onde poderia ter devolvido um valor, como o `Int32.Parse` do .NET recebendo um texto que o usuário digitou; uma exceção que o design da API cria, transformada em valor na hora ou evitada com a forma `Try` da API, `Int32.TryParse`.[^dotnet-exceptions]
* "Exogenous" (exógena): "*o resultado de realidades externas bagunçadas invadindo a lógica bonita e precisa do seu programa*", como um arquivo que sumiu; a exceção deste livro.

Ao lado do erro e da exceção, este livro acrescenta um terceiro tipo: a recusa, a resposta de uma regra quando ela diz não, como um número de telefone com poucos dígitos.
Nenhum I/O falhou, e nenhum código está errado; a regra fez o trabalho dela.

Então uma falha é uma de três:

* **Exceção:** uma falha esperada de fora do programa (o banco de dados, a rede, o armazenamento do celular), capturada na fronteira com o mundo de fora (o I/O, e a leitura do que ele traz) e devolvida como valor.
* **Recusa:** uma regra dizendo não, verificada no código ou por uma restrição do banco de dados, como um índice único, e devolvida como valor; mesmo quando é o banco que responde, nada falhou.
* **Erro:** um bug, lançado e nunca capturado, então chega à sua tela enquanto você desenvolve e ao seu analytics quando o app roda.

A área chama o princípio de "erros como valores", a partir do Go[^go-errors] e do Rust,[^rust-result] e o capítulo 6 disse por que este livro diz exceção.[^book-adr-0016]
O kit e a clínica ainda usam a palavra da área, `error`, no campo do `Result` e nos documentos, para o que este livro chama de exceção ou recusa.
O próprio docs/03 da clínica já chama cada resultado das suas regras de recusa, como `SlotTaken`, "a recusa quando um agendamento pede um horário que não está livre".

## Por que não lançar

Uma exceção lançada para conduzir o fluxo do programa, em vez de devolvida, custa quatro coisas:

1. Um `throw` é uma saída que o ponto da chamada não mostra. Joel Spolsky escreveu em 2003 que as exceções "*são invisíveis no código-fonte*" e "*criam pontos de saída demais para uma função*".[^spolsky-exceptions]
2. A assinatura não diz o que pode falhar, então o compilador não consegue verificar que todo caso foi tratado. Um `Result` diz isso no seu tipo, e o `Record` sobre `BookingRefusal` da próxima seção não compila quando uma recusa fica sem status.
3. Um throw custa mais que um return. No benchmark `ExceptionThrowCatch` de Stephen Toub, publicado em 2024-09-12, 1.000 throws, cada um capturado através de 10 frames assíncronos, levaram 123,03 ms no .NET 8 e 54,68 ms no .NET 9.[^toub-net9] O guia de ASP.NET Core da Microsoft tira a regra: "*lançar e capturar exceções é lento em comparação com outros padrões de fluxo de código. Por isso, exceções não devem ser usadas para controlar o fluxo normal do programa.*"[^aspnet-best-practices] As Framework Design Guidelines dizem assim: "*NÃO use exceções para o fluxo normal de controle, se possível.*"[^fdg-exception-throwing]
4. Um catch largo o bastante para conduzir o fluxo também captura bugs, como mostra o `query` da próxima seção: um `TypeError` dentro dele vira `DatabaseFailed`.

## Exceções como valores na clínica

Um `Result` guarda o valor ou o que o impediu.
Este é o [`src/lib/result.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/lib/result.ts), inteiro:

```ts
export type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

export function ok<T>(value: T): { ok: true; value: T } {
	return { ok: true, value };
}

export function err<E>(error: E): { ok: false; error: E } {
	return { ok: false, error };
}
```

Quem chama lê `ok` antes de chegar a `value` ou `error`, e o TypeScript estreita o tipo nessa verificação.

Um repositório, o código que busca e salva, roda todo comando SQL dentro de `query`, de [`src/server/database.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/server/database.server.ts):

```ts
export type DatabaseFailed = { code: "DatabaseFailed"; message: string };

// Where a repository's SQLite exception becomes a Result. First use: the
// clinic repository; second use: the session queries.
export function query<T>(run: () => T): Result<T, DatabaseFailed> {
	try {
		return ok(run());
	} catch (error) {
		const message = error instanceof Error ? error.message : String(error);
		return err({ code: "DatabaseFailed", message });
	}
}
```

Este é o único `try`/`catch` dentro do qual o SQL de um repositório roda, e ele transforma a exceção do banco em um valor.

`query` captura todo valor lançado, não só os do banco, então um bug dentro de `run`, como um `TypeError` ou um comando malformado, também vira `DatabaseFailed`.
Uma captura mais estreita não separaria os dois: o SQLite informa um comando malformado com o mesmo código de uma tabela ausente ou de um arquivo travado, `ERR_SQLITE_ERROR`.[^node-sqlite-error]
A definição de erro diz o que o código busca; uma captura no I/O é onde um bug pode ser capturado por acidente.
As rotas respondem `DatabaseFailed` só com o código e não registram nada, então um bug capturado ali não chega nem à sua tela nem ao seu analytics.

Uma exceção também pode virar uma recusa.
Em [`src/features/appointments/repository.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/repository.server.ts), a inserção de um agendamento pode falhar de dois jeitos:

```ts
export type InsertError = { code: "SlotTaken" } | DatabaseFailed;
```

```ts
// The index appointment_booked_slot is the last guard against a double
// booking (docs/02): its failure is SlotTaken. Any other, a repeated booking
// code included, is DatabaseFailed.
export function insertAppointment(
	db: DatabaseSync,
	appointment: NewAppointment,
): Result<void, InsertError> {
	const inserted = query(() => {
		db.prepare(
			"INSERT INTO appointment (professional_id, starts_at, client_name, client_phone, booking_code) VALUES (?, ?, ?, ?, ?)",
		).run(
			appointment.professionalId,
			appointment.startsAt,
			appointment.clientName,
			appointment.clientPhone,
			appointment.bookingCode,
		);
	});
	if (
		!inserted.ok &&
		inserted.error.message.includes(
			"UNIQUE constraint failed: appointment.professional_id, appointment.starts_at",
		)
	) {
		return err({ code: "SlotTaken" });
	}
	return inserted;
}
```

Quando dois clientes agendam o mesmo horário ao mesmo tempo, o índice único recusa a segunda inserção, e o repositório devolve isso como a recusa `SlotTaken`; qualquer outra falha continua a exceção `DatabaseFailed`.
É a mesma regra verificada duas vezes: o caso de uso `book` recusa antes um horário que não está livre, como mostra o [capítulo 15](15-four-pieces.md#um-evento-um-novo-estado), e o índice é a última barreira quando dois clientes agendam ao mesmo tempo.

Uma recusa de uma regra não envolve I/O nenhum.
Esta é `checkClientPhone`, de [`src/features/appointments/rules.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/rules.ts):

```ts
const phoneCharacters = /^[\d +\-.()]*$/;

// The digits to store: only digits, spaces, +, -, . and brackets typed, and
// 6 to 15 digits.
export function checkClientPhone(
	raw: string,
): Result<string, "InvalidPhoneNumber"> {
	if (!phoneCharacters.test(raw)) return err("InvalidPhoneNumber");
	const digits = raw.replace(/\D/g, "");
	if (digits.length < 6 || digits.length > 15) {
		return err("InvalidPhoneNumber");
	}
	return ok(digits);
}
```

É uma função pura, texto entra e um valor sai, então ela não tem nada a capturar.
A clínica chama uma função assim de caso de uso, uma peça que o capítulo 15 ensina.

Todo caso precisa ser tratado, e o compilador consegue conferir isso.
Este é `refusalStatus`, de [`src/features/appointments/route.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/route.server.ts), o status HTTP de cada recusa de um agendamento:

```ts
// The three time refusals share 409: the client shows them alike.
const refusalStatus: Record<BookingRefusal, 400 | 409> = {
	InvalidClientName: 400,
	InvalidPhoneNumber: 400,
	OutsideBookingWindow: 409,
	OutsideWorkingHours: 409,
	SlotTaken: 409,
};
```

Um `Record` sobre `BookingRefusal` tem de nomear todo membro desse tipo, então uma recusa acrescentada às regras sem um status não compila.

A clínica captura só onde o I/O acontece: `openDatabase` e `query` em `database.server.ts` (`transaction` roda dentro de `query`), o executor de migrations em `migrate.server.ts`, `request` em `src/lib/request.ts` para a rede no cliente, e `remembered.ts` para o armazenamento do celular.
Cada rota que lê o corpo de uma requisição também captura, já que o corpo chega pela rede: um corpo que não pode ser lido vira na hora a resposta `BadRequest`.

O app em si nunca lança.
Dois helpers que só os testes rodam lançam: `box` em `e2e.server.ts`, quando um elemento não está na tela, e `memoryDatabase`, em [`src/server/testDatabase.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/server/testDatabase.server.ts):

```ts
// For Vitest: an in-memory SQLite with the real migrations applied.
export function memoryDatabase(): DatabaseSync {
	const db = new DatabaseSync(":memory:");
	const folder = fileURLToPath(new URL("./migrations/", import.meta.url));
	const migrated = migrate(db, folder);
	if (!migrated.ok) {
		throw new Error(
			`Migration ${migrated.error.file}: ${migrated.error.message}`,
		);
	}
	return db;
}
```

Uma migration que falha em um teste é um bug, um erro, então é lançada e o teste para ali.

## A fronteira

Uma exceção pertence ao domínio que a lança.
Pense em um login pela Apple: quando o SDK da Apple falha, ele lança a exceção da própria Apple, e o código que chama o SDK a captura e devolve um valor do seu app, digamos `AuthFailure`.
Nada depois desse código sabe que a Apple existe, então uma segunda forma de login, ou uma versão nova do SDK da Apple, muda só esse código.
O domain-driven design chama esse tradutor de camada anticorrupção, cujo "*propósito central ... é proteger o modelo de domínio*";[^anti-corruption-layer] o padrão traduz modelos e chamadas, e este livro dá um passo a mais: traduz as exceções também.

A clínica faz isso com o SQLite, em `book-v1/closing-a-milestone`.
`git grep node:sqlite -- src` acha `DatabaseSync` importado como valor, fora dos arquivos de teste, só em `database.server.ts`, onde `query` transforma a falha do SQLite em `DatabaseFailed`, e em `testDatabase.server.ts`, o banco em memória dos testes.
Todo outro arquivo que o nomeia, os repositórios e as rotas entre eles, importa só o tipo dele, para receber e repassar o banco aberto; nenhuma regra, hook, tela ou `api.ts` o importa.
`git grep "UNIQUE constraint"` acha o texto da falha de `UNIQUE` do SQLite em um arquivo só, `appointments/repository.server.ts`, onde ele vira `SlotTaken`.

Então toda exceção fora do I/O é um bug? Quase:

* Uma exceção "vexing" da leitura de um texto vem de um texto que o I/O trouxe, então fica na mesma fronteira: uma rota transforma um corpo de requisição que não pode ser lido na resposta `BadRequest` na hora.
* Uma "fatal", como a memória acabar, não é tratada por ninguém.
* O fluxo de controle do próprio framework é lançado de propósito e deve passar intocado. O `redirect` do Next.js "*lança um erro, então deve ser chamado **fora** do bloco `try` quando se usa `try/catch`*",[^nextjs-redirect] e um `try`/`catch` em volta do `notFound` "*o suprime, e a tela de não encontrado não aparece*".[^nextjs-not-found] O .NET cancela uma chamada assíncrona lançando `OperationCanceledException`, para que "*a pilha de chamadas*" seja "*desfeita assim que um pedido de cancelamento é observado*";[^dotnet-exceptions] ela pertence ao código que pediu o cancelamento, nunca a um catch no banco.

Então a regra é: capture na fronteira com o mundo de fora, e deixe todo o resto passar.

## Uma falha, do começo ao fim

O docs/01 da clínica, na seção "How errors travel", dá o caminho que uma falha percorre.
`SlotTaken`, quando o índice recusa um agendamento, segue esse caminho em cinco passos, sem nenhum `throw` no meio:

1. `insertAppointment` em `repository.server.ts` devolve `SlotTaken`.
2. A rota de agendamento em `route.server.ts` responde 409 com o corpo `{ "error": { "code": "SlotTaken" } }`.
3. `postAppointment` em `api.ts` nomeia 409 como `SlotTaken`, e `request` em `src/lib/request.ts` o devolve como essa recusa.
4. `useBooking.ts`, o hook, recarrega os horários livres e publica um estado cuja mensagem é `SlotTaken`.
5. `BookingView.tsx` mostra a mensagem que `strings.ts` dá a esse código: "This time is no longer free. Pick another." ("Este horário não está mais livre. Escolha outro.").

`strings.ts` liga cada falha de agendamento a uma mensagem com um `Record`, como a rota faz com os status, então um código sem mensagem também não compila.

## Pontos-chave

* Uma funcionalidade é uma coisa que o app guarda, com toda ação sobre ela, e a fatia vertical dela é uma pasta, sem pasta por camada; uma mudança na funcionalidade mexe nessa pasta, e remover a funcionalidade remove essa pasta.
* Um arquivo entra em uma fatia quando se paga; o código sobre uma coisa que o app guarda fica na fatia dela, que as outras fatias importam, e o código que não pertence a nenhuma coisa entra em `lib/` no segundo uso.
* Um erro é um bug, corrigido e nunca capturado; uma exceção é uma falha de fora do programa, capturada na fronteira e devolvida como valor; uma recusa é uma regra dizendo não, no código ou numa restrição do banco; o nome da classe não distingue nenhum deles.
* Um throw é uma saída que quem chama não vê e o compilador não verifica, então nunca conduz o fluxo.
* A exceção de uma biblioteca pertence à biblioteca: o código na fronteira a transforma no valor do domínio, e o resto do app não lança nada.
* Um `Result` tratado com um `Record` sobre os seus casos não compila quando um caso é esquecido.

## Exercícios

Estes exercícios usam a clínica, por conversa com o agente, nunca à mão.

### Exercício 14.1

Peça ao agente que liste todo `try`, `catch` e `throw` da sua clínica fora dos testes, e que diga, para cada um, que I/O ele protege e que valor ele devolve.
Peça também que nomeie todo tipo de exceção de uma biblioteca que chega a um código fora do lugar que faz o I/O dessa biblioteca.
Qualquer um que não proteja I/O é candidato para a sua fila, não uma correção agora.

### Exercício 14.2

Peça ao agente que siga `CancellationTooLate` da regra até a tela, nomeando cada arquivo.
Depois diga quais arquivos teriam de mudar se a regra o lançasse.

### Exercício 14.3

O marco 2 traz `absences`.
Pergunte ao agente onde os arquivos dela ficariam, em uma pasta própria ou em uma subpasta de `weeklyHours`, e que arquivos existentes ela tocaria.
Decida, e diga por quê; nada é construído.

[^vertical-slice]: Jimmy Bogard, "Vertical Slice Architecture", 2018. <https://www.jimmybogard.com/vertical-slice-architecture/>
[^dart-core]: Dart, "Exception class" e "Error class", referência da API de `dart:core`, acesso em 2026-09-29: uma `Exception` "*foi feita para ser capturada*"; um `Error` é "*uma falha do programa que o programador deveria ter evitado*". <https://api.dart.dev/stable/dart-core/Exception-class.html> e <https://api.dart.dev/stable/dart-core/Error-class.html>
[^go-errors]: Rob Pike, "Errors are values", The Go Blog, 2015. <https://go.dev/blog/errors-are-values>
[^rust-result]: The Rust Programming Language, "Recoverable Errors with Result", capítulo 9.2, acesso em 2026-09-29. <https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html>
[^book-adr-0016]: J.C. Ködel, "One Page at a Time", o ADR-0016 deste livro, `docs/adr/ADR-0016-the-books-definition-of-focus.md`, de 2026-09-28, na pasta de ADRs em `main`. <https://github.com/JCKodel/focus-kit-book/tree/main/docs/adr>
[^node-sqlite-error]: Node.js, "Errors", referência da API, `ERR_SQLITE_ERROR`, acesso em 2026-09-30: "*um erro foi retornado pelo SQLite*". <https://nodejs.org/api/errors.html#err_sqlite_error>
[^lippert-vexing]: Eric Lippert, "Vexing exceptions", Fabulous Adventures in Coding, 2008-09-10, acesso em 2026-09-30. <https://ericlippert.com/2008/09/10/vexing-exceptions/>
[^dotnet-exceptions]: Microsoft Learn, "Best practices for exceptions", .NET, acesso em 2026-09-30, seções "Call `Try*` methods to avoid exceptions" e "Catch cancellation and asynchronous exceptions": "*essas exceções permitem que a execução seja interrompida de forma eficiente e que a pilha de chamadas seja desfeita assim que um pedido de cancelamento é observado*". <https://learn.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions>
[^spolsky-exceptions]: Joel Spolsky, "Exceptions", Joel on Software, 2003-10-13, acesso em 2026-09-30. <https://www.joelonsoftware.com/2003/10/13/13/>
[^toub-net9]: Stephen Toub, "Performance Improvements in .NET 9", .NET Blog, 2024-09-12, seção "VM", benchmark `ExceptionThrowCatch`, acesso em 2026-09-30. <https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-9/>
[^aspnet-best-practices]: Microsoft Learn, "ASP.NET Core Best Practices", seção "Minimize exceptions", acesso em 2026-09-30. <https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices>
[^fdg-exception-throwing]: Krzysztof Cwalina e Brad Abrams, "Exception Throwing", Framework Design Guidelines, 2ª edição, 2008, no Microsoft Learn, acesso em 2026-09-30. <https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/exception-throwing>
[^anti-corruption-layer]: Microsoft, "Anti-Corruption Layer pattern", Azure Architecture Center, acesso em 2026-09-30: "*o propósito central de uma camada anticorrupção é proteger o modelo de domínio, não prescrever nenhuma escolha de produto específica*". <https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer>
[^nextjs-redirect]: Next.js, "redirect", referência da API, 16.3.7, acesso em 2026-09-30. <https://nextjs.org/docs/app/api-reference/functions/redirect>
[^nextjs-not-found]: Next.js, "notFound", referência da API, 16.3.7, acesso em 2026-09-30: "*um `try/catch` em volta da chamada o suprime, e a tela de não encontrado não aparece*". <https://nextjs.org/docs/app/api-reference/functions/not-found>
