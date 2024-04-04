# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        #taking a list instead of string b/c it is a mutable structure
        res = []
        #Preorder recursive function
        def preorder(root):
            if not root:
                return
            res.append('(')
            res.append(str(root.val))
            if not root.left and root.right:
                res.append('()')
            #Recursive calls
            preorder(root.left)
            preorder(root.right)
            res.append(')')     
        preorder(root) 
        #since brackets would be included for all nodes removing it for root node while concatenating 
        return ''.join(res)[1:-1]       
