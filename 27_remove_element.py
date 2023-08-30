import unittest
from typing import List


"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums[:]:
            if i == val:
                nums.remove(i)
        return len(nums)


class RemoveElementTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_remove_element(self):
        res = self.obj.removeElement([3, 2, 2, 3], 3)
        expected = 2
        self.assertEqual(res, expected, f'expected - {expected}, actual - {res}')
