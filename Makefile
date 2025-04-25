.PHONY: format black isort lint fix type-check test all

black:
	poetry run black .

isort:
	poetry run isort app

format:
	make black isort

lint:
	poetry run flake8 app

fix:
	poetry run black . && poetry run isort app

type-check:
	poetry run mypy app

test:
	PYTHONPATH=. poetry run pytest --cov=app --cov-report=term-missing

all: format lint type-check test

