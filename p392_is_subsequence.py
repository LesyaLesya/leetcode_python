import unittest

"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


class IsSubsequenceTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_is_subsequence(self):
        res = self.obj.isSubsequence('ab', 'baab')
        self.assertTrue(res, f'expected - True, actual - {res}')

    def test_2_is_subsequence(self):
        res = self.obj.isSubsequence('axc', 'ahbgdc')
        self.assertFalse(res, f'expected - False, actual - {res}')
