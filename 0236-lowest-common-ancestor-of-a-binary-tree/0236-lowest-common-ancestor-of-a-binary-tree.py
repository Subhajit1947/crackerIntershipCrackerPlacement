# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val==p.val or root.val==q.val:
            return root 
        lt= self.lowestCommonAncestor(root.left,p,q) 
        
        rt= self.lowestCommonAncestor(root.right,p,q)  
        if lt==None and rt==None:
            return None
        elif lt is not None and rt is None:
            return lt
        elif lt is None and rt is not None:
            return rt
        else:
            return root
        