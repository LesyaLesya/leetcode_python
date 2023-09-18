import unittest

"""
1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

Example 1:
Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.

Example 2:
Input: sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2
Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, 
but we return 2 as it's the minimal index.

Example 3:
Input: sentence = "i am tired", searchWord = "you"
Output: -1
Explanation: "you" is not a prefix of any word in the sentence.
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return i+1
        return -1


class IsPrefixTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_is_prefix(self):
        res = self.obj.isPrefixOfWord('i love eating burger', 'burg')
        expected = 4
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
