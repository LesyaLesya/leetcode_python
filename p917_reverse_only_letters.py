import unittest


"""
917. Reverse Only Letters

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = list(s)
        res = list(reversed([i for i in s if i.isalpha()]))
        buffer = [(l[i], i) for i in range(len(l)) if not l[i].isalpha()]
        for i in buffer:
            res.insert(i[1], i[0])
        return ''.join(res)


class ReverseOnlyLettersTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_1_reverse_letters(self):
        res = self.obj.reverseOnlyLetters('ab-cd')
        expected = 'dc-ba'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')

    def test_2_reverse_letters(self):
        res = self.obj.reverseOnlyLetters('a-bC-dEf-ghIj')
        expected = 'j-Ih-gfE-dCba'
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
