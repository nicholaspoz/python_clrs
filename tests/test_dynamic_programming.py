import unittest

from python_clrs.dynamic_programming.fib import fib


class FibTests(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(fib(0), 1)
        self.assertEqual(fib(1), 1)

    def test_fib(self):
        # 1 1 2 3 5 8 13
        self.assertEqual(fib(6), 13)
        self.assertEqual(fib(7), 21)
