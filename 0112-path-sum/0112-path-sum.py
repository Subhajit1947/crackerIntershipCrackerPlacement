# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, noot: Optional[TreeNode], targetSum: int) -> bool:
        def pathsum(root,sum1):
            if not root:
                return False
            sum1+=root.val
            if not root.left and not root.right:
                return sum1==targetSum
            ls=pathsum(root.left,sum1)
            rs=pathsum(root.right,sum1)
            return ls or rs
        return pathsum(noot,0)