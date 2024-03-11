# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Recursive solution 
        #Postorder Traversal (Left--->Right--->Root)
        res = []
        def postOrder(root):
            #Base Case
            if not root:
                return
            #Recursive calls
            postOrder(root.left)
            postOrder(root.right)
            res.append(root.val)    
        postOrder(root)
        return res    
