from typing import List
import unittest

"""
414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = list(reversed(sorted(list(set(nums)))))
        print(l)
        try:
            return l[2]
        except IndexError:
            return l[0]


class ThirdMaxTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_third_max(self):
        res = self.obj.thirdMax([2,2,3,1])
        expected = 1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_third_max(self):
        res = self.obj.thirdMax([1, 2])
        expected = 2
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
