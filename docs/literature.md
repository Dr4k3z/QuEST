# Ledoit-Wolf Literature and Code References

Initial reference set for building a high-performance QuEST port.

## Core papers

1. Ledoit, O. and Wolf, M. (2004).
   *A well-conditioned estimator for large-dimensional covariance matrices*.
   Journal of Multivariate Analysis, 88(2), 365-411.

2. Ledoit, O. and Wolf, M. (2012).
   *Nonlinear shrinkage estimation of large-dimensional covariance matrices*.
   Annals of Statistics, 40(2), 1024-1060.

3. Ledoit, O. and Wolf, M. (2015).
   *Spectrum estimation: A unified framework for covariance matrix estimation and PCA in large dimensions*.
   Journal of Multivariate Analysis, 139, 360-384.

4. Ledoit, O. and Wolf, M. (2017).
   *Numerical implementation of the QuEST function*.
   Computational Statistics & Data Analysis, 115, 199-223.
   DOI: 10.1016/j.csda.2017.06.004.

5. Ledoit, O. and Wolf, M. (2020).
   *Analytical nonlinear shrinkage of large-dimensional covariance matrices*.
   Annals of Statistics, 48(5), 3043-3065.
   DOI: 10.1214/19-AOS1921.

## Code source

- Official shrinkage package (MATLAB/R/Python):
  https://github.com/oledoit/covShrinkage

  This repository is linked from MathWorks File Exchange entry `covShrinkage`
  (version 1.1.0, updated Feb 5, 2022).

## Porting focus for this project

1. Reproduce QuEST numerical outputs against reference MATLAB implementation.
2. Implement Jacobian and inversion routines with robust convergence behavior.
3. Optimize for large `p` and `n` using vectorization + cache-aware loops.
4. Expose a stable Python API via nanobind while keeping C++ core independent.
5. Build a benchmark suite for correctness and speed regressions.
