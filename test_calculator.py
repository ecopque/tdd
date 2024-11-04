# FILE: /TDD/test_calculator.py

import unittest
from calculator import sum_sum

class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_should_return_10(self): #1:
        self.assertEqual(sum_sum(5, 5), 10)

    def test_sum_5_negative_and_5_should_return_0(self):
        self.assertEqual(sum_sum(-5, 5), 1)

unittest.main(verbosity=2)


#1: Os nomes devem ser enormes? Parece que por convenção, sim!

# https://linktr.ee/edsoncopque