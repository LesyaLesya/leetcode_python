import unittest
from typing import List
import itertools

"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

 

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 1 or len(nums) > 6:
            return []
        for i in nums:
            if i < -10 or i > 10:
                return []
        if len(set(nums)) != len(nums):
            return []
        perm = itertools.permutations(nums)
        return [list(i) for i in list(perm)]


class PermutationsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_premute(self):
        res = self.obj.permute([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
