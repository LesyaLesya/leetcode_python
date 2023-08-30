import unittest
from typing import List

"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        try:
            first = nums.index(target)
            res.append(first)
            last = len(nums) - nums[::-1].index(target) - 1
            res.append(last)
            return res
        except ValueError:
            res = [-1, -1]
            return res


class SearchRangeTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_search_range(self):
        res = self.obj.searchRange([5, 7, 7, 8, 8, 10], 8)
        expected = [3, 4]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
