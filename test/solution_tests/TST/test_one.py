from lib.solutions.TST import one
import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        assert one.get() == 1
