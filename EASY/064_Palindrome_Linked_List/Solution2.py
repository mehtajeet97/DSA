from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Create two pointers : Fast and Slow
        fast, slow = head, head
        # Iterate through the array so that Fast is at end and Slow is midway
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Once you have midpoint reverse the string
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # Now check for palindrome through both way travel
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True