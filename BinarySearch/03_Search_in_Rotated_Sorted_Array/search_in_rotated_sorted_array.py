from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Define low and high
        low, high = 0, len(nums)-1

        #Initialize Binary Search with mid
        while low<=high:
            mid = (low+high)//2
            
            # Success Condition
            if nums[mid] == target:
                return mid
            
            # Left side check
            if nums[0] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            # Right side check
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        # Failure Return Value
        return -1