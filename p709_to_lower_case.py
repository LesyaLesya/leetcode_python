import unittest


"""
709. To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


class LowerCaseTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_lower_case(self):
        res = self.obj.toLowerCase('Hello')
        expected = 'hello'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
