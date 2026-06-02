.PHONY: help install install-dev test test-cov lint format type-check clean build dist \
         cli-run gui-run exe-cli exe-gui installer run-cli run-gui check

help:
	@echo "Available commands:"
	@echo "  make install       - Install the package"
	@echo "  make install-dev   - Install with dev dependencies"
	@echo "  make test          - Run tests"
	@echo "  make test-cov      - Run tests with coverage report"
	@echo "  make lint          - Run ruff linter"
	@echo "  make format        - Format code with black"
	@echo "  make type-check    - Run type checking with mypy"
	@echo "  make clean         - Remove build artifacts"
	@echo "  make build         - Build distribution packages"
	@echo "  make dist          - Create distribution (wheel + sdist)"
	@echo ""
	@echo "Application & Packaging:"
	@echo "  make run-cli       - Run CLI application"
	@echo "  make run-gui       - Run GUI application (web)"
	@echo "  make exe-cli       - Build CLI executable"
	@echo "  make exe-gui       - Build GUI executable"
	@echo "  make installer     - Build Windows installer"
	@echo "  make exe           - Build all executables"
	@echo "  make check         - Run all quality checks"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

test:
	pytest

test-cov:
	pytest --cov=factory_sim --cov-report=html --cov-report=term-missing

lint:
	ruff check .

format:
	black .

type-check:
	mypy factory_sim

clean:
	rm -rf build dist *.egg-info .pytest_cache .coverage htmlcov .mypy_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pyinstaller 2>/dev/null || true

build: clean
	python -m build

dist: clean
	python -m build

run-cli:
	python -m factory_sim.cli

run-gui:
	streamlit run factory_sim/gui.py

exe-cli:
	python build_executable.py cli

exe-gui:
	python build_executable.py gui

exe: clean
	python build_executable.py

installer:
	pyinstaller --clean factory_sim_cli.spec --onefile --distpath=dist/cli
	pyinstaller --clean factory_sim_gui.spec --onefile --distpath=dist/gui
	@if command -v makensis >/dev/null 2>&1; then \
		makensis windows_installer.nsi; \
	else \
		echo "NSIS not installed. Windows installer skipped."; \
	fi

check: lint type-check test
	@echo "All checks passed!"
