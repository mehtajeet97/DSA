from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
      # Check if root node is Null to return zero
      # If root value is less than high, check root left
      # If root value is greater than low, check root right
      # If not, return val adding check for root left and root right

        if not root:
            return 0
        
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        return (
            root.val + 
            self.rangeSumBST(root.left, low, high) + 
            self.rangeSumBST(root.right, low, high)
            )