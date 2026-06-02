"""Custom build script for factory-sim-framework."""

import sys
from pathlib import Path


def check_python_version():
    """Ensure Python 3.11+ is being used."""
    if sys.version_info < (3, 11):
        print("Error: Python 3.11+ is required")
        sys.exit(1)


def check_dependencies():
    """Check that required build dependencies are installed."""
    try:
        import setuptools
        import wheel
    except ImportError as e:
        print(f"Error: Missing required dependency: {e}")
        print("Install with: pip install setuptools wheel build")
        sys.exit(1)


def main():
    """Run build checks."""
    check_python_version()
    check_dependencies()
    print("✓ All pre-build checks passed")


if __name__ == "__main__":
    main()
