# Kairos Scheduler

Industrial Job Shop Scheduling Library using Google OR-Tools CP-SAT.

## Features

- **Clean Architecture**: Modular domain, solver, data, and visualization layers
- **Multiple Solvers**: CP-SAT (full optimization), SPT/LPT/EDD (heuristics)
- **Smart Compatibility**: Solvers reject incompatible problem types automatically
- **Sequence-Dependent Setup Times**: Machine-specific setup matrices
- **Excel Import**: Load problems from Excel files
- **Gantt Visualization**: Plotly-based schedule visualization

## Installation

```bash
pip install -e .
```

## Quick Start

```python
import kairos as kr

# Create problem
problem = kr.SchedulingProblem()

# Add machines
problem.add_machine(kr.Machine(id=1, name="Lathe"))
problem.add_machine(kr.Machine(id=2, name="CNC"))

# Add tasks
task1 = kr.Task(id=101, name="Part_A", task_type=0)
task1.add_alternative(machine_id=1, duration=100)
task1.add_alternative(machine_id=2, duration=80)
problem.add_task(task1)

# Solve
solver = kr.SolverFactory.get_solver(kr.SolverType.CP_SAT)
result = solver.solve(problem)
print(f"Makespan: {result.objective_value}")
```

## License

Proprietary - See LICENSE file for details.
