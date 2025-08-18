# Generated-by: Cursor (claude-4-sonnet)
# Lint Targets
# =============

.PHONY: lint format

lint: requirements-dev ## Run linting and type checking
	@$(VENV_PYTHON) -m ruff check src/ tests/
	@$(VENV_PYTHON) -m mypy src/
	@printf "$(GREEN)✅ Linting complete$(RESET)\n"

format: requirements-dev ## Format code
	@$(VENV_PYTHON) -m ruff format src/ tests/
	@$(VENV_PYTHON) -m ruff check --fix src/ tests/ || true
	@printf "$(GREEN)✅ Code formatted$(RESET)\n"