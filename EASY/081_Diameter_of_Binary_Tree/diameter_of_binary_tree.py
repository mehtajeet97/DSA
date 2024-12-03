from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Create Global Variable for Diameter
        self.diameter = 0
        # Create Recursive function to calculate height
        def dfs(curr):
            if not curr: return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        
        return self.diameter