.PHONY: serve build verify scan hooks book release

BUMP ?= patch

.venv/.installed: requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	touch .venv/.installed

serve: .venv/.installed
	.venv/bin/mkdocs serve

build: .venv/.installed
	.venv/bin/python scripts/build.py

verify: build
	python3 scripts/check_parity.py
	python3 scripts/check_em_dash.py
	python3 scripts/check_prose.py
	python3 scripts/check_width.py
	python3 scripts/check_examples.py
	python3 scripts/check_links.py
	python3 scripts/check_disclosure.py

scan:
	python3 scripts/check_disclosure.py

hooks:
	git config core.hooksPath .githooks

book:
	python3 scripts/build_book.py

release:
	python3 scripts/release.py $(BUMP)
