from typing import List
import unittest


"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = set(nums1)
        l2 = set(nums2)
        return list(l1.intersection(l2))


class IntersectionArraysTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_intersection_arrays(self):
        res = self.obj.intersection([1,2,2,1], [2,2])
        expected = [2]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
