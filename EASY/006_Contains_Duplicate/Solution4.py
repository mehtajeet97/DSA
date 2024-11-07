# Set Method -- Single Line code
# Time & Space same as Solution 3 but Solution 3 has better acceptance rate


from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)