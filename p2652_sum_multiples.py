import unittest

"""
2652. Sum Multiples

Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.



Example 1:

Input: n = 7
Output: 21
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7.
The sum of these numbers is 21.

Example 2:

Input: n = 10
Output: 40
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10.
The sum of these numbers is 40.

Example 3:

Input: n = 9
Output: 30
Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9.
The sum of these numbers is 30.
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res = [i for i in range(1, n+1) if i %3 == 0 or i %5 == 0 or i%7==0]
        return sum(res)


class SumMultiplesTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_sum_multiples_1(self):
        res = self.obj.sumOfMultiples(7)
        expected = 21
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_sum_multiples_2(self):
        res = self.obj.sumOfMultiples(10)
        expected = 40
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
