from typing import List
import collections
import unittest

"""
350. Intersection of Two Arrays II

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) > len(nums2):
            max_arr = nums1
            min_arr = nums2
        else:
            max_arr = nums2
            min_arr = nums1
        c = dict(collections.Counter(max_arr))
        for i in min_arr:
            if i in c and c[i] != 0:
                c[i] -= 1
                res.append(i)
        return res


class IntersectTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_intersect(self):
        res = self.obj.intersect([1,2,2,1], [2,2])
        expected = [2, 2]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
