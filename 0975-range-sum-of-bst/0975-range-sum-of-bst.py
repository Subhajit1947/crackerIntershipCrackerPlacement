# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def helper(node,sum1):
            if not node:
                return 0
            sl=helper(node.left,sum1)   
            sr=helper(node.right,sum1) 
            if node.val>=low and node.val<=high:
                return sl+sr+node.val
            return sl+sr
        return helper(root,0)
          