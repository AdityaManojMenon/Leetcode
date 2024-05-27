# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self,left: Optional[TreeNode] ,right: Optional[TreeNode]):
        if not right and not left:
            return True
        if not right or  not left:
            return False
        return left.val == right.val and self.mirror(left.left,right.right) and self.mirror(right.left,left.right)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        return(self.mirror(root.left,root.right))