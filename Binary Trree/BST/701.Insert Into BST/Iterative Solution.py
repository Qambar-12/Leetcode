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
        
        #Iterative solution ---> O(h) time complexity and takes constant memory O(1) because we are just moving curr pointer
        #Same base case as recursive solution
        if not root:
            return TreeNode(val)
        curr = root
        #we keep going until we reach a null node
        while True:
            if val < curr.val:
                #if we cannot go any further left we need to insert the node and return root
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left    
            else:
                #if we cannot go any further right we need to insert the node and return root
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right    

