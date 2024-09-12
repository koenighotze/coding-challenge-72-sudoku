init:
	pip install -r requirements.txt

lint: init
	flake8 sudoku --exclude=venv --count --select=E9,F63,F7,F82 --show-source --statistics

test: init
	py.test tests

.PHONY: init test