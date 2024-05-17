# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #one thing for sure is that postorder[-1] gives the root if tree
        #and finding its index in inorder array we can say values to left to it go in left subtree and to right of it in right subtree
        #if we pop from post order we get another subproblem so we can recursively build the tree
        hashMap = {val : i for i , val in enumerate(inorder)}       #building a hashmap so that we donot need to use inorder.index() every time O(n) operation itself
        #base case null nodes
        if not inorder:
            return 
        root = TreeNode(postorder.pop())
        #lookup time in dictionary is O(1) const time
        index = hashMap[root.val]
        #we need to build right subtree first because popping from postorder gives right most values
        #recursive calls
        root.right = self.buildTree(inorder[index+1:],postorder)
        root.left = self.buildTree(inorder[:index],postorder)
        return root
