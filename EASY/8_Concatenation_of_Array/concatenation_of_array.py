# Range method -- Inputing nums[i] at two points in the ans array
# Best solution is single line but avoid :  return nums+nums

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=[0]* 2 * n
        for i in range(n):
            ans[i] = ans[i+n] = nums[i]
        return ans