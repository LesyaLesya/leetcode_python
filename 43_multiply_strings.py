import unittest

"""
43. Multiply Strings

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


class MultiplyStringsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_multiply(self):
        res = self.obj.multiply('2', '3')
        expected = '6'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
