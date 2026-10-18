# 5. Um teste para cada peça

Depois deste capítulo você consegue dizer que teste guarda cada uma das quatro peças e o que ele troca, só o I/O e o que muda entre execuções, e seguir uma regra pelos testes dela.
Você também consegue escrever uma implementação falsa que faz o teste falhar quando é chamada sem ser esperada, e dar nomes aos testes para que um revisor os leia como as frases da regra.
Você consegue manter rápidos os testes que toda entrega roda, e dizer onde rodam os lentos.
E você sabe por que um teste que um agente escreveu só merece confiança verde depois de ter sido visto vermelho.

## O problema

O motivo para ter poucos testes era o custo de escrevê-los, e um agente escreve um em segundos, então esse motivo acabou.
O risco passou para o outro lado: um agente escreve testes com tanta facilidade que escreve demais, o mesmo caso de cinco jeitos, até a suíte levar minutos e ninguém rodá-la antes de dizer "pronto".
Um agente também não se importa com quanto tempo um teste leva para rodar, e quando toda entrega roda os testes, um teste lento faz toda entrega esperar.
Eu já vi agentes escreverem testes que levavam 20 minutos para rodar: 20 minutos em toda entrega.
Pergunte a um teste o que o capítulo 3 pergunta a qualquer passo: que regra quebrada ele pegaria que nenhum outro teste pega?

Um teste que precisa da aplicação inteira rodando, um servidor de pé, um banco populado, um navegador aberto, também leva minutos para começar, e quebra por motivos que nada têm a ver com o código que ele confere.
Então ele também fica sem rodar, e uma regra que mudou semana passada é encontrada quebrada por um usuário.
As quatro peças do [capítulo 4](04-focus.md) têm uma forma que deixa testar cada uma sozinha, no tempo de salvar um arquivo.

## Um teste para cada peça

Um teste unitário chama uma peça diretamente, no processo do executor de testes, sem servidor e sem navegador; ele roda o código real que essa peça chama, exceto o I/O e o relógio.
Um teste ponta a ponta conduz a aplicação rodando pela tela dela, como um usuário faria, pela rede até um servidor e um banco reais.
Em TypeScript, o Vitest roda testes unitários no Node,[^vitest] e o Playwright conduz um navegador real para os testes ponta a ponta.[^playwright]

| Peça | O teste dela | O que ele troca |
|---|---|---|
| Caso de uso | chamado com dados; sem preparação | nada: ele não tem I/O, e a data chega como valor |
| Repositório | contra um banco em memória com as migrações reais do projeto | o arquivo do banco, pela mesma engine de banco de dados em memória |
| Orquestrador | com repositórios falsos que respondem o que o teste define e lançam em qualquer chamada que o teste não esperava | os repositórios |
| Tela | um teste ponta a ponta em um navegador; poucos, um por cenário que o usuário vê | nada |

A maioria dos testes é dos três primeiros tipos, e eles rodam em segundos.
Testes ponta a ponta são poucos porque cada um é lento e falha por muitos motivos; Mike Cohn desenhou essa forma como uma pirâmide, muitos testes unitários na base e poucos testes ponta a ponta no topo,[^cohn] e o guia de Ham Vocke no site de Martin Fowler a ensina com código.[^vocke-pyramid]

Manter os testes em ordem, incluindo quanto tempo eles levam, é trabalho seu; o agente não faz isso se você não pedir.
É mais um motivo para manter uma regra em um caso de uso puro: o teste dele é uma chamada com dados, o teste mais rápido do projeto.
Testes ponta a ponta, e qualquer teste que precise da aplicação ou de uma rede, só são escritos onde provam algo que os rápidos não conseguem.
O que toda entrega roda é o comando de verificação do projeto, o comando que precisa passar antes de uma entrega ser dada como pronta, e você decide o que ele roda.
Um teste lento pode ficar fora dele e rodar em outro comando, que você mesmo roda, por exemplo antes de um marco fechar.
Um marco é um grupo de entregas com um parágrafo que diz o que é verdade quando ele fecha.

