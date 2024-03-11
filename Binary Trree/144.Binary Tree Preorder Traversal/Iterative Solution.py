# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative solution for Preorder traversal
        #(Root--->Left--->Right)
        res = []
        stack = []
        curr = root
        #The loop continues until all nodes have been traversed 
        #Worst space complexity is when all nodes have been pushed to stack i.e still O(n) i.e structures look similar to a linked list
        while curr or stack:
            if curr:
                res.append(curr.val)   
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return res           
