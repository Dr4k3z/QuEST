import numpy as np
import pytest

from quest import add, add_10_times, vector_dot


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 50),
        (-1, 1, 0),
        (1, -2, -10),
    ],
)
def test_add_10_times(a: int, b: int, expected: int) -> None:
    assert add_10_times(a, b) == expected


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        (
            np.array([1.0, 2.0, 3.0], dtype=np.float64),
            np.array([4.0, 5.0, 6.0], dtype=np.float64),
            32.0,
        ),
        (
            np.array([[1.0], [2.0], [3.0]], dtype=np.float64),
            np.array([[1.0], [2.0], [3.0]], dtype=np.float64),
            14.0,
        ),
        (
            np.array([[1.0, 2.0, 3.0]], dtype=np.float64),
            np.array([[1.0, 2.0, 3.0]], dtype=np.float64),
            14.0,
        ),
    ],
)
def test_vector_dot_valid_shapes(x: np.ndarray, y: np.ndarray, expected: float) -> None:
    assert vector_dot(x, y) == pytest.approx(expected)


def test_vector_dot_mismatched_length_raises() -> None:
    x = np.array([1.0, 2.0], dtype=np.float64)
    y = np.array([1.0, 2.0, 3.0], dtype=np.float64)
    with pytest.raises(ValueError, match="same length"):
        vector_dot(x, y)


def test_vector_dot_invalid_shape_raises() -> None:
    x = np.ones((2, 2), dtype=np.float64)
    with pytest.raises(ValueError, match="shape"):
        vector_dot(x, x)
