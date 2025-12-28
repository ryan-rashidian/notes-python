"""Demonstration of the event sourcing pattern.

Source: YouTube - ArjanCodes
This code was written while following a tutorial series
"""

from event_store import EventStore
from inventory import Inventory
from item import Item


def main() -> None:
    store = EventStore()
    inventory = Inventory(store)

    watch = Item(name='watch', rarity='medium', origin='home')
    book = Item(name='book', rarity='low', origin='library')
    pen = Item(name='pen', rarity='low', origin='office')
    match = Item(name='match', rarity='very low', origin='corner store')

    inventory.add_item(watch)
    inventory.add_item(book)
    inventory.add_item(pen)
    inventory.add_item(match)
    inventory.add_item(match)
    inventory.add_item(match)
    inventory.remove_item(match)

    print(inventory.get_items())
    print(inventory.get_count('match'))


if __name__ == '__main__':
    main()

