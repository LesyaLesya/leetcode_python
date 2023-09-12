from typing import List
import unittest


"""
905. Sort Array By Parity

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i % 2 == 0 or i == 0:
                res.insert(0, i)
            else:
                res.append(i)
        return res


class SortArrayParityTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_sort_array_parity(self):
        res = self.obj.sortArrayByParity([3,1,2,4])
        expected = [4, 2, 3, 1]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
