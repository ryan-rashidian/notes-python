"""Demonstration of the breadth-first search algorithm."""

from collections import deque

search_target = 'jon'

friend_group = {
    'you': ['bob', 'jane'],
    'bob': ['alice', 'jane'],
    'peggy': ['tom', 'jon'],
    'alice': ['peggy'],
    'jane': [],
    'tom': [],
    'jon': []
}


def breadth_first_search(graph: dict, name: str) -> bool:
    """Search your friend group."""
    search_queue = deque()
    search_queue += graph['you']
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person == name:
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


if __name__ == '__main__':
    if breadth_first_search(friend_group, search_target):
        print(f'{search_target} is in your group.')
    else:
        print(f'{search_target} is NOT in your group.')

