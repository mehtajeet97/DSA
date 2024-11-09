# Since element is found in more than half, just sort the array and find the number at half position
# int division for whenever array is of odd length

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]