

"""
2239. Find Closest Number to Zero

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
"""
import unittest
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        buf = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i]) < abs(buf):
                buf = nums[i]
            elif abs(nums[i]) == abs(buf):
                buf = max(buf, nums[i])
        return buf


class FindClosestTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_find_closest_1(self):
        res = self.obj.findClosestNumber([-4,-2,1,4,8])
        expected = 1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_find_closest_2(self):
        res = self.obj.findClosestNumber([2,-1,1])
        expected = 1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
