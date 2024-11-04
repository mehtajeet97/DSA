class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredarray=[]
        for i in range(len(nums)):
            squaredarray.append(nums[i]**2)
        return sorted(squaredarray)