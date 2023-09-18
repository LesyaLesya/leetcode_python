import unittest

"""
541. Reverse String II

Given a string s and an integer k, reverse the first k characters for every 2k characters 
counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but 
greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = [s[i:i+k] for i in range(0, len(s), k)]
        for i in range(0, len(l), 2):
            l[i] = l[i][::-1]
        return ''.join(l)


class ReverseStrTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_reverse_str(self):
        res = self.obj.reverseStr('abcdefg', 2)
        expected = 'bacdfeg'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
