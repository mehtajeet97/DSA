from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a pointer pointing to head of LinkedList
        curr = head
        # Iterate through the LinkedList, check if next val is duplicate
        while curr:
            while curr.next and curr.next.val == curr.val:
                # If duplicate, pointer should skip the next node
                curr.next = curr.next.next
            curr = curr.next
        return head