from typing import Optional

# Recursive Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        # Check if leaf node return True or False
        # Apply ifs for val 2 and 3 for and/or operation recursively

        if not root.left and not root.right:
            return root.val == 1

        if root.val == 2:
            return (
                self.evaluateTree(root.left) or 
                self.evaluateTree(root.right)
                )

        if root.val == 3:
            return (
                self.evaluateTree(root.left) and 
                self.evaluateTree(root.right)
                )