from math import floor


def insertion_sort(A: list, n: int) -> list:
    """Sorting algorithm, with the goal of a permutation of the input array in descending order
    Time complexity: 𝚯(n^2)

    Args:
        A (list): Input array
        n (int): Number of elements

    Returns:
        list: The array sorted
    """
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A


def bubble_sort(A: list, n: int) -> list:
    """Sorting algorithm, with the goal of a permutation of the input array in descending order
    Time complexity 𝚯(n^2)

    Args:
        A (list): Input array
        n (int): Number of elements

    Returns:
        list: The sorted array
    """
    for i in range(n - 1):
        for j in range(n - 1, 0, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A


def merge(A, p, q, r):
    n_L = q - p + 1
    n_R = r - q
    L = [None] * n_L
    R = [None] * n_R

    for i in range(n_L):
        L[i] = A[p + i]

    for j in range(n_R):
        R[j] = A[q + j + 1]

    i = 0
    j = 0
    k = p

    while i < n_L and j < n_R:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1

    while i < n_L:
        A[k] = L[i]
        i = i + 1
        k = k + 1

    while j < n_R:
        A[k] = R[j]
        j = j + 1
        k = k + 1


def merge_sort(A, p, r):
    if p >= r:
        return
    q = floor((p + r) / 2)
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)
