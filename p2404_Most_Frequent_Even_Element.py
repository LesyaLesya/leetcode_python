import unittest
from typing import List

"""
2404. Most Frequent Even Element

Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

 

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.

Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
"""


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        l = sorted([i for i in nums if i % 2 == 0])
        if len(l) == 0: return -1
        return max(l, key=l.count)


class MostFrequentEvenTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_frequent_even_1(self):
        res = self.obj.mostFrequentEven([0,2,2,4,4,1])
        expected = 2
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_frequent_even_2(self):
        res = self.obj.mostFrequentEven([29,47,21,41,13,37,25,7])
        expected = -1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
