import unittest

"""
29. Divide Two Integers

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
    -231 <= dividend, divisor <= 231 - 1
    divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2** 31:
            return -2 ** 31
        else:
            return res


class DivideTwoIntTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_divide(self):
        res = self.obj.divide(10, 3)
        expected = 3
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
