# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative solution
        res = []
        stack = []
        curr = root
        #the outer while loop continues until all nodes are traversed
        while curr or stack:
            #Go as much left as possible until curr.left == None
            while curr:
                stack.append(curr)
                curr = curr.left
            #pop statement here is an alternate to retrun statement in recursive sol
            curr = stack.pop()
            res.append(curr.val)
            #we finally move on to right child (inorder: left--->root--->right)
            curr = curr.right
        return res        
