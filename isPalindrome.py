"""
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return True if s == s[::-1] else False


print(Solution().isPalindrome(121))
