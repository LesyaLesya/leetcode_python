import unittest

"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True


class ContainDuplicateTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_duplicate(self):
        res = self.obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
        self.assertTrue(res, f'actual - {res}')

    def test_2_duplicate(self):
        res = self.obj.containsDuplicate([1,2,3,4])
        self.assertFalse(res, f'actual - {res}')
