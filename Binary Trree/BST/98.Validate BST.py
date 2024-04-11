# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Valid BST must contain all node values less than root node in left subtree
        #and similarly all node values greater tahn root node in right subtree
        #and this must continue recursively considering each of node as BST
        #       5   root can be any val in b/w : -inf < 5 < +inf
        #      / \
        #     1   6    -inf < 1 < 5     5 < 6 < +inf
        #        / \
        #       3   7   5 < 3 < 6  (false)   6 < 7 < inf
        #Helper function valid DFS
        def valid(node,left,right):
            #base case because a null node is also a BST
            if not node:
                return True
            if not(node.val > left and node.val < right):
                return False
            #Recursive calls for left and right sub possible BSTs
            #going down left subtree we know left boundary remains same i.e all values greater than -inf
            #but also all values must be less than parent node so right bound is node.val
            #vice versa while going down right subtree
            return (valid(node.left,left,node.val) and valid(node.right,node.val,right))

        return valid(root,float('-inf'),float('+inf'))        
