"""Demonstration of hash tables in Python.

Python's dictionary object is a built-in hash table interface.
CPython's implementation of a hash table is already highly optimized.

This code creates a hash table interface for the purpose of demonstration.
"""

from typing import Iterator

TABLE_SIZE = 16


def _hash_key(key: str) -> int:
    """Simple hash function.
    
    This example is prone to collision, but shows the general idea.
    """
    total = 0
    for ch in key:
        total += ord(ch) - (ord('A') - 1)
    return int(total / len(key)) % TABLE_SIZE


class Item:
    """Element for HashT."""

    def __init__(self, key: str, value: int) -> None:
        self.key = key
        self.value = value

    def __eq__(self, other) -> bool:
        return self.key == other.key

    def __hash__(self) -> int:
        return _hash_key(self.key)


class HashT:
    """Hash Table object."""

    def __init__(self) -> None:
        """Initialize table with TABLE_SIZE slots."""
        self.table_arr: list[list[Item]] = [[] for _ in range(TABLE_SIZE)]

    def __len__(self) -> int:
        total_len = 0
        for slot in self.table_arr:
            total_len += len(slot)
        return total_len

    def __iter__(self) -> Iterator:
        for table_slot in self.table_arr:
            for item in table_slot:
                yield item.key

    def __getitem__(self, key: str) -> int | None:
        idx = hash(Item(key, 0))
        table_slot = self.table_arr[idx]
        for item in table_slot:
            if item.key == key:
                return item.value

    def __setitem__(self, key: str, value: int) -> None:
        new_item = Item(key, value)
        table_slot = self.table_arr[hash(new_item)]
        for item in table_slot:
            if item == new_item: # Using __eq__ method in Item
                item.value = value
                return None
        table_slot.append(new_item)

    def __delitem__(self, key: str) -> None:
        idx = hash(Item(key, 0))
        table_slot = self.table_arr[idx]
        for i, item in enumerate(table_slot):
            if item.key == key:
                del table_slot[i]
                return
        raise KeyError(key)

    def __contains__(self, key: str) -> bool:
        idx = hash(Item(key, 0))
        return any(item.key == key for item in self.table_arr[idx])

    def items(self) -> Iterator[tuple[str, int]]:
        for table_slot in self.table_arr:
            for item in table_slot:
                yield (item.key, item.value)

