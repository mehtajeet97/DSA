from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive Solution
        # Write base case for root equals Null
        if root is None:
            return None
        
        # Swap the left and right child
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Recursive call to both left and right
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return the root
        return root