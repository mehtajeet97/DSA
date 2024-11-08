# Declare a set, check if twice/ half the element of array is present in Set
# if Yes, return true
# else add the element to the set

from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        
        for num in arr:
            if num*2 in seen or num/2 in seen:
                return True
            seen.add(num)
        return False