# Prefix Array is used to predefine the sums of each increaing array element
# Example : if array is [1, 2, 3] the prefix array will be [1, 3, 6]

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for num in nums:
            cur = cur + num
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)