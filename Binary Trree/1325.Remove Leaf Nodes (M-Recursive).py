# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #recursive solution 
        #to cater a parent may also become a leaf using postorder DFS
        if not root:
            return None
        #saving the return values for left and right subtrees    
        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right , target)

        if not root.left and not root.right and root.val == target:
            return None
        return root        

        #Iterative Solution
        #stack to mimic recursive call stack
        #to have postorder traversal using iterative version : L --> R --> N
        #we use a hashset (visited)
        stack = [root]
