from lib.solutions.CHK import checkout_solution
import unittest


class TestCHK(unittest.TestCase):
    def test_checkout(self):
        assert checkout_solution.checkout('') == 0
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('AAABC') == 180
        assert checkout_solution.checkout('AXA') == -1
        assert checkout_solution.checkout('ABBBB') == 140
        assert checkout_solution.checkout('AAAA') == 180


