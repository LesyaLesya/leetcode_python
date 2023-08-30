import unittest


"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
    -231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        minus = ''
        if len(s) == 1:
            return x
        if s[0] == '-':
            minus = '-'
            s.remove('-')
        if s[-1] == '0':
            s.pop(-1)
        res = int(minus + ''.join(list(s))[::-1])
        if res >= 2 ** 31 - 1 or res <= -2 ** 31:
            return 0
        else:
            return res


class ReverseIntegerTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_reverse(self):
        res = self.obj.reverse(123)
        expected = 321
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_reverse(self):
        res = self.obj.reverse(-123)
        expected = -321
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_3_reverse(self):
        res = self.obj.reverse(120)
        expected = 21
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
