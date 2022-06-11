from lib.solutions.CHK import checkout_solution
import unittest


class TestCHK(unittest.TestCase):
    def test_checkout(self):
        assert checkout_solution.checkout('') == -1
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('AAAAAABC') == 310
        assert checkout_solution.checkout('ABBBB') == 140



