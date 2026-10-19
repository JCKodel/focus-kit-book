English: [README.md](README.md)

# Uma Página de Cada Vez

*entregando software e projetos com agentes de IA*

J.C. Ködel

Um livro gratuito que leva quem nunca seguiu processo algum a conduzir projetos inteiros com agentes de IA: Spec-Driven Development como ideia, focus-kit como método e ferramenta, FOCUS como arquitetura opcional e o git necessário para trabalhar com agentes em paralelo e com equipes.

## Ler

* O site: <https://jckodel.github.io/focus-kit-book/pt/>
* PDF e EPUB, em português e inglês: nas [Releases](https://github.com/JCKodel/focus-kit-book/releases) deste repositório

## Gerar localmente

Você precisa de Python 3 e make, e de Node.js 26.12.0 ou mais novo para o `make verify`.

* `make` lista os seus comandos, uma linha cada.
* `make serve` abre o site em <http://127.0.0.1:8000/>.
* `make verify` roda as verificações. A varredura de exposição precisa de uma lista que só o autor tem; sem ela, é pulada.
  A verificação dos exemplos roda os exemplos da fronteira com o banco de dados do capítulo 3, nas duas edições, com o Node, e falha quando o Node falta ou é mais antigo; os outros exemplos do livro não são executados.
  * qualquer sistema: o instalador ou o binário da 26.12.0 para ele em <https://nodejs.org/dist/v26.12.0/>
  * macOS: `brew install node` também serve: instala a versão atual, 26.12.0 ou mais nova
* `make release`, só para o autor, publica o livro: com a `main` limpa, sem estar atrás da `origin/main`, com commits desde a tag `v*` mais nova, `make verify` verde e `VERSION` nomeando essa tag, grava a próxima versão e a data de hoje em `VERSION`, gera o livro (pandoc, weasyprint e pypdf, como no `make book`) e pergunta; com `y`, faz o commit só do `VERSION` e envia a `main` e a próxima tag (`BUMP=minor` ou `BUMP=major` para um passo maior), e o Actions anexa o PDF e o EPUB das duas edições a uma nova Release. Os passos estão em `docs/manuals/release-the-book.md`.
* `make hooks`, rodado uma vez num clone, liga os hooks do git que rodam a varredura de exposição nos arquivos preparados e na mensagem de cada commit. Eles recusam todo commit quando falta a lista, então só o autor, que tem a lista, os liga; com a lista, `make verify` falha até que estejam ligados.
* `make book` grava o PDF e o EPUB das duas edições em `output/`, cada um abrindo na sua capa. Precisa de pandoc, weasyprint e pypdf:
  * macOS: `brew install pandoc weasyprint` e `pip install pypdf`
  * Debian ou Ubuntu: `sudo apt install pandoc weasyprint python3-pypdf`

## Como é escrito

O livro é escrito com o [focus-kit](https://github.com/JCKodel/focus-kit): `docs/` guarda os documentos do projeto, `docs/06-Queue.md` a fila e `work/done/` uma página por entrega.
Este repositório é o exemplo, no livro, de um projeto que não é software.

## Contribuir

* Um erro ou uma sugestão: abra uma issue.
* Uma correção: abra um pull request que altere as duas edições, com `make verify` verde.

Contribuições são aceitas sob a licença do arquivo que alteram.

## Licença

| O quê | Licença | Arquivo |
|---|---|---|
| O texto e as figuras do livro (`book/`), os documentos do projeto (`docs/`, `work/`) e estes READMEs | CC BY-SA 4.0 | [`LICENSE-TEXT`](LICENSE-TEXT) |
| Scripts, build e configuração do site (`scripts/`, `Makefile`, `mkdocs.yml`, `overrides/`, `book/assets/site.css`, `pandoc/*.css`) | AGPL-3.0-only | [`LICENSE`](LICENSE) |
| As fontes do PDF (`pandoc/fonts/`): Merriweather, Instrument Serif, Iosevka Term | SIL Open Font License 1.1 | `pandoc/fonts/<Família>-OFL.txt` |
| Os arquivos de comando instalados pelo focus-kit | AGPL-3.0-only, nos termos do focus-kit | [`LICENSE`](LICENSE) |
