import unittest

"""
434. Number of Segments in a String

Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
Input: s = "Hello"
Output: 1
"""


class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip(' ')
        if len(s) == 0:
            return 0
        else:
            l = s.split(' ')
            for i in l[:]:
                if i == '':
                    l.remove(i)
        return len(l)


class CountSegmentsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_count_segments(self):
        res = self.obj.countSegments(", , , ,        a, eaefa")
        expected = 6
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_count_segments(self):
        res = self.obj.countSegments("Hello, my name is John")
        expected = 5
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
