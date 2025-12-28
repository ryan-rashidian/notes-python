"""Search algorithm demonstrations."""


def linear_search(lst: list, target) -> int | None:
    """Linear search."""
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i

    return None


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

