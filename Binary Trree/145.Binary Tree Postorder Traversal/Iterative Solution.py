# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative solution 
        #Postorder Traversal (Left--->Right--->Root)
        """Value of node is appended to result when node visited 2nd time i.e
        when bool value in visit array is True"""
        stack,visit = [root],[False]
        res = []
        while stack:
            curr,v = stack.pop(), visit.pop()
            #Else condition not included because None is eventually popped out of stack
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    #since now when node in stack would be visited it would be second time we need to append True to visit array
                    stack.append(curr)
                    visit.append(True)
                    #Before evening moving on to left child,parent and right child must be appended to stack in respective order
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        return res            
                    
