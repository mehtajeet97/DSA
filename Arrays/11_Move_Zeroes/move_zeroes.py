# Count the non zero elements and write them with two pointer
# Run a second loop to make the rest of the elements zero

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use a pointer which starts from 0 
        # The pointer only moves if a nonzero number is encountered
        writer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[writer] = nums[i]
                writer = writer+1
        # After copying the nonzero elements at the start, 
        # Rewrite the latter elements to zero
        for i in range(writer, len(nums)):
            nums[i] = 0