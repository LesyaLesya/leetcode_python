import unittest
from typing import List
from collections import Counter

"""
169. Majority Element

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for key, value in c.items():
            if value > len(nums) / 2:
                return key


class MajorityElementTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_majority_element(self):
        res = self.obj.majorityElement([2,2,1,1,1,2,2])
        expected = 2
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_majority_element(self):
        res = self.obj.majorityElement([3,2,3])
        expected = 3
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
