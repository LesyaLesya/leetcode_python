"""
2299. Strong Password Checker II

A password is said to be strong if it satisfies all the following criteria:

    It has at least 8 characters.
    It contains at least one lowercase letter.
    It contains at least one uppercase letter.
    It contains at least one digit.
    It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
    It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).

Given a string password, return true if it is a strong password. Otherwise, return false.



Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.

Example 2:

Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.

Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.
"""
import unittest


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not any([i.islower() for i in password]):
            return False
        if not any([i.isupper() for i in password]):
            return False
        if not any([i.isdigit() for i in password]):
            return False
        if not any([i in password for i in "!@#$%^&*()-+"]):
            return False
        if not all(a != b for a, b in zip(password, password[1:])):
            return False
        return True


class StrongestPasswordCheckerTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_passw_checker_1(self):
        res = self.obj.strongPasswordCheckerII("IloveLe3tcode!")
        self.assertTrue(res, f'expected - True, actual - {res}')

    def test_passw_checker_2(self):
        res = self.obj.strongPasswordCheckerII("Me+You--IsMyDream")
        self.assertFalse(res, f'expected - False, actual - {res}')
