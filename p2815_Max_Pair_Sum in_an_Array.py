"""
2815. Max Pair Sum in an Array

You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers
from nums such that the maximum digit in both numbers are equal.

Return the maximum sum or -1 if no such pair exists.



Example 1:

Input: nums = [51,71,17,24,42]
Output: 88
Explanation:
For i = 1 and j = 2, nums[i] and nums[j] have equal maximum digits with a pair sum of 71 + 17 = 88.
For i = 3 and j = 4, nums[i] and nums[j] have equal maximum digits with a pair sum of 24 + 42 = 66.
It can be shown that there are no other pairs with equal maximum digits, so the answer is 88.

Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: No pair exists in nums with equal maximum digits.
"""
from typing import List
import unittest


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if res < s and max(str(nums[i])) == max(str(nums[j])):
                    res = s
        return res


class MaxPairSumTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_max_sum_1(self):
        res = self.obj.maxSum([51,71,17,24,42])
        expected = 88
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_max_sum_2(self):
        res = self.obj.maxSum([1,2,3,4])
        expected = -1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
