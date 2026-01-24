import pytest

from algorithms.core import fib


def test_fib_small() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(5) == 5


def test_fib_rejects_negative() -> None:
    with pytest.raises(ValueError):
        fib(-1)
