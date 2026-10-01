# 8. Um teste para cada peça

Depois deste capítulo você consegue dizer que teste guarda cada uma das quatro peças e o que ele troca, só o I/O e o relógio, e seguir uma regra pelos testes dela.
Você também consegue escrever um fake (uma implementação falsa) que faz o teste falhar quando é chamado sem ser esperado, e dar nomes aos testes para que um revisor os leia como as frases da regra.

## O problema

Um teste que precisa da aplicação inteira rodando, um servidor de pé, um banco populado, um navegador aberto, leva minutos para começar e quebra por motivos que nada têm a ver com o código que ele confere.
Então ninguém o roda antes de dizer "pronto", e uma regra que mudou semana passada é encontrada quebrada por um usuário.
As quatro peças do [capítulo 7](07-four-pieces.md) têm uma forma que deixa testar cada uma sozinha, no tempo de salvar um arquivo.

## Um teste para cada peça

Um teste unitário chama uma peça diretamente, no processo do executor de testes, sem servidor e sem navegador; ele roda o código real que essa peça chama, exceto o I/O e o relógio.
Um teste ponta a ponta conduz a aplicação rodando pela tela dela, como um usuário faria, pela rede até um servidor e um banco reais.
Em TypeScript, o Vitest roda testes unitários no Node,[^vitest] e o Playwright conduz um navegador real para os testes ponta a ponta.[^playwright]

| Peça | O teste dela | O que ele troca |
|---|---|---|
| Caso de uso | chamado com dados; sem preparação | nada: ele não tem I/O, e a data chega como valor |
| Repositório | contra um banco em memória com as migrações reais do projeto | o arquivo do banco, pelo mesmo motor em memória |
| Orquestrador | com repositórios falsos que respondem o que o teste define e lançam em qualquer chamada que o teste não esperava | os repositórios |
| Tela | um teste ponta a ponta em um navegador; poucos, um por cenário que o usuário vê | nada |

A maioria dos testes é dos três primeiros tipos, e eles rodam em segundos.
Testes ponta a ponta são poucos porque cada um é lento e falha por muitos motivos; Mike Cohn desenhou essa forma como uma pirâmide, muitos testes unitários na base e poucos testes ponta a ponta no topo,[^cohn] e o guia de Ham Vocke no site de Martin Fowler a ensina com código.[^vocke-pyramid]

## O que é um fake

Gerard Meszaros chamou de "test doubles" (dublês de teste) os objetos que um teste põe no lugar dos reais, por causa do dublê de um filme, no livro *xUnit Test Patterns* (2007).[^meszaros]
Martin Fowler resumiu os tipos: um stub responde o que o teste definiu, um mock confere as chamadas que mandaram ele esperar, e um fake tem uma implementação que funciona e pega um atalho, como um banco em memória.[^fowler-mocks]

Nos nomes de Meszaros, o banco em memória é um fake e um repositório que responde o que o teste define é um stub.
Este livro chama os dois de fakes, porque os dois trocam o I/O por uma segunda implementação que responde, e nenhum deles afirma como o código testado foi escrito.

Um mock afirma isso.
Um teste que espera que `buscarMembro` seja chamado uma vez com `"m1"`, depois `buscarExemplar` com `"e1"`, repete o código do orquestrador linha por linha, e falha quando você troca a ordem de duas chamadas sem mudar nada que o usuário vê.
Fowler descreve o mesmo custo na seção "Coupling Tests to Implementations" do mesmo artigo.[^fowler-mocks]
Um fake deixa o teste conferir o que importa, o estado que sai, e deixa o código livre para mudar por dentro.

## Troque só o I/O e o relógio

As quatro peças decidem o que um teste pode trocar.
Só um repositório faz I/O, e só o orquestrador recebe repositórios, então o teste do orquestrador troca os repositórios e o teste do repositório troca o arquivo do banco.
Nada mais é trocado: um caso de uso nunca é falso, porque ele é puro e rápido, e um teste que o troca por um fake não testa nada.

O relógio também é I/O: `new Date()` responde algo diferente a cada chamada.
Na biblioteca, ele é lido uma vez, onde a requisição chega, e repassado como valor, `hoje`, então um teste passa `"2026-10-01"` e não precisa de relógio falso nenhum.

## Uma regra pelos testes dela