## O que é uma implementação falsa

Gerard Meszaros chamou de "test doubles" (dublês de teste) os objetos que um teste põe no lugar dos reais, por causa do dublê de um filme, no livro *xUnit Test Patterns* (2007).[^meszaros]
Nos nomes dele, um banco em memória, uma implementação que funciona e pega um atalho, é um *fake*, e um repositório que responde o que o teste define é um *stub*.
Este livro chama os dois de implementações falsas, porque os dois trocam o I/O por uma segunda implementação que responde, e nenhum deles afirma como o código testado foi escrito.

Um mock afirma isso: ele confere as chamadas que mandaram ele esperar.
Um teste que espera que `buscarMembro` seja chamado uma vez com `"m1"`, depois `buscarExemplar` com `"e1"`, repete o código do orquestrador linha por linha, e falha quando você troca a ordem de duas chamadas sem mudar nada que o usuário vê.
Martin Fowler descreve esse custo na seção "Coupling Tests to Implementations" do artigo "Mocks Aren't Stubs".[^fowler-mocks]
Uma implementação falsa deixa o teste conferir o que importa, o estado que sai, e deixa o código livre para mudar por dentro.

## Troque só o I/O e o que muda entre execuções

As quatro peças decidem o que um teste pode trocar.
Só um repositório faz I/O, e só o orquestrador recebe repositórios, então o teste do orquestrador troca os repositórios e o teste do repositório troca o arquivo do banco.
Nada mais é trocado: um caso de uso nunca é trocado, porque ele é puro e rápido, e um teste que o troca por uma implementação falsa não testa nada.

O relógio também é I/O: `new Date()` responde algo diferente a cada chamada.
Na biblioteca, ele é lido uma vez, onde a requisição chega, e repassado como valor, `hoje`, então um teste passa `"2026-10-01"` e não precisa de relógio falso nenhum.

Um valor aleatório de `Math.random()`, um id novo e um valor lido do ambiente também respondem diferente de uma execução para outra, então cada um é I/O no mesmo sentido.
Cada um é lido uma vez e repassado como valor, como `hoje`, então o teste passa o valor que quer e não precisa de implementação falsa.
Se `emprestar` desse a cada empréstimo um id novo com `crypto.randomUUID()`, o teste dele não conseguiria dizer que empréstimo espera; o id é criado onde a requisição chega, ou pelo banco quando ele salva o empréstimo.
Um valor do ambiente, como uma variável, o fuso horário ou o idioma da máquina, é lido uma vez onde o programa começa, então um teste não responde diferente em outra máquina.

Não há nada para trocar na ordem de um conjunto.
Os empréstimos de um membro lidos sem `ORDER BY` voltam em qualquer ordem em que o banco os encontre, então um teste que os espera na ordem em que foram salvos pode passar hoje e falhar depois que os dados ou um índice mudam.
A consulta declara a ordem que promete, ou o teste compara os empréstimos sem ordem.

Um teste cuja resposta depende de qualquer um desses passa hoje e falha amanhã, ou em outra máquina, com o mesmo código, e então um teste vermelho deixa de dizer que uma regra quebrou.

## Uma regra pelos testes dela

A regra: um membro com um livro atrasado não pode pegar outro emprestado.
Ela mora no caso de uso `emprestar` do [capítulo 4](04-focus.md), e cada peça que ela atravessa tem um teste.

O desenvolvimento guiado por testes de Kent Beck escreve o teste antes do código, em um ciclo de três passos: vermelho, o teste falha porque o código ainda não existe; verde, o menor código que o faz passar; depois a limpeza, com o teste ainda verde.[^beck-tdd]
Uma regra pura é o lugar mais fácil de fazer isso, porque o teste dela é uma chamada com dados: rode o primeiro teste abaixo antes de `emprestar` existir e ele está vermelho, escreva `emprestar` e ele está verde.
A página de uma entrega lista os seus comportamentos (capítulo 12), cada um vira um teste vermelho, e a entrega está pronta quando todos eles estão verdes e nada que estava verde ficou vermelho.

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
Essa é a única parte do empréstimo que só o banco consegue garantir, já que dois bibliotecários podem apertar "Emprestar" no mesmo instante, e ela é testada contra a engine de banco de dados real e o esquema real.

