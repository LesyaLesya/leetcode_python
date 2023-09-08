import unittest

"""
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while 
still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(map(lambda x: x[::-1], s.split(' '))))


class ReverseWordsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_reverse_words(self):
        res = self.obj.reverseWords('God Ding')
        expected = 'doG gniD'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
