import unittest
from typing import List

"""
260. Single Number III

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:

Input: nums = [-1,0]
Output: [-1,0]

Example 3:

Input: nums = [0,1]
Output: [1,0]
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [i for i in nums if nums.count(i) == 1]


class SingleNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_single_number(self):
        res = self.obj.singleNumber([1,2,1,3,2,5])
        expected = [3, 5]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
