from typing import List
import collections
import unittest


"""
442. Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return sorted([item for item, count in collections.Counter(nums).items() if count > 1])


class FindDuplicatesTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_add_string(self):
        res = self.obj.findDuplicates([4,3,2,7,8,2,3,1])
        expected = [2, 3]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_add_string(self):
        res = self.obj.findDuplicates([1])
        expected = []
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
