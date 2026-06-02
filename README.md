# Factory Sim Framework

A constraint programming-based scheduling and simulation validation framework for multi-stage production systems. Built on SimPy, it enables reusable simulation of fixed weekly production schedules under stochastic conditions without resequencing batches.

## Features

- **SimPy-Based Simulation**: Discrete event simulation for production systems
- **Constraint Programming**: Integrate with constraint solvers for scheduling
- **Stochastic Simulation**: Validate schedules under uncertainty
- **Visualization**: Interactive Plotly visualizations of simulation results
- **Kairos Integration**: Adapter for Kairos scheduler
- **Product Tracking**: Comprehensive product flow tracking and validation
- **Type Hints**: Full type annotation support
- **Production Ready**: Comprehensive testing and documentation

## Installation

### From PyPI

```bash
pip install factory-sim-framework
```

### From Source (Development)

```bash
git clone https://github.com/turaca-cell/factory-sim-framework.git
cd factory-sim-framework/bitirme\ schedule
pip install -e .
```

### With Development Dependencies

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from factory_sim import SimulationEngine, ProductionSchedule

# Create your production system
schedule = ProductionSchedule()
schedule.add_stage("Stage 1")
schedule.add_stage("Stage 2")

# Run simulation
engine = SimulationEngine(schedule)
results = engine.run()

# Visualize results
from factory_sim.visualization import plot_results
plot_results(results)
```

## Development

### Setup

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Common Commands

```bash
# Run tests
make test

# Run tests with coverage
make test-cov

# Format code
make format

# Lint code
make lint

# Type checking
make type-check

# Build distribution
make build

# Run all checks
make check
```

### Testing Across Python Versions

```bash
# Install tox
pip install tox

# Test all environments
tox

# Test specific version
tox -e py311
```

## Documentation

For more information, see:
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [CHANGELOG.md](CHANGELOG.md) - Release history
- [examples/](examples/) - Usage examples

## Building and Releasing

### Local Build

```bash
# Build wheel and source distribution
pip install build
python -m build
```

### Release to PyPI

Releases are automated via GitHub Actions. To release:

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create a GitHub release with tag `vX.Y.Z`
4. GitHub Actions automatically publishes to PyPI

See [CONTRIBUTING.md](CONTRIBUTING.md#release-process) for details.

## License

MIT - See LICENSE file for details

## Authors

- Alen Maryo Turaç

## Citation

If you use this framework in research, please cite:
```bibtex
@software{factory-sim-framework,
  title={Factory Sim Framework: Constraint Programming-Based Scheduling and Simulation Validation},
  author={Turaç, Alen Maryo},
  year={2024},
  url={https://github.com/turaca-cell/factory-sim-framework}
}
```

## Support

- 📧 Email: turaca@mef.edu.tr
- 🐛 Issues: [GitHub Issues](https://github.com/turaca-cell/factory-sim-framework/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/turaca-cell/factory-sim-framework/discussions)
