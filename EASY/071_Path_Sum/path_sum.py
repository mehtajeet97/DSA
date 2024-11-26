from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Create Function to check current sum
        def checksum(node, currentSum):
            # Check Base case of Null
            if not node:
                return False
            
            # Increment currentSum by adding nodes value
            currentSum = currentSum + node.val

            # Check for leaf nodes if currentSum equal the target
            if not node.left and not node.right:
                return currentSum == targetSum
            
            # If Not leaf node then recursive left or right
            return (checksum(node.left, currentSum) or 
            checksum(node.right, currentSum))
        
        return checksum(root, 0)