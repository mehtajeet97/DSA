# Count the non zero elements and write them with two pointer
# Run a second loop to make the rest of the elements zero

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[writer] = nums[i]
                writer = writer+1
        for i in range(writer, len(nums)):
            nums[i] = 0