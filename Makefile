check:
	ruff check . --fix
	ruff format --check .
	mypy src
	pytest -q
