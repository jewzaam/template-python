# Generated-by: Cursor (claude-4-sonnet)
# Environment Setup Targets
# ==========================

.PHONY: venv uv requirements requirements-dev clean

venv: ## Create Python virtual environment
	@if [ ! -d "$(VENV_DIR)" ]; then \
		$(PYTHON) -m venv $(VENV_DIR); \
		printf "$(GREEN)✅ Virtual environment created$(RESET)\n"; \
	fi

uv: venv ## Install uv package manager
	@if [ ! -f "$(VENV_DIR)/bin/uv" ]; then \
		$(VENV_PIP) install uv; \
		printf "$(GREEN)✅ uv installed$(RESET)\n"; \
	fi

requirements: venv uv ## Install all dependencies (runtime)
	@$(VENV_UV) pip install --upgrade pip >/dev/null
	@$(VENV_UV) pip install -r requirements.txt
	@echo "✅ All dependencies installed in $(VENV_DIR)"

requirements-dev: venv uv requirements ## Install all dev dependencies
	@$(VENV_UV) pip install -r requirements-dev.txt
	@$(VENV_UV) pip install -e .
	@echo "✅ All dev dependencies installed in $(VENV_DIR)"

clean: ## Remove temporary and backup files
	# Python caches
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	# Test artifacts
	@rm -rf .pytest_cache .coverage htmlcov .tox .coverage-percentage .mypy_cache .ruff_cache 2>/dev/null || true
	# Build artifacts
	@rm -rf dist build *.egg-info/ src/*.egg-info/ 2>/dev/null || true
	# Python virtual environment (main one only)
	@rm -rf $(VENV_DIR) 2>/dev/null || true
	# Misc artifacts
	@rm -rf local scratch logs 2>/dev/null || true
	@echo "✅ Cleanup completed"