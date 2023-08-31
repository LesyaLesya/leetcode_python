import unittest
from typing import List

"""
136. Single Number

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [i for i in nums if nums.count(i) == 1][0]


class SingleNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_single_number(self):
        res = self.obj.singleNumber([2,2,1])
        expected = 1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_single_number(self):
        res = self.obj.singleNumber([4,1,2,1,2])
        expected = 4
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
