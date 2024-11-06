# Set Method -- Use a set to check if value already exists in it, if not copy the value and move forward
# Time : O(n)
# Space : O(n)

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exists = set()
        for num in nums:
            if num in exists:
                return True
            exists.add(num)
        return False