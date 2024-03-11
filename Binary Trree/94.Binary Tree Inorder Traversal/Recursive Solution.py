# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive solution (Inorder traversal left--->root--->right)
        #each node can be considered a sub-tree
        #traverse as much as left as possible until node.left = None
        #Each return call returns to its parent and root.val is appended to stack|
        #it is then checked whether node.right is None or not i.e parent has any right children  
        res =[]   #global variable
        def inorder(root):
            #Base case
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res        
