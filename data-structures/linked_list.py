"""Demonstration of a linked list in Python."""


class Node:
    """Object for storing a single node of a linked list."""

    def __init__(self, data):
        self.data = data
        self.next_node: Node | None = None

    def __repr__(self) -> str:
        return f'<Node>: {self.data}'


class LinkedList:
    """Singly linked list."""

    def __init__(self):
        self.head: Node | None = None

    def __repr__(self) -> str:
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f'[Head: {current.data}]')
            elif current.next_node is None:
                nodes.append(f'[Tail: {current.data}]')
            else:
                nodes.append(f'[{current.data}]')

            current = current.next_node

        return '-> '.join(nodes)

    def __bool__(self) -> bool:
        return self.head is not None

    def __len__(self) -> int:
        current = self.head
        
        count = 0
        while current:
            count += 1
            current = current.next_node

        return count

    def __getitem__(self, index: int) -> Node | None:
        if index == 0:
            return self.head
        if index > 0:
            current = self.head

            while index >= 1 and current:
                current = current.next_node
                index -= 1

            return current

    def add(self, data) -> None:
        """Adds a new node containing data at head of the list.
        0(1) constant time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key) -> Node | None:
        """Search for first node containing data that matches key.
        0(n) linear time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None

    def insert(self, data, index: int) -> None:
        """Insert a new node containing data at index position.
        0(n) linear time
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1 and current:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node if current else None

            if prev_node:
                prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key) -> Node | None:
        """Removes node containing data that matches the key.
        0(n) linear time
        """
        current = self.head
        previous: Node | None = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                if previous:
                    previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

