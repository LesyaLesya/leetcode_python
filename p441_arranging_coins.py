import unittest

"""
441. Arranging Coins

You have n coins and you want to build a staircase with these coins. The staircase consists 
of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1: return 1
        row = 0
        s = n
        while s != 0:
            row = row + 1
            if s > row:
                s = s - row
            elif s == row: return row
            else:
                return row - 1


class ArrangeCoinsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_arrange_coins(self):
        res = self.obj.arrangeCoins(8)
        expected = 3
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_arrange_coins(self):
        res = self.obj.arrangeCoins(5)
        expected = 2
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_3_arrange_coins(self):
        res = self.obj.arrangeCoins(1)
        expected = 1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_4_arrange_coins(self):
        res = self.obj.arrangeCoins(3)
        expected = 2
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
