# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #BST : sorted property to tree  ---> goes on recursively
        #i.e left subtree of node values is strictly smaller than parent node and vice versa for right subtree
        #since it is guaranteed that all values are unique
        #trivial way to solve it is to look for a null node for insertion although multiple sol may exist
        
        #Recursive solution ---> O(h) time complexity and takes extra memory O(h) b/c it maintains call stack
        #Base case
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right,val)
        else:
            root.left = self.insertIntoBST(root.left,val)
        return root            
