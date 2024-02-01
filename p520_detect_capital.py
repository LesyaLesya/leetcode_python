import unittest


"""
520. Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.


Example 1:

Input: word = "USA"
Output: true

Example 2:

Input: word = "FlaG"
Output: false
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == word.capitalize()


class DetectCapitalTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_detect_capital_1(self):
        res = self.obj.detectCapitalUse('USA')
        self.assertTrue(res, f'expected - True, actual - {res}')

    def test_detect_capital_2(self):
        res = self.obj.detectCapitalUse('FlAg')
        self.assertFalse(res, f'expected - False, actual - {res}')
