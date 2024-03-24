# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Recursive function 
        def invert(root):
            #Base case when null 
            if not root :
                return
            #Swapping the children of a root and then recursively call function on left and right children considering each of them as root of a subtree
            root.left , root.right = root.right,root.left
            invert(root.left)
            invert(root.right)
        invert(root)
        return root        
    
