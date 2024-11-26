# This solution also works for Followup question, for simpler solution use Hashset
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Create two ptrs at the start of each list
        l1, l2 = headA, headB
        # Iterate through both lists until intersection is found
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        # If no intersection, then return either of the ptrs as it will be null
        return l1