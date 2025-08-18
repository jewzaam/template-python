<!-- Generated-by: Cursor (claude-4-sonnet) -->
# Python Template Project

[![Test](https://github.com/your-username/template-python/workflows/Test/badge.svg)](https://github.com/your-username/template-python/actions/workflows/test.yml)
[![Coverage](https://github.com/your-username/template-python/workflows/Coverage%20Check/badge.svg)](https://github.com/your-username/template-python/actions/workflows/coverage.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

A comprehensive Python project template with optional MCP (Model Context Protocol) server capabilities. This template provides a solid foundation for Python projects with modern tooling, testing frameworks, and development practices.

## 🚀 Features

- **Modern Python Setup**: Uses `pyproject.toml` with setuptools build backend
- **Modular Makefile**: Clean, organized build system with separate concerns
- **Comprehensive Tooling**: Linting (ruff), type checking (mypy), formatting (ruff)
- **Testing Framework**: pytest with coverage reporting and separate unit/integration tests
- **MCP Server Ready**: Optional Model Context Protocol server integration for Cursor IDE
- **Development Environment**: Isolated virtual environments with uv package manager
- **CI/CD Ready**: Pre-configured for GitHub Actions and other CI systems

## 📁 Project Structure

```
template-python/
├── src/
│   └── template_python/          # Main package
│       ├── __init__.py           # Package metadata
│       ├── main.py               # Application entry point
│       └── mcp_server.py         # MCP server implementation (template)
├── tests/
│   ├── unit/                     # Unit tests
│   ├── integration/              # Integration tests
│   └── __init__.py
├── make/                         # Modular Makefile components
│   ├── common.mk                 # Shared variables and constants
│   ├── env.mk                    # Environment setup
│   ├── lint.mk                   # Linting, type checking & formatting
│   ├── test.mk                   # Testing targets
│   └── mcp.mk                    # MCP server development
├── scripts/
│   ├── test_mcp_client.py          # MCP server test client
│   └── update_cursor_config.py     # Cursor configuration script
├── docs/                         # Documentation
├── Makefile                      # Main build file
├── pyproject.toml               # Python project configuration
├── requirements-dev.txt         # Backup dev dependencies
└── .gitignore                  # Git ignore patterns
```

## 🛠️ Quick Start

### 1. Clone and Set Up

```bash
# Clone this template (or create from template)
git clone <your-repo-url> my-python-project
cd my-python-project

# Set up development environment
make requirements-dev
```

### 2. Customize for Your Project

1. **Update `pyproject.toml`**:
   - Change `name`, `description`, `authors`
   - Update dependencies as needed
   - Uncomment MCP dependencies if building an MCP server

2. **Rename the package**:
   ```bash
   mv src/template_python src/your_package_name
   # Update imports in files accordingly
   ```

3. **Customize the main module**:
   - Edit `src/your_package_name/main.py`
   - Implement your application logic

### 3. Development Workflow

```bash
# Run critical development tasks
make test lint format coverage

# Or run individual tasks
make lint          # Linting and type checking
make test          # Run tests
make format        # Format code
make coverage      # Tests with coverage threshold check
make clean         # Clean up artifacts
```

## 📋 Critical Make Targets

**Essential development commands:**

```bash
make test              # Run all tests
make lint              # Run linting and type checking  
make coverage          # Run tests with coverage report
make install-cursor    # Configure Cursor IDE for MCP integration
```

**Complete list:**

Run `make help` to see all available targets. Key targets include:

### Environment Management
- `make requirements-dev` - Complete development setup
- `make venv` - Create virtual environment
- `make clean` - Clean temporary files and artifacts

### Development
- `make format` - Format code with ruff
- `make lint` - Run linting with ruff and mypy
- `make test` - Run all tests
- `make coverage` - Run tests with coverage threshold check
- `make coverage-report` - Generate coverage report without threshold
- `make coverage-verify` - Verify coverage meets threshold

### MCP Server Development
- `make install-cursor` - Configure Cursor IDE integration
- `make venv-cursor` - Create dedicated Cursor virtual environment
- `make clean-cursor` - Clean MCP-specific artifacts

## 🔧 MCP Server Development

This template includes optional MCP (Model Context Protocol) server support for integration with Cursor IDE.

### Enabling MCP Functionality

1. **Uncomment MCP dependencies** in `pyproject.toml`:
   ```toml
   dependencies = [
       "mcp>=1.0.0",
       "httpx>=0.25.0",
       "anyio>=3.0.0",
       "pydantic>=2.0.0",
   ]
   ```

2. **Uncomment the script entry point**:
   ```toml
   [project.scripts]
   your-mcp-server = "your_package.server:main"
   ```

3. **Implement your MCP server** in `src/your_package/mcp_server.py`
4. **Set up Cursor integration**:
   ```bash
   make install-cursor
   ```

### MCP Development Workflow

```bash
# Configure Cursor IDE with MCP integration
make install-cursor

# Test your MCP server
python scripts/test_mcp_client.py

# Restart Cursor and test integration
```

## 🧪 Testing

The template includes a comprehensive testing setup:

- **Unit tests**: Fast, isolated tests in `tests/unit/`
- **Integration tests**: End-to-end tests in `tests/integration/`
- **Coverage reporting**: HTML and terminal coverage reports
- **Pytest configuration**: Pre-configured in `pyproject.toml`

```bash
make test              # Run all tests
make test-unit         # Run unit tests only
make test-integration  # Run integration tests only
make coverage          # Run with coverage reporting and threshold check
make coverage-report   # Generate coverage reports without threshold
```

## 📏 Code Quality

### Linting and Formatting

- **ruff**: Fast Python linter and formatter (replaces black, isort, and multiple linters)
- **mypy**: Static type checking

```bash
make lint        # Check code quality (ruff + mypy)
make format      # Format code and auto-fix issues with ruff
```

### Configuration

All tools are configured in `pyproject.toml` with sensible defaults:

- Line length: 88 characters
- Python target: 3.10+
- Strict type checking enabled
- Comprehensive ruff rule set

## 🏗️ Project Organization Best Practices

### Package Structure

1. **Use `src/` layout**: Separates source code from tests and other files
2. **Single package**: Keep related code in one package under `src/`
3. **Clear module organization**: Separate concerns into different modules
4. **Type hints**: Use type hints throughout your code

### Development Practices

1. **Virtual environments**: Always use isolated environments
2. **Dependency management**: Pin versions in `pyproject.toml`
3. **Testing**: Write tests for all public functionality
4. **Documentation**: Document modules, classes, and functions
5. **Linting**: Run linters before committing code

### Make System Organization

The modular Makefile system separates concerns:

- **`common.mk`**: Shared variables and constants (colors, paths, thresholds)
- **`env.mk`**: Environment and dependency management
- **`lint.mk`**: Code quality checks and formatting
- **`test.mk`**: Testing targets and coverage
- **`mcp.mk`**: MCP server specific tasks

This makes the build system maintainable and extensible.

## 🔄 Workflow Examples

### Starting a New Feature

```bash
# Create feature branch
git checkout -b feature/my-feature

# Set up environment
make requirements-dev

# Write code and tests
# ...

# Check code quality
make lint test coverage

# Format code
make format

# Commit and push
git add .
git commit -m "Add my feature"
git push origin feature/my-feature
```

### Building an MCP Server

```bash
# 1. Enable MCP in pyproject.toml
# 2. Implement your server in mcp_server.py
# 3. Configure Cursor
make install-cursor

# 4. Test your MCP server
python scripts/test_mcp_client.py

# 5. Test in Cursor IDE
# Restart Cursor and test your server
```

## 🤖 LLM Context and AI Assistance

This template is designed to work well with AI coding assistants like Cursor, GitHub Copilot, and Claude. Here are some tips:

### Project Context for AI

When working with AI assistants, provide this context:

> "This is a Python project using the template-python structure. It has:
> - Source code in `src/template_python/`
> - Tests in `tests/unit/` and `tests/integration/`
> - Modular Makefile system in `make/`
> - Modern Python tooling (ruff, mypy, pytest)
> - Optional MCP server support
> - All configuration in `pyproject.toml`"

### Common AI Prompts

- **Add a new feature**: "Add a new module to handle [functionality] with proper tests and type hints"
- **Improve code quality**: "Review this code for potential improvements using ruff/mypy standards"
- **Add tests**: "Create comprehensive tests for the [module] including edge cases"
- **MCP integration**: "Help me implement an MCP tool that [describes functionality]"
- **Improve coverage**: "Help me increase test coverage to meet the threshold"

### AI-Friendly Patterns

The template follows patterns that AI assistants understand well:

- Standard Python project structure
- Clear separation of concerns
- Consistent naming conventions
- Comprehensive type hints
- Well-documented code

## 🚀 Deployment

### Packaging

```bash
# Build package
python -m build

# Install from wheel
pip install dist/template_python-0.1.0-py3-none-any.whl
```

### CI/CD

The template is ready for CI/CD systems. Example GitHub Actions workflow:

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: make requirements-dev
      - run: make lint test coverage
```

## 📚 Additional Resources

- [MCP Documentation](https://github.com/modelcontextprotocol/python-sdk)
- [pytest Documentation](https://docs.pytest.org/)
- [ruff Documentation](https://docs.astral.sh/ruff/)
- [mypy Documentation](https://mypy.readthedocs.io/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `make lint test coverage` to ensure quality
5. Submit a pull request

---

**Happy coding! 🎉**

This template provides a solid foundation for Python projects. Customize it to fit your specific needs and enjoy productive development with modern Python tooling.