from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create Two Pointers: previous and current
        # Current at head and Previous at null
        prev, curr = None, head
        # Iterate until current pointer is null
        while curr:
            nxt = curr.next
        # Reverse the pointers to reverse the linkedlist
            curr.next = prev
            prev = curr
            curr = nxt
        # Prev will point to end of LinkedList and return it as head
        return prev