A regra: um membro com um livro atrasado não pode pegar outro emprestado.
Ela mora no caso de uso `emprestar` do [capítulo 5](05-rules-and-exceptions.md), e cada peça que ela atravessa tem um teste.

**O caso de uso.** `regras.test.ts` chama `emprestar` com dados:

```ts
describe("emprestar", () => {
	const exemplar = { id: "e1", livroId: "l1" };
	const membro = { id: "m1", emAtraso: 0, suspenso: false };

	it("recusa um membro com um livro atrasado", () => {
		const resultado = emprestar(exemplar, { ...membro, emAtraso: 1 }, "2026-10-01");
		expect(resultado).toEqual({ ok: false, error: "TemLivrosEmAtraso" });
	});

	it("empresta por 21 dias a um membro sem nada atrasado", () => {
		const resultado = emprestar(exemplar, membro, "2026-10-01");
		expect(resultado.ok && resultado.value.devolverEm).toBe("2026-10-22");
	});
});
```

Sem banco, sem servidor, sem mock: o membro é um objeto, a data é uma string, e a resposta é um valor.

**O repositório.** `repositorio.server.test.ts` abre o SQLite em memória, roda os mesmos arquivos de migração que a aplicação roda, e chama `inserirEmprestimo` duas vezes para o mesmo exemplar.
A primeira chamada devolve o empréstimo; a segunda devolve a recusa `JaEmprestado`, porque o índice único a recusou.
Essa é a única parte do empréstimo que só o banco consegue garantir, já que duas bibliotecárias podem apertar "Emprestar" no mesmo instante, e ela é testada contra o motor real e o esquema real.

**O orquestrador.** `eventosDeEmprestimo.test.ts` passa repositórios falsos a `emprestimoPedido`, o orquestrador do [capítulo 7](07-four-pieces.md):

```ts
function naoEsperado(): never {
	throw new Error("não chamado neste teste");
}

function falsos(repositorios: Partial<RepositoriosDeEmprestimo>): RepositoriosDeEmprestimo {
	const nenhum = { buscarMembro: naoEsperado, buscarExemplar: naoEsperado, inserirEmprestimo: naoEsperado };
	return { ...nenhum, ...repositorios };
}

describe("emprestimoPedido", () => {
	it("recusa um membro com um livro atrasado e não salva nada", () => {
		const repositorios = falsos({
			buscarMembro: () => ok({ id: "m1", emAtraso: 1, suspenso: false }),
			buscarExemplar: () => ok({ id: "e1", livroId: "l1" }),
		});
		const estado = emprestimoPedido({ exemplarId: "e1", membroId: "m1" }, "2026-10-01", repositorios);
		expect(estado).toEqual({ tipo: "Recusado", recusa: "TemLivrosEmAtraso" });
	});
});
```

`falsos` preenche só os repositórios que o teste define, e todos os outros lançam.
Este teste não define `inserirEmprestimo`, então, se o orquestrador tentasse salvar um empréstimo para um membro com um livro atrasado, o fake lançaria e o teste falharia.
Ele prova a recusa e que nada foi salvo, e não afirma nenhuma ordem de chamadas.

**A tela.** Um teste ponta a ponta, em um navegador, abre a tela de empréstimo, empresta um exemplar a um membro que tem um livro atrasado, e espera ler "Devolva primeiro os seus livros atrasados."
Ele prova o que nenhum dos outros consegue: que a mensagem chega à tela.

Cada teste prova algo que os outros não provam: o caso de uso, a regra; o repositório, a disputa; o orquestrador, o fluxo; a tela, o que o usuário vê.

## Nomes de teste são frases

O nome de um teste é o que um revisor lê primeiro, então escreva-o como uma frase da regra:

* `emprestar recusa um membro com um livro atrasado`
* `emprestar empresta por 21 dias a um membro sem nada atrasado`
* `inserirEmprestimo recusa um segundo empréstimo aberto do mesmo exemplar`
* `emprestimoPedido recusa um membro com um livro atrasado e não salva nada`
* `a tela de empréstimo diz a um membro com um livro atrasado que o devolva primeiro`

Lidos em sequência, os nomes são as regras do empréstimo, e uma regra que não tem frase entre eles não tem teste.
Nomes como `teste1` ou `emprestar funciona` não dizem nada ao leitor e escondem a regra que falta.
O livro de Kent Beck *Test-Driven Development: By Example* (2002) escreve o teste antes do código, então o teste é a primeira afirmação do que o código tem de fazer; um nome que se lê como frase o mantém uma afirmação que uma pessoa consegue conferir.[^beck-tdd]

