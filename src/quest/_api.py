"""Thin Python wrappers around the compiled nanobind extension."""

import numpy as np

from ._quest_core import add as _add
from ._quest_core import vector_dot as _vector_dot


def add(a: int, b: int) -> int:
    """Add two integers using the compiled backend."""
    return _add(a, b)


def add_10_times(a: int, b: int) -> int:
    """Apply add(a, b) ten times and return the accumulated result."""
    total = 0
    for _ in range(10):
        total = _add(total, _add(a, b))
    return total


def _as_1d_float64_vector(x) -> np.ndarray:
    arr = np.asarray(x, dtype=np.float64)
    if arr.ndim == 1:
        return arr
    if arr.ndim == 2 and (arr.shape[0] == 1 or arr.shape[1] == 1):
        return arr.reshape(-1)
    raise ValueError("vector_dot expects 1D input or 2D input with shape (n,1) or (1,n)")


def vector_dot(x, y) -> float:
    """Compute the dot product of two vectors."""
    return _vector_dot(_as_1d_float64_vector(x), _as_1d_float64_vector(y))
