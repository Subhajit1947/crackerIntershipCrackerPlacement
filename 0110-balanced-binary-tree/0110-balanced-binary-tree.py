# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self,t: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return -1,True
            lh,lb=helper(root.left)
            rh,rb=helper(root.right)
            balance=lb and rb and (True if abs(lh-rh)<=1 else False)
            return max(lh,rh)+1,balance
        h,b=helper(t)
        return b