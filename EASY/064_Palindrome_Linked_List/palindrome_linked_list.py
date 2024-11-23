from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Create an array
        nums = []
        # Copy the LinkedList into the Array
        while head:
            nums.append(head.val)
            head = head.next

        # Check if palindrome through two pointers across array
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] != nums[r]:
                return False
            l = l+1
            r = r-1
        return True