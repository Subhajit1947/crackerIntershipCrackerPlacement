# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterheight(self,root):
        if not root:
            return -1,0
        lh,ld=self.diameterheight(root.left)
        rh,rd=self.diameterheight(root.right)
        htemp=max(lh,rh)+1
        fes=lh+rh+2
        dia=max(fes,max(ld,rd))
        return htemp,dia
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        h,d=self.diameterheight(root)
        return d