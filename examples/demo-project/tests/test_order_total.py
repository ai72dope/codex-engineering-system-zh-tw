import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.order_total import calculate_order_total

class OrderTotalTests(unittest.TestCase):
    def test_calculates_total(self) -> None:
        self.assertEqual(calculate_order_total([10.0, 20.0], 2), 60.0)

    def test_empty_prices_returns_zero(self) -> None:
        self.assertEqual(calculate_order_total([], 3), 0.0)

if __name__ == "__main__":
    unittest.main()
