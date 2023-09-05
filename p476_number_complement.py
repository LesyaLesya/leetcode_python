import unittest


"""
476. Number Complement

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's 
in its binary representation.
For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""


class Solution:
    def findComplement(self, num: int) -> int:
        b = '{0:b}'.format(num)
        l = []
        for i in b:
            if i == '0':
                l.append('1')
            else:
                l.append('0')
        res = ''.join(l)
        return int(res, 2)


class FindComplementTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_find_complement(self):
        res = self.obj.findComplement(5)
        expected = 2
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
