# Generated-by: Cursor (claude-4-sonnet)
"""
Example integration tests.

These tests verify that different components work together correctly.
"""

import subprocess
import sys
from pathlib import Path


def test_main_module_executable():
    """Test that the main module can be executed."""
    result = subprocess.run(
        [sys.executable, "-m", "template_python.main", "--help"],
        check=False,
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent.parent / "src",
    )
    assert result.returncode == 0
    assert "Python Template Project" in result.stdout


def test_package_import():
    """Test that the package can be imported successfully."""
    import template_python

    assert hasattr(template_python, "__version__")
    assert template_python.__version__ == "0.1.0"
