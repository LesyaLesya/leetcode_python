import unittest

"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i) == 1:
                return s.find(i)
        return -1


class FirstUniqueCharTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_first_unique(self):
        res = self.obj.firstUniqChar("aabb")
        expected = -1
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')

    def test_2_first_unique(self):
        res = self.obj.firstUniqChar("loveleetcode")
        expected = 2
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')


