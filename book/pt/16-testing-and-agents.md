---
status: draft
---

# Testes, e FOCUS com agentes

Depois deste capítulo você consegue dizer que teste guarda cada peça do FOCUS, e por que esse teste não troca nada além do I/O e do relógio.
Você consegue seguir uma regra da clínica por um teste em cada nível, e dizer, com o registro da própria clínica, como uma fatia e os seus testes mantêm pequena a leitura de um agente e dizem a ele quando terminou.

## Um teste para cada peça

Todo excerto abaixo vem do projeto guiado na tag do capítulo [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone), como no capítulo 15, e é citado como rodou; o código aninhado dentro de uma função aparece sem a indentação de fora.

O [`docs/04-Conventions.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/docs/04-Conventions.md) da clínica, na seção "Tests", dá os seus níveis em uma tabela.
O original está em inglês; esta é a tradução:

| Nível | Ferramenta | O quê |
|---|---|---|
| Caso de uso | Vitest | Toda regra, com o relógio passado como parâmetro. Sem banco, sem rede. |
| Repositório | Vitest | Consultas contra um SQLite em memória com as migrations reais. |
| Tela | Playwright | Cada cenário do Behaviour de uma página que tem tela, mais os screenshots do docs/05. |

A mesma seção termina com a regra da clínica: "*Toda regra tem um teste. Uma regra sem teste não está feita.*"

O Vitest roda um teste no Node, sem navegador.[^vitest]
O Playwright conduz o app em um navegador de verdade, como um usuário faria, clicando e digitando.[^playwright]

Um teste que o Vitest roda é um teste unitário: ele roda um pedaço de código, como um caso de uso chamado com os seus dados ou um repositório contra um banco em memória.
Um teste que o Playwright roda é um teste ponta a ponta: ele conduz o app rodando pela tela, pelos orquestradores, pelo servidor e pelo banco.
São os arquivos `.test.ts` e `.e2e.ts` da fatia do agendamento no [capítulo 14](14-errors-and-slices.md#fatias-verticais), cada um ao lado do arquivo que testa.

## Uma regra, quatro testes

A regra: um cliente cancela um agendamento até 24 horas antes do início.
É o caso de uso `cancel` da clínica, que o [exercício 14.2](14-errors-and-slices.md#exercicios) seguiu da regra até a tela; aqui ele é seguido pelos seus testes.

**O caso de uso.** Este é o `describe("cancel", ...)`, de [`src/features/appointments/rules.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/rules.test.ts):

```ts
describe("cancel", () => {
	// The deadline of at("08:00") is Monday 28 September, 08:00 UTC.
	const deadline = Date.parse("2026-09-28T08:00:00.000Z");

	it("succeeds one millisecond before and exactly at the deadline", () => {
		for (const now of [deadline - 1, deadline]) {
			expect(cancel(at("08:00"), new Date(now))).toEqual({
				ok: true,
				value: undefined,
			});
		}
	});

	it("is too late one millisecond after the deadline", () => {
		expect(cancel(at("08:00"), new Date(deadline + 1))).toEqual({
			ok: false,
			error: "CancellationTooLate",
		});
	});

	it("is too late for a start already past", () => {
		expect(cancel(at("08:00"), new Date(at("09:00")))).toEqual({
			ok: false,
			error: "CancellationTooLate",
		});
	});
});
```

`at` é um auxiliar do mesmo arquivo que dá um horário na terça-feira, 29 de setembro de 2026, em UTC, então `at("08:00")` começa às 08:00 e o seu prazo é 24 horas antes.
`cancel` recebe o início e `now`, e devolve um `Result`: `now` é um dado, então o teste tenta um milissegundo antes do prazo, o próprio prazo e um milissegundo depois, sem banco e sem mock.

