# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #Depth first search algorithm
        def DFS(left,right):
            #when both left and right are null we can immediately stop searching and return True
            if not left and not right:
                return True
            #when any of left or right are null we can immediately stop searching and return False
            if not left or not right:
                return False
            #if left.val == left.right evaluates to False we donot enter into the recursive calls
            #comparing the mirror images i.e left of left with right of right and then left of right with right of left
            truthVal = (left.val == right.val and DFS(left.left,right.right) and DFS(left.right,right.left))
            return truthVal
        return DFS(root.left,root.right)    
