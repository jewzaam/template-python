# Generated-by: Cursor (claude-4-sonnet)
# Test Targets
# =============

.PHONY: test test-unit test-integration test-all coverage coverage-report coverage-verify

test: test-unit test-integration ## Run all tests (unit + integration)
	@$(VENV_PYTHON) -m pytest tests/ -v $(ARGS)
	@printf "$(GREEN)✅ All tests completed$(RESET)\n"

test-unit: requirements-dev ## Run unit tests only
	@$(VENV_PYTHON) -m pytest tests/unit/ -v $(ARGS)
	@printf "$(GREEN)✅ Unit tests completed$(RESET)\n"

test-integration: requirements-dev ## Run integration tests only
	@$(VENV_PYTHON) -m pytest tests/integration/ -v $(ARGS)
	@printf "$(GREEN)✅ Integration tests completed$(RESET)\n"

coverage-report: requirements-dev ## Run tests with coverage report (no threshold check)
	@$(VENV_PYTHON) -m pytest tests/ --cov=src --cov-report=html --cov-report=term --cov-report=xml $(ARGS)
	@$(VENV_PYTHON) -m coverage report | tail -1 | awk '{print $$4}' | sed 's/%//' > .coverage-percentage
	@printf "$(GREEN)✅ Coverage report generated$(RESET)\n"

coverage-verify: ## Verify coverage meets threshold (run after coverage-report)
	@if [ ! -f .coverage-percentage ]; then \
		printf "$(RED)❌ No coverage data found. Run 'make coverage-report' first.$(RESET)\n"; \
		exit 1; \
	fi; \
	COVERAGE=$$(cat .coverage-percentage); \
	echo "Current coverage: $${COVERAGE}%"; \
	if [ "$$(echo "$${COVERAGE}" | cut -d. -f1)" -lt $(COVERAGE_THRESHOLD) ]; then \
		printf "$(RED)❌ Coverage check failed: $${COVERAGE}%% is below the required $(COVERAGE_THRESHOLD)%% threshold$(RESET)\n"; \
		exit 1; \
	else \
		printf "$(GREEN)✅ Coverage check passed: $${COVERAGE}%% meets the required $(COVERAGE_THRESHOLD)%% threshold$(RESET)\n"; \
	fi

coverage: coverage-report coverage-verify ## Run tests with coverage report and enforce threshold