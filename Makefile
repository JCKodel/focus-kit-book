.PHONY: serve build verify

.venv: requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	touch .venv

serve: .venv
	.venv/bin/mkdocs serve

build: .venv
	.venv/bin/python scripts/build.py

verify: build
	python3 scripts/check_parity.py
	python3 scripts/check_em_dash.py
