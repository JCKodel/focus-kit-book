# As quatro peças

Depois deste capítulo você consegue pôr cada arquivo de uma funcionalidade em uma das quatro peças, tela, orquestrador, caso de uso e repositório, no cliente e no servidor.
Você consegue seguir um evento por elas até um novo estado, e decidir, para uma funcionalidade, quais peças se pagam e sem quais ela fica.

## As quatro peças

O capítulo 6 deu o FOCUS em um parágrafo, em [as duas escolhas](06-the-documents.md#as-duas-escolhas), a partir do ADR-0016 deste livro;[^book-adr-0016] este capítulo mostra as peças dele em código que roda.
Todo excerto abaixo vem do projeto guiado na tag do capítulo [`book-v1/four-pieces`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/four-pieces), o código que o capítulo 12 deixou mais a entrega [`orchestrator-tests`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/work/done/orchestrator-tests.md) do marco 1.1 da clínica (o docs/06 dessa tag ainda o chama de marco 2; o capítulo 12 diz por quê), e é citado como rodou; o código aninhado dentro de uma função aparece sem a indentação de fora.

A `orchestrator-tests` não é um achado da revisão: o autor pôs a linha dela no marco 1.1 porque o capítulo 16 precisava de orquestradores do cliente com testes.
Se você segue a clínica, adicione essa linha como a primeira do marco 1.1 que o exercício 12.3 escreveu, como a fila da clínica a tem, e acrescente "every client orchestrator has unit tests" (todo orquestrador do cliente tem testes unitários) ao parágrafo desse marco:

```
[ ] orchestrator-tests   every use<Feature>.ts hook's events move to plain functions with repositories as a parameter, tested in Node
```

Depois rode `/propose orchestrator-tests`, responda às perguntas dele com o briefing do autor,[^clinic-orchestrator-tests-run] em que "milestone 2" é o seu marco 1.1, e rode `/apply orchestrator-tests` antes de seguir a leitura.

A clínica adotou o FOCUS inteiro no capítulo 7, e o [`docs/01-Architecture.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/docs/01-Architecture.md) dela, na seção "How the code is organized", dá as quatro peças em uma tabela.
O original está em inglês; esta é a tradução:

| Peça | Faz | Proíbe |
|---|---|---|
| Tela | dispara eventos, renderiza o estado | regras de negócio, acesso a dados |
| Orquestrador | converte evento em estado, busca, chama casos de uso, publica o estado | decidir regras, persistir |
| Caso de uso | o único lugar das regras de negócio; puro; recebe dados, devolve um Result | IO, framework, exceção de domínio |
| Repositório | buscar e salvar; o único lugar onde uma exceção de infra vira um Result | regras de negócio |

A mesma seção lista os arquivos de uma fatia, uma pasta `features/<feature>/`, com a peça que cada arquivo faz, também traduzida:

```text
features/<feature>/
  rules.ts               Casos de uso: puros, importados pelo cliente e pelo servidor
  rules.test.ts
  route.server.ts        Orquestrador do servidor: uma rota do Hono
  repository.server.ts   Repositório do servidor: SQL
  repository.server.test.ts
  api.ts                 Repositório do cliente: fetch, falha de rede vira um Result
  <name>Events.ts        Orquestrador do cliente: o estado do hook, o valor
                         inicial dele e o que cada evento faz, como funções simples
  <name>Events.test.ts
  use<Feature>.ts        Orquestrador do cliente: um hook do React que publica um estado
  <Feature>View.tsx      Tela
  strings.ts             todo texto que o usuário lê nesta funcionalidade
```

Leia primeiro a coluna "Proíbe": é ela que mantém uma peça no seu trabalho, então uma tela com uma regra de negócio ou um repositório que decide uma quebra a tabela, faça o que fizer de certo.
A "exceção de domínio" da tabela, que um caso de uso não pode lançar, é o que este livro chama de recusa, e os "erros como valores" da clínica são as exceções como valores do livro, as duas do [capítulo 14](14-errors-and-slices.md#excecao-recusa-erro).
O orquestrador é o que o Flutter conhece como BLoC[^bloc] e o .NET como o padrão Mediator, como no MediatR.[^mediatr]
O Clean do FOCUS são as camadas da Clean Architecture[^clean-architecture] com uma diferença: um caso de uso não recebe repositório, então uma regra não alcança o I/O, nem por uma interface.[^book-adr-0016]

## Dois lados, um conjunto de regras

Uma fatia da clínica roda em dois lados, o navegador do celular e o servidor, e cada lado tem o seu próprio orquestrador e os seus próprios repositórios.

No cliente, o orquestrador são dois arquivos.
`<name>Events.ts` guarda o que cada evento faz, como funções simples: as chamadas a repositórios e casos de uso, em ordem, e o novo estado.
O hook `use<Feature>.ts` é só a parte do React: ele guarda o estado, publica o estado em andamento e a resposta, lê o relógio e descarta uma resposta velha.
Os repositórios do orquestrador são `api.ts`, que alcança a rede, e, na fatia dos agendamentos, `remembered.ts`, que alcança o armazenamento do celular.
A listagem da clínica rotula só `api.ts` como repositório; este livro põe `remembered.ts` ali também, porque ele faz o trabalho de um repositório: a seção "How data is accessed" do mesmo docs/01 faz dele o único código que mexe no armazenamento do celular, e ele devolve a sua falha como um `Result`.

No servidor, o orquestrador é a rota `route.server.ts`, e o repositório é `repository.server.ts`, que roda o SQL.

`rules.ts`, os casos de uso, é importado pelos dois lados, e o docs/01 da clínica diz por quê:

> "*O servidor impõe toda regra. O cliente importa o mesmo caso de uso só para decidir o que mostrar (por exemplo, se o botão de cancelar aparece), então uma regra é escrita uma vez e testada uma vez.*"

A tela existe só no cliente; no servidor, o novo estado a que um evento leva é a resposta à requisição.

## Um evento, um novo estado

Um cliente agenda um horário: o toque em "Book" (agendar) é o evento, e a tela que mostra o código do agendamento é o novo estado.
Estes são os passos entre os dois.

**1. A tela dispara o evento.** Este é o passo do formulário de [`src/features/appointments/BookingView.tsx`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/BookingView.tsx):

```ts
case "form": {
	const timeZone = state.slots?.timeZone ?? "UTC";
	const submitForm = (event: FormEvent) => {
		event.preventDefault();
		submit();
	};
	return (
		<form noValidate onSubmit={submitForm}>
			<p>{summary(step.startsAt, timeZone, step.professional.name)}</p>
			{tooLateToCancel && <p>{strings.tooLateToCancel}</p>}
			<p>
				<label htmlFor="client-name">{strings.name}</label>
				<input
					id="client-name"
					autoComplete="name"
					value={state.name}
					onChange={(event) => typeName(event.target.value)}
					style={field}
				/>
				{state.nameError && (
					<span role="alert">{errorStrings[state.nameError]}</span>
				)}
			</p>
			<p>
				<label htmlFor="client-phone">{strings.phone}</label>
				<input
					id="client-phone"
					type="tel"
					autoComplete="tel"
					value={state.phone}
					onChange={(event) => typePhone(event.target.value)}
					style={field}
				/>
				{state.phoneError && (
					<span role="alert">{errorStrings[state.phoneError]}</span>
				)}
			</p>
			<div style={buttons}>
				<button type="submit" style={action} disabled={busy}>
					{strings.book}
				</button>
				{backButton}
			</div>
		</form>
	);
}
```

A tela renderiza o que `state` guarda e entrega toda mudança ao hook, como `typeName`, `typePhone`, `back` ou `submit`; o toque em "Book" envia o formulário, e `submitForm` chama `submit` e não faz mais nada.

**2. O orquestrador do cliente.** Os eventos dele são funções simples em [`src/features/appointments/bookingEvents.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/bookingEvents.ts); agendar usa dois, `submitStarted` e `submit`:

```ts
// Name and phone are checked here to show the message beside the field
// and send nothing; the server checks them again.
export function submitStarted(state: BookingState): {
	state: BookingState;
	send: boolean;
} {
	if (state.step.kind !== "form" || !state.slots) return { state, send: false };
	const name = checkClientName(state.name);
	const phone = checkClientPhone(state.phone);
	const checked = {
		...state,
		nameError: name.ok ? undefined : name.error,
		phoneError: phone.ok ? undefined : phone.error,
	};
	if (!name.ok || !phone.ok) return { state: checked, send: false };
	return { state: { ...checked, busy: true, failed: undefined }, send: true };
}

// `state` is the one `submitStarted` accepted.
export async function submit(
	state: BookingState,
	now: Date,
	repositories = bookingRepositories,
): Promise<BookingOutcome> {
	const { step, slots } = state;
	if (step.kind !== "form" || !slots) return { update: (s) => s };
	const result = await repositories.postAppointment({
		professionalId: step.professional.id,
		startsAt: step.startsAt,
		clientName: state.name,
		clientPhone: state.phone,
	});
	if (result.ok) {
		const booked = result.value;
		// A storage failure leaves the code on screen: nothing else to do.
		repositories.remember(
			{
				bookingCode: booked.bookingCode,
				clientPhone: booked.clientPhone,
				professionalName: booked.professional.name,
				startsAt: booked.startsAt,
				timeZone: slots.timeZone,
			},
			now,
		);
		return {
			update: (s) => ({
				...s,
				step: { kind: "booked", booked, timeZone: slots.timeZone },
				busy: false,
				name: "",
				phone: "",
			}),
		};
	}
	const code = result.error.code;
	if (code === "ProfessionalNotFound") {
		return { next: "loadProfessionals", message: "ProfessionalNotFound" };
	}
	if (code === "SlotTaken") {
		return {
			next: "loadSlots",
			professional: step.professional,
			after: { message: "SlotTaken", date: step.date },
		};
	}
	return { update: (s) => ({ ...s, busy: false, failed: "book" }) };
}
```

`submitStarted` confere nome e telefone com os casos de uso `checkClientName` e `checkClientPhone`, só para mostrar uma mensagem ao lado de um campo, e dá o estado em andamento, com `busy` ligado.
`submit` envia o agendamento pelo repositório `postAppointment` e guarda uma cópia no celular pelo repositório `remember`, os dois alcançados por `repositories`, com `now` recebido de fora; ele devolve uma atualização do estado, o passo `booked`, ou o próximo evento a rodar: `loadProfessionals` quando o profissional sumiu, `loadSlots` quando o horário foi tomado.

O `submit` que a tela chama é o do próprio hook, que entrega o evento a `run`, por isso o hook importa o `submit` de `bookingEvents.ts` como `submitEvent`.
Aqui estão o estado do hook, suas duas refs e `run`, de [`src/features/appointments/useBooking.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/useBooking.ts):

```ts
const [state, setState] = useState<BookingState>(initialBookingState);
// Only the answer to the latest request is shown; Back or another tap
// makes earlier ones stale.
const latest = useRef(0);
// The state last shown: what a booking sends.
const shown = useRef(state);
shown.current = state;

// Any event with a call: its in-flight state, then its answer, which is
// an update or the next event to run.
const run = useCallback(async function run(next: BookingNext) {
	let outcome: Promise<BookingOutcome>;
	if (next.next === "submit") {
		const snapshot = shown.current;
		const started = submitStarted(snapshot);
		setState(started.state);
		if (!started.send) return;
		outcome = submitEvent(snapshot, new Date());
	} else if (next.next === "loadSlots") {
		setState((s) => loadSlotsStarted(s, next.professional));
		outcome = loadSlots(next.professional, next.after);
	} else {
		setState((s) => loadProfessionalsStarted(s, next.message));
		outcome = loadProfessionals();
	}
	const call = ++latest.current;
	const answer = await outcome;
	if (call !== latest.current) return;
	if ("update" in answer) setState(answer.update);
	else await run(answer);
}, []);
```

O hook põe o estado em andamento, lê `new Date()` e o passa a `submitEvent`, descarta uma resposta que não é a mais recente, e publica a atualização ou roda o próximo evento.
`shown` guarda o último estado renderizado, que o ramo do submit lê como `snapshot`; `submitStarted` e `submitEvent` recebem os dois esse snapshot.
`latest` é uma contagem de pedidos: cada chamada pega o número seguinte, e uma resposta cujo número já não é o mais recente é descartada; `back` também avança `latest`, então uma resposta que chega depois de um toque em "Back" é descartada também.

**3. O repositório do cliente.** Este é `postAppointment`, de [`src/features/appointments/api.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/api.ts):

```ts
// The client checks name and phone with the same use cases before sending,
// so a 400 would mean the server cannot be relied on: it reads as
// ServerUnreachable, as in weeklyHours/api.ts.
export function postAppointment(
	body: BookingBody,
): Promise<Result<Booked, BookError>> {
	return request<Booked, NotFound | NotFree>(
		"/api/appointments",
		{
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(body),
		},
		bookedOf,
		{ 404: { code: "ProfessionalNotFound" }, 409: { code: "SlotTaken" } },
	);
}
```

Ele alcança a rede por `request`, de `src/lib/request.ts` no capítulo 14, que devolve a resposta como um `Result`, e nomeia as duas respostas que espera como recusas: 404 é `ProfessionalNotFound` e 409 é `SlotTaken`.

**4. O orquestrador do servidor busca.** A requisição chega a [`src/features/appointments/route.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/route.server.ts), cujo `slotsOf` lê aquilo contra o que um agendamento é conferido:

```ts
// What both routes read after the body: the active professional, the clinic
// and what the slots are cut from, with `now`; else the answer. Synchronous,
// so no other request of the process runs between this read and the insert.
function slotsOf(
	db: DatabaseSync,
	c: Context,
	professionalId: number | undefined,
	now: Date,
): Result<{ professional: Professional; input: SlotInput }, Response> {
	if (professionalId === undefined) return err(notFound(c));
	const active = findActiveProfessionals(db);
	if (!active.ok) return err(databaseFailed(c));
	const professional = active.value.find((p) => p.id === professionalId);
	if (!professional) return err(notFound(c));
	const clinic = findClinic(db);
	if (!clinic.ok) return err(databaseFailed(c));
	// A professional exists only once the clinic is set up; kept for the types.
	if (!clinic.value) {
		return err(c.json({ error: { code: "ClinicNotSetUp" } }, 500));
	}
	const { timeZone, slotMinutes } = clinic.value;
	const periods = findWorkingPeriods(db, professionalId);
	if (!periods.ok) return err(databaseFailed(c));
	const from = new Date(now.getTime() - slotMinutes * 60 * 1000);
	const booked = findBookedStarts(db, professionalId, from.toISOString());
	if (!booked.ok) return err(databaseFailed(c));
	return ok({
		professional,
		input: {
			periods: periods.value,
			booked: booked.value,
			timeZone,
			slotMinutes,
			now,
		},
	});
}
```

Ele pede os dados a quatro funções de repositório, de quatro fatias: `findActiveProfessionals` de `professionals`, `findClinic` de `clinic`, `findWorkingPeriods` de `weeklyHours` e `findBookedStarts` de `appointments`.
Cada uma fica na fatia da coisa que lê, e `slotsOf` a importa de lá, como diz a regra do [capítulo 14](14-errors-and-slices.md#fatias-verticais).
`now` entra como parâmetro, e o `Result` dele guarda os dados ou a resposta a enviar, montada por `notFound` e `databaseFailed`, dois helpers do mesmo arquivo.

**5. O orquestrador do servidor decide e salva.** Este é o handler `.post("/appointments", ...)`, do mesmo arquivo:

```ts
.post("/appointments", async (c) => {
	const body: unknown = await c.req.json().catch(() => undefined);
	if (!isBookingBody(body)) {
		return c.json({ error: { code: "BadRequest" } }, 400);
	}
	const read = slotsOf(db, c, body.professionalId, new Date());
	if (!read.ok) return read.error;
	const { professional, input } = read.value;
	const booking = book(body, input);
	if (!booking.ok) {
		const code = booking.error;
		return c.json({ error: { code } }, refusalStatus[code]);
	}
	const bookingCode = drawBookingCode();
	const inserted = insertAppointment(db, {
		professionalId: professional.id,
		bookingCode,
		...booking.value,
	});
	if (!inserted.ok) {
		const code = inserted.error.code;
		if (code === "SlotTaken") return c.json({ error: { code } }, 409);
		return databaseFailed(c);
	}
	return c.json(
		{
			bookingCode,
			startsAt: booking.value.startsAt,
			clientPhone: booking.value.clientPhone,
			professional,
		},
		201,
	);
})
```

Em ordem: o formato do corpo, `slotsOf`, o caso de uso `book`, cuja recusa vira um status por `refusalStatus` do [capítulo 14](14-errors-and-slices.md#excecoes-como-valores-na-clinica), o código do agendamento, o repositório `insertAppointment`, cujo SQL está na mesma seção do capítulo 14, e a resposta 201.
A rota lê o corpo ela mesma, porque a requisição é o evento que ela recebe; um corpo que não pode ser lido vira `BadRequest`, como diz o [capítulo 14](14-errors-and-slices.md#excecoes-como-valores-na-clinica).
`drawBookingCode` sorteia o código na rota, porque o acaso, como o relógio, cabe ao orquestrador fornecer, e assim nenhum caso de uso deixa de ser puro; o docs/01 da clínica diz isso do relógio: "*Casos de uso recebem a hora atual como parâmetro. Nenhum caso de uso lê o relógio.*"

**6. O caso de uso decide.** Este é `book`, de [`src/features/appointments/rules.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/rules.ts):

```ts
// The appointment to store, checked in order: name, phone, window, hours,
// taken. `startsAt` comes back as toISOString().
export function book(
	request: BookingRequest,
	input: SlotInput,
): Result<Booking, BookingRefusal> {
	const clientName = checkClientName(request.clientName);
	if (!clientName.ok) return clientName;
	const clientPhone = checkClientPhone(request.clientPhone);
	if (!clientPhone.ok) return clientPhone;

	const start = Date.parse(request.startsAt);
	const now = input.now.getTime();
	// A start that is not a date is in no window.
	if (!(start > now && start <= now + windowMs)) {
		return err("OutsideBookingWindow");
	}
	const startsAt = new Date(start).toISOString();
	if (!freeSlots({ ...input, booked: [] }).includes(startsAt)) {
		return err("OutsideWorkingHours");
	}
	if (!freeSlots(input).includes(startsAt)) return err("SlotTaken");
	return ok({
		startsAt,
		clientName: clientName.value,
		clientPhone: clientPhone.value,
	});
}
```

Dados entram, `now` dentro de `input`, e um `Result` sai; ele chama `checkClientName`, `checkClientPhone` e `freeSlots`, todos em `rules.ts`, e nenhum repositório.

A volta não precisa de excerto: a rota responde 201, `postAppointment` devolve o agendamento como valor, `submit` devolve a atualização com o passo `booked`, o hook a publica, e a tela o renderiza no seu `case "booked"`, com o código do agendamento.

O fluxo nunca volta pelo caminho errado: a tela nunca muda o estado, e um caso de uso nunca chama um repositório.
Então "o que acontece quando este evento chega?" tem uma resposta, e o capítulo 16 a transforma em um teste.

## O que a clínica injeta

O ADR-0016, com as suas emendas, dá a regra: uma peça recebe uma dependência só onde o teste dela passa uma segunda implementação.[^book-adr-0016]
A clínica a segue nos dois lados.

O orquestrador do servidor recebe o banco de dados, o driver que os repositórios dele usam, e o entrega a cada função de repositório: a rota é `appointmentsRoute(db)`, e `slotsOf` e o handler acima entregam `db` a toda chamada de repositório, e cada função de repositório também recebe `db`, porque o próprio teste dela passa direto um banco em memória, como mostra o [capítulo 16](16-testing-and-agents.md#uma-regra-cinco-testes).
O teste da rota passa `memoryDatabase`, o SQLite em memória do capítulo 14, no lugar do arquivo, e o docs/01 da clínica diz por que a rota recebe o driver:

> "*Rotas do servidor que precisam do banco de dados são funções dele (`clinicRoute(db)`), então o Vitest as conduz pelo `app.request` do Hono contra um SQLite em memória (`testDatabase.server.ts`).*"

O Vitest é o executor de testes da clínica, `app.request` envia uma requisição a uma rota sem rede, e `testDatabase.server.ts` guarda `memoryDatabase`.

O orquestrador do cliente recebe os seus repositórios, nomeados em `bookingEvents.ts`:

```ts
export type BookingRepositories = {
	fetchProfessionals: typeof fetchProfessionals;
	fetchSlots: typeof fetchSlots;
	postAppointment: typeof postAppointment;
	remember: typeof remember;
};

export const bookingRepositories: BookingRepositories = {
	fetchProfessionals,
	fetchSlots,
	postAppointment,
	remember,
};
```

`submit`, no passo 2, recebe `repositories = bookingRepositories`, os reais por padrão, então o hook não passa nenhum.
Os testes dos eventos passam, no lugar deles, repositórios que respondem o que o teste define.
O docs/01 da clínica diz isso na seção "How the code is organized"; o original está em inglês, e esta é a tradução:

> "*As funções de evento dele recebem os seus repositórios como parâmetro, os reais por padrão (`<name>Repositories`), e o relógio como `now`: nenhuma função ali o lê.*"

O SQLite em memória é um banco falso, e esses são repositórios falsos: falso, aqui, é uma segunda implementação que um teste passa no lugar da real.
Um caso de uso não recebe repositório (ADR-0016) e uma tela não recebe nada: cada um tem uma só implementação, então um parâmetro ali existiria por cerimônia, o que o KISS descarta.
`now`, que a rota ou o hook lê, é passado adiante como dado, um valor, não uma dependência.
O capítulo 16 mostra os testes e os repositórios falsos deles.

## Quando as peças se pagam

Uma peça só pode existir quando tem um trabalho.
Um caso de uso existe quando há uma regra: a fatia `health` do [capítulo 14](14-errors-and-slices.md#fatias-verticais) não tem nenhuma, então não tem `rules.ts`.
Um repositório existe quando há I/O, um orquestrador quando um evento leva a um novo estado, e uma tela quando há uma tela para mostrar.

O [ADR-0002](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/docs/adr/ADR-0002-focus-whole.md) da clínica, a decisão de adotar o FOCUS inteiro, nomeia o custo nas suas Consequences: "*Uma fatia tem mais arquivos do que um componente que busca os dados sozinho; um arquivo só aparece quando se paga.*"
O Context dele nomeia o que a clínica compra com isso: um produto que valoriza "*toda regra tem um teste*", e uma regra em uma função pura é o lugar mais barato para um.

Um trabalho é necessário, e não basta: o orquestrador do cliente da fatia `health` tem um e mesmo assim não se paga.
O trabalho dele é real: `check`, em [`healthEvents.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/health/healthEvents.ts), transforma a resposta do servidor em `ok` ou `unreachable`.
O custo dele, contado com `wc -l` em cada tag: em `book-v1/closing-a-milestone` era um arquivo, `useHealth.ts`, de 20 linhas; em `book-v1/four-pieces` são três, `useHealth.ts` (21), `healthEvents.ts` (16) e `healthEvents.test.ts` (17), 54 linhas.
Ele traz também uma função de atualização que ignora o estado atual, e um parâmetro `repositories` que só o teste usa.
O ganho dele já é dado: os dois casos do Vitest em `healthEvents.test.ts`, "gives ok" (dá ok) e "gives unreachable" (dá unreachable), afirmam o que [`HealthView.e2e.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/health/HealthView.e2e.ts) afirma, cujos quatro testes do Playwright mostram "Server: ok" uma vez e "Server: unreachable" duas, com um 500 e sem resposta.
A mesma peça se paga em `bookingEvents.ts`, o passo 2 de [Um evento, um novo estado](#um-evento-um-novo-estado): o teste dele "keeps a name typed in flight through a taken slot" (mantém um nome digitado em andamento apesar de um horário tomado) prova o que nenhum teste do Playwright na tag prova.
Sozinho, `healthEvents.ts` custa mais do que dá.
A clínica o mantém porque [`orchestrator-tests`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/work/done/orchestrator-tests.md), a entrega que o escreveu, escolheu "*Todo evento se move*", para que todo hook tenha uma só forma: essa forma é o que a clínica paga, não a peça.

Onde o código já tem a sua própria forma, as peças podem custar mais do que dão.
No projeto brownfield do [capítulo 8](08-analyze.md#focus-em-codigo-sem-arquitetura), o FOCUS inteiro significava uma refatoração grande, e a resposta foi nenhum.
Entre os dois fica a resposta do meio do kit, só os dois princípios do [capítulo 14](14-errors-and-slices.md#dois-principios-que-se-sustentam-sozinhos): fatias e exceções como valores, sem nenhuma peça.
KISS, YAGNI e DRY decidem, como o [capítulo 6](06-the-documents.md#as-duas-escolhas) disse: uma peça é escrita quando uma entrega precisa do trabalho dela, e não antes.

## Pontos-chave

* A tela dispara eventos e renderiza o estado, o orquestrador transforma um evento em um novo estado, um caso de uso guarda uma regra como função pura, e o repositório é a única peça que busca e salva.
* Uma peça é escrita quando tem um trabalho e esse trabalho dá mais do que custa; a coluna "Proíbe" a mantém nesse trabalho.
* Na clínica cada lado tem o seu orquestrador e os seus repositórios, e os dois importam os mesmos casos de uso: o servidor impõe uma regra, e o cliente a usa só para decidir o que mostrar.
* Um evento corre em um só sentido: a tela nunca muda o estado, e um caso de uso nunca chama um repositório.
* Uma peça recebe uma dependência só onde o teste dela passa uma segunda implementação, uma falsa: o orquestrador os seus repositórios ou o driver que eles usam, e um repositório do servidor esse driver; um caso de uso e uma tela não recebem nenhuma, e `now` é passado como dado.

## Exercícios

Estes exercícios usam a clínica, por conversa com o agente, nunca à mão.

### Exercício 15.1

Peça ao agente que ponha cada arquivo de `src/features/professionals/` em uma das quatro peças, cliente ou servidor, e que nomeie qualquer código que faça o trabalho de outra peça.
O que ele encontrar é candidato para a sua fila, não uma correção agora.

### Exercício 15.2

Uma regra nova: um cliente pode ter no máximo dois agendamentos futuros.
Pergunte ao agente que arquivos mudam e quais não, onde o servidor impõe a regra e onde o cliente a usa para decidir o que mostrar.
Nada é construído.

### Exercício 15.3

A página inicial ganha uma linha de ajuda, "Keep your booking code to cancel" (guarde o seu código de agendamento para cancelar), escrita uma vez em `strings.ts` e nunca editada pelo dono.
Pergunte ao agente de quais das quatro peças isso precisa, e por que cada uma das outras não se paga.
Nada é construído.

[^book-adr-0016]: J.C. Ködel, "One Page at a Time", o ADR-0016 deste livro, `docs/adr/ADR-0016-the-books-definition-of-focus.md`, de 2026-09-28, emendado em 2026-09-29 e 2026-09-30, na pasta de ADRs em `main`. <https://github.com/JCKodel/focus-kit-book/tree/main/docs/adr>
[^bloc]: Bloc, "Bloc State Management Library", documentação, acesso em 2026-09-29. <https://bloclibrary.dev/>
[^mediatr]: Jimmy Bogard, "MediatR: Simple, unambitious mediator implementation in .NET", acesso em 2026-09-29. <https://github.com/jbogard/MediatR>
[^clean-architecture]: Robert C. Martin, "The Clean Architecture", 2012. <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[^clinic-orchestrator-tests-run]: A construção dos testes dos orquestradores do projeto guiado deste livro, 2026-09-29, com o Claude Code 2.1.284 e o modelo `claude-opus-5-5`: cada turno, e a saída do `npm run verify` no commit `e6653b5` da clínica em `verify.txt`. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/clinic-orchestrator-tests-run/README.md>
