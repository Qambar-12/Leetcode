# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        #BST ---> Sorted property 
        #Inorder traversal ---> (L---Root---R)
        prevNode , res = None , float('inf')
        #Recursive Solution
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            #enclosing namespace for modification need to declare them nonlocal
            nonlocal prevNode , res
            #if prev node is not null
            if prevNode:
                res = min(res,abs(node.val-prevNode.val))
            prevNode = node
            inorder(node.right)
        inorder(root)
        return res        