## O que os testes provam, e o que não provam

Por anos, o motivo para ter poucos testes foi o custo de escrevê-los.
Um agente escreve um teste em segundos, então esse motivo acabou.
O risco passou para o outro lado: um agente escreve testes com tanta facilidade que escreve demais, o mesmo caso de cinco jeitos, até a suíte levar minutos e ninguém rodá-la antes de dizer "pronto".
Pergunte a um teste o que o capítulo 4 pergunta a qualquer passo: que regra quebrada ele pegaria que nenhum outro teste pega?

Vermelho e verde são como o teste de um agente ganha confiança (o [capítulo 5](05-rules-and-exceptions.md) mostrou o ciclo).
Um teste visto vermelho antes de o código existir, e verde depois, provou que consegue falhar.
Um teste escrito depois do código, pelo agente que escreveu o código, pode afirmar o que o código faz no lugar do que a regra diz, e passar para sempre.

Uma suíte verde ainda não prova que o software funciona.
Um teste pode estar errado e passar.
Os testes unitários conferem cada peça sozinha, e a soma das peças pode falhar onde nenhuma peça falha: um campo que o cliente envia com um nome e o servidor lê com outro passa em todos os testes unitários dos dois lados.
Esse é o trabalho dos poucos testes ponta a ponta, e o motivo de uma entrega levar também uma prova, o resultado visto funcionando, antes que alguém a chame de pronta ([capítulo 15](15-apply.md)).

## O que isso dá a um agente

Um agente que muda `emprestar` roda os testes unitários da fatia e sabe em segundos se quebrou a regra, antes de rodar a verificação inteira do [capítulo 15](15-apply.md).
Ele não precisa subir um servidor nem abrir um navegador para descobrir, então roda os testes a cada mudança, e um teste que falha diz a ele qual frase da regra ele quebrou.
Quando ele acrescenta uma regra, os nomes dos testes que escreveu dizem a você, antes de você ler qualquer código, em que casos ele pensou e em quais não.

## O que o time ganha

Toda peça tem um teste que roda sem a aplicação, então um agente confere o próprio trabalho antes de dizer "pronto", e um revisor confere uma entrega lendo nomes de teste.
Este livro não dá uma contagem de base de quanto mais cedo um time pega uma regra quebrada assim; o ganho é que a conferência existe e roda em segundos.

## Pontos-chave

* Um caso de uso é testado só com dados, um repositório contra um banco em memória com as migrações reais, um orquestrador com repositórios falsos, e a tela com poucos testes ponta a ponta em um navegador.
* Um teste troca só o I/O e o relógio, e o relógio é um valor passado como parâmetro, então a maioria dos testes não troca nada além dos repositórios.
* Um fake responde o que o teste define e lança em qualquer chamada que o teste não esperava; prefira-o a um mock, que repete o código que testa.
* Cada nível de teste prova o que os outros não provam, e uma suíte verde ainda prova menos que software funcionando: um teste pode estar errado, e as peças podem falhar juntas, então veja um teste vermelho antes de confiar nele verde, e guarde a prova.
* O nome de um teste é uma frase da regra: um revisor lê os nomes, e uma regra sem frase não tem teste.

[^vitest]: Vitest, "Getting Started", documentação, acesso em 2026-09-29. <https://vitest.dev/guide/>
[^playwright]: Playwright, "Installation", documentação, acesso em 2026-09-29. <https://playwright.dev/docs/intro>
[^vocke-pyramid]: Ham Vocke, "The Practical Test Pyramid", martinfowler.com, 2018. <https://martinfowler.com/articles/practical-test-pyramid.html>
[^meszaros]: Gerard Meszaros, "xUnit Test Patterns: Refactoring Test Code", Addison-Wesley, 2007.
[^fowler-mocks]: Martin Fowler, "Mocks Aren't Stubs", 2007. <https://martinfowler.com/articles/mocksArentStubs.html>
[^beck-tdd]: Kent Beck, "Test-Driven Development: By Example", Addison-Wesley, 2002.
[^cohn]: Mike Cohn, "Succeeding with Agile: Software Development Using Scrum", Addison-Wesley, 2009.
