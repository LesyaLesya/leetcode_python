import unittest
from typing import List

"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if len(strs) == 0:
            return ''
        min_word = min(strs, key=len)
        for i in range(len(min_word)):
            if all([j.startswith(min_word[:i+1]) for j in strs]):
                res += min_word[i]
            else:
                break
        return res


class CommonPrefixTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_longest_common_prefix(self):
        res = self.obj.longestCommonPrefix(['flower', 'flow', 'flight'])
        expected = 'fl'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_longest_common_prefix(self):
        res = self.obj.longestCommonPrefix(['dog', 'racecar', 'car'])
        expected = ''
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
