import unittest
from typing import List

"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        try:
            return nums.index(target)
        except ValueError:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)


class SearchInsertPositionTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_serach_insert(self):
        res = self.obj.searchInsert([1, 3, 5, 6], 5)
        expected = 2
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_serach_insert(self):
        res = self.obj.searchInsert([1,3,5,6], 2)
        expected = 1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_3_serach_insert(self):
        res = self.obj.searchInsert([2,3,5,6], 7)
        expected = 4
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

