from typing import List
from collections import Counter
import re
import unittest


"""
819. Most Common Word

Given a string paragraph and a string array of the banned words banned, return the most frequent 
word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"
"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',', ' ').replace('.', ' ')
        l = re.sub(r'[^\w\s]', '', paragraph.lower()).split()
        c = Counter(l).most_common()
        for i in c:
            if i[0] not in banned:
                return i[0]


class MostCommonWordTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_most_common_word(self):
        res = self.obj.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ["hit"])
        expected = 'ball'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_most_common_word(self):
        res = self.obj.mostCommonWord('a.', [])
        expected = 'a'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_3_most_common_word(self):
        res = self.obj.mostCommonWord('a, a, a, a, b,b,b,c, c', ['a'])
        expected = 'b'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
