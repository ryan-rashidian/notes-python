"""Demonstration of how Enums are used in Python."""

from enum import Enum


class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELED = 5


def advance_status(status: OrderStatus) -> OrderStatus:
    transistions = {
        OrderStatus.PENDING: OrderStatus.PROCESSING,
        OrderStatus.PROCESSING: OrderStatus.SHIPPED,
        OrderStatus.SHIPPED: OrderStatus.DELIVERED,
    }
    return transistions.get(status, status)

