# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Preorder DFS Iterative (using 2D stacks)
        #using node depth to our advantage
        #edge test case when tree is empty
        if not root:
            return 0
        stack = [[root,1]]    
        res = 1
        while stack:
            #unpacking list
            currNode , depth = stack.pop()
            res = max(res,depth)
            if currNode.right:
                stack.append([currNode.right,depth+1])
            if currNode.left:
                stack.append([currNode.left,depth+1])    
        return res
