import unittest


"""
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0: return False
        while n != 1:
            if n % 4 != 0:
                return False
            n = n // 4
        return True


class isPowerFourTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_power_four(self):
        res = self.obj.isPowerOfFour(16)
        self.assertTrue(res, f'expected - True, actual - {res}')

    def test_2_power_four(self):
        res = self.obj.isPowerOfFour(5)
        self.assertFalse(res, f'expected - False, actual - {res}')
