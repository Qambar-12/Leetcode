# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        #BFS algorithm using queues
        from collections import deque
        q = deque([root])
        while q:
            currNode = q.popleft()
            if currNode:
                q.append(currNode.left)
                q.append(currNode.right)
            #if we ever reach a null then every other value we pop from queue q must be null aswell else immediately return False
            else:
                while q:
                    if q.popleft() is not None:
                        return False
        return True                         
