from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Compare the root's left and right subtrees using a recursive fn
        def dfs(s1, s2):
        # When both subtrees are null
            if not s1 and not s2:
                return True
        # When only one subtree is null
            if not s1 or not s2:
                return False
        
        # Since both subtrees are not null, compare value and left, right
            return ((s1.val == s2.val) and dfs(s1.left, s2.right) 
            and dfs(s1.right, s2.left))
        
        return dfs(root.left, root.right)