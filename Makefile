init:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

autoformat: init
	autopep8 --in-place -r --aggressive --aggressive sudoku tests

lint: init autoformat
	#flake8 sudoku --exclude=venv --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 sudoku --exclude=venv --count --show-source --statistics

pylint: autoformat
	pylint --recursive=yes --disable=missing-docstring,line-too-long,too-few-public-methods sudoku tests

test: init
	pytest -v tests

test.coverage: init
	pytest --cov=sudoku tests

qa: lint pylint test

freeze:
	python3 -m pip freeze > requirements.txt

.PHONY: init test