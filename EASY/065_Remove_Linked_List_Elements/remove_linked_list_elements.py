from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create Dummy Node
        dummy = ListNode(next=head)
        # Create two pointers : previous and current
        prev, curr = dummy, head

        while curr:
        # If value matches remove the node and update only current
            if curr.val == val:
                tmp = curr.next
                prev.next = curr.next
                curr = tmp
            
            # If mismatch update both pointers
            else:
                prev = prev.next
                curr = curr.next
        return dummy.next