from algorithms.core import bubble_sort, insertion_sort

# Small example test array
A = [5, 2, 4, 6, 1, 3]


def test_insertion_sort_small() -> None:
    assert insertion_sort(A, len(A)) == [1, 2, 3, 4, 5, 6]


def test_bubble_sort_small() -> None:
    assert bubble_sort(A, len(A)) == [1, 2, 3, 4, 5, 6]
