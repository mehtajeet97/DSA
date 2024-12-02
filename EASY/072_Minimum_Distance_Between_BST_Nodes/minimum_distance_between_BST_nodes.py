from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Use inorder traversal so that tree is sorted
        # Check difference between consecutive values for minimum
        # return the least of them as final output

        prev, res = None, float("inf")

        def dfs(node):
            nonlocal prev, res
            if not node:
                return

            dfs(node.left)
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)
        
        dfs(root)
        return res