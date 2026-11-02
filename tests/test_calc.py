# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
from decimal import Decimal
import unittest
from calc import calculate

class CalculatorTests(unittest.TestCase):
    def test_decimal_exactness(self):
        self.assertEqual(calculate("add", "0.1", "0.2"), Decimal("0.3"))
    def test_operations(self):
        self.assertEqual(calculate("subtract", "8", "3"), Decimal("5"))
        self.assertEqual(calculate("multiply", "2", "3"), Decimal("6"))
        self.assertEqual(calculate("divide", "6", "2"), Decimal("3"))
    def test_legacy_alias(self):
        self.assertEqual(calculate("substract", "5", "3"), Decimal("2"))
    def test_errors(self):
        for args in (("divide", "1", "0"), ("add", "abc", "1"), ("add", "NaN", "1")):
            with self.assertRaises(ValueError):
                calculate(*args)

if __name__ == "__main__":
    unittest.main()
