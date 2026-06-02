# Build and Packaging Guide

This guide covers building, testing, and distributing Factory Sim Framework.

## Table of Contents

1. [Installation](#installation)
2. [Development Setup](#development-setup)
3. [Building](#building)
4. [Testing](#testing)
5. [Distribution](#distribution)
6. [Docker](#docker)

## Installation

### User Installation (From PyPI)

```bash
pip install factory-sim-framework
```

### Development Installation

```bash
git clone https://github.com/yourusername/factory-sim-framework.git
cd factory-sim-framework/bitirme\ schedule
pip install -e .
```

### With Optional Dependencies

```bash
# Development tools
pip install -e ".[dev]"

# Documentation
pip install -e ".[docs]"

# All extras
pip install -e ".[dev,docs]"
```

## Development Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install with Development Dependencies

```bash
pip install -e ".[dev]"
```

### 3. Set Up Pre-commit Hooks (Optional)

```bash
pip install pre-commit
pre-commit install
```

This will run code quality checks before each commit.

### 4. Install Build Tools

```bash
pip install build wheel twine
```

## Building

### Quick Build

```bash
make build
```

This creates:
- `dist/factory_sim_framework-0.1.0-py3-none-any.whl` (wheel)
- `dist/factory_sim_framework-0.1.0.tar.gz` (source distribution)

### Manual Build

```bash
python -m build
```

### Custom Build with build.py

```bash
python build.py
```

### Check Distribution

```bash
twine check dist/*
```

This verifies wheel and sdist are valid.

## Testing

### Run All Tests

```bash
make test
```

### Run with Coverage

```bash
make test-cov
```

Generates HTML coverage report in `htmlcov/index.html`

### Test Multiple Python Versions

```bash
# Install tox
pip install tox

# Test all configured versions
tox

# Test specific version
tox -e py311,py312
```

### Lint and Format

```bash
# Check code style
make lint

# Auto-format code
make format

# Type checking
make type-check

# All checks
make check
```

## Distribution

### Build Distribution

```bash
make dist
```

### Test Installation

```bash
# Create a test virtual environment
python -m venv test_env
source test_env/bin/activate

# Install from local wheel
pip install dist/factory_sim_framework-0.1.0-py3-none-any.whl

# Test import
python -c "from factory_sim import SimulationEngine; print('Success!')"
```

### Upload to PyPI (Automated)

Automated via GitHub Actions when you:
1. Update version in `pyproject.toml`
2. Create a GitHub release with tag `vX.Y.Z`

For manual upload:

```bash
# Test PyPI (requires account)
twine upload --repository testpypi dist/*

# Production PyPI
twine upload dist/*
```

## Docker

### Build Docker Image

```bash
docker build -t factory-sim-framework:latest .
```

### Run Container

```bash
docker run -it factory-sim-framework:latest
```

### Docker Compose

```bash
# Build and run
docker-compose up

# Run tests in container
docker-compose run test
```

### Build Multi-platform Images

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t factory-sim:latest .
```

## Version Management

Update version in:
1. `pyproject.toml` - `version = "X.Y.Z"`
2. `CHANGELOG.md` - Add release notes
3. Create GitHub release with tag `vX.Y.Z`

## Release Checklist

- [ ] Update `pyproject.toml` with new version
- [ ] Update `CHANGELOG.md`
- [ ] Run full test suite: `tox`
- [ ] Run code quality checks: `make check`
- [ ] Build distribution: `make dist`
- [ ] Check distribution: `twine check dist/*`
- [ ] Commit changes
- [ ] Create Git tag: `git tag vX.Y.Z`
- [ ] Push to GitHub: `git push --tags`
- [ ] Create GitHub Release (triggers PyPI publish)

## Troubleshooting

### Build Fails

```bash
# Clean build artifacts
make clean

# Rebuild
make dist
```

### Test Failures

```bash
# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_framework.py -v

# Debug with pdb
pytest tests/test_framework.py --pdb
```

### Import Errors After Install

```bash
# Reinstall in development mode
pip uninstall factory-sim-framework
pip install -e .
```

### Docker Build Issues

```bash
# Build with no cache
docker build --no-cache -t factory-sim-framework .

# View build output
docker build -t factory-sim-framework . --progress=plain
```

## Additional Resources

- [pyproject.toml Documentation](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [setuptools Documentation](https://setuptools.pypa.io/)
- [Wheel Documentation](https://wheel.readthedocs.io/)
- [Twine Documentation](https://twine.readthedocs.io/)
