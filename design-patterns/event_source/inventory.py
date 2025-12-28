"""Main inventory."""

from collections import Counter
from event import Event, EventType
from event_store import EventStore
from functools import lru_cache
from item import Item



class Inventory:
    def __init__(self, store: EventStore[Item]) -> None:
        self.store = store

    def add_item(self, item: Item) -> None:
        self.store.append(Event(EventType.ITEM_ADDED, item))
        self._clear_cache()

    def remove_item(self, item: Item) -> None:
        if self.get_count(item.name) <= 0:
            raise ValueError(f'{item} not in inventory')
        self.store.append(Event(EventType.ITEM_REMOVED, item))
        self._clear_cache()

    def _clear_cache(self) -> None:
        self.get_items.cache_clear()

    @lru_cache(maxsize=2)
    def get_items(self) -> list[tuple[str, int]]:
        counts = Counter[str]()
        for event in self.store.get_all_events():
            name = event.data.name
            if event.type == EventType.ITEM_ADDED:
                counts[name] += 1
            elif event.type == EventType.ITEM_REMOVED:
                counts[name] -= 1

        return [(item, count) for item, count in counts.items() if count > 0]

    def get_count(self, item: str) -> int:
        return dict(self.get_items()).get(item, 0)

