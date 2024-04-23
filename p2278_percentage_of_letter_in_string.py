"""
2278. Percentage of Letter in String

Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.



Example 1:

Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.

Example 2:

Input: s = "jjjj", letter = "k"
Output: 0
Explanation:
The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
"""
import unittest


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int((s.count(letter) / len(s)) * 100)


class PercentageOfLetterTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_persentage_1(self):
        res = self.obj.percentageLetter("foobar", "o")
        expected = 33
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_persentage_2(self):
        res = self.obj.percentageLetter("kkkk", "j")
        expected = 0
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
