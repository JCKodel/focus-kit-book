# Features, não camadas

Depois deste capítulo você consegue organizar o código em fatias verticais, uma pasta por feature, decidir o que é uma feature e onde fica o código que duas features compartilham.
Você também consegue decidir qual peça recebe uma dependência como parâmetro e qual não recebe nenhuma, por um teste só: o teste dela passa uma segunda implementação?

## O problema

Muitos projetos separam o código por camada técnica: uma pasta de telas, uma de controllers, uma de services, uma de models, uma de acesso ao banco de dados.
Cada feature fica espalhada por todas elas.
Emprestar um livro em uma biblioteca assim mexe em um arquivo em `views/`, `controllers/`, `services/`, `models/` e `repositories/`, e uma mudança em como o empréstimo funciona é uma mudança em cinco pastas.

O custo cai sobre quem faz a mudança.
Uma pessoa precisa encontrar os cinco arquivos e guardá-los na cabeça ao mesmo tempo; um agente precisa abrir as cinco pastas para aprender o que o empréstimo faz, e cada arquivo que ele carrega para entender a mudança enche o contexto em que ele trabalha (capítulo 2).
As pastas dizem de que o código é feito, e nada sobre o que o programa faz.

## Camadas, e para que serviam

As camadas respondiam a um problema real: regras misturadas com telas e SQL não podem ser mudadas, nem testadas, umas sem as outras.
Robert C. Martin desenhou a resposta em 2012 como círculos concêntricos, com as regras de negócio no centro e o banco de dados, a web e os frameworks na borda, unidos por uma regra, a regra de dependência: "*dependências de código-fonte só podem apontar para dentro*".[^martin-clean-2012]
Uma regra nunca nomeia uma tela, uma tabela ou uma biblioteca, então o lado de fora pode mudar sem tocá-la.
Ele desenvolveu a ideia no livro *Clean Architecture* em 2017.[^martin-clean-2017]

Alistair Cockburn tinha desenhado a mesma fronteira em 2005 como um hexágono, o padrão que ele chamou de portas e adaptadores, cuja intenção é "*permitir que uma aplicação seja conduzida igualmente por usuários, programas, testes automatizados ou scripts em lote, e seja desenvolvida e testada isolada dos dispositivos e bancos de dados que vai usar ao rodar*".[^cockburn-hexagonal]
E o próprio Martin perguntou, em 2011, o que as pastas de primeiro nível de um projeto gritam: o sistema, uma biblioteca ou um sistema de saúde, ou o framework com que ele foi construído.[^martin-screaming]
Um projeto cujas pastas são `controllers/` e `models/` grita o seu framework.

Este livro mantém a regra de dependência: uma regra não importa nada de uma tela, de um banco de dados ou de uma biblioteca.
Ele abandona a pasta por camada, e com ela a cerimônia de uma interface e de um mapeamento em cada fronteira para código que tem uma implementação só.

## Fatias verticais

Uma fatia vertical é uma pasta que guarda tudo de que uma feature precisa: as telas, as chamadas ao servidor, as rotas, as regras, o acesso ao banco de dados e os testes.
Jimmy Bogard deu nome ao estilo em 2018 depois de anos construindo sistemas assim, e deu a regra dele em uma linha: "*Minimize o acoplamento entre as fatias, e maximize o acoplamento dentro de uma fatia.*"[^bogard-vertical-slice]
Código que muda junto mora junto; código que muda por razões diferentes mora separado.

A biblioteca de empréstimos, o exemplo da Parte I, fica organizada assim:

```text
src/features/loans/          LendView.tsx, lendEvents.ts, rules.ts,
                             repository.server.ts, route.server.ts,
                             rules.test.ts, lendEvents.test.ts,
                             repository.server.test.ts
src/features/loans/return/   returning a copy
src/features/members/        what the library keeps about a member
src/features/catalog/        books and copies
src/lib/result.ts            Result, ok and err
```

