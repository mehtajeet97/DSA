from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #Check difference between first and last element
        #Reverse for difference less than zero
        if nums[-1] - nums[0] < 0:
            nums.reverse()
        
        #Check each number less than previous
        for i in range(len(nums)-1):
            if not (nums[i]<=nums[i+1]):
                return False
        return True