.PHONY: help serve build verify scan hooks book release
.DEFAULT_GOAL := help

BUMP ?= patch

help: ## this list
	@awk -F ':.*## ' '/^[a-z]+:.*## /{printf "make %-8s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.venv/.installed: requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	touch .venv/.installed

serve: .venv/.installed ## serve the site at http://127.0.0.1:8000/
	.venv/bin/mkdocs serve

build: .venv/.installed ## build the site into site/, strict
	.venv/bin/python scripts/build.py

verify: build ## build, then every check; green before anything is done
	python3 scripts/check_parity.py
	python3 scripts/check_em_dash.py
	python3 scripts/check_prose.py
	python3 scripts/check_width.py
	python3 scripts/check_examples.py
	python3 scripts/check_links.py
	python3 scripts/check_disclosure.py

scan: ## the disclosure scan alone
	python3 scripts/check_disclosure.py

hooks: ## turn on the git hooks, once per clone
	git config core.hooksPath .githooks

book: ## the PDF and EPUB of both editions, in output/
	python3 scripts/build_book.py

release: ## publish the next version, author only (BUMP=minor|major)
	python3 scripts/release.py $(BUMP)
