from typing import List
import unittest

"""
747. Largest Number At Least Twice of Others

You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every 
other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 
Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_value = max(nums)
        if all([i * 2 <= max_value for i in nums if i != max_value]):
            return nums.index(max_value)
        else:
            return -1


class DominantIndexTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_dominant_index(self):
        res = self.obj.dominantIndex([3,6,1,0])
        expected = 1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_dominant_index(self):
        res = self.obj.dominantIndex([1,2,3,4])
        expected = -1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