**O orquestrador.** `eventosDeEmprestimo.test.ts` passa repositórios falsos a `emprestimoPedido`, o orquestrador do [capítulo 4](04-focus.md):

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
Este teste não define `inserirEmprestimo`, então, se o orquestrador tentasse salvar um empréstimo para um membro com um livro atrasado, o repositório falso lançaria e o teste falharia.
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

## O que os testes provam, e o que não provam

Vermelho e verde, o ciclo de "Uma regra pelos testes dela" acima, são como o teste de um agente ganha confiança.
Um teste visto vermelho antes de o código existir, e verde depois, provou que consegue falhar.
Um teste escrito depois do código, pelo agente que escreveu o código, pode afirmar o que o código faz no lugar do que a regra diz, e passar para sempre.

Uma suíte verde ainda não prova que o software funciona.
Um teste pode estar errado e passar.
Os testes unitários conferem cada peça sozinha, e a soma das peças pode falhar onde nenhuma peça falha: um campo que o cliente envia com um nome e o servidor lê com outro passa em todos os testes unitários dos dois lados.
Esse é o trabalho dos poucos testes ponta a ponta, e o motivo de uma entrega levar também uma prova, o resultado visto funcionando, antes que alguém a chame de pronta ([capítulo 13](13-apply.md)).

## O que o time ganha

Toda peça tem um teste que roda sem a aplicação, e cada teste pega uma regra quebrada que nenhum outro pega, então a suíte roda em segundos e um agente a roda a cada mudança, não só antes de dizer "pronto".
Um agente que muda `emprestar` descobre pelo nome do teste que falha qual frase da regra ele quebrou, antes de rodar a verificação inteira.
Como cada teste foi visto vermelho primeiro, "pronto" é a saída do executor de testes e não a opinião do agente.
E um revisor confere uma entrega lendo nomes de teste, que dizem, antes de qualquer código, em que casos o agente pensou e em quais não.

## Pontos-chave

* Um caso de uso é testado só com dados, um repositório contra um banco em memória com as migrações reais, um orquestrador com repositórios falsos, e a tela com poucos testes ponta a ponta em um navegador, então o que toda entrega roda continua rápido.
* Um teste troca só o I/O e o que muda entre execuções, que ele passa como valor, e espera uma ordem só onde a consulta fixa uma, então a maioria dos testes não troca nada além dos repositórios.
* Uma implementação falsa responde o que o teste define e lança em qualquer chamada que o teste não esperava; prefira-a a um mock, que repete o código que testa.
* Cada nível de teste prova o que os outros não provam, e uma suíte verde ainda prova menos que software funcionando: um teste pode estar errado, e as peças podem falhar juntas, então veja um teste vermelho antes de confiar nele verde.
* O nome de um teste é uma frase da regra: um revisor lê os nomes, e uma regra sem frase não tem teste.

[^vitest]: Vitest, "Getting Started", documentação, acesso em 2026-09-29. <https://vitest.dev/guide/>
[^playwright]: Playwright, "Installation", documentação, acesso em 2026-09-29. <https://playwright.dev/docs/intro>
[^vocke-pyramid]: Ham Vocke, "The Practical Test Pyramid", martinfowler.com, 2018. <https://martinfowler.com/articles/practical-test-pyramid.html>
[^meszaros]: Gerard Meszaros, "xUnit Test Patterns: Refactoring Test Code", Addison-Wesley, 2007.
[^fowler-mocks]: Martin Fowler, "Mocks Aren't Stubs", 2007. <https://martinfowler.com/articles/mocksArentStubs.html>
[^beck-tdd]: Kent Beck, "Test-Driven Development: By Example", Addison-Wesley, 2002.
[^cohn]: Mike Cohn, "Succeeding with Agile: Software Development Using Scrum", Addison-Wesley, 2009.
