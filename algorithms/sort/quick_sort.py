"""Demonstration of the quicksort algorithm."""

def quicksort(lst: list[int]) -> list[int]:
    """Quicksort"""
    if len(lst) < 2:
        # Base case
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

