# zip function in for loop creates consecutive pairs
# Think of all conditions for return False

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0]>arr[1]:
            return False
        
        inc = True
        
        for left, right in zip(arr, arr[1:]):
            
            if left == right:
                return False
            
            if left < right:
                if not inc:
                    return False
            
            if left > right:
                inc = False
        
        return not inc