# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #DFS Recursive algorithm --->preorder traversal
        #root is always considered a good node so count is atleast 1
        #count = 1 + left + right
        #then we need to how many good nodes in left and right subtree respectively
        #we need to keep track of greatest node val seen so far along path so currNode is a good node only if its greater than or equal to greatest so far
        count = 0
        def dfs(node,maxVal):
            #base case since empty tree doesnot have any good nodes
            if not node:
                return 0
            count = 1 if node.val >= maxVal else 0   
            maxVal = max(maxVal,node.val)    
            count += dfs(node.left,maxVal)
            count += dfs(node.right,maxVal)
            return count    
        return dfs(root,root.val)    
