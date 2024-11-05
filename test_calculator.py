# FILE: /TDD/test_calculator.py

import unittest
from calculator import sum_sum

class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_should_return_10(self): #1: ##
        self.assertEqual(sum_sum(5, 5), 10) ##

    def test_sum_5_negative_and_5_should_return_0(self):
        self.assertEqual(sum_sum(-5, 5), 0)

    def test_sum_multiple_entries(self): ##
        x_y_outputs = (
            (10, 10, 20),
            (15, 15, 30),
            (15.5, 15.5, 31.0),
            (10, 10, 25),
            (1, 2, 3),
        )

        for i in x_y_outputs: ##
            with self.subTest(i=x_y_outputs): ##
                x, y, outputs = i
                self.assertEqual(sum_sum(x, y), outputs) ##

    def test_sum_x_is_not_int_or_float_should_return_assertionerror(self): ##
        with self.assertRaises(AssertionError): ##
            sum_sum('10', 5)

unittest.main(verbosity=2) ##


#1: Os nomes devem ser enormes? Parece que por convenção, sim!

# https://linktr.ee/edsoncopque