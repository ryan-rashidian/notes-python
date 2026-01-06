"""Demonstration of the selection sort algorithm."""


def find_smallest(lst: list[int]) -> int: 
    """Find the smallest value in a list."""
    smallest = lst[0]
    smallest_idx = 0
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            smallest_idx = i
    return smallest_idx


def selection_sort(lst: list[int]) -> list[int]:
    """Selection sort algorithm."""
    new_lst = []
    copied_lst = lst.copy()
    for _ in range(len(copied_lst)):
        smallest = find_smallest(copied_lst)
        new_lst.append(copied_lst.pop(smallest))
    return new_lst

