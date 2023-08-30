from typing import Optional

"""
2. Add Two Numbers

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = []
        ll2 = []
        while l1 is not None:
            ll1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            ll2.append(l2.val)
            l2 = l2.next

        n1 = int(''.join(map(str, ll1[::-1])))
        n2 = int(''.join(map(str, ll2[::-1])))
        s = n1 + n2
        res = list(reversed(list(map(int, list(str(s))))))
        head = ListNode(res[0])
        tail = head
        e = 1
        while e < len(res):
            tail.next = ListNode(res[e])
            tail = tail.next
            e += 1
        return head
