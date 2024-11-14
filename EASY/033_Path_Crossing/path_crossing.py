class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Map each direction with changes in x,y
        dir = {
            "N" : (0,1),
            "S" : (0, -1),
            "E" : (1, 0),
            "W" : (-1, 0)
        }
        # Create a set for all visited points
        visit = set()
        x, y = 0, 0

        # Check if new point in visited set
        for c in path:
            visit.add((x,y))
            dx, dy = dir[c]
            x, y = x+dx, y+dy
            if (x,y) in visit:
                return True
            
        return False