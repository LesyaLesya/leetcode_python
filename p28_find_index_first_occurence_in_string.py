import unittest


"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first 
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class IndexFirstOccurenceTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_str_str(self):
        res = self.obj.strStr('sadbutsad', 'sad')
        expected = 0
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_str_str(self):
        res = self.obj.strStr('leetcode', 'leeto')
        expected = -1
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
