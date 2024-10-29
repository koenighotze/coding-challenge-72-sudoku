PYTHON_VERSION := 3.12
UV := uv
PIP := $(UV) pip
RUN := $(UV) run --python $(PYTHON_VERSION)
VENV := .venv

# Declare all non-file targets as phony to ensure they always run
.PHONY: all install-uv init clean local.setup autoformat lint test qa freeze

# Default target: run all quality assurance checks
all: qa

# Install uv if not present
install-uv:
	@command -v $(UV) >/dev/null 2>&1 || { echo "Installing uv..."; curl -LsSf https://astral.sh/uv/install.sh | sh; }

# Initialize the project environment
init:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Clean up generated files and directories
clean:
	rm -rf 3.10/ $(VENV)/ __pycache__/ bin/ lib/ include/ .pytest_cache/ .coverage .mypy_cache/

# Set up local development environment
local.setup: install-uv
	$(UV) venv
	@echo "Virtual environment created. Activate it with: source $(VENV)/bin/activate"
	@echo "Then run: make init"

# Auto-format code
autoformat: 
	$(RUN) black --fast -v .

lint.code: 
	$(RUN) pydocstyle sudoku tests *py

# Check types
lint.types:
	$(RUN) mypy .

# Run all linters
lint: lint.code lint.types

# Run tests
test:  
	$(RUN) pytest -v tests

# Run tests with coverage
test.coverage:
	$(RUN) pytest --cov=sudoku tests

# Run all quality assurance checks
qa: lint test

# Freeze dependencies
freeze:
	$(PIP) freeze > requirements.txt
