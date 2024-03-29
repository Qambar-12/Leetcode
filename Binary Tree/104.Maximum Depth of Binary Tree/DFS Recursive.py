# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Recursive DFS algorithm
        #Base case is when our root is None
        if not root:
            return 0
        #we are simply figuring out max b/w left and right subtrees plus 1 i.e our root 
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))   
