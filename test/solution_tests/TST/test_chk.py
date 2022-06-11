from lib.solutions.CHK import checkout_solution
import unittest


class TestCHK(unittest.TestCase):
    def test_checkout(self):
        assert checkout_solution.checkout('3A') == 130




