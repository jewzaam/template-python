# Generated-by: Cursor (claude-4-sonnet)
"""
Unit tests for the main module.
"""

import logging
from io import StringIO
from unittest.mock import patch

import pytest

from template_python.main import main


def test_main_help():
    """Test that main shows help when no arguments provided."""
    with (
        patch("sys.argv", ["main"]),
        patch("sys.stdout", new_callable=StringIO) as mock_stdout,
    ):
        result = main([])
        assert result == 0
        # Help should be displayed
        output = mock_stdout.getvalue()
        assert "Python Template Project" in output


def test_main_example(caplog):
    """Test the example functionality."""
    with caplog.at_level(logging.INFO):
        result = main(["--example"])
        assert result == 0
        # Check that the expected log messages were recorded
        assert "Hello from the Python Template Project!" in caplog.text


def test_main_log_level():
    """Test setting log level."""
    result = main(["--log-level", "DEBUG", "--example"])
    assert result == 0


@pytest.mark.parametrize("log_level", ["DEBUG", "INFO", "WARNING", "ERROR"])
def test_valid_log_levels(log_level):
    """Test all valid log levels."""
    result = main(["--log-level", log_level, "--example"])
    assert result == 0
