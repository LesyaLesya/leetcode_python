import unittest
from typing import List

"""
137. Single Number II

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99

"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [i for i in nums if nums.count(i) == 1][0]


class SingleNumber2TestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_single_number(self):
        res = self.obj.singleNumber([2,2,3,2])
        expected = 3
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_single_number(self):
        res = self.obj.singleNumber([0,1,0,1,0,1,99])
        expected = 99
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
