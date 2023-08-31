import unittest


"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if 104 < len(s) < 1:
            return 0
        return len((s.strip().split(' '))[-1])


class LengthLastWordTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_length_last_word(self):
        res = self.obj.lengthOfLastWord('   fly me   to   the moon  ')
        expected = 4
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_length_last_word(self):
        res = self.obj.lengthOfLastWord('luffy is still joyboy')
        expected = 6
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
