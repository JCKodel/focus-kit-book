# Simplicidade é uma decisão: KISS, YAGNI, DRY

Depois deste capítulo você consegue recusar um trecho de código, um documento ou uma verificação de que nenhuma entrega precisa, e dizer qual princípio o recusa e quem deu nome a ele.
Você também sabe distinguir a duplicação que precisa sair da duplicação que deve ficar, e sabe o momento em que uma versão compartilhada é devida: a segunda ocorrência concreta.

## O problema

Projetos de software raramente morrem de um problema difícil.
Morrem de muitas coisas pequenas, cada uma razoável quando entrou, que juntas deixam toda mudança lenta: uma camada de que ninguém precisava, uma opção que ninguém usou, uma regra escrita em três lugares que agora dizem três coisas.
Fred Brooks dividiu a dificuldade do software em duas em 1987: a complexidade essencial, que pertence ao próprio problema, e a complexidade acidental, que as pessoas que constroem acrescentam pelo caminho.[^brooks-silver-bullet]
Ninguém consegue remover a primeira.
A segunda é uma escolha, feita um arquivo por vez, e os três princípios deste capítulo são três maneiras de recusá-la.

Um agente deixa mais barato errar essa escolha.
Ele escreve a camada, a opção e a terceira cópia em segundos, cada uma plausível, e cada uma vira código que alguém precisa ler, revisar e manter verdadeiro.

## KISS: mantenha simples

"Keep it simple, stupid" (mantenha simples, estúpido) é atribuído a Kelly Johnson, o engenheiro aeronáutico que liderou a Skunk Works da Lockheed, a equipe que projetou o U-2 e o SR-71, dois aviões espiões da Guerra Fria.
O relato mais comum é que Johnson entregou aos seus engenheiros um punhado de ferramentas comuns e fixou a regra: o avião que eles projetassem tinha de poder ser consertado em campo, por um mecânico mediano em condições de combate, com aquelas ferramentas e nada mais.
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

Fowler contou, em 2015, o que custa uma feature presumida, e são quatro custos.[^fowler-yagni]

1. **Construir.** O esforço de analisar, programar e testar, perdido quando se descobre que ninguém precisa dela.
2. **Atrasar.** A feature que tem valor agora e espera enquanto a presumida é construída.
3. **Carregar.** O código dela "*acrescenta alguma complexidade ao software*", o que deixa toda outra feature mais difícil de mudar e de depurar, enquanto ele ficar.
4. **Consertar.** Quando ela é necessária afinal, as necessidades mudaram, e ela precisa ser refeita antes de servir.

Até a feature presumida que se mostra certa paga o atraso e a carga.
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

David Parnas deu a razão em 1972, antes de o nome existir: decomponha um sistema por "*uma lista de decisões de projeto difíceis ou de decisões de projeto que provavelmente vão mudar*", de modo que "*cada módulo seja então projetado para esconder uma dessas decisões dos outros*".[^parnas-1972]
Uma decisão escondida em um módulo muda em um módulo.
Uma decisão copiada em três módulos muda em três, e uma cópia sempre é esquecida.

Sandi Metz deu nome à falha oposta em 2016: "*duplicação é muito mais barata que a abstração errada*".[^metz-wrong-abstraction]
A abstração errada é a função compartilhada que dois chamadores usavam por razões diferentes; cada novo chamador acrescenta um parâmetro e uma condição, até que ninguém consiga mudá-la sem quebrar alguém.
O remédio dela é devolver o código a cada chamador e recomeçar do que cada um precisa.
DRY e Metz concordam: um lugar para cada conhecimento, e uma versão compartilhada só para o que é o mesmo conhecimento.

## A disciplina: abstração na segunda ocorrência

Os três princípios se encontram em uma regra, que o processo deste livro escreve em todo projeto: uma abstração é escrita na segunda ocorrência concreta, e a entrega que a escreve diz qual foi a primeira.
Uma cópia não é prova de que uma versão compartilhada seja necessária: é um palpite, e YAGNI recusa palpites.
Duas cópias são o erro que já aconteceu, e DRY pede um lugar só.
Nomear a primeira cópia torna o movimento verificável: quem revisa abre as duas e vê que são o mesmo conhecimento, que é o teste de Metz.

Na biblioteca de empréstimos, `Result`, o tipo que carrega um valor ou o que o impediu (capítulo 5), aparece primeiro dentro da feature de empréstimos, como o tipo de retorno de `emprestar` em `features/emprestimos/regras.ts`.
Ele fica lá enquanto tem um usuário.
Depois, uma entrega de membros precisa de uma regra que pode recusar, e `Result` seria escrito uma segunda vez; essa entrega o move para `src/lib/result.ts`, a pasta do código que não pertence a nenhuma feature (capítulo 6), e diz isso:

```ts
// Primeiro uso: features/emprestimos/regras.ts (emprestar).
// Segundo uso: features/membros/regras.ts (cadastrar).
export type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };
```

