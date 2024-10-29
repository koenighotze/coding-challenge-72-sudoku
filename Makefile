init:
	uv pip install -r requirements.txt
	# uv tool install black
	# uv tool install ruff
	# uv tool install pydocstyle
	# uv tool install 

autoformat: 
	uv run -- black --fast -v .

lint.code:
	uv run -- pydocstyle sudoku tests *py

lint.docs: 
	uv run -- pydocstyle sudoku tests *py

# lint.types:
#     python -m mypy .

# lint: lint.code lint.docs lint.types

# test:  
#     uv -m pytest -v tests

# test.coverage:
#     uv -m pytest --cov=sudoku tests

# qa: lint test
