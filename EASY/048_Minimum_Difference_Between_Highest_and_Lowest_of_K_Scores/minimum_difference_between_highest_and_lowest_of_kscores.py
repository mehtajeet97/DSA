from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Sort the input array
        nums.sort()
        # Initiate the left and right pointers
        l, r = 0, k-1
        res = float("inf")
        # Sliding Window of k, check minimum diff
        while r<len(nums):
            res = min(res, nums[r]-nums[l])
            l=l+1
            r=r+1
        return res
