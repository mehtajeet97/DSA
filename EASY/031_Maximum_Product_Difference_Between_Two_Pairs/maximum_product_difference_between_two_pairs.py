from typing import List
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Sort Tha Array
        nums.sort()
        # Subtract the product of last two(max) and first two(min)
        return nums[-1] * nums[-2] - nums[0] * nums[1]