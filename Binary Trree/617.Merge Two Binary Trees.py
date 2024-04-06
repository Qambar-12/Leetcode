# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1
        else: #t1, t2 exist
            new_tree = TreeNode(root1.val + root2.val) #create new treenode with summed value
            new_tree.left = self.mergeTrees(root1.left, root2.left)
            new_tree.right = self.mergeTrees(root1.right, root2.right)
        return new_tree
                 