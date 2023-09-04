import unittest

"""
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_pattern = {pattern[i]: [j for j in range(len(pattern)) if pattern[j] == pattern[i]] for i in range(len(pattern))}
        l = s.split(' ')
        dict_str = {l[i]: [j for j in range(len(l)) if l[i] == l[j]] for i in range(len(l))}
        if len(dict_str.keys()) != len(dict_pattern.keys()):
            return False
        else:
            return True if sorted(dict_pattern.values()) == sorted(dict_str.values()) else False


class WordPatternTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_word_patterm(self):
        res = self.obj.wordPattern("abba", "dog cat cat dog")
        expected = True
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')

    def test_2_word_patterm(self):
        res = self.obj.wordPattern("abba", "dog cat cat fish")
        expected = False
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')
