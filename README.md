# QuEST

`quest-rmt` is an in-progress, high-performance implementation of the QuEST function
(Quantized Eigenvalues Sampling Transform) for nonlinear shrinkage of covariance matrices.

## Scope

This repository is being built as:
- A C++ core implementation focused on numerical performance.
- A Python package with nanobind bindings for research and production workflows.

## Current status

The package skeleton and extension build pipeline are in place.
The QuEST numerical kernels and validation suite are the next milestones.

## Development

Create a virtual environment and install in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

Quick sanity check:

```bash
python -c "import quest; print(quest.add(2, 3))"
```
