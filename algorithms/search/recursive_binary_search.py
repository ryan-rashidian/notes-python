"""Demonstration of the recursive binary search algorithm."""


def recursive_binary_search(lst: list, target) -> bool:
    """Recursive binary search."""
    if len(lst) == 0:
        return False
    else:
        mid = len(lst) // 2

    if lst[mid] == target:
        return True
    else:
        if lst[mid] < target:
            return recursive_binary_search(lst[mid + 1:], target)
        else:
            return recursive_binary_search(lst[:mid - 1], target)

