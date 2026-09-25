.PHONY: serve build verify scan

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
	python3 scripts/check_prose.py
	python3 scripts/check_links.py
	python3 scripts/check_disclosure.py

scan:
	python3 scripts/check_disclosure.py
