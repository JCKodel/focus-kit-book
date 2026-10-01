# FOCUS: as quatro peças

Depois deste capítulo você consegue pôr qualquer arquivo de uma feature em uma de quatro peças, tela, orquestrador, caso de uso ou repositório, e seguir um evento por elas até um novo estado.
Você também consegue dizer o que cada letra de FOCUS significa, o que ela corrige na Clean Architecture e quando uma peça não vale ser escrita.

## O problema

Na maioria das aplicações, uma regra de negócio mora onde alguém precisou dela primeiro: uma parte em uma tela que esconde um botão, outra no handler que salva o formulário, e uma cópia em uma consulta.
Pergunte "o que acontece quando uma bibliotecária empresta este exemplar a este membro?" e ninguém consegue responder lendo um lugar só.
Você descobre rodando o app, clicando e olhando o banco.
Uma pessoa não consegue testar essa resposta sem o app inteiro, e um agente a quem se pede para mudar a regra encontra duas das três cópias e muda essas duas.

FOCUS é o nome que este livro dá a um jeito de dar a essa pergunta uma resposta única: quatro peças, cada uma com um trabalho, e uma direção para tudo o que passa entre elas.

## A sigla, letra por letra

**F, Feature-oriented (orientado a features).** O código é organizado em fatias verticais: uma pasta guarda tudo o que uma feature precisa, e não há pasta por tecnologia, nem `controllers/` nem `services/` (o [capítulo 6](06-features-not-layers.md) ensina as fatias).
As quatro peças de uma feature moram na pasta dela, lado a lado.

**C, Clean (limpo).** As peças são as camadas da Clean Architecture de Robert C. Martin, cuja regra de dependência diz que o código pode apontar para dentro, para as regras, e nunca para fora, para uma tela ou um banco.[^clean-architecture]
O FOCUS mantém essa regra com uma correção.
No desenho de Martin, um caso de uso fala com o armazenamento por uma interface que recebe, então uma regra ainda consegue chegar ao I/O, só que por uma porta com outro nome.
No FOCUS, um caso de uso não recebe repositório nenhum: ele é uma função pura ([capítulo 5](05-rules-and-exceptions.md)), dados entram, um `Result` sai.
O orquestrador é a peça que pede dados aos repositórios e pede a eles que salvem, e ele recebe os repositórios como parâmetro, porque o teste dele passa fakes (implementações falsas) no lugar deles.
O capítulo 6 dá a regra por trás dessa escolha: uma peça recebe uma dependência só onde o teste dela passa uma segunda implementação.

**U, Unidirectional (unidirecional).** Tudo flui em um sentido: um evento, o orquestrador, os casos de uso e repositórios que ele chama, e um novo estado.
Não há binding, o mecanismo que alguns frameworks oferecem em que um campo na tela e um valor na memória atualizam um ao outro nos dois sentidos.
Nenhum estado volta: a tela nunca muda o estado que renderiza, e um caso de uso nunca chama um repositório.
Então "o que acontece quando o evento X chega?" tem uma resposta, e um teste consegue conferi-la.

**S, Scalable (escalável).** Toda peça é isolada e tem o próprio teste, então uma feature nova acrescenta a própria pasta e os próprios testes e não muda nenhuma outra, e a aplicação se sustenta em qualquer tamanho.

## As quatro peças

| Peça | Faz | Proíbe |
|---|---|---|
| Tela | dispara eventos, renderiza o estado que recebe | regras de negócio, acesso a dados |
| Orquestrador | transforma um evento em um novo estado: valida a entrada, busca pelos repositórios, aplica as regras pelos casos de uso, pede aos repositórios que salvem, publica o estado | decidir uma regra, persistir |
| Caso de uso | o único lugar de uma regra de negócio; puro: dados entram, `Result` sai | I/O, o framework, exceções |
| Repositório | busca e salva; o único lugar em que uma exceção vinda dos dados vira um `Result` | regras de negócio |

Leia primeiro a coluna "Proíbe": ela mantém cada peça no seu trabalho.
Uma tela que decide quem pode pegar emprestado, ou um repositório que decide isso, quebra a tabela, faça o que fizer de certo.

Um evento é o que aconteceu: um toque em "Emprestar", ou uma requisição chegando a um servidor.
Um estado é o que o orquestrador publica depois dele, inteiro: em uma tela, o que a tela renderiza; em um servidor, a resposta à requisição.
Um repositório chega ao banco por um driver, a biblioteca que fala com o motor, como um cliente de banco ou um ORM; o projeto raramente escreve um.

## Um evento, um novo estado

Uma bibliotecária empresta um exemplar a um membro.
O toque em "Emprestar" é o evento, e a tela que mostra o empréstimo, ou o motivo da recusa, é o novo estado.
Estes são os passos entre os dois.

1. **A tela dispara o evento.**
   A tela de empréstimo envia `EmprestimoPedido { exemplarId, membroId }` e não faz mais nada.
2. **O orquestrador o recebe.**
   Ele confere que o evento traz os dois ids; em um servidor o evento é a requisição, então ler o corpo dela faz parte de recebê-lo.
3. **Os repositórios buscam.**
   O orquestrador pede o membro a `buscarMembro` e o exemplar a `buscarExemplar`.
