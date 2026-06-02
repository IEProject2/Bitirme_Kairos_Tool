# Contributing to Factory Sim Framework

We appreciate your interest in contributing! Here's how to get started.

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/turaca-cell/factory-sim-framework.git
   cd factory-sim-framework/bitirme\ schedule
   ```

2. **Install development dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

3. **Set up pre-commit hooks (optional but recommended):**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Development Workflow

### Running Tests
```bash
# Run all tests
make test

# Run tests with coverage report
make test-cov
```

### Code Quality
```bash
# Format code
make format

# Lint code
make lint

# Type checking
make type-check

# Run all checks
make check
```

### Building Distribution
```bash
# Build wheel and source distribution
make dist
```

## Git Workflow

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Commit with clear messages: `git commit -m "Add feature X"`
4. Push to your fork: `git push origin feature/your-feature`
5. Open a Pull Request

## Code Style

- **Format:** Black (line length: 100)
- **Linting:** Ruff
- **Type hints:** MyPy (optional but appreciated)
- **Tests:** Pytest

## Pull Request Checklist

- [ ] Tests pass: `make test`
- [ ] Code is formatted: `make format`
- [ ] Linter passes: `make lint`
- [ ] Type checks pass (optional): `make type-check`
- [ ] PR has a clear description
- [ ] Changes are documented

## Running CI Locally

To run the same checks as GitHub Actions:
```bash
tox
```

Or run specific environments:
```bash
tox -e py311          # Test on Python 3.11
tox -e lint           # Run linting
tox -e type           # Run type checking
tox -e coverage       # Run with coverage report
```

## Release Process

Releases are automated via GitHub Actions on tag creation:

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create a GitHub release with tag `vX.Y.Z`
4. GitHub Actions automatically publishes to PyPI

## Questions or Issues?

- Open an issue on GitHub
- Check existing issues first

Thank you for contributing!
