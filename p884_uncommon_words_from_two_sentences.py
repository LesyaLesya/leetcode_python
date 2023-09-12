from typing import List
import unittest


"""
884. Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        ls1 = s1.split()
        ls2 = s2.split()
        for i in ls1:
            if ls1.count(i) == 1 and i not in ls2:
                res.append(i)
        for i in ls2:
            if ls2.count(i) == 1 and i not in ls1:
                res.append(i)
        return res


class UncommonFromSentecesTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_uncommon_from_sentences(self):
        res = self.obj.uncommonFromSentences("d b zu d t", "udb zu ap")
        expected = ['b', 't', 'udb', 'ap']
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
