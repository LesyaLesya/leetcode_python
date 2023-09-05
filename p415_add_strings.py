import sys
import unittest

"""
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(0)
        return str(int(num1) + int(num2))


class AddStringTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_add_string(self):
        res = self.obj.addStrings('11', '123')
        expected = '134'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_add_string(self):
        res = self.obj.addStrings('456', '77')
        expected = '533'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
