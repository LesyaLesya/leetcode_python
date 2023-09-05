import collections
import unittest

"""
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        coll = collections.Counter(s)
        result = ''
        for i in sorted(coll, key=lambda x: coll[x], reverse=True):
            result += coll[i] * i
        return result


class FrequencySortTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_frequency_sort(self):
        res = self.obj.frequencySort("Aabb")
        expected = "bbAa"
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