`LendView.tsx` é a tela de empréstimo; `lendEvents.ts` recebe o que a tela pede e responde com o novo estado; `rules.ts` guarda as regras do capítulo 5, como `lend`; `repository.server.ts` lê e escreve no banco de dados, e `route.server.ts` é o endereço do empréstimo no servidor.
Um nome terminado em `.server.ts` roda só no servidor, e o código do cliente nunca importa um deles.
Os testes ficam ao lado do código que testam.
O capítulo 7 chama esses quatro tipos de arquivo de as quatro peças, e o capítulo 8 dá a cada uma o seu teste.

A pasta de cima grita a biblioteca: empréstimos, membros, catálogo.
Uma mudança em como o empréstimo funciona mexe em `loans/`, e tirar os empréstimos do produto tira uma pasta.
O critério de Parnas de 1972 (capítulo 4) funciona também neste tamanho: a fatia esconde as decisões da sua feature do resto do programa.

## O que é uma feature

Uma feature é uma coisa que o app guarda, nomeada por um termo do vocabulário do projeto (o empréstimo, o membro, o livro), ou uma coisa que o app faz sem guardar nada, nomeada pelo que faz, como uma verificação de `status` que responde se o serviço está no ar.
A fatia dela guarda toda ação sobre ela.
Emprestar e devolver agem os dois sobre o empréstimo: compartilham as regras, a tabela e o repositório dele, então são uma fatia só.
Membros e livros são outras coisas que a biblioteca guarda, cada uma com a sua tabela e as suas telas, então cada uma tem uma fatia própria.

Uma subfeature é uma subpasta.
Devolver um exemplar tem a sua tela e o seu evento, e mora em `loans/return/`, dentro da fatia cujo empréstimo ela encerra.

Um arquivo aparece em uma fatia quando se paga.
Uma feature sem regra não tem `rules.ts`, e uma feature que não guarda nada não tem repositório.
Não guardar nada não a torna menos feature: se ela tem a sua própria rota ou tela, tem a sua própria fatia.

## Onde mora o código compartilhado

O assunto do código decide onde ele mora quando duas features o usam.
Código sobre uma feature fica na fatia dessa feature, e outra fatia importa de lá o que precisa, seja um tipo, uma função de repositório ou uma tela.
`loans/rules.ts` importa o tipo `Member` de `members/`, porque um membro é o que aquela fatia guarda; a página de um membro que lista os empréstimos dele importa de `loans/`.
Duas fatias podem importar uma da outra.

O que não pertence a nenhuma feature, a forma de um valor como um endereço de email, ou encanamento como `Result`, sai das fatias para `src/lib/`.
Ele vai para lá no segundo uso e não antes, a regra do capítulo 4, e o arquivo diz onde estão o primeiro e o segundo uso.

## Dependências só onde existe um fake

Uma dependência é algo de que um trecho de código precisa, de fora dele, para rodar: o banco de dados, a rede, o relógio, outro módulo.
Martin Fowler deu nome à prática de entregá-la de fora em 2004: depois de longa discussão, escreveu, "*nos decidimos pelo nome Injeção de Dependência*".[^fowler-injection]
Mark Seemann acrescentou onde as partes reais são montadas: em um lugar, "*o mais perto possível do ponto de entrada da aplicação*", que ele chamou de composition root (raiz de composição).[^seemann-composition-root]

Injetadas em toda parte, as dependências viram a sua própria camada de cerimônia: uma interface para cada classe, um contêiner, um parâmetro que ninguém varia.
Este livro traça uma linha mais estreita: uma peça recebe uma dependência como parâmetro só onde o teste dela passa uma segunda implementação.
Essa segunda implementação é um fake (um falso): um repositório que responde o que o teste define, ou um banco de dados em memória com as tabelas reais.

O orquestrador da fatia de empréstimos recebe os seus repositórios:

```ts
export const lendRepositories = { findMember, findCopy, insertLoan };

export async function lendRequested(
	event: LendRequested,
	today: string,
	repositories = lendRepositories,
): Promise<LendState> {
	const member = await repositories.findMember(event.memberId);
	if (!member.ok) return { kind: "Failed", exception: member.error };
	const copy = await repositories.findCopy(event.copyId);
	if (!copy.ok) return { kind: "Failed", exception: copy.error };
	const loan = lend(copy.value, member.value, today);
	if (!loan.ok) return { kind: "Refused", refusal: loan.error };
	const saved = await repositories.insertLoan(loan.value);
	if (saved.ok) return { kind: "Lent", loan: saved.value };
	if (saved.error === "AlreadyLent") return { kind: "Refused", refusal: "AlreadyLent" };
	return { kind: "Failed", exception: saved.error };
}
```

