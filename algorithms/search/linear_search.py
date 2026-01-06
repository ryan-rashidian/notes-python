"""Demonstration of the linear search algorithm."""


def linear_search(lst: list, target) -> int | None:
    """Linear search."""
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i

    return None

