import unittest

"""
371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])


class SumIntTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_sum_integers(self):
        res = self.obj.getSum(2, 3)
        expected = 5
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')
