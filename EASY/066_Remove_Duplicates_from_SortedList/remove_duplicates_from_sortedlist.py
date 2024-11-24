from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Empty Input
        if head is None:
            return head
        
        # Create two pointers 
        previous = head
        current = head.next
        
        # Iterate with second
        while current:
            # When match, delete node
            if current.val == previous.val:
                previous.next = current.next
                current = None
                current = previous.next
            
            # When mismatch, first equals second
            else:
                previous = current
                current = current.next
        
        # Return Head
        return head