import unittest


"""
242. Valid Anagram

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)


class AnagramTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_anagram(self):
        res = self.obj.isAnagram("anagram",  "nagaram")
        self.assertTrue(res, f'expected - True, actual - {res}')

    def test_2_anagram(self):
        res = self.obj.isAnagram("rat", "car")
        self.assertFalse(res, f'expected - False, actual - {res}')
