init:
	pip install -r requirements.txt

autoformat: init
	autopep8 --in-place -r --aggressive --aggressive sudoku tests

lint: init autoformat
	#flake8 sudoku --exclude=venv --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 sudoku --exclude=venv --count --show-source --statistics

pylint: autoformat
	pylint --recursive=yes --disable=missing-docstring,line-too-long,too-few-public-methods sudoku tests

test: init
	py.test --cov=sudoku tests

qa: lint pylint test

.PHONY: init test