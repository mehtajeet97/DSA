from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Put all origin cities in hashset
        origin = set()
        for p in paths:
            origin.add(p[0])
        
        # Check destination city in hashset
        for p in paths:
            if p[1] not in origin:
                return p[1]