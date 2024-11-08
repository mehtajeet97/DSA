# Two points -- l and r
# Let r pointer iterate through every element
# for every unique element found, replace it at pointer l position and then increment position l by 1
# start from index 1 (both pointers l and r) and compare with element at previous index in the loop

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l]=nums[r]
                l = l+1
        return l