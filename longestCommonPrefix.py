from typing import List

"""
Input: strs = ["flower","flow","flight"]
Output: "fl"


Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if len(strs) == 0:
            return ''
        min_word = min(strs, key=len)
        for i in range(len(min_word)):
            if all([j.startswith(min_word[:i+1]) for j in strs]):
                res += min_word[i]
            else:
                break
        return res


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
