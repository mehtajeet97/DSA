# Simpler solution using Hashset

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # Create a pointer current and a hashset
        hashset = set()
        l1 = headA
        curr = headB
        # Add all nodes from list1 to hashset
        while l1:
            hashset.add(l1)
            l1 = l1.next
        # Iterate through the second list checking each node 
        # if present in Set
        while curr:
            if curr in hashset:
                return curr
            curr = curr.next
        return None