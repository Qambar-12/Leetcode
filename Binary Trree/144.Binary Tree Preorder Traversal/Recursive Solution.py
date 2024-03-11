# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Recursive solution for Preorder traversal
        #(Root--->Left--->Right)
        res = []
        def preorder(root):
            #Base case
            if not root:
                return
            res.append(root.val)
            #Recursive calls
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res        