`ok` e `err`, as duas funções que constroem um `Result`, vão junto, e as duas features os importam de lá.
Se o movimento tivesse vindo no primeiro uso, teria sido um palpite que por acaso deu certo; no segundo, é um fato com duas testemunhas.

## Os mesmos três princípios em um processo

Um processo também é código: cada documento, cada verificação e cada passo é algo que uma pessoa precisa ler, e que alguém precisa manter verdadeiro quando o projeto muda.
Os três princípios se aplicam a ele sem mudança.

* **KISS.** O menor número de documentos e passos que levam uma entrega. Um processo que um membro novo não consegue seguir depois de uma leitura não vai ser seguido por ninguém.
* **YAGNI.** Uma verificação é uma capacidade construída para erros que você presume que vão acontecer. Uma verificação que nunca pega um erro real é uma feature presumida, e paga construção, atraso e carga em cada entrega que precisa satisfazê-la.
* **DRY.** Cada fato do projeto mora em um documento. Uma decisão escrita no plano, na especificação, no ADR e no código são quatro lugares que vão discordar, e o agente lê o que abrir primeiro.

Um passo entra no processo quando nomeia o erro concreto que teria pegado, e sai quando não nomeia nenhum.
O capítulo 17, o regulador, transforma isso na pergunta que todo passo do processo precisa responder.

> **Cuidado.** Um agente escreve mais do que código nessa velocidade: escreve também scripts, verificações, regras e passos, cada um plausível, e um processo cresce como o código cresce, uma adição razoável por vez.
> Enquanto este livro era escrito, o agente propôs que todo marco terminasse com um passo de revisão, uma boa ideia; a revisão achou erros, que abriram um marco de correções, cuja própria revisão abriu um segundo, e um terceiro estava a caminho quando eu o interrompi.
> O que eu devia estar fazendo era ler os capítulos e dizer o que mudar.
> Por conta própria, o agente tinha entrado numa espiral de verificações que verificavam verificações, e a pergunta acima é o que a interrompe: que erro concreto este passo teria pegado?

## O que o time ganha

Menos para ler, menos para revisar e menos para manter verdadeiro.
Cada arquivo, opção e verificação que não é escrito é um que nenhuma pessoa revisa, nenhum agente carrega em uma sessão, e nenhuma entrega precisa satisfazer.

Na Ninjobs, o meu próprio produto, eu deixei a complexidade crescer antes de o processo dela mudar.
Uma entrega tinha que passar por 29 verificações, e nenhuma delas jamais tinha pegado um erro no produto: eram caras de satisfazer e fáceis de contornar.
Uma decisão morava em seis lugares que podiam discordar: os documentos, as especificações, as mudanças, os ADRs, um roteiro e o código.
E porque eu exigia a forma completa, em camadas, da arquitetura em toda feature, formulários triviais incluídos, mostrar um campo em uma tela levava oito arquivos.
A culpa não era da arquitetura; KISS e YAGNI se perderam, uma adição razoável por vez.
O processo que o substituiu manteve duas verificações, cada uma ligada a um erro que ela pega, e um lugar por fato (capítulo 9).

## Pontos-chave

* A complexidade acidental é a parte que as pessoas acrescentam; ela é uma escolha, e KISS, YAGNI e DRY são três maneiras de recusá-la.
* KISS: a forma mais simples que faz o trabalho, simples o bastante para a pessoa que vem depois.
* YAGNI: uma capacidade presumida custa construção, atraso, carga e conserto; ele nunca argumenta contra testes, nomes claros ou outra qualidade interna.
* DRY: um lugar autoritativo para cada conhecimento; linhas idênticas podem ser conhecimentos diferentes, e duplicação é mais barata que a abstração errada.
* Uma abstração é escrita na segunda ocorrência concreta, e a entrega diz qual foi a primeira; em um processo, um passo só entra quando nomeia o erro concreto que teria pegado.

[^brooks-silver-bullet]: Frederick P. Brooks Jr., "No Silver Bullet: Essence and Accidents of Software Engineering", IEEE Computer 20(4), 1987.
[^beck-xp]: Kent Beck, "Extreme Programming Explained: Embrace Change", Addison-Wesley, 1999.
[^fowler-yagni]: Martin Fowler, "Yagni", martinfowler.com, 2015-05-26, acesso em 2026-09-30. <https://martinfowler.com/bliki/Yagni.html>
[^pragmatic-programmer]: Andrew Hunt e David Thomas, "The Pragmatic Programmer", Addison-Wesley, 1999; edição de 20 anos, 2019.
[^parnas-1972]: D. L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules", Communications of the ACM 15(12), 1972. <https://doi.org/10.1145/361598.361623>
[^metz-wrong-abstraction]: Sandi Metz, "The Wrong Abstraction", 2016-01-20, acesso em 2026-09-30. <https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction>
