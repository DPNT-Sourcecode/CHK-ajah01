from lib.solutions.CHK import checkout_solution
import unittest


class TestCHK(unittest.TestCase):
    def test_sum(self):
        assert checkout_solution.checkout('AB') == 80