**O driver que os testes do servidor trocam.** Este é `memoryDatabase`, de [`src/server/testDatabase.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/server/testDatabase.server.ts), que o capítulo 14 mostrou entre o código que captura:

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

É a única troca de que o servidor precisa: o mesmo motor SQLite, em memória, com os mesmos arquivos de migration que o app roda, então todo teste começa de um banco vazio com o schema real.

**O repositório.** Este é o `it("cancels once, keeping the row, and frees the slot", ...)`, de [`src/features/appointments/repository.server.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/repository.server.test.ts), onde cada teste recebe um `memoryDatabase` novo com dois profissionais:

```ts
it("cancels once, keeping the row, and frees the slot", () => {
	insertAppointment(db, appointment);

	expect(cancelAppointment(db, 1)).toEqual({ ok: true, value: true });
	expect(cancelAppointment(db, 1)).toEqual({ ok: true, value: false });

	expect(rows()).toEqual([
		expect.objectContaining({ booking_code: "K7MXQ2", status: "cancelled" }),
	]);
	expect(findBookedStarts(db, 1, "2026-09-29T00:00:00.000Z")).toEqual({
		ok: true,
		value: [],
	});
	expect(
		insertAppointment(db, { ...appointment, bookingCode: "ZZZZZZ" }).ok,
	).toBe(true);
});
```

`appointment` é um agendamento do mesmo arquivo e `rows` lê cada linha da tabela.
O teste roda o SQL real: o segundo cancelamento não muda nada, a linha fica com o status `cancelled`, e o horário aceita um novo agendamento.

**A rota.** O orquestrador do servidor é testado em [`src/features/appointments/route.server.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/route.server.test.ts), que prepara cada teste assim:

```ts
// Monday 28 September 2026, 01:00 in Lisbon.
const now = new Date("2026-09-28T00:00:00.000Z");

let db: DatabaseSync;
let app: Hono;

function setUpClinic() {
	saveClinicAndOwner(db, {
		name: "Clinica Sol",
		timeZone: "Europe/Lisbon",
		slotMinutes: 30,
		email: "owner@example.com",
		passwordHash: "unused",
	});
}

beforeEach(() => {
	vi.useFakeTimers({ toFake: ["Date"] });
	vi.setSystemTime(now);
	db = memoryDatabase();
	app = new Hono().route("/api", appointmentsRoute(db));
	setUpClinic();
	// 1 works on Tuesdays 09:00 to 11:00; 2 has no hours; 3 is removed.
	insertProfessional(db, "Ana Lima");
	insertProfessional(db, "Rui Lopes");
	insertProfessional(db, "Eva Reis");
	replaceWorkingPeriods(db, 1, [{ weekday: 2, start: "09:00", end: "11:00" }]);
	replaceWorkingPeriods(db, 3, [{ weekday: 2, start: "09:00", end: "11:00" }]);
	setRemovedAt(db, 3, "2026-09-27T10:00:00.000Z");
});

afterEach(() => {
	db.close();
	vi.useRealTimers();
});
```

`vi.useFakeTimers({ toFake: ["Date"] })` troca só o `Date`, então `new Date()` responde o que `vi.setSystemTime` definiu, e o `afterEach` devolve o relógio real.
A rota é o `appointmentsRoute(db)` do capítulo 15, que recebe o `memoryDatabase` e é montada em um app `Hono`, e `app.request` manda uma requisição a ela sem rede, como o [capítulo 15](15-four-pieces.md#o-que-a-clinica-injeta) disse.

Este é o teste da regra, `it("cancels at the deadline, and answers 409 one millisecond later, keeping it booked", ...)`, dentro do `describe("POST /api/appointments/cancel", ...)` do arquivo:

```ts
it("cancels at the deadline, and answers 409 one millisecond later, keeping it booked", async () => {
	const bookingCode = await booked();
	const body = { clientPhone: valid.clientPhone, bookingCode };
	// 24 hours before tuesday[0].
	const deadline = Date.parse("2026-09-28T08:00:00.000Z");

	vi.setSystemTime(deadline + 1);
	await expectError(await postCancel(body), 409, "CancellationTooLate");
	expect(statuses()).toEqual(["booked"]);

	vi.setSystemTime(deadline);
	expect((await postCancel(body)).status).toBe(200);
});
```

`booked` agenda `tuesday[0]`, às 08:00 UTC de terça-feira, pela rota de agendamento e responde o código dele; `valid` é o corpo desse agendamento, `postCancel` manda um cancelamento, `expectError` confere o status e o código de erro, e `statuses` lista o status de cada linha.
O relógio vai primeiro a um milissegundo depois do prazo: a resposta é 409 com `CancellationTooLate`, e a linha continua `booked`; depois, no próprio prazo, a mesma requisição responde 200.

Este é o "um evento, um novo estado" do [capítulo 15](15-four-pieces.md#um-evento-um-novo-estado) como um teste: uma requisição é o evento, e a resposta e as linhas são o novo estado.
O teste do caso de uso passa `now` como dado, e o teste da rota falsifica o relógio, porque a rota é a peça que lê `new Date()` e o entrega a `cancel`, como diz o item do docs/01 da clínica que o capítulo 15 citou: "*Casos de uso recebem a hora atual como parâmetro. Nenhum caso de uso lê o relógio.*"

**A tela.** Este é o `test("an appointment under 24 hours away is refused by the typed form, and shows no Cancel when remembered", ...)`, de [`src/features/appointments/CancelView.e2e.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/CancelView.e2e.ts):

