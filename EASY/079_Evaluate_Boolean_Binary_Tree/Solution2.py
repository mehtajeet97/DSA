from typing import Optional

# Iterative Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # Maintain a stack and a hashmap
        stack = [root]
        value = {} # Map Node --> Key

        while stack:
            node = stack.pop()
            
            # for Leaf Node
            if not node.left and not node.right:
                value[node] = node.val == 1
            
            # for Non-Leaf Nodes
            else:
                # Children Visited
                if node.left in value:
                    # OR
                    if node.val == 2:
                        value[node] = value[node.left] or value[node.right]
                    
                    # AND
                    if node.val == 3:
                        value[node] = value[node.left] and value[node.right]
                
                # Children not visited
                else:
                    stack.append(node)
                    stack.append(node.left)
                    stack.append(node.right)
        
        return value[root]