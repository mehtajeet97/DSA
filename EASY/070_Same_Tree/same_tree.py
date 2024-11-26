from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive solution
        # Check base condition -- if both null
        if not p and not q:
            return True
        # Check base condition -- if one of them is null
        if not p or not q:
            return False
        # Check base condition -- if root values are equal
        if p.val != q.val:
            return False
        # Recursive call for left and right subtree
        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
