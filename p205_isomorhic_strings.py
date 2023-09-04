import unittest

"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_idx = list(map(s.find, s))
        print(s_idx)
        t_idx = list(map(t.find, t))
        return s_idx == t_idx


class IsomorphicStringsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_is_isomorphic(self):
        res = self.obj.isIsomorphic('paper', 'title')
        expected = True
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')

    def test_2_is_isomorphic(self):
        res = self.obj.isIsomorphic('foo', 'bar')
        expected = False
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')
