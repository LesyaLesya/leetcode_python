import unittest


"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        list_s = list(s)
        l = ([i for i in range(len(s)) if s[i] in vowels])[::-1]
        vow_s = [i for i in s if i in vowels]
        zipped = list(zip(vow_s, l))
        for letter, idx in zipped:
            list_s[idx] = letter
        return ''.join(list_s)


class ReverseVowelsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_rev_vowels(self):
        res = self.obj.reverseVowels('hello')
        expected = 'holle'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_rev_vowels(self):
        res = self.obj.reverseVowels('leetcode')
        expected = 'leotcede'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
