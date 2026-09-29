# Exceções como valores e fatias verticais

Depois deste capítulo você consegue organizar o código por funcionalidade, em fatias verticais, e devolver toda exceção como um valor.
Você sabe distinguir uma exceção de uma recusa e de um erro, e sabe que os dois princípios funcionam sem as quatro peças do capítulo 15.

## Dois princípios que se sustentam sozinhos

Fatias verticais e exceções como valores não precisam de nenhuma das quatro peças, a tela, o orquestrador, o caso de uso e o repositório.
Qualquer estrutura que a sua stack favoreça consegue pôr cada funcionalidade em uma pasta e devolver exceções como valores: essa é a segunda resposta do kit para a arquitetura, entre [as duas escolhas](06-the-documents.md#as-duas-escolhas) do capítulo 6, e o capítulo 15 acrescenta as peças.
A clínica adotou o FOCUS inteiro no capítulo 7, então o código dela mostra os dois princípios.
Todo excerto abaixo vem do projeto guiado na tag do capítulo [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone), a tag anotada que marca o código que o capítulo 12 deixou, e é citado como rodou.

## Fatias verticais

Uma fatia vertical é uma pasta que guarda tudo o que uma funcionalidade precisa: as telas, as chamadas ao servidor, as rotas, as regras, o SQL e os testes.[^vertical-slice]
Não há pasta por tecnologia ou camada, nem `controllers/`, nem `models/`.
Uma subfuncionalidade é uma subpasta, como `authentication/change-password/`; a clínica ainda não tem nenhuma.

Esta é a saída de `git ls-tree -r --name-only book-v1/closing-a-milestone src/features/appointments`, a [fatia do agendamento](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone/src/features/appointments), 22 arquivos:

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

Uma mudança no agendamento mexe nesta pasta, e remover o agendamento remove esta pasta.
A fatia também delimita o que um agente lê em uma entrega sobre agendamento, assunto do capítulo 16.

A [fatia de saúde](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone/src/features/health), a verificação do servidor do primeiro marco, tem 6 arquivos:

```text
src/features/health/HealthView.e2e.ts
src/features/health/HealthView.tsx
src/features/health/api.ts
src/features/health/route.server.ts
src/features/health/strings.ts
src/features/health/useHealth.ts
```

Ela não tem `rules.ts`, porque não tem regra, nem `repository.server.ts`, porque não guarda nada: um arquivo aparece em uma fatia quando se paga.

O que duas funcionalidades já compartilham sai das fatias para `src/lib/`.
`email.ts`, `id.ts`, `name.ts` e `request.ts` dizem cada um, em um comentário, onde estão o primeiro e o segundo uso, como "First use: health/api.ts (`skeleton`); second use: clinic/api.ts." em `request.ts`; `result.ts` é usado por toda funcionalidade.
É a regra da segunda ocorrência do [capítulo 13](13-the-governor.md#a-mesma-pergunta-no-codigo), aplicada a pastas: o código vai para `lib/` no segundo uso, e não antes.

## Exceção, recusa, erro

O Dart divide as falhas em duas classes de `dart:core`.[^dart-core]
Uma `Exception` foi feita para ser capturada, uma falha esperada como uma conexão perdida; um `Error` é uma falha do programa que o programador deveria ter evitado, um bug.[^dart-core]

Este livro acrescenta um terceiro tipo: a recusa, a resposta de uma regra quando ela diz não, como um número de telefone com poucos dígitos.
Nenhum I/O falhou, e nenhum código está errado; a regra fez o trabalho dela.

Então uma falha é uma de três:

* **Exceção:** uma falha esperada no I/O (o banco de dados, a rede, o armazenamento do celular), capturada onde o I/O acontece e devolvida como valor.
* **Recusa:** uma regra dizendo não, devolvida como valor, sem I/O envolvido.
* **Erro:** um bug, lançado e nunca capturado, então chega à sua tela enquanto você desenvolve e ao seu analytics quando o app roda.

A área chama o princípio de "erros como valores", a partir do Go[^go-errors] e do Rust,[^rust-result] e o capítulo 6 disse por que este livro diz exceção.[^book-adr-0016]
O kit e a clínica ainda usam a palavra da área, `error`, no campo do `Result` e nos documentos, para o que este livro chama de exceção ou recusa.
O próprio docs/03 da clínica já chama cada resultado das suas regras de recusa, como `SlotTaken`, "a recusa quando um agendamento pede um horário que não está livre".

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

* Uma fatia vertical é uma pasta por funcionalidade, sem pasta por camada; uma mudança na funcionalidade mexe nessa pasta, e remover a funcionalidade remove essa pasta.
* Um arquivo entra em uma fatia quando se paga, e o código entra em `lib/` no segundo uso.
* Uma exceção existe só no I/O, uma recusa só em uma regra, e nenhuma das duas é lançada.
* Um erro é um bug: nunca capturado, chega à sua tela e ao seu analytics.
* Um `Result` tratado com um `Record` sobre os seus casos não compila quando um caso é esquecido.

## Exercícios

Estes exercícios usam a clínica, por conversa com o agente, nunca à mão.

### Exercício 14.1

Peça ao agente que liste todo `try`, `catch` e `throw` da sua clínica fora dos testes, e que diga, para cada um, que I/O ele protege e que valor ele devolve.
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
