import unittest

"""
397. Integer Replacement

Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:

Input: n = 4
Output: 2
"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            elif n % 4 == 1 or n == 3:
                n = n - 1
            else:
                n = n + 1
            count += 1
        return count


class IntegerReplacementTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_integer_replacement(self):
        res = self.obj.integerReplacement(8)
        expected = 3
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_integer_replacement(self):
        res = self.obj.integerReplacement(1234)
        expected = 14
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