A tela chama `lendRequested(event, today)` e recebe os repositórios reais por padrão; o teste passa fakes no lugar deles.
O resto segue do mesmo teste.

* **Um orquestrador recebe os seus repositórios**, porque o teste dele passa repositórios falsos.
* **Um repositório do servidor recebe o banco de dados que usa**, `findMember(db, id)`, porque o teste dele passa um banco de dados em memória com as migrações reais; o código de início do servidor abre o banco real e o repassa, e essa é a raiz de composição.
* **Um caso de uso não recebe nenhuma.** `lend` recebe dados e devolve um valor; o teste dele passa dados, e não há nada para trocar.
* **Uma tela não recebe nenhuma.** Ela tem uma implementação só, e um parâmetro ali existiria por cerimônia, o que o KISS descarta (capítulo 4).
* **O relógio é passado como valor.** `today` é lido uma vez, onde o evento chega, e repassado como dado; nenhuma regra lê o relógio, então o teste de uma data de devolução passa a data que quiser.

## O que isso dá a um agente

Uma entrega sobre empréstimo nomeia uma fatia, e o agente lê essa pasta: a tela, o evento, as regras, o acesso ao banco de dados e os testes deles, lado a lado.
Ele não procura em cinco camadas as partes de uma feature, e o que ele carrega no contexto é aquilo de que a mudança trata.
As dependências que ele encontra são as que um teste troca, então os testes mostram a ele o que fingir e nada mais.

## O que o time ganha

Uma mudança mexe em uma pasta, e um agente lê uma fatia.
Quem revisa vê o diff de uma entrega dentro de uma pasta e sabe que ela não mexeu em mais nada, e remover uma feature é remover uma pasta.
O livro não tem uma medida de base para isso contra uma organização em camadas; ele o afirma como uma descrição da estrutura, e cada leitor pode conferir na próxima mudança no seu próprio código.

## Pontos-chave

* Pastas por camada espalham uma feature por cinco lugares; uma fatia vertical guarda tudo de que uma feature precisa em uma pasta.
* A regra de dependência fica: uma regra não importa nada de uma tela, de um banco de dados ou de uma biblioteca.
* Uma feature é uma coisa que o app guarda, nomeada pelo vocabulário, ou uma coisa que ele faz sem guardar nada; uma subfeature é uma subpasta.
* Código compartilhado fica na fatia de que trata e é importado de lá; código que não pertence a nenhuma feature vai para `lib/` no segundo uso.
* Uma peça recebe uma dependência só onde o teste dela passa um fake: orquestradores e repositórios do servidor recebem, casos de uso e telas não, e o relógio é um valor.

[^martin-clean-2012]: Robert C. Martin, "The Clean Architecture", The Clean Code Blog, 2012-08-13, acesso em 2026-09-30. <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[^martin-clean-2017]: Robert C. Martin, "Clean Architecture: A Craftsman's Guide to Software Structure and Design", Prentice Hall, 2017.
[^cockburn-hexagonal]: Alistair Cockburn, "Hexagonal Architecture", 2005, acesso em 2026-09-30. <https://alistair.cockburn.us/hexagonal-architecture/>
[^martin-screaming]: Robert C. Martin, "Screaming Architecture", The Clean Code Blog, 2011-09-30, acesso em 2026-09-30. <https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html>
[^bogard-vertical-slice]: Jimmy Bogard, "Vertical Slice Architecture", 2018, acesso em 2026-09-30. <https://www.jimmybogard.com/vertical-slice-architecture/>
[^fowler-injection]: Martin Fowler, "Inversion of Control Containers and the Dependency Injection pattern", martinfowler.com, 2004, acesso em 2026-09-30. <https://martinfowler.com/articles/injection.html>
[^seemann-composition-root]: Mark Seemann, "Composition Root", 2011-07-28, acesso em 2026-09-30. <https://blog.ploeh.dk/2011/07/28/CompositionRoot/>
