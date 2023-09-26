import unittest

"""
125. Valid Palindrome

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join([i.lower() for i in s if i.isalpha() or i.isdigit()])
        return a == a[::-1]


class PalindromeTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_palindrome(self):
        res = self.obj.isPalindrome("A man, a plan, a canal: Panama")
        self.assertTrue(res, f'expected - True, actual - {res}')
