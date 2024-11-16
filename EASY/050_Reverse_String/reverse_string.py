# Can also solve this problem using Stack and Recursion but they are less efficient in Space

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Create two pointers : Left and right
        l, r = 0, len(s)-1
        temp = 0
        # Swap the values at their positions
        while l<r:
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            
            l = l+1
            r = r-1