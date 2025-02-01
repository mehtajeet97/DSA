from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Define low-high, check for empty array
        low, high = 0, len(nums)-1

        if len(nums) == 0:
            return -1
        
        # Loop until low>high
        while low <= high:
            
        # Define mid
            mid = (low + high)//2

        # Check if target at mid, less than mid or greater than mid
            if nums[mid] == target:
                return mid
                
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1 
            
        return -1