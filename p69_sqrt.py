import math
import unittest

"""
69. Sqrt(x)

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))


class SqrtTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_sqrt(self):
        res = self.obj.mySqrt(8)
        expected = 2
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
