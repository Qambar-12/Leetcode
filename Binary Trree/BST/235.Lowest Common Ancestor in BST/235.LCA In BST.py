# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #root node is common ancestor of all nodes but not necassarily Lowest Common Ancestor
        #starting from root we see if p and q is smaller or greater respectively than root node
        #if for e.g p is smaller than root we need to search the left subtree
        #if for e.g q is greater than root we need to search the right subtree
        #if while searching we reach p or q itself that is LCA because node is considered descendant of itself
        #and since all node values are unique
        #Thus where a split occurs b/w p and q that is LCA i.e one of them in left and one of them in right subtree
        #O(log2n) because each time we eliminate one side / subtree of BST ---> similar to Binary Search
        
        curr = root
        #no need to place return statement outside because all node values are unique and it is guaranteed that we would find LCA
        while curr:
            #searching to left subtree if True
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            #searching to right subtree if True
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            #either splitting occurs i.e p in left and q in right subtree or viceversa or a node itself is reached
            else:
                return curr    