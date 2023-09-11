from typing import List
import string
import unittest

"""
744. Find Smallest Letter Greater Than Target

You are given an array of characters letters that is sorted in non-decreasing order, 
and a character target. There are at least two different characters in letters.
Return the smallest character in letters that is lexicographically greater than target. 
If such a character does not exist, return the first character in letters.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ascii_lower = string.ascii_lowercase
        target_idx = ascii_lower.find(target)
        for i in range(target_idx+1, len(ascii_lower)):
            if ascii_lower[i] in letters:
                return ascii_lower[i]
        return letters[0]


class NextGreatestLetterTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_next_greatest_letter(self):
        res = self.obj.nextGreatestLetter(["c","f","j"], 'a')
        expected = 'c'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_next_greatest_letter(self):
        res = self.obj.nextGreatestLetter(["c","f","j"], 'c')
        expected = 'f'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_3_next_greatest_letter(self):
        res = self.obj.nextGreatestLetter(["x","x","y","y"], 'z')
        expected = 'x'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