4. **O caso de uso decide.**
   O orquestrador entrega os dois a `emprestar`, a função pura que devolve um `Emprestimo` com vencimento 21 dias depois, ou a recusa `TemLivrosEmAtraso` ou `MembroSuspenso`.
5. **O repositório salva.**
   O orquestrador pede a `inserirEmprestimo` que salve o empréstimo; um índice único sobre o exemplar recusa um segundo empréstimo aberto, e o repositório transforma essa falha na recusa `JaEmprestado`, como o [capítulo 5](05-rules-and-exceptions.md) mostrou.
6. **O orquestrador publica o novo estado.**
   `Emprestado` com o empréstimo, `Recusado` com a recusa, ou `Falhou` com a exceção, e a tela o renderiza: a data de vencimento, "Devolva primeiro os seus livros atrasados.", ou "Não foi possível acessar o banco da biblioteca. Tente de novo."

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
`hoje` chega como valor: o código que recebe a requisição lê o relógio uma vez e o repassa, então nem `emprestimoPedido` nem `emprestar` o leem, e um teste passa a data que quiser.
`repositorios` chega como parâmetro: o servidor passa os reais, ligados ao banco dele, e um teste passa fakes ([capítulo 8](08-testing-each-piece.md)).
O fluxo nunca volta: `emprestar` nunca vê um repositório, e a tela nunca vê nada além do estado.

## O orquestrador em outros lugares

O orquestrador tem outros nomes em outras stacks, e o trabalho é o mesmo.
No Flutter ele é um BLoC, uma classe que recebe eventos e emite estados;[^bloc] no .NET ele é o padrão Mediator, como na biblioteca MediatR de Jimmy Bogard, em que cada requisição vai para um handler;[^mediatr] em um servidor ele é o handler da rota que recebe a requisição e devolve a resposta; em um cliente React ele é um hook que guarda o estado e executa o evento.
Em um cliente os repositórios chegam à rede, então o orquestrador espera por eles com `await`; nada mais nele muda.

Uma feature muitas vezes tem os dois: um orquestrador no cliente para a tela e um no servidor para a requisição, cada um com os próprios repositórios.
Eles compartilham os mesmos casos de uso.
O servidor impõe `emprestar`, e o cliente importa `podePegarEmprestado` só para decidir o que mostrar, como deixar "Emprestar" apagado para um membro com um livro atrasado.
A regra é escrita uma vez e testada uma vez, e a cópia da decisão no cliente nunca discorda da do servidor.

## Quando uma peça se paga

Nada no FOCUS existe por cerimônia.
Um caso de uso existe quando há uma regra, um repositório quando há I/O, um orquestrador quando um evento leva a um novo estado, e uma tela quando há uma tela para mostrar.
Uma feature que mostra uma lista de livros sem regra nenhuma não tem caso de uso: o orquestrador pergunta ao repositório e publica o que recebeu.
KISS (mantenha simples), YAGNI (você não vai precisar disso) e DRY (não se repita) ([capítulo 4](04-simplicity.md)) decidem quando uma peça é escrita: quando uma entrega precisa do trabalho dela, e não antes.

Na Ninjobs, eu exigi toda peça em toda feature, formulários triviais incluídos, e mostrar um campo levava oito arquivos.
A culpa foi da exigência, nunca da arquitetura: eu deixei a complexidade crescer e perdi o KISS e o YAGNI pelo caminho ([capítulo 9](09-birth-of-focus-kit.md)).
As quatro peças são um lugar para cada trabalho, e uma feature com menos trabalhos tem menos peças.

## O que o time ganha

"O que acontece quando o evento X chega?" é um teste: chame o orquestrador com o evento e repositórios falsos, e confira o estado que ele devolve.
Toda regra fica em um caso de uso, uma função pura, então toda regra tem um teste que não precisa de preparação, e um revisor ou um agente encontra a regra em um lugar só.
Nenhum estudo mede um time com essas peças contra o mesmo time sem elas, e este livro não dá uma base de comparação.

## Pontos-chave

* FOCUS é Feature-oriented (fatias verticais), Clean (as camadas da Clean Architecture, com um caso de uso que não recebe repositório), Unidirectional (evento, orquestrador, novo estado, nada volta) e Scalable (toda peça isolada e testada).
* A tela dispara eventos e renderiza o estado; o orquestrador transforma um evento em um novo estado; um caso de uso guarda uma regra como função pura; o repositório busca e salva, e transforma uma exceção vinda dos dados em um `Result`.
* O orquestrador recebe os repositórios como parâmetro porque o teste dele passa fakes; o relógio chega como valor.
* Cliente e servidor têm os próprios orquestradores e repositórios e compartilham os mesmos casos de uso: o servidor impõe uma regra, o cliente a usa para decidir o que mostrar.
* Uma peça é escrita quando uma entrega precisa do trabalho dela: uma feature sem regra não tem caso de uso.

[^clean-architecture]: Robert C. Martin, "The Clean Architecture", 2012. <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[^bloc]: Bloc, "Bloc State Management Library", documentação, acesso em 2026-09-29. <https://bloclibrary.dev/>
[^mediatr]: Jimmy Bogard, "MediatR", acesso em 2026-09-29. <https://github.com/jbogard/MediatR>
