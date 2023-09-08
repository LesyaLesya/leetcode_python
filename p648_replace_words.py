from typing import List
import unittest

"""
648. Replace Words

Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
"""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        l = sentence.split()
        for i in range(len(l)):
            for j in dictionary:
                if l[i].startswith(j):
                    l[i] = j
        return ' '.join(l)


class ReplaceWordsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_reverse_words(self):
        res = self.obj.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery")
        expected = 'the cat was rat by the bat'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
