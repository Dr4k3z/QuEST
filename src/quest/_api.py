"""Thin Python wrappers around the compiled nanobind extension."""

from ._quest_core import add as _add


def add(a: int, b: int) -> int:
    """Add two integers using the compiled backend."""
    return _add(a, b)


def add_10_times(a: int, b: int) -> int:
    """Apply add(a, b) ten times and return the accumulated result."""
    total = 0
    for _ in range(10):
        total = _add(total, _add(a, b))
    return total
