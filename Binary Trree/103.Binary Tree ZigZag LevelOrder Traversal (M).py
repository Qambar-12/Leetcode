# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #base case
        if not root:
            return []
        #BFS --->Level Order Traversal (using deque beacause popping from infront of it is O(1) operation)
        #stausLevel = 0 corresponds to left --> right and vice versa
        statusLevel = 1
        #2D list where each sublist corresponds to a level
        res = []
        from collections import deque
        q = deque([root])
        while q:
            currLevel = []
            nextLevel = []
            for n in range(len(q)):
                if not statusLevel:
                    currNode = q.pop()
                    currLevel.append(currNode.val)
                    if currNode.right:
                        nextLevel.append(currNode.right)    
                    if currNode.left:
                        nextLevel.append(currNode.left)
                else:
                    currNode = q.popleft()
                    currLevel.append(currNode.val)
                    if currNode.left:
                        nextLevel.append(currNode.left)
                    if currNode.right:
                        nextLevel.append(currNode.right)                     
            res.append(currLevel)
            if statusLevel:
                q.extend(nextLevel)
                statusLevel = 0
            else:
                q.extend(nextLevel[::-1])
                statusLevel = 1    
        return res    