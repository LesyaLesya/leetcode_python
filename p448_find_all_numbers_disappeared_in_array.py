from typing import List
import unittest


"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in s]


class FindDisappearedTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_find_numbers(self):
        res = self.obj.findDisappearedNumbers([4,3,2,7,8,2,3,1])
        expected = [5, 6]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_find_numbers(self):
        res = self.obj.findDisappearedNumbers([1, 1])
        expected = [2]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
