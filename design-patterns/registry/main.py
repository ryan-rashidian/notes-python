"""Demonstration of the registery design pattern.

Credit to: YouTube - ArjanCodes
This code was written while following a tutorial series
"""

from typing import Callable
from functools import wraps

type Func = Callable[[str], None]

registry: dict[str, Func] = {}


def register_foo(name: str):
    def decorator(func: Func) -> Func:
        registry[name] = func

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
    return decorator


@register_foo('A')
def foo_a(data: str) -> None:
    print(f'A: {data}')


@register_foo('B')
def foo_b(data: str) -> None:
    print(f'B: {data}')


@register_foo('C')
def foo_c(data: str) -> None:
    print(f'C: {data}')


def get_foo(data: str, select: str) -> None:
    func = registry.get(select)
    if func is None:
        raise ValueError(f'Not found: {select}')
    func(data)


def main() -> None:
    data = 'Hello Registry'

    get_foo(data, 'A')
    get_foo(data, 'B')
    get_foo(data, 'C')


if __name__ == '__main__':
    main()