```ts
test("an appointment under 24 hours away is refused by the typed form, and shows no Cancel when remembered", async ({
	page,
}) => {
	const name = tagged("Ana");
	const id = await professionalWith(page, name, allWeek("08:00", "20:00"));
	const [[earliest]] = await slotsByDay(page, id);
	const phone = randomPhone();
	const appointment = await bookThroughApi(page, id, name, earliest, phone);
	await page.goto("/");

	const form = await typeAndSend(page, phone, appointment.bookingCode);

	await expect(form.getByText(tooLate)).toBeVisible();
	await expect(form.getByLabel("Booking code")).toHaveValue(
		appointment.bookingCode,
	);

	await plant(page, [appointment]);
	const item = itemOf(page, appointment);
	await expect(item).toBeVisible();
	await expect(
		item.getByText("Can no longer be cancelled in the app."),
	).toBeVisible();
	await expect(button(item, "Cancel")).toHaveCount(0);
});
```

Os auxiliares são do arquivo e da fatia: `professionalWith` cadastra um profissional que trabalha `allWeek` das 08:00 às 20:00, `slotsByDay` dá os horários livres, `bookThroughApi` agenda o mais cedo, que está a menos de 24 horas, `typeAndSend` preenche e manda o formulário de cancelamento, `plant` põe o agendamento no armazenamento do celular e recarrega, e `itemOf` acha a linha dele em "Your appointments" (seus agendamentos); `tooLate` é a mensagem das 24 horas.
Ele roda no relógio real, e em um navegador conduz a tela e o orquestrador do cliente: o formulário digitado mostra por que recusou e mantém o código, e a linha guardada não mostra o botão Cancel (cancelar).

O caso de uso prova o limite no milissegundo, e o repositório que uma linha cancelada é mantida e o seu horário, liberado.
A rota prova que o servidor recusa depois do prazo e não muda nada, e a tela que o cliente vê por quê.

## O I/O do cliente

O cliente tem dois repositórios, e cada um tem o seu I/O trocado do mesmo jeito.

`remembered.ts`, o armazenamento do celular, lê e escreve o `localStorage`, que o Node não tem.
Esta é a preparação de [`src/features/appointments/remembered.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/remembered.test.ts):

```ts
let stored: Map<string, string>;

beforeEach(() => {
	stored = new Map();
	vi.stubGlobal("localStorage", {
		getItem: (key: string) => stored.get(key) ?? null,
		setItem: (key: string, value: string) => stored.set(key, value),
	});
});

afterEach(() => {
	vi.unstubAllGlobals();
});
```

`vi.stubGlobal` põe um `localStorage` apoiado em um `Map` no lugar do do navegador, e `vi.unstubAllGlobals` o remove depois de cada teste.

A rede passa por uma função, `request` em `src/lib/request.ts`, do capítulo 14, que todo `api.ts` chama.
O teste dela, [`src/lib/request.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/lib/request.test.ts), troca o `fetch` do mesmo jeito, e estes são os testes sob o seu `describe("request", ...)`:

