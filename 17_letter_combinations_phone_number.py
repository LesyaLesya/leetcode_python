import unittest
from functools import reduce
from typing import List

"""
17. Letter Combinations of a Phone Number

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

        if len(digits) > 4 or len(digits) == 0:
            return []
        for i in digits:
            if i not in ['2', '3', '4', '5', '6', '7', '8', '9']:
                return []
        l = [d[i] for i in digits]
        res = reduce(lambda a, b: [i+j for i in a for j in b], l)
        return res


class LetterCombinationsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_letter_combinations(self):
        res = self.obj.letterCombinations('23')
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_letter_combinations(self):
        res = self.obj.letterCombinations('')
        expected = []
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_3_letter_combinations(self):
        res = self.obj.letterCombinations('2')
        expected = ["a","b","c"]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
