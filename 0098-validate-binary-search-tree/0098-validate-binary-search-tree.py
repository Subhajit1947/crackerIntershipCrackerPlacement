# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self,t: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return True,-float('inf'),float('inf')
            lbst,lmax,lmin=helper(root.left)
            rbst,rmax,rmin=helper(root.right)
            mbst=lbst and rbst and (root.val>lmax and root.val<rmin)
            mmin=min(root.val,lmin,rmin)
            mmax=max(root.val,lmax,rmax)
            return mbst,mmax,mmin
        bst,max1,min1=helper(t)
        return bst

