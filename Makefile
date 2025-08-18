# Generated-by: Cursor (claude-4-sonnet)
# Python Template Project Makefile
# =================================

# Include common variables first
include make/common.mk

# Include modular makefiles
include make/env.mk
include make/test.mk
include make/lint.mk
include make/mcp.mk

.DEFAULT_GOAL := help
.PHONY: help

help: ## Display this help message
	@echo "Python Template Project"
	@echo "======================="
	@echo ""
	@echo "Available targets:"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)