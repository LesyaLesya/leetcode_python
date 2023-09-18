import unittest


"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        while n != 1:
            if n % 2 != 0:
                return False
            n = n // 2
        return True


class isPowerTwoTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_power_two(self):
        res = self.obj.isPowerOfTwo(1)
        self.assertTrue(res, f'expected - True, actual - {res}')

    def test_2_power_two(self):
        res = self.obj.isPowerOfTwo(3)
        self.assertFalse(res, f'expected - False, actual - {res}')
