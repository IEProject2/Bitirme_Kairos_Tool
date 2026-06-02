# Validation Plan

## JSPLIB Benchmark Validation

JSPLIB validation is a benchmark-only mode for the core deterministic job-shop
scheduling logic. It uses fixed machine routings, positive processing times,
operation precedence within each job, and machine no-overlap constraints.

This mode deliberately does not validate project-specific production features:
due dates, priority weights, setup times, workforce constraints, flexible
machine assignment, or stochastic simulation behavior. Those remain part of the
real project model and are validated separately.

The OR-Library/JSPLIB `ft06` instance is included because its known optimal
makespan is 55. Passing `ft06` means the solver correctly handles:

- operation precedence inside each job
- machine no-overlap
- start and end time calculation
- makespan minimization
- complete schedule extraction

Run the benchmark validation with:

```bash
python -m src.validation.jsplib_runner benchmarks/jsplib/ft06.txt
```

Run that command from the `bitirme schedule` directory. From the repository's
outer directory, use the integrated launcher and choose
`Validate core job-shop solver with JSPLIB ft06`:

```bat
launch_visual_factory_tool.bat
```

Expected key output:

```text
Solver status: OPTIMAL
Makespan: 55
Schedule feasibility passed: True
ft06 optimum check passed: True
```

## Weighted Tardiness Validation

Weighted tardiness is not part of JSPLIB. It is validated separately with a
manual single-machine example:

- Job A has processing time 4, due date 5, and weight 10.
- Job B has processing time 3, due date 4, and weight 1.
- Sequence A -> B has total weighted tardiness 3.
- Sequence B -> A has total weighted tardiness 20.

The expected optimal weighted-tardiness sequence is A before B. Later validation
can add OR-Library weighted tardiness data for broader benchmark coverage.

## Simulation Validation

Simulation validation should replay a deterministic optimizer schedule with
randomness disabled first. Simulated completion times should match the optimizer
schedule exactly before stochastic variability, breakdown sampling, or random
processing-time distributions are introduced.
