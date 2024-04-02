# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #DFS Recursively
        #Base cases 
        if not p and not q :
            return True
        #return False if one of them is null and other is not null or if both are not null but their values are not equal
        elif (not p or not q) or (p.val != q.val):
            return False
        
        #recursive call we need to check that our both left "and" right subtrees are equal simultaneoulsy
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)        
