# Calculate right total and left totals
# iterate through array if left total = right total return i
# Once an element passes, left total = left total + new element, right total = right total - element

from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums) #O(n)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum = leftSum + nums[i]
        return -1