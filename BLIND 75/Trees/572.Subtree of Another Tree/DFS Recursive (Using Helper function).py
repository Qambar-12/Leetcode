# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Recursive call stack
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root : return False
        if self.isSametree(root,subRoot):
            return True
        else:
            #if they are not subtree of root node then start comparing subRoot parameter if left and right subtrees of the root
            #if any of them returns true output must be True
            return (self.isSubtree(root.left,subRoot)) or (self.isSubtree(root.right,subRoot))    
    #Helper function
    def isSametree(self,root,subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.isSametree(root.left,subRoot.left)) and (self.isSametree(root.right,subRoot.right))  
        #if neither of above condition executes means exactly one of them is empty so we need to return False
        return False         
