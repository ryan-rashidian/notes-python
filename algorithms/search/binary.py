"""Demonstration of the binary search algorithm."""


def binary_search(lst: list[int], target) -> int | None:
    """Iterative binary search."""
    target_lst = sorted(lst)
    min = 0
    max = len(target_lst) - 1

    while min <= max:
        mid = (min + max) // 2
        if target_lst[mid] == target:
            return mid
        elif target_lst[mid] > target:
            max = mid - 1
        else:
            min = mid + 1

    return None

