from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        w = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                temp = nums[w]
                nums[w]=nums[i]
                nums[i]=temp
                w = w+1
        return nums