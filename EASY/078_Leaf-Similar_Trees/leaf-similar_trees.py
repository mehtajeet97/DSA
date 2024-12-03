from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Use DFS recursively -- create fn
        # BFS cannot be used as it will ruin the sequence of leaf encountered        
        # Use two arrays to populate with leaf and compare them

        def dfs(root, leaf):
            if not root:
                return
                
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []

        dfs(root1, leaf1)
        dfs(root2, leaf2)

        return leaf1 == leaf2