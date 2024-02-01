import unittest
from typing import List

"""
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].


Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]
"""


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            s = list(str(i))
            try:
                if all([i % int(j) == 0 for j in s]):
                    res.append(i)
            except Exception:
                continue
        return res


class SelfDividingNumbersTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_self_div_num_1(self):
        res = self.obj.selfDividingNumbers(1, 22)
        expected = [1,2,3,4,5,6,7,8,9,11,12,15,22]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_self_div_num_2(self):
        res = self.obj.selfDividingNumbers(47, 85)
        expected = [48,55,66,77]
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
