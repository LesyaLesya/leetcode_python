import unittest

"""
2710. Remove Trailing Zeros From a String

Example 1:

Input: num = "51230100"
Output: "512301"
Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

Example 2:

Input: num = "123"
Output: "123"
Explanation: Integer "123" has no trailing zeros, we return integer "123".
"""


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0').lstrip('0')


class RemoveTrailingZerosTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_remove_zeros_1(self):
        res = self.obj.removeTrailingZeros("51230100")
        expected = "512301"
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_test_remove_zeros_2(self):
        res = self.obj.removeTrailingZeros("00051230100")
        expected = "512301"
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
