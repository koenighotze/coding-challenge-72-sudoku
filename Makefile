init:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

clean:
	rm -fr 3.10/ .venv/ __pycache__/ bin/ lib/ include/ .pytest_cache/ .coverage  .mypy_cache/

# Run this to prepare your local environment
local.setup: 
	python3 -m venv .venv
	. .venv/bin/activate
	make init
	echo "Do not forget to . .venv/bin/activate"

autoformat: 
	python3 -m black --fast -v .

lint.code: 
	python3 -m pydocstyle sudoku tests *py

lint.docs: 
	python3 -m pydocstyle sudoku tests *py

lint.types:
	python -m mypy .

lint: lint.code lint.code lint.types

test:  
	pytest -v tests

test.coverage:
	pytest --cov=sudoku tests

qa: lint test

freeze:
	python3 -m pip freeze > requirements.txt

.PHONY: init test