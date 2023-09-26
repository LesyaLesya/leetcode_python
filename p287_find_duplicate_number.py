import collections
import unittest
from typing import List

"""
287. Find the Duplicate Number

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return [i for i, count in collections.Counter(nums).items() if count > 1][0]


class FindDuplTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_find_dupl(self):
        res = self.obj.findDuplicate([3,1,3,4,2])
        expected = 3
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
