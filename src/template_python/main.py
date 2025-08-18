# Generated-by: Cursor (claude-4-sonnet)
"""
Main application module.

This is an example entry point for your application.
Customize this file based on your project's needs.
"""

import argparse
import logging


def setup_logging(level: str = "INFO") -> None:
    """Set up logging configuration."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def main(args: list[str] | None = None) -> int:
    """Main application entry point."""
    parser = argparse.ArgumentParser(
        description="Python Template Project",
        epilog="This is a template - customize for your needs!",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Set the logging level",
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Run example functionality",
    )

    parsed_args = parser.parse_args(args)
    setup_logging(parsed_args.log_level)

    logger = logging.getLogger(__name__)
    logger.info("Starting Python Template Project")

    if parsed_args.example:
        logger.info("Running example functionality...")
        print("🎉 Hello from the Python Template Project!")
        print("✨ This is an example - customize src/template_python/main.py")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    exit(main())
