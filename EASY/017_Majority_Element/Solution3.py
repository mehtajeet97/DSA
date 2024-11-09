# Boyer-Moore Solution -- Follow Up Question -- Linear Time and O(1) Space
# If array has a majority element, take first number as result and a counter with it
# If next element of array is same then increment counter else decrement the counter
# When counter is zero, swap the current element as result element

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num
            if res == num:
                count = count + 1
            else:
                count = count - 1
        return res