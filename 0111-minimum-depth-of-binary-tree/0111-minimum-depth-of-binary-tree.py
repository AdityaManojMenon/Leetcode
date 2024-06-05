# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        elif root.left is None and root.right is None:
            return 1
        
        else:
            num_min = 1000000000000000
            if root.left != None:
                num_min = min(self.minDepth(root.left),num_min)
            if root.right != None:
                num_min = min(self.minDepth(root.right),num_min)
            
            return num_min + 1
            
                
        