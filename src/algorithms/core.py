def insertion_sort(A: list, n: int) -> list:
    """Sorting algorithm, with the goal of a permutation of the input array in descending order
    Time complexity: 𝚯(n^2)

    Args:
        A (list): Array of numbers to sort
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
                temp = A[j]
                A[j - 1] = temp
                A[j] = A[j - 1]
    return A
