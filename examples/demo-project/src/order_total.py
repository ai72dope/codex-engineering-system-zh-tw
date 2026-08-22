from typing import Iterable

def calculate_order_total(prices: Iterable[float], quantity: int = 1) -> float:
    """Calculate the total price for a quantity of identical baskets."""
    subtotal = sum(prices)
    return round(subtotal * quantity, 2)
