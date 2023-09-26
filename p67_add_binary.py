import unittest

"""
67. Add Binary

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]


class AddBinaryTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_add_binary(self):
        res = self.obj.addBinary('11', '1')
        expected = '100'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
