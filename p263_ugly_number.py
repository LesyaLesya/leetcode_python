import unittest

"""
263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False
        return True


class IsUglyTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_is_ugly(self):
        res = self.obj.isUgly(6)
        expected = True
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')

    def test_2_is_ugly(self):
        res = self.obj.isUgly(14)
        expected = False
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')
