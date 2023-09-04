import unittest

"""
389. Find the Difference

You are given two strings s and t.
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t.

Example 1:
Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:
Input: s = "", t = "y"
Output: "y"
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = list(s)
        t_list = list(t)
        for i in s_list[:]:
            if i in t_list:
                t_list.remove(i)
        return t_list[0] or ''


class FindDifferenceTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_find_diff(self):
        res = self.obj.findTheDifference('a', 'aa')
        expected = 'a'
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')

    def test_2_find_diff(self):
        res = self.obj.findTheDifference('abcd', 'abcde')
        expected = 'e'
        self.assertEqual(res, expected, f'actual - {res}, expected - {expected}')
