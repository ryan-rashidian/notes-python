"""Demonstration of the Dependency Injection pattern.

Dependency injection is useful for designing flexible APIs, where
different behaviors can be accessed from a single callable.

In this demonstration, an export function is passed to the client.
The `export` method 'depends' on a function object, allowing its
behavior to be easily swapped.
"""

from typing import Callable


def export_to_csv(data) -> None:
    """Simulated export function."""
    print(f'{data} exported to /exports/data')


class APIWrapper:
    """Simulated API wrapper."""

    def request(self, endpoint: str) -> None:
        print(f'Requesting data from {endpoint}...')
        self.data = {'A': 1, 'B': 2, 'C': 3}

    def export(self, export_fn: Callable) -> None:
        export_fn(self.data)


if __name__ == '__main__':
    client = APIWrapper()
    client.request('endpoint/data')
    client.export(export_to_csv)

