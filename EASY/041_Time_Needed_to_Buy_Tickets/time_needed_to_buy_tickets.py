from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        
        for i in range(len(tickets)):
            # For values before or at kth index, check they are less or equal
            if i <= k:
                res += min(tickets[i], tickets[k])
            #For values after kth index, check they are less
            else:
                res += min(tickets[i], tickets[k]-1)
        
        return res