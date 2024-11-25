from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create two ptrs : One slow, One fast at 2x speed
        slow, fast = head, head

        # Iterate through LinkedList
        # When fast ptr reaches end, slow ptr is at middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow