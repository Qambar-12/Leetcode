# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
        #diameter is the longest path b/w any two leaves (having no children)
        #Using a bottom up approach DFS recursively to achieve linear time complexity
        #diameter = height_left_subTree + height_right_subTree
        diameter = 0
        #dfs functions actually returns depth of each node / subtree
        def dfs(root):
            #enclosing namespace
            nonlocal diameter
            if not root:
                return 0
            depth_left_subTree = dfs(root.left)
            depth_right_subTree = dfs(root.right)
            diameter = max(diameter,(depth_left_subTree + depth_right_subTree))
            
            return 1 + max(depth_left_subTree,depth_right_subTree)
        dfs(root)
        return diameter        
print(diameterOfBinaryTree(TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3)))) #3