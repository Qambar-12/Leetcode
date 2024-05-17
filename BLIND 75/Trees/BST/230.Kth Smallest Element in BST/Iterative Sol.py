# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        #Iterative sol to simulate inorder traversal using stack
        n = 0
        stack = []
        curr = root
        while curr or stack:
            #go as left as possible in bst until arrive at null
            #if we get to null we need to pop back up so that we can visit nodes 'Inorder Traversal'
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            #if k is not zero yet we need to move to right child and repeat the same process for it
            curr = curr.right            
