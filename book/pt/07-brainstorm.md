# `/brainstorm`, um projeto novo

Depois deste capítulo você consegue rodar o `/brainstorm` em um projeto novo, responder às perguntas dele ou dizer "your call" (você decide), e revisar os documentos que ele escreve antes de fazer o commit.
Você também consegue escolher uma stack pelo que o projeto precisa e por quanto o agente a conhece.

## O que ele pergunta

O `/brainstorm` é o comando para um repositório que ainda não tem código.
Ele conversa um assunto de cada vez, nesta ordem, e segue adiante quando já conseguiria escrever aquele documento sozinho, como diz o seu arquivo, `brainstorm/SKILL.md`:

1. O produto (docs/00): o que ele é, para quem, o que ele não é, como é uma boa decisão.
2. O vocabulário (docs/03): as palavras sem as quais o produto não pode ser descrito, cada uma com o seu nome no código.
3. Como ele é construído (docs/01): a stack e a forma do código, com as [duas escolhas](06-the-documents.md#as-duas-escolhas) do kit, FOCUS e a estratégia de git.
4. As convenções (docs/04): idiomas, estilo, onde ficam os testes, o formato do commit.
5. Os slots do processo (docs/05): o comando de verificação, os ambientes, como uma tela é provada, a política de publicação.
6. O primeiro marco (docs/06): as suas primeiras entregas, uma linha cada, em ordem.

Ele só pergunta o que não consegue decidir com um padrão sensato, e diz o padrão junto com a pergunta.
Por isso "your call" é sempre uma resposta válida: o agente fica com o padrão, e quem não sabe responder a uma pergunta ainda recebe um bom documento.
O que você ainda não sabe, como um comando de verificação antes de existir qualquer código, ele escreve como "criado pela primeira entrega".

Quando os seis assuntos estão cobertos, ele escreve os docs/00 a 06, um ADR por decisão que uma sessão futura poderia desfazer, o `AGENTS.md`, o `CLAUDE.md` com a linha `@AGENTS.md` e uma pasta `work/done/` vazia.
Ele não escreve código, nem configuração, nem arquivo de dependências: a primeira entrega faz isso, com uma página própria.

## Escolher a stack

Quando a conversa chega a como o projeto é construído, três perguntas escolhem a stack, nesta ordem.

**Do que o projeto precisa?**
Comece pelo valor dele, não por uma linguagem: quem o abre, em que aparelho, quais regras nunca podem quebrar e quanto ele pode custar para rodar.
Uma stack que não entrega isso está fora, por mais que o agente a conheça.

**De quanto código público o agente aprendeu?**
Um modelo escreve melhor o que mais viu durante o treinamento, e a medida pública mais próxima disso é quantas pessoas escrevem uma linguagem em aberto.
Pela contagem do GitHub, o TypeScript se tornou a linguagem mais usada no GitHub em agosto de 2025, com 2.636.006 contribuidores mensais, à frente de Python e JavaScript.[^octoverse]
Ela conta pessoas, não linhas de código, então leia como uma classificação, não como um tamanho.
No Ninjobs, o mesmo agente errava o design em Flutter e o acertou em React ([capítulo 4](04-birth-of-focus-kit.md)).

**O agente consegue conferir o próprio trabalho ali?**
Um compilador que rejeita um tipo errado e testes que rodam em segundos avisam o agente de que ele errou antes que você precise avisar.
Uma stack em que o erro só aparece em tempo de execução, em uma tela, deixa essa conferência para você.

A clínica responde a elas assim:

* TypeScript, estrito: a linguagem mais usada por aquela contagem, e os tipos pegam os erros do agente antes que qualquer coisa rode.
* Um PWA em React (um app web que o celular abre no navegador, sem instalar): os clientes agendam pelo celular, e React é onde o agente acertou o design do Ninjobs.
* Um servidor Node pequeno: o cliente e o dono compartilham os mesmos agendamentos, então as regras que os mantêm certos rodam onde um celular não consegue pulá-las, na mesma linguagem das telas.
* SQLite em um arquivo: os dados de uma clínica cabem em um arquivo, sem servidor de banco de dados para manter, e um backup é uma cópia.
* Nenhum serviço pago: roda em uma máquina da clínica ou em qualquer hospedagem gratuita.

O briefing abaixo já dá essa stack, então a execução mostra os critérios por trás da resposta, não uma escolha ao vivo.

## A execução na clínica

A execução partiu da clínica na tag do capítulo `book-v1/install-and-hosts`: o README, as licenças e o kit que o capítulo 5 instalou, sem nenhum documento e sem código.
Ela foi respondida a partir de um briefing, com a mesma forma do briefing do capítulo 3: uma seção por assunto, mais a regra para uma pergunta que o briefing não responde.[^brainstorm-run]
O original está em inglês; aqui vai traduzido:

```markdown
# Briefing

## Produto
Um app de agendamento para uma clínica de bairro. Os clientes agendam e cancelam os próprios agendamentos com os profissionais da clínica pelo celular; o dono cadastra os profissionais e os horários semanais deles.
Dois lados: o cliente, que não tem conta e informa um nome e um telefone; o dono, que entra com login (como: "your call").
Regras: um profissional não pode ter dois agendamentos no mesmo horário. Um cliente pode cancelar o próprio agendamento até 24 horas antes do início; um agendamento cancelado libera o seu horário; um cancelamento mais tarde é recusado com uma mensagem que diz por quê. Os horários são a hora local da clínica.
Não: pagamentos, notificações (SMS, e-mail, push), prontuários ou qualquer dado de saúde, mais de uma clínica.

## Stack
TypeScript, estrito. Um PWA em React que o cliente e o dono abrem no navegador, sobre um servidor Node pequeno que guarda os dados em um arquivo SQLite. Nenhum serviço pago: roda em uma máquina da clínica ou em qualquer hospedagem gratuita.
Por quê: a maior parte do código público com que o agente aprendeu está nesta linguagem e nesta biblioteca, e tipos e testes deixam que ele confira o próprio trabalho.

## Escolhas
FOCUS: FOCUS inteiro. Git: trunk.

## Convenções e processo
Inglês para documentos e identificadores. Verificação: criada pela primeira entrega. Todo o resto: "your call".

## Primeiro marco
Quando ele fecha, o dono consegue cadastrar profissionais e os horários semanais deles, um cliente consegue agendar um horário livre, e um cliente consegue cancelar até 24 horas antes. As ausências de um profissional e a visão do dia do dono vêm no segundo marco.

## Princípios
Mantenha simples. Toda regra tem um teste. Nenhum travessão em nenhum documento.

## Regra para uma pergunta que o briefing não responde
Responda "your call".
```

Abra o seu host na raiz do seu repositório, em uma sessão nova, e digite `/brainstorm`; eu o rodei sem interface no Claude Code e respondi a cada rodada com as seções do briefing para os assuntos perguntados, palavra por palavra, ou "your call".[^brainstorm-run]
Uma execução sem interface é o Claude Code rodado no terminal com `claude -p`, um prompt por chamada: ele imprime a resposta e sai, sem ninguém ali para aprovar nada.[^claude-code-headless]
Cada resposta a uma rodada foi uma nova chamada com `--continue`, que a envia para a conversa mais recente daquele diretório.[^claude-code-headless]
As execuções do livro são sem interface para que cada turno fique registrado; em uma sessão interativa, você só digita a sua resposta na mesma sessão.
Ele perguntou em rodadas de um ou dois assuntos.
Na rodada sobre como a clínica é construída, ele escreveu o que segue; o original está em inglês, e aqui vai traduzido:[^brainstorm-run]

```markdown
## 3. Como ele é construído (docs/01)

O que o produto precisa da stack:
- uma página web pensada para o celular, para os clientes, sem instalar e sem conta
- um login para um dono
- um **servidor que guarda as regras**, porque não dá para confiar em um celular para fazer valer o prazo de 24 horas ou impedir agendamentos duplicados
- regras fáceis de testar, já que toda regra tem um teste

**1. Stack. Minha recomendação: um app web em TypeScript (SvelteKit) com um banco SQLite, em um servidor pequeno.**
- É uma linguagem e um projeto, e as regras rodam no servidor como funções simples que o Vitest testa em milissegundos.
- Um agendamento duplicado é impossível no nível do banco: os horários são alinhados, então um índice único em (profissional, início) sobre os agendamentos ativos resolve qualquer disputa.
- O login do dono é uma senha com hash mais um cookie de sessão, cerca de uma página de código.
- Os dados são um arquivo, e um backup é uma cópia desse arquivo.

A alternativa é uma página fina sobre um serviço de backend hospedado (Postgres mais login embutido). Você ganha hospedagem e autenticação de graça, mas as regras morariam em funções SQL e seriam testadas em uma segunda linguagem. Isso combina pior com "toda regra tem um teste" e "mantenha simples". A recomendação se mantém?

**2. Como o código é organizado.** O kit oferece o FOCUS, uma arquitetura em quatro peças em que os dados correm em um só sentido:
- a **tela** só mostra o estado e informa o que o usuário fez
- um **orquestrador** transforma o que o usuário fez no próximo estado
- **casos de uso** guardam toda regra de negócio como funções puras que recebem dados e devolvem um resultado ou uma recusa
- um **repositório** é o único código que fala com o banco

O código é agrupado por funcionalidade (agendar, cancelar, horários semanais…), não por camada, e os erros são devolvidos como valores em vez de lançados.

Você pode adotá-lo inteiro, adotar só os dois princípios (pastas por funcionalidade + erros como valores) ou nenhum. **Minha recomendação: FOCUS inteiro.** Ele se encaixa no SvelteKit sem maquinário extra: a página é a tela, o arquivo de servidor da página é o orquestrador, `rules.ts` guarda os casos de uso e `repository.ts` guarda as consultas. Ele também põe a regra das 24 horas e a regra dos horários em funções puras, que é onde "toda regra tem um teste" sai mais barato.

**3. Git.** Em todas as opções o agente nunca faz commit nem merge; ele coloca em stage e sugere a mensagem. Você pode trabalhar no branch principal, uma entrega de cada vez, e revisar e fazer o commit depois de cada uma. Ou cada entrega ganha o próprio branch, que você faz o merge. Ou cada entrega ganha o próprio branch em uma pasta separada, para que vários agentes construam ao mesmo tempo. **Minha recomendação: o branch principal**, já que você é uma pessoa trabalhando em uma entrega de cada vez.
```

A resposta foram as duas seções do briefing para esse assunto, aqui traduzidas:[^brainstorm-run]

```markdown
## Stack
TypeScript, estrito. Um PWA em React que o cliente e o dono abrem no navegador, sobre um servidor Node pequeno que guarda os dados em um arquivo SQLite. Nenhum serviço pago: roda em uma máquina da clínica ou em qualquer hospedagem gratuita.
Por quê: a maior parte do código público com que o agente aprendeu está nesta linguagem e nesta biblioteca, e tipos e testes deixam que ele confira o próprio trabalho.

## Escolhas
FOCUS: FOCUS inteiro. Git: trunk.
```

O agente partiu do que o produto precisa, a primeira pergunta da stack, disse um padrão para cada escolha com o seu motivo e a sua alternativa, e perguntou se ele se mantinha; o briefing deixou o SvelteKit de fora e o React dentro, e o agente então escolheu sozinho as peças menores dentro dessa stack, o que o ADR dele registra como decisão do agente.

Depois da rodada sobre as convenções e os slots do processo ele escreveu os documentos, e o `git status --short` mostrou:[^brainstorm-run]

```
?? AGENTS.md
?? CLAUDE.md
?? docs/
?? work/
```

Essas linhas guardam os docs/00 a 06, um ADR cada em `docs/adr/` para a stack, o FOCUS inteiro, o trunk, os clientes sem conta e uma duração fixa de agendamento, o `AGENTS.md`, o `CLAUDE.md` e o `work/done/.gitkeep`.[^brainstorm-run]
Os três abaixo são citados na tag do capítulo `book-v1/brainstorm`, como foram commitados; no repositório eles estão em inglês, e aqui vão traduzidos.

O docs/00 abre com o propósito do produto em um parágrafo; o exercício 6.2 pediu que você escrevesse o da clínica à mão.
Este é o §Purpose (propósito) de [`docs/00-Product.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/docs/00-Product.md):

```markdown
## Propósito

Um app de agendamento para uma clínica de bairro. Os clientes agendam e
cancelam os próprios agendamentos com os profissionais da clínica pelo
celular, sem criar uma conta. O dono cadastra os profissionais e os horários
semanais deles, e vê quem vem. O app substitui o telefonema e a agenda de
papel no caso simples: escolher um profissional, escolher um horário livre,
pronto.
```

É o produto do briefing com a falta de conta do cliente incorporada, e a última frase é da conversa: o que o app substitui, o que diz a uma sessão futura quão pequeno é o "simples" aqui.

O capítulo 5 disse que este capítulo escreve o `AGENTS.md`, o arquivo de regras que toda sessão lê primeiro.
Os inegociáveis dele são o modelo do kit com as regras do próprio projeto acima das três linhas fixas.
Esta é a seção Non-negotiables (inegociáveis) do [`AGENTS.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/AGENTS.md):

```markdown
## Inegociáveis
- Toda regra de negócio é um caso de uso puro com um teste. O servidor a faz
  valer; o cliente a reutiliza só para exibir (docs/01).
- Nada de pagamentos, nada de notificações, nada de dados de saúde, uma
  clínica (docs/00).
- Um cliente não tem conta: um nome, um telefone, um código de agendamento,
  nada mais (ADR-0004).
- Instantes são guardados em UTC e raciocinados na hora da clínica (docs/03).
- Nenhum serviço pago (ADR-0001).
- Uma decisão em aberto no docs/00 é perguntada, nunca presumida.
- Uma entrega = uma página em work/<slug>.md: /propose para definir, /apply
  para construir.
- Nenhum travessão em nenhum texto que um usuário lê.
- O agente coloca em stage e sugere a mensagem de commit. Ele nunca faz commit.
```

Cada linha do projeto aponta para o documento ou o ADR que guarda o seu motivo, e o código de agendamento vem de um "your call": a resposta do agente para como um cliente sem conta prova que um agendamento é dele.

O docs/06 é a fila: marcos, cada um com um parágrafo que diz o que é verdade quando ele fecha, e uma linha por entrega abaixo dele (o capítulo 9 ensina as marcas).
Este é o primeiro marco de [`docs/06-Queue.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/docs/06-Queue.md), com os slugs como estão:

````markdown
## Marco 1: um cliente agenda e cancela

Quando ele fecha, o dono consegue cadastrar profissionais e os horários
semanais deles, um cliente consegue agendar um horário livre, e um cliente
consegue cancelar até 24 horas antes.

```
[ ] skeleton             PWA e servidor vazios em um projeto, npm run verify, primeira captura de tela
[ ] clinic-setup         um comando de configuração cria a clínica e o dono; o dono entra e sai
[ ] professionals        o dono cadastra, renomeia e remove profissionais
[ ] weekly-hours         o dono define os horários semanais de cada profissional
[ ] book-appointment     um cliente vê os horários livres de 30 dias e agenda com nome e telefone
[ ] cancel-appointment   um cliente cancela até 24 horas antes, ou fica sabendo por que não
```
````

O parágrafo é a frase do briefing, e a primeira linha é o esqueleto sobre o qual as outras se apoiam, que cria o `npm run verify`; a próxima seção mostra que a primeira versão deste marco dizia outra coisa.

## Revise antes do commit

Na execução o comando não colocou nada em stage nem fez commit, e terminou mostrando a fila: primeiro você lê o que ele escreveu.[^brainstorm-run]
Confira que:

* cada resposta que você deu chegou ao documento que é dono dela: o produto no docs/00, a stack no docs/01 e no seu ADR, o marco no docs/06.
* cada padrão de "your call" é um que você aceita. Na execução o agente os listou no fim; cada um que você recusa é uma correção agora, antes que uma entrega se apoie nele.
* cada ADR registra uma decisão que você tomou, ou diz que foi decisão do agente.

Quando algo está errado, peça a correção ao agente na mesma sessão, que ainda guarda a conversa, e deixe que ele escreva a mudança ([capítulo 6](06-the-documents.md)).

Na execução, o agente escreveu os documentos sem perguntar sobre o primeiro marco, o seu último assunto.[^brainstorm-run]
O marco 1 dele tinha uma linha `owner-schedule`, a visão do dia do dono, e um parágrafo que dizia que o dono "vê a agenda do dia", enquanto o briefing põe essa visão no segundo marco.
Os documentos liam bem, e nada neles dizia que um assunto tinha sido pulado: o texto de um agente parece certo mesmo quando está errado, e só a conferência com o que você respondeu o encontra.
A correção foi a seção do briefing para esse assunto, enviada à mesma sessão; o original está em inglês, e aqui vai traduzido:[^brainstorm-run]

```markdown
## Primeiro marco
Quando ele fecha, o dono consegue cadastrar profissionais e os horários semanais deles, um cliente consegue agendar um horário livre, e um cliente consegue cancelar até 24 horas antes. As ausências de um profissional e a visão do dia do dono vêm no segundo marco.
```

O agente mudou só o docs/06.
O diff fica como o comando o imprimiu, em inglês: o parágrafo novo do marco 1 é o traduzido acima, e o marco 2 novo diz "Quando ele fecha, o dono consegue registrar as ausências de um profissional, que removem os horários dele, e vê os agendamentos do dia por profissional; e o app roda fora da máquina do desenvolvedor sem nenhum serviço pago".[^brainstorm-run]

````diff
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@ -5,11 +5,8 @@
 
 ## Milestone 1: a client books and cancels
 
-When it closes, the owner has set up the clinic, registered its
-professionals and their weekly hours, and sees the day's schedule; a client
-on a phone books a free slot with a name and a phone number and cancels it up
-to 24 hours before; and the app runs outside the developer's machine with no
-paid service.
+When it closes, the owner can register professionals and their weekly hours,
+a client can book a free slot, and a client can cancel up to 24 hours before.
 
 ```
 [ ] skeleton             empty PWA and server in one project, npm run verify, first screenshot
@@ -18,6 +15,16 @@
 [ ] weekly-hours         the owner sets each professional's weekly hours
 [ ] book-appointment     a client sees free slots for 30 days and books with name and phone
 [ ] cancel-appointment   a client cancels up to 24 hours before, or is told why not
+```
+
+## Milestone 2: the owner runs the day
+
+When it closes, the owner can record a professional's absences, which remove
+their slots, and sees the day's appointments per professional; and the app
+runs outside the developer's machine with no paid service.
+
+```
+[ ] absences             the owner records a professional's absences, and their slots disappear
 [ ] owner-schedule       the owner sees the day's appointments per professional
 [ ] deploy               the app runs on a clinic machine or a free host, with a backup of the data
 ```
````

Ele também passou o `deploy` para o segundo marco por conta própria, e disse isso na resposta, então a escolha ficou à vista para aceitar ou recusar, e a revisão a aceitou.

## Pontos-chave

* O `/brainstorm` conversa sobre seis assuntos em ordem (produto, vocabulário, como é construído, convenções, slots do processo, primeiro marco) e escreve os documentos do projeto, os ADRs, o `AGENTS.md` e o `CLAUDE.md`, nunca código.
* Cada pergunta vem com um padrão, então "your call" é uma resposta válida, e você confere cada padrão que o agente manteve.
* Escolha uma stack pelo que o projeto precisa, depois por quanto código público o agente viu, depois por se tipos e testes deixam que ele confira o próprio trabalho.
* Revise antes do commit: cada resposta no documento que é dono dela, cada padrão um que você aceita, cada ADR uma decisão que você tomou.
* Peça a correção na mesma sessão e deixe o agente escrevê-la; os documentos parecem certos mesmo quando um assunto foi pulado.

## Exercícios

### Exercício 7.1

No seu clone do projeto guiado, faça checkout de `book-v1/install-and-hosts` em um branch seu, rode o `/brainstorm` e responda com o briefing deste capítulo.
Compare o que você obtém com `book-v1/brainstorm`: o que difere, e alguma diferença quebra uma resposta do briefing?

### Exercício 7.2

Pegue o Propósito e os três inegociáveis que você escreveu no exercício 6.2 e compare com os da clínica.
O que a conversa acrescentou que você não escreveu?

### Exercício 7.3

Escolha uma stack para um projeto seu pelas três perguntas deste capítulo, e diga qual pergunta decidiu.

[^octoverse]: GitHub, "Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1", 2025, o relatório mais recente em 2026-09-28: contribuidores mensais no GitHub, agosto de 2025. <https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/>
[^brainstorm-run]: A execução do `/brainstorm` deste livro no projeto guiado, 2026-09-28, com o Claude Code 2.1.283 e o modelo `claude-opus-5-5`, de `book-v1/install-and-hosts` até a tag do capítulo `book-v1/brainstorm`: o briefing, os comandos, a saída de cada turno, cada pergunta e resposta, e a correção. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/brainstorm-run/README.md>
[^claude-code-headless]: Anthropic, "Run Claude Code programmatically", documentação do Claude Code, acesso em 2026-09-29. <https://code.claude.com/docs/en/headless>
