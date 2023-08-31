import unittest


"""
151. Reverse Words in a String

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


class ReverseWordsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_reverse_words(self):
        res = self.obj.reverseWords('a good   example')
        expected = 'example good a'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_reverse_words(self):
        res = self.obj.reverseWords('  hello world  ')
        expected = 'world hello'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
