# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, node: Optional[TreeNode]) -> List[str]:
        res=[]
        def helper(root,path):
            if not root:
                return 
            
            if not root.left and not root.right:
                res.append(path+str(root.val))
            else:
                path+=str(root.val)+'->'
            helper(root.left,path)
            helper(root.right,path)
        helper(node,'')
        return res

            