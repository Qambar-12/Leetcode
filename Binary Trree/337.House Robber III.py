# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #basic recurrence relation is either to compute with or without root 
        #DFS algorithm
        # returns pair [withRoot , withoutRoot]
        def dfs(node):
            #base case 
            if not node:
                return [0,0]
            leftSubtree = dfs(node.left)
            rightSubtree  = dfs(node.right)
            withRoot = node.val + leftSubtree[1] + rightSubtree[1]
            #no restrictions to choose withoutRoot in this case
            withoutRoot = max(leftSubtree) + max(rightSubtree)   

            return [withRoot, withoutRoot]

        return max(dfs(root))     