* ``gives what `read` accepts from a 2xx body`` (dá o que `read` aceita de um corpo 2xx)
* `gives the refusal named for the status` (dá a recusa nomeada para o status)
* `gives ServerUnreachable for a status not named` (dá `ServerUnreachable` para um status não nomeado)
* ``gives ServerUnreachable for a body `read` does not accept`` (dá `ServerUnreachable` para um corpo que `read` não aceita)
* `gives ServerUnreachable when the network fails` (dá `ServerUnreachable` quando a rede falha)
* `reads no body from a 204` (não lê corpo de um 204)

No cliente, como no servidor, só o I/O é trocado: o armazenamento e a rede, nunca um hook ou um caso de uso.

## O que não tem teste próprio

Os orquestradores do cliente, os hooks `use<Feature>.ts` (na fatia do agendamento, `useBooking.ts`, `useCancel.ts` e `useRemembered.ts`), e o `api.ts` de cada funcionalidade, os repositórios da rede, não têm `.test.ts`, e a tabela da clínica não tem linha para eles.
Eles não guardam regra, já que as regras estão em `rules.ts`; um `api.ts` só diz que status é que recusa, sobre `request`, que é testada; e os testes ponta a ponta conduzem todos eles.
Isso é tolerável hoje, e é também uma lacuna que você pode achar com o agente: um hook que publicasse o estado errado só seria pego por um teste no navegador, o mais lento de rodar.
Como o que o exercício 15.1 pede ao agente para achar, ela é candidata à fila da clínica, não uma correção agora, e a clínica fica como está.

## Quantos

O `npm run verify` da clínica no seu último commit do marco 1, `f16f83b`, rodou 25 arquivos do Vitest com 238 testes em 1,10 segundo, e 144 execuções do Playwright em 21,0 segundos.[^clinic-milestone-1-run]
As 144 execuções são 91 testes distintos: todo teste roda em 390×844, e os 53 testes dos arquivos das três telas do dono rodam de novo em 1280×800, como o docs/04 da clínica diz na seção "Tests".
Os 91 e os 53 são as linhas que começam com `test(` nos arquivos `.e2e.ts` da tag, os sete para os 91 e os três das telas do dono para os 53.
A tag `book-v1/closing-a-milestone`, commit `c54d011`, difere de `f16f83b` só na fila da clínica, o docs/06, então essas contagens valem na tag.

## O que a fatia dá a um agente

O capítulo 14 disse que uma fatia limita o que um agente lê.
O registro do marco 1 da clínica deixa você contar isso, para as duas entregas da fatia do agendamento.[^clinic-milestone-1-run]

Contei os arquivos distintos sob `src/` que existiam no commit pai da entrega e cujo conteúdo o turno do `/apply` leu, por uma chamada `Read` ou uma chamada de shell que imprime um arquivo (`cat`, `sed -n`, `head`, `tail`); um `grep` ou um `ls` não é leitura, uma chamada que o registro lista como negada não leu nada, o turno do `/apply` é o que o README do registro nomeia para aquela entrega, e o total é o que `git ls-tree -r --name-only <pai> src` lista.

`cancel-appointment` acrescentou uma funcionalidade dentro de uma fatia que já existia.
O turno do `/apply` dela leu 20 dos 95 arquivos de `src/` no seu commit pai, `442f88a`.
15 dos 20 estavam em `src/features/appointments/`, que tinha 17, e os outros cinco eram código compartilhado que ela chama: `src/app/main.tsx`, `src/lib/request.ts`, `src/lib/result.ts`, `src/server/database.server.ts` e `src/features/professionals/repository.server.ts`.

`book-appointment` começou a fatia.
O turno do `/apply` dela leu 33 dos 77 arquivos de `src/` no seu commit pai, `afc833a`: sem fatia própria ainda, leu as outras fatias, 9 arquivos delas de `src/features/weeklyHours/`, e disse isso:

