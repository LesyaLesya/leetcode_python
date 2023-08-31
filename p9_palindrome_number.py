import unittest

"""
9. Palindrome Number

Given an integer x, return true if x is a
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return True if s == s[::-1] else False


class CheckPalindromTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_is_palindrom(self):
        res = self.obj.isPalindrome(121)
        expected = True
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_is_palindrom(self):
        res = self.obj.isPalindrome(10)
        expected = False
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
