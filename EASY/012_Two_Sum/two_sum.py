# Create a HasMap, check if the difference between target and current element in array is present in hashmap, 
# if not enter the element in hashmap 
# Time: O(n)
# Space: O(n) 

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {} # value : index
        for i,n in enumerate(nums):
            diff = target - n
            if diff in map1:
                return [map1[diff], i]
            map1[n] = i
        return "Error"