> "I've studied the `weeklyHours` slice to use as the pattern."

Em português: "Estudei a fatia `weeklyHours` para usar como padrão."
Uma fatia nova copia a forma de uma fatia irmã, e uma entrega dentro de uma fatia lê essa fatia e o código compartilhado que ela chama.

Os dois turnos rodaram os testes da fatia sozinhos antes da verificação inteira.
`cancel-appointment` rodou `npx vitest run src/features/appointments`, depois `npx playwright test --project=phone src/features/appointments`, depois `npm run verify`.
`book-appointment` rodou `npx vitest run src/features/appointments`, depois `npx playwright test src/features/appointments src/features/clinic`, depois `npx playwright test src/features/appointments --repeat-each=3`, depois `npm run verify`.
Os testes da própria fatia dizem ao agente em segundos se ele terminou a fatia, e a verificação depois diz que nada mais quebrou.

Menos arquivos lidos é menos contexto, e o [capítulo 2](02-how-agents-see.md#mais-contexto-menos-precisao) mostrou que a precisão de um modelo cai conforme a janela de contexto enche, o que é a degradação de contexto.

A sua parte é a revisão.
O nome de um teste é uma frase da regra, como "is too late one millisecond after the deadline" (é tarde demais um milissegundo depois do prazo), então revisar os testes que um agente pôs no stage começa por ler os nomes deles, como na [revisão do capítulo 11](11-apply.md#revise-antes-do-commit): uma regra sem frase entre eles não tem teste.

## Pontos-chave

* Cada peça tem o seu teste: um caso de uso chamado com os seus dados e `now`, um repositório contra um SQLite em memória com as migrations reais, uma rota por `app.request` com um relógio falso, e a tela em um navegador com o Playwright.
* Um teste troca só o I/O e o relógio, porque só os repositórios fazem I/O e só os orquestradores leem o relógio.
* Uma regra seguida por todos os níveis mostra o que cada nível prova que os outros não provam: o limite, a linha, a resposta do servidor e o que o cliente vê.
* Código sem regra própria, como os orquestradores do cliente e cada `api.ts`, pode ficar sem teste próprio enquanto testes ponta a ponta o conduzem; nomeie a lacuna e ponha na fila.
* Uma fatia mantém pequena a leitura de um agente, 20 de 95 arquivos para uma entrega dentro dela, e os testes dela, rodados sozinhos, dizem ao agente quando a fatia está feita.

## Exercícios

Estes exercícios usam a clínica, por conversa com o agente, nunca à mão.

### Exercício 16.1

Pergunte ao agente que testes guardam a regra de que o nome de um cliente tem no máximo 80 caracteres, em todos os níveis, e peça que rode só esses.
Compare o que ele rodou com o que o `npm run verify` roda.

### Exercício 16.2

Pegue a regra do exercício 15.2: um cliente pode ter no máximo dois agendamentos futuros.
Pergunte ao agente que arquivos de teste mudam, e o que cada teste novo afirma, em cada nível.
Nada é construído.

### Exercício 16.3

Em uma sessão nova, pergunte ao agente que arquivos ele leria para acrescentar uma entrega em que o dono vê os agendamentos do dia, e por quê.
Compare a lista dele com as fatias que ele nomeia e com as contagens de "O que a fatia dá a um agente".
Nada é construído.

[^vitest]: Vitest, "Getting Started", o guia da documentação, acesso em 2026-09-29. <https://vitest.dev/guide/>
[^playwright]: Playwright, "Installation", a documentação, acesso em 2026-09-29. <https://playwright.dev/docs/intro>
[^clinic-milestone-1-run]: A construção do marco 1 do projeto guiado deste livro, 2026-09-28, com o Claude Code 2.1.284 e o modelo `claude-opus-5-5`: cada turno de cada entrega, a saída do `npm run verify` no último commit da clínica em `verify.txt`, e as chamadas negadas no README. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-milestone-1-run